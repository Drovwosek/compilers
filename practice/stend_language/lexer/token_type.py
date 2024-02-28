from enum import Enum

class TokenType(Enum):
    STRING_TYPE = 6
    INT_TYPE = 7
    FLOAT_TYPE = 8
    BOOLEAN_TYPE = 9
    CHAR_TYPE = 10
    FLOAT = 28
    NUMBER = 29
    STRING = 30
    CHAR = 31
    CONST = 2
    NOC = 3
    VAR = 4
    RAV = 5
    IDENTIFIER = 27
    ASSIGN = 25
    SEMICOLON = 26
    STAR = 36
    PLUS = 37
    MINUS = 38
    SLASH = 39
    OR = 24
    LPAREN = 32
    RPAREN = 33
    GREATER_THAN = 42
    GREATER_OR_EQUAL_THAN = 43
    LESS_THAN = 44
    LESS_OR_EQUAL_THAN = 45
    DIV = 11
    MOD = 12
    NOT = 13
    AND = 50
    EQUAL = 51
    NOT_EQUAL = 52
    START = 0
    FINISH = 1
    LBRACE = 40
    RBRACE = 41