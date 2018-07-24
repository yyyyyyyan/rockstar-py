import re
from sys import argv

simple_subs = {
				'(':'#',
				')':'',
				'Give back':'return',
				'Take it to the top':'continue',
				'Break it down':'break',
				' false ':' False ',
				' wrong ':' False ',
				' no ':' False ',
				' lies ':' False ',
				' null ':' False ',
				' nothing ':' False ',
				' nowhere ':' False ',
				' nobody ':' False ',
				' true ':' True ',
				' right ':' True ',
				' yes ':' True ',
				' ok ':' True ',
				' plus ':' + ',
				' with ':' + ',
				' minus ':' - ',
				' without ':' - ',
				' times ':' * ',
				' of ':' * ',
				' over ':' / ',
				' by ':' / ',
				' is higher than ':' > ',
				' is greater than ':' > ',
				' is bigger than ':' > ',
				' is stronger than ':' > ',
				' is lower than ':' < ',
				' is less than ':' < ',
				' is smaller than ':' < ',
				' is weaker than ':' < ',
				' is as high as ':' >= ',
				' is as great as ':' >= ',
				' is as big as ':' >= ',
				' is as strong as ':' >= ',
				' is as low as ':' <= ',
				' is as little as ':' <= ',
				' is as small as ':' <= ',
				' is as weak as ':' <= ',
				' is not ':' != ',
				' ain\'t ':' != ',
				'Until ':'while not ',
				'While ':'while '
			}

def get_comments(line):
	if '(' in line:
		line, comment = line.split('(')
		comment = ' #' + comment.strip(')\n ')
	else:
		comment = ''
	return line, comment

def create_function(line):
	global ident
	match = re.match(r'([A-Za-z]+(?: [A-Za-z]+)*) takes ([A-Za-z ]+)', line)
	if match:
		ident += 1
		line = 'def {}({}):'.format(match.group(1), match.group(2).replace(' and', ','))
	return line

def create_while(line):
	global ident
	if line.startswith('while '):
		line = line.replace(' is ', ' == ')
		line += ':'
		ident += 1
	return line

def create_if(line):
	global ident
	match = re.match(r'If .*', line)
	if match:
		ident += 1
		line = line.replace(' is ', ' == ')
		line = line.replace('If', 'if')
		line += ':'
	return line

def find_poetic_number_literal(line):
	poetic_type_literals_keywords = ['True', 'False']
	match = re.match(r'([A-Za-z]+(?: [A-Za-z]+)*) (?:is|was|were) (.+)', line)
	if match and match.group(2) not in poetic_type_literals_keywords:
		line = '{} = '.format(match.group(1))
		for word_number in match.group(2).split():
			period = '.' if word_number.endswith('.') else ''
			alpha_word = re.sub('[^A-Za-z]', '', word_number)
			line += str(len(alpha_word) % 10) + period
	return line


def find_proper_variables(line):
	match_list = re.findall(r'[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)+', line)
	if match_list:
		for match in match_list:
			line = line.replace(match, match.replace(' ', '_').lower())
	return line

def find_common_variables(line):
	match_list = re.findall(r'((?:[Mm]y|[Aa]n?|[Tt]he|[Yy]our)) ([a-z]+)', line)
	if match_list:
		for match in match_list:
			line = line.replace(' '.join(match), '{}_{}'.format(*match).lower())
	return line

def find_named(line):
	match = re.match(r'([A-Za-z]+(?:_[A-Za-z]+)*) [+-]?= .+', line)
	if match:
		return match.group(1)

def convert_code(rockstar_code, py_rockstar):
	global ident
	ident = 0
	most_recently_named = ''
	for line in rockstar_code:
		if line == '\n':
			ident = ident - 1 if ident > 0 else 0
		else:
			line_ident = '    ' * ident

			line, comments = get_comments(line)

			for key in simple_subs:
				line = line.strip()
				line += ' '
				line = line.replace(key, simple_subs[key])
			py_line = line.strip('\n ,.;')

			most_recently_named_keywords = [' it ', ' he ', ' she ', ' him ', ' her ', ' them ', ' they ']
			for keyword in most_recently_named_keywords:
				py_line = py_line.replace(keyword, ' {} '.format(most_recently_named))

			py_line = create_function(py_line)
			py_line = create_while(py_line)
			py_line = create_if(py_line)
			line_ident = '    ' * (ident - 1) if py_line == 'Else' else line_ident
			py_line = 'else:' if py_line == 'Else' else py_line

			py_line = re.sub(r'Put (.*) into ([A-Za-z]+(?: [A-Za-z]+)*)', r'\g<2> = \g<1>', py_line)
			py_line = re.sub(r'Build ([A-Za-z]+(?: [A-Za-z]+)*) up', r'\g<1> += 1', py_line)
			py_line = re.sub(r'Knock ([A-Za-z]+(?: [A-Za-z]+)*) down', r'\g<1> -= 1', py_line)
			py_line = re.sub(r'Listen to ([A-Za-z]+(?: [A-Za-z]+)*)', r'\g<1> = input()', py_line)
			py_line = re.sub(r'(?:Say|Shout|Whisper|Scream) (.*)', r'print(\g<1>)', py_line)

			py_line = find_poetic_number_literal(py_line)
			py_line = py_line.replace(' is ', ' = ')
			py_line = re.sub(r'([A-Za-z]+(?: [A-Za-z]+)*) says (.*)', r'\g<1> = "\g<2>"', py_line)

			py_line = find_proper_variables(py_line)
			py_line = find_common_variables(py_line)

			py_line = re.sub(r'([A-Za-z]+(?: [A-Za-z]+)*) taking ([A-Za-z_]+(?:, [A-Za-z_]+)*)', r'\g<1>(\g<2>)', py_line)
			
			line_named = find_named(py_line)
			most_recently_named = line_named if line_named else most_recently_named

			py_rockstar.write(line_ident + py_line + comments + '\n')
	

if __name__ == '__main__':
	if len(argv) == 3:
		try:
			rockstar_file = open(argv[1], 'r')
			rockstar_code = rockstar_file.readlines()
			rockstar_file.close()
		except FileNotFoundError:
			print('File not found.')

		py_rockstar = open(argv[2], 'w')
		convert_code(rockstar_code, py_rockstar)
		py_rockstar.close()

	else:
		print('Usage: python rockstar.py program.{rock|rockstar} output.py')