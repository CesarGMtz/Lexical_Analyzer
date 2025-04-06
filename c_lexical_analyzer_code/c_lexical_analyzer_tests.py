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

# Falta Predefined identifiers, y Universal character names
class TestIDs(unittest.TestCase):
    def setUp(self):
        self.lexer = c_lexical_analyzer.getLexer()
        
    def test_basic_ID(self):
        self.lexer.input('value')
        token = self.lexer.token()
        self.assertEqual(token.type, 'ID')
        self.assertEqual(token.value, 'value')
    
    def test_underscore_ID(self):
        self.lexer.input('_Value')
        token = self.lexer.token()
        self.assertEqual(token.type, 'ID')
        self.assertEqual(token.value, '_Value')
    
    def test_underscore_middle_ID(self):
        self.lexer.input('value_123')
        token = self.lexer.token()
        self.assertEqual(token.type, 'ID')
        self.assertEqual(token.value, 'value_123')
    
    def test_digit_ID(self):
        self.lexer.input('value123')
        token = self.lexer.token()
        self.assertEqual(token.type, 'ID')
        self.assertEqual(token.value, 'value123')

# Falta integer-suffix
class TestInts(unittest.TestCase):
    def setUp(self):
        self.lexer = c_lexical_analyzer.getLexer()
        
    def test_basic_decimal(self):
        self.lexer.input('1900')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, '1900')
    
    def test_basic_octal(self):
        self.lexer.input('07')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, '07')
        
    def test_basic_hexadecimal(self):
        self.lexer.input('0x1')
        token = self.lexer.token()
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, '0x1')

if __name__ == '__main__':
    unittest.main()
