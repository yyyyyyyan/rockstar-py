import re


class Transpiler(object):
    SIMPLE_VARIABLE_FMT = r"\b[A-Za-z]+\b"
    COMMON_VARIABLE_FMT = r"\b(?:[Aa]n?|[Tt]he|[Mm]y|[Yy]our) [a-z]+\b"
    PROPER_VARIABLE_FMT = r"\b[A-Z][A-Za-z]*(?: [A-Z][A-Za-z]*)*\b"
    REGEX_VARIABLES = r"(?:{}|{}|{})".format(COMMON_VARIABLE_FMT, PROPER_VARIABLE_FMT, SIMPLE_VARIABLE_FMT)
    QUOTE_STR_FMT = r"\"[^\"]*\""

    def __init__(self):
        self.indentation_style = " " * 4
        self._current_indentation = 0
        self.in_function = False
        self.globals = set()
        self.most_recently_named = ""
        self.simple_subs = {
            "(": "#",
            ")": "",
            "Give back": "return",
            "Take it to the top": "continue",
            "Break it down": "break",
            " false ": " False ",
            " wrong ": " False ",
            " no ": " False ",
            " lies ": " False ",
            " null ": " False ",
            " nothing ": " False ",
            " nowhere ": " False ",
            " nobody ": " False ",
            " empty ": " False ",
            " gone ": " False ",
            " mysterious ": " False ",
            " true ": " True ",
            " right ": " True ",
            " yes ": " True ",
            " ok ": " True ",
            " plus ": " + ",
            " with ": " + ",
            " minus ": " - ",
            " without ": " - ",
            " times ": " * ",
            " of ": " * ",
            " over ": " / ",
            " is higher than ": " > ",
            " is greater than ": " > ",
            " is bigger than ": " > ",
            " is stronger than ": " > ",
            " is lower than ": " < ",
            " is less than ": " < ",
            " is smaller than ": " < ",
            " is weaker than ": " < ",
            " is as high as ": " >= ",
            " is as great as ": " >= ",
            " is as big as ": " >= ",
            " is as strong as ": " >= ",
            " is as low as ": " <= ",
            " is as little as ": " <= ",
            " is as small as ": " <= ",
            " is as weak as ": " <= ",
            " is not ": " != ",
            " aint ": " != ",
            "Until ": "while not ",
            "While ": "while ",
        }

    @property
    def current_indentation(self):
        return self._current_indentation

    @current_indentation.setter
    def current_indentation(self, value):
        self._current_indentation = value if value > 0 else 0

    def get_comments(self, line):
        comment_match = re.search(r"\((.*)\)", line)
        if comment_match:
            line = line.replace(comment_match.group(), "")
            comment = " # " + comment_match.group(1)
        elif "(" in line or ")" in line:
            raise SyntaxError("Missing parentheses in comment")
        else:
            comment = ""
        return line, comment

    def create_function(self, line):
        match = re.match(
            r"\b({0}) takes ({0}(?: and {0})*)\b".format(self.REGEX_VARIABLES), line
        )
        if match:
            self.current_indentation += 1
            line = "def {}({}):".format(
                match.group(1), match.group(2).replace(" and", ",")
            )
            self.in_function = True
        return line

    def create_while(self, line):
        if line.startswith("while "):
            line = line.replace(" is ", " == ")
            line += ":"
            self.current_indentation += 1
        return line

    def create_if(self, line):
        match = re.match(r"If .*", line)
        if match:
            self.current_indentation += 1
            line = line.replace(" is ", " == ")
            line = line.replace("If", "if")
            line += ":"
        return line

    def replace_let_be_with_is(self, line):
        match = re.match(r"Let ({0}) be (.+)".format(self.REGEX_VARIABLES), line)
        if match:
            return match.group(1) + " is " + match.group(2)
        return line

    def find_poetic_number_literal(self, line):
        poetic_type_literals_keywords = ["True", "False"]
        match = re.match(
            r"\b({0})(?: is|\'s| was| were) ([\d\w\.,\:\!\;\'\-\s]+)".format(
                self.REGEX_VARIABLES
            ),
            line,
        )
        if match and match.group(2).split()[0] not in poetic_type_literals_keywords:
            line = "{} = ".format(match.group(1))
            for word_number in match.group(2).split():
                if re.match(r"\d+", word_number):
                    line += str(word_number)
                else:
                    period = "." if word_number.endswith(".") else ""
                    alpha_word = re.sub(r"[^A-Za-z\-]", "", word_number)
                    line += str(len(alpha_word) % 10) + period
        return line

    def find_variables(self, line, fmt, clean_func=str):
        variables = set(re.findall(fmt, line))
        if variables:
            for variable in variables:
                line = re.sub(r"\b{}\b".format(variable), clean_func(variable).replace(" ", "_"), line)
        return line

    def find_proper_variables(self, line):
        return self.find_variables(line, self.PROPER_VARIABLE_FMT, lambda variable: variable.title())

    def find_common_variables(self, line):
        return self.find_variables(line, self.COMMON_VARIABLE_FMT, lambda variable: variable.lower())

    def find_named(self, line):
        match = re.match(r"([A-Za-z]+(?:_[A-Za-z]+)*) [+-]?= .+", line)
        if match:
            return match.group(1)

    def get_strings(self, line):
        strings = dict()
        says_match = re.match(r"({}) says (.*)".format(self.REGEX_VARIABLES), line)
        if says_match:
            line = says_match.group(1) + ' = {str_0}'
            strings["str_0"] = '"{}"'.format(says_match.group(2).replace('"', r'\"'))
            return line, strings
        else:
            for str_number, string in enumerate(re.findall(self.QUOTE_STR_FMT, line)):
                fmt_var = f"str_{str_number}"
                line = re.sub(self.QUOTE_STR_FMT, f"{{str_{str_number}}}", line, 1)
                strings[fmt_var] = string
        return line, strings

    def transpile_line(self, line):
        if line == "\n":
            self.current_indentation -= 1
            return ""
        else:
            line_ident = self.indentation_style * self.current_indentation
            self.in_function = False if self.current_indentation == 0 else self.in_function

            py_line, line_strings = self.get_strings(line)
            py_line, comments = self.get_comments(py_line)

            for key in self.simple_subs:
                py_line = py_line.strip()
                py_line += " "
                py_line = py_line.replace(key, self.simple_subs[key])
            py_line = py_line.strip("\n ,.;")

            py_line = self.replace_let_be_with_is(py_line)
            py_line = self.find_poetic_number_literal(py_line)

            py_line = py_line.replace("'", "")

            for key in self.simple_subs:
                py_line = py_line.strip()
                py_line += " "
                py_line = py_line.replace(key, self.simple_subs[key])
            py_line = py_line.strip("\n ,.;")

            most_recently_named_keywords = [
                " it ",
                " he ",
                " she ",
                " him ",
                " her ",
                " them ",
                " they ",
                " ze ",
                " hir ",
                " zie ",
                " zir ",
                " xe ",
                " xem ",
                " ve ",
                " ver ",
            ]
            for keyword in most_recently_named_keywords:
                py_line = py_line.replace(
                    keyword, " {} ".format(self.most_recently_named)
                )

            py_line = self.create_function(py_line)
            py_line = self.create_while(py_line)
            py_line = self.create_if(py_line)
            line_ident = self.indentation_style * (self.current_indentation - 1) if py_line == "Else" else line_ident
            py_line = "else:" if py_line == "Else" else py_line

            py_line = re.sub(
                r"Put (.*) into ({})".format(self.REGEX_VARIABLES),
                r"\g<2> = \g<1>",
                py_line,
            )
            py_line = re.sub(
                r"Build ({}) up".format(self.REGEX_VARIABLES), r"\g<1> += 1", py_line
            )
            py_line = re.sub(
                r"Knock ({}) down(\, down)*".format(self.REGEX_VARIABLES),
                r"\g<1> -= " + str(1 + py_line.count(", down")),
                py_line,
            )
            py_line = re.sub(
                r"Listen to ({})".format(self.REGEX_VARIABLES),
                r"\g<1> = input()",
                py_line,
            )
            py_line = re.sub(
                r"(?:Say|Shout|Whisper|Scream) (.*)", r"print(\g<1>)", py_line
            )

            py_line = py_line.replace(" is ", " = ", 1)

            py_line = re.sub(
                r"({0}) taking ((?:{0}|\"[^\"]*\"|[0-9]+)(?:, ?(?:{0}|\"[^\"]*\"|[0-9]+))*)".format(
                    self.REGEX_VARIABLES
                ),
                r"\g<1>(\g<2>)",
                py_line,
            )

            py_line = self.find_proper_variables(py_line)
            py_line = self.find_common_variables(py_line)

            line_named = self.find_named(py_line)
            if line_named:
                self.most_recently_named = line_named
                if not self.in_function:
                    self.globals.add(line_named)
                elif line_named in self.globals:
                    py_line = f"global {line_named}\n" + line_ident + py_line

            py_line = py_line.format(**line_strings)

            return line_ident + py_line + comments + "\n"
