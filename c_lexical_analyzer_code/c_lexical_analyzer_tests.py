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

# Falta Predefined identifiers
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
        
# Falta floating-suffix
class TestFloats(unittest.TestCase):
    def setUp(self):
        self.lexer = c_lexical_analyzer.getLexer()
        
    def test_basic_decimal_float_fraction1(self):
        self.lexer.input('10.20')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '10.20')
    
    def test_basic_decimal_float_fraction2(self):
        self.lexer.input('.20')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '.20')
        
    def test_basic_decimal_float_fraction3(self):
        self.lexer.input('1.')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '1.')
        
    def test_basic_decimal_float_fraction4(self):
        self.lexer.input('1.e11')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '1.e11')
    
    def test_basic_decimal_float_digit1(self):
        self.lexer.input('1e10')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '1e10')
        
    def test_basic_decimal_float_digit2(self):
        self.lexer.input('1e+10')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '1e+10')
    
    def test_basic_hexadecimal_float_digit1(self):
        self.lexer.input('0X.23p32')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '0X.23p32')
    
    def test_basic_hexadecimal_float_digit2(self):
        self.lexer.input('0xAf.P32')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '0xAf.P32')
        
    def test_basic_hexadecimal_float_digit3(self):
        self.lexer.input('0xFFP32')
        token = self.lexer.token()
        self.assertEqual(token.type, 'FLOAT')
        self.assertEqual(token.value, '0xFFP32')
        
class TestChars(unittest.TestCase):
    def setUp(self):
        self.lexer = c_lexical_analyzer.getLexer()
        
    def test_basic_char(self):
        self.lexer.input("'ab'")
        token = self.lexer.token()
        self.assertEqual(token.type, 'CHAR')
        self.assertEqual(token.value, "'ab'")

class TestStrs(unittest.TestCase):
    def setUp(self):
        self.lexer = c_lexical_analyzer.getLexer()
        
    def test_basic_char(self):
        self.lexer.input('"ab"')
        token = self.lexer.token()
        self.assertEqual(token.type, 'STR')
        self.assertEqual(token.value, '"ab"')

if __name__ == '__main__':
    unittest.main()
    
# No voy a hacer Ennumeration constants por la combinación de palabra reservada con identifier "int Value"
# No considero los "\" en CHAR porque intervienen en el regex
# No considero los scap0e secuence, octal y hexadecimal chars por l,a dificultad en probralos