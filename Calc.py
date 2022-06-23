from sly import Lexer, Parser
import math
import gnureadline


class CalculatorLexer(Lexer):
    '''sly expression lexer'''
    # Set of token names
    tokens = {ID, NUMBER, DIV, SIN, ARCSIN, COS,
              ARCCOS, TG, ARCTG, CTG, ARCCTG, LOG, CHOOSE}

    literals = {'+', '-', '*', '/', '%', '^', '!', '(', ')'}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Ignored pattern
    ignore_newline = r'\n+'

    # Regular expression rules for tokens
    NUMBER = '(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['div'] = DIV
    ID['sin'] = SIN
    ID['arcsin'] = ARCSIN
    ID['cos'] = COS
    ID['arccos'] = ARCCOS
    ID['tg'] = TG
    ID['arctg'] = ARCTG
    ID['ctg'] = CTG
    ID['arcctg'] = ARCCTG
    ID['log'] = LOG
    ID['choose'] = CHOOSE


class CalculatorParser(Parser):
    '''sly expression parser'''

    # Get the token list from the lexer
    tokens = CalculatorLexer.tokens

    # string containing result of calculations
    result = ''

    # boolean variable that si true (false) if calculator does all internal calculations in degrees (radians)
    deg = True

    precedence = (
        ('left', "+", "-"),
        ('left', "*", "/", DIV, "%", CHOOSE),
        ('right', SIN, COS, TG, CTG, ARCSIN, ARCCOS, ARCTG, ARCCTG, LOG),
        ('right', "^"),
        ('right', UMINUS, UPLUS),
        ('left', "!")
    )

    # retrieving deg using getter
    def get_deg():
        '''getter method'''
        return self.deg

    # setting deg using setter
    def set_deg(self, bool):
        '''setter method'''
        self.deg = bool

    # retrieving result using getter
    def get_result(self):
        '''getter method'''
        return self.result

    # setting result using setter
    def set_result(self, str):
        '''setter method'''
        self.result = str

    # Grammar rules and actions

    @_('expr')
    def statement(self, p):
        self.set_result(str(p.expr))

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('expr "%" expr')
    def expr(self, p):
        return p.expr0 % p.expr1

    @_('expr DIV expr')
    def expr(self, p):
        return p.expr0//p.expr1

    @_('expr "^" expr')
    def expr(self, p):
        return p.expr0**p.expr1

    @_('expr CHOOSE expr')
    def expr(self, p):
        if (float(p.expr0) - int(float(p.expr0)) == 0) and (float(p.expr1) - int(float(p.expr1)) == 0):
            return math.comb(int(p.expr0), int(p.expr1))
        else:
            return math.comb(p.expr0, p.expr1)

    @_(' "-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_(' "+" expr %prec UPLUS')
    def expr(self, p):
        return p.expr

    @_('expr "!"')
    def expr(self, p):
        if float(p.expr) - int(float(p.expr)) == 0:
            return math.factorial((int(p.expr)))
        else:
            return math.factorial(p.expr)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return float(p.NUMBER)

    @_('SIN expr')
    def expr(self, p):
        if not self.deg:
            return math.sin(p.expr)
        else:
            return math.sin(math.radians(p.expr))

    @_('COS expr')
    def expr(self, p):
        if not self.deg:
            return math.cos(p.expr)
        else:
            return math.cos(math.radians(p.expr))

    @_('TG expr')
    def expr(self, p):
        if not self.deg:
            return math.tan(p.expr)
        else:
            return math.tan(math.radians(p.expr))

    @_('CTG expr')
    def expr(self, p):
        if not self.deg:
            return 1 / math.tan(p.expr)
        else:
            return 1 / math.tan(math.radians(p.expr))

    @_('LOG expr "(" expr ")" ')
    def expr(self, p):
        return math.log(p.expr1, p.expr0)

    @_('ARCSIN expr')
    def expr(self, p):
        if not self.deg:
            return math.asin(p.expr)
        else:
            return math.degrees(math.asin(p.expr))

    @_('ARCCOS expr')
    def expr(self, p):
        if not self.deg:
            return math.acos(p.expr)
        else:
            return math.degrees(math.acos(p.expr))

    @_('ARCTG expr')
    def expr(self, p):
        if not self.deg:
            return math.atan(p.expr)
        else:
            return math.degrees(math.atan(p.expr))

    @_('ARCCTG expr')
    def expr(self, p):
        if not self.deg:
            return math.pi/2-math.atan(p.expr)
        else:
            return math.degrees(math.pi/2-math.atan(p.expr))

    def error(self, token):
        '''Error handling rule'''
        if token:
            lineno = getattr(token, "lineno", 0)
            if lineno:
                raise Exception(
                    f"sly: Syntax error at line {lineno}, token={token.type}")
            else:
                raise Exception(f"sly: Syntax error, token={token.type}")
        else:
            raise Exception("sly: Parse error in input. EOF")


class Calculator:
    '''Calculator class'''
    lexer = CalculatorLexer()
    parser = CalculatorParser()

    expr = ""

    # retrieving deg using getter
    def get_deg(self):
        '''getter method'''
        return self.parser.get_deg()

    # setting deg using setter
    def set_deg(self, bool):
        '''setter method'''
        self.parser.set_deg(bool)

    # retrieving expr using getter
    def get_expr(self):
        '''getter method'''
        return self.expr

    # setting expr using setter
    def set_expr(self, str):
        '''setter method'''
        self.expr = str

    # retrieving result using getter
    def get_result(self):
        '''getter method'''
        if self.expr:
            try:
                self.parser.parse(self.lexer.tokenize(self.expr))

            finally:
                if self.parser.get_result() != '':
                    result = self.parser.get_result()
                    self.parser.set_result('')
                    self.set_expr('')
                    return result
                else:
                    return 'Error!'


if __name__ == '__main__':
    calc = Calculator()

    while True:

        try:
            expression = input('calc > ')
        except EOFError:
            break

        if expression:
            calc.set_expr(expression)
            print('calc > {}'.format(calc.get_result()))
