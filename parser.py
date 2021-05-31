from rply import ParserGenerator
from ast import Number, Sum, Sub,Mul,Div,Print


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB','MUL','DIV'],
             # A list of precedence rules with ascending precedence, to
             # disambiguate ambiguous production rules.
            precedence=[
            ('left', ['SUM', 'SUB']),
            ('left', ['MUL', 'DIV'])
            ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])
        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            # p is a list of the pieces matched by the right hand side of the
            # rule
            # return Number(int(p[0].getstr()))
            return Number(self.builder, self.module, int(p[0].getstr()))

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_parens(p):
            return p[1]
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if p[1].gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)
            else:
                raise AssertionError('Oops, this should not be possible!')

            # if operator.gettokentype() == 'SUM':
            #     return Sum(self.builder, self.module, left, right)
            # elif operator.gettokentype() == 'SUB':
            #     return Sub(self.builder, self.module, left, right)

        # @self.pg.production('expression : NUMBER')
        # def number(p):
        #     return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
