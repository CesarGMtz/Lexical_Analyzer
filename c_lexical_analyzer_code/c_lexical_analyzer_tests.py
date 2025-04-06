import unittest
import ply.lex as lex
import c_lexical_analyzer

class TestKeywords(unittest.TestCase):
    def setUp(self):
        self.lexer = c_lexical_analyzer.getLexer()
        
    def test_basic_keyword(self):
        self.lexer.input('auto')
        token = self.lexer.token()
        self.assertEqual(token.type, 'KEYWORD')
        self.assertEqual(token.value, 'auto')
    
    def test_underscore_keyword(self):
        self.lexer.input('_Bool')
        token = self.lexer.token()
        self.assertEqual(token.type, 'KEYWORD')
        self.assertEqual(token.value, '_Bool')

if __name__ == '__main__':
    unittest.main()
