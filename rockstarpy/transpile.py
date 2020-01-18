import re


class Transpiler(object):

    def __init__(self):
        self.ident = 0
        self.regex_variables = r'\b(?:(?:[Aa]n?|[Tt]he|[Mm]y|[Yy]our) [a-z]+|[A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)*)\b'
        self.most_recently_named = ''
        self.simple_subs = {
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
            ' empty ':' False ',
            ' gone ':' False ',
            ' mysterious ':' False ',
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
            ' aint ':' != ',
            'Until ':'while not ',
            'While ':'while '
        }

    def get_comments(self, line):
        if '(' in line:
            line, comment = line.split('(')
            comment = ' # ' + comment.strip(')\n ')
        else:
            comment = ''
        return line, comment

    def create_function(self, line):
        match = re.match(r'\b({0}) takes ({0}(?: and {0})*)\b'.format(self.regex_variables), line)
        if match:
            self.ident += 1
            line = 'def {}({}):'.format(match.group(1), match.group(2).replace(' and', ','))
        return line

    def create_while(self, line):
        if line.startswith('while '):
            line = line.replace(' is ', ' == ')
            line += ':'
            self.ident += 1
        return line

    def create_if(self, line):
        match = re.match(r'If .*', line)
        if match:
            self.ident += 1
            line = line.replace(' is ', ' == ')
            line = line.replace('If', 'if')
            line += ':'
        return line

    def find_poetic_number_literal(self, line):
        poetic_type_literals_keywords = ['true', 'false', 'nothing', 'nobody', 'nowhere', 'empty', 'wrong', 'gone', 'no', 'lies', 'right', 'yes', 'ok', 'mysterious']
        match = re.match(r'\b({})(?: is|\'s| was| were) (.+)'.format(self.regex_variables), line)
        if match and match.group(2).split()[0] not in poetic_type_literals_keywords:
            line = '{} = '.format(match.group(1))
            for word_number in match.group(2).split():
                period = '.' if word_number.endswith('.') else ''
                alpha_word = re.sub('[^A-Za-z]', '', word_number)
                line += str(len(alpha_word) % 10) + period
        return line

    def find_proper_variables(self, line):
        match_list = re.findall(r'\b[A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)*\b', line)
        if match_list:
            for match in match_list:
                line = line.replace(match, match.replace(' ', '_'))
        return line

    def find_common_variables(self, line):
        match_list = re.findall(r'\b([Aa]n?|[Tt]he|[Mm]y|[Yy]our) ([a-z]+)\b', line)
        if match_list:
            for match in match_list:
                line = line.replace(' '.join(match), '{}_{}'.format(*match).lower())
        return line

    def find_named(self, line):
        match = re.match(r'([A-Za-z]+(?:_[A-Za-z]+)*) [+-]?= .+', line)
        if match:
            return match.group(1)

    def get_strings(self, line):
        says_match = re.match(r'({}) says (.*)'.format(self.regex_variables), line)
        if says_match:
            line = says_match.group(1) + ' = "{}"'
            return line, says_match.group(2)
        quotes_match = re.match(r'([^\"]* )(\".*\"(?:, ?\".*\")*)([^\"]*)', line)
        if quotes_match:
            line = quotes_match.group(1) + '{}' + quotes_match.group(3)
            return line, quotes_match.group(2)
        return line, None

    def transpile_line(self, line):
        if line == '\n':
            self.ident = self.ident - 1 if self.ident > 0 else 0
            return ''
        else:
            line_ident = '    ' * self.ident

            line, comments = self.get_comments(line)
            py_line, line_strings = self.get_strings(line)

            for key in self.simple_subs:
                py_line = py_line.strip()
                py_line += ' '
                py_line = py_line.replace(key, self.simple_subs[key])
            py_line = py_line.strip('\n ,.;')

            py_line = self.find_poetic_number_literal(py_line)

            py_line = py_line.replace('\'', '')

            for key in self.simple_subs:
                py_line = py_line.strip()
                py_line += ' '
                py_line = py_line.replace(key, self.simple_subs[key])
            py_line = py_line.strip('\n ,.;')

            most_recently_named_keywords = [' it ', ' he ', ' she ', ' him ', ' her ', ' them ', ' they ',
                                            ' ze ', ' hir ', ' zie ', ' zir ', ' xe ', ' xem ', ' ve ', ' ver ']
            for keyword in most_recently_named_keywords:
                py_line = py_line.replace(keyword, ' {} '.format(self.most_recently_named))

            py_line = self.create_function(py_line)
            py_line = self.create_while(py_line)
            py_line = self.create_if(py_line)
            line_ident = '    ' * (self.ident - 1) if py_line == 'Else' else line_ident
            py_line = 'else:' if py_line == 'Else' else py_line

            py_line = re.sub(r'Put (.*) into ({})'.format(self.regex_variables), r'\g<2> = \g<1>', py_line)
            py_line = re.sub(r'Build ({}) up'.format(self.regex_variables), r'\g<1> += 1', py_line)
            py_line = re.sub(r'Knock ({}) down(\, down)*'.format(self.regex_variables), r'\g<1> -= ' + str(1 + py_line.count(", down")), py_line)
            py_line = re.sub(r'Listen to ({})'.format(self.regex_variables), r'\g<1> = input()', py_line)
            py_line = re.sub(r'(?:Say|Shout|Whisper|Scream) (.*)', r'print(\g<1>)', py_line)

            py_line = py_line.replace(' is ', ' = ', 1)

            py_line = re.sub(r'({0}) taking ((?:{0}|\"[^\"]*\"|[0-9]+)(?:, ?(?:{0}|\"[^\"]*\"|[0-9]+))*)'.format(self.regex_variables), r'\g<1>(\g<2>)', py_line)

            py_line = self.find_proper_variables(py_line)
            py_line = self.find_common_variables(py_line)

            line_named = self.find_named(py_line)
            self.most_recently_named = line_named if line_named else self.most_recently_named

            py_line = py_line.format(line_strings) if line_strings else py_line

            return line_ident + py_line + comments + '\n'
