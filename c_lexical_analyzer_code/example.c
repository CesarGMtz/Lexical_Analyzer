// test_identifiers.c (GENERADO CON CHATGPT)
#include <wchar.h>

// === IDENTIFIERS ===
int _underscore;
int a;
int L;
int myVar1;
int Another_Var123;
int _9startsWithUnderscoreAndDigit;
int café;     // Accented character (e.g. \u00E9)
int __doubleUnderscore;

// === UNIVERSAL CHARACTER NAMES ===
// In identifiers (allowed since C99)
int \u03B1 = 10;              // α
int \u4E2D\u6587 = 20;        // 中文 (Chinese)
int \U0001F600 = 30;         // 😀
int \u03A9\U0001F44D = 40; // Ω

// === INTEGER CONSTANTS ===
// Decimal constants
int dec1 = 1;               // nonzero-digit
int dec2 = 123456789;       // decimal-constant with multiple digits

// Octal constants
int oct1 = 0;               // zero
int oct2 = 01234567;        // full range of octal digits

// Hexadecimal constants
int hex1 = 0x1;             // minimal hex
int hex2 = 0XABCDEF;        // hex with uppercase letters
int hex3 = 0xabcdef;        // hex with lowercase letters
int hex4 = 0x123456789;     // hex with digits

// Integer constants with suffixes
int u1 = 100U;              // unsigned
int u2 = 200u;              // unsigned (lowercase)
long l1 = 300L;             // long
long l2 = 400l;             // long (lowercase)
long long ll1 = 500LL;      // long long
long long ll2 = 600ll;      // long long (lowercase)
unsigned long ul1 = 700UL;  // unsigned + long
unsigned long ul2 = 800lu;  // long + unsigned (mixed case)
unsigned long long ull1 = 900LLU; // unsigned + long long
unsigned long long ull2 = 1000ull; // unsigned + long long (lowercase)

// === FLOATING CONSTANTS ===
// Decimal floating constants (fractional-constant)
float f1 = .123;               // digit-sequenceopt . digit-sequence
float f2 = 123.;               // digit-sequence .
float f3 = 1.23;               // digit-sequence . digit-sequence
float f4 = 1.23e10;            // exponent part: e + digits
float f5 = 1.23E-10;           // exponent part: E - digits
float f6 = 123e+2;             // digit-sequence exponent-part
float f7 = 3.14f;              // with suffix f
float f8 = 2.71F;              // with suffix F
double f9 = 6.022e23l;         // with suffix L
double f10 = 6.022e23L;         // with suffix L

// Hexadecimal floating constants (C99 feature)
double hf1 = 0x1.1p1;          // hexadecimal-fractional-constant with binary exponent
double hf2 = 0X.8p+2;          // fractional: .digit, binary exponent
double hf3 = 0x10.0P-1;        // hex digit . digit + binary exponent
double hf4 = 0xABC.DEFp0;      // hex-fractional with binary exponent
float hf5 = 0x1.0p2f;          // with suffix f
float hf6 = 0x1.0p2F;          // with suffix F
double hf7 = 0x1.0p2l;         // with suffix L
double hf8 = 0x1.0p2L;         // with suffix L

// === CHARACTER CONSTANTS ===
// Single characters
char ch1 = 'a';           // basic character
char ch2 = 'Z';           // another normal char

// Multicharacter constant (implementation-defined but valid C)
int ch3 = 'ab';           // 2-character constant
int ch4 = 'ABC';          // 3-character constant

// Wide character
wchar_t wch1 = L'x';      // wide character

// Simple escape sequences
char esc1 = '\'';         // single quote
char esc2 = '\"';         // double quote
char esc3 = '\?';         // question mark
char esc4 = '\\';         // backslash
char esc5 = '\a';         // alert/bell
char esc6 = '\b';         // backspace
char esc7 = '\f';         // form feed
char esc8 = '\n';         // newline
char esc9 = '\r';         // carriage return
char esc10 = '\t';        // horizontal tab
char esc11 = '\v';        // vertical tab

// Octal escape sequences
char octesc1 = '\0';      // null character
char octesc2 = '\07';     // octal single digit
char octesc3 = '\123';    // octal 3-digit

// Hexadecimal escape sequences
char hexesc1 = '\xA';     // hex single digit
char hexesc2 = '\x1F';    // hex two digits
char hexesc3 = '\x7F';    // hex boundary test

// Universal character names
char uni1 = '\u03B1';     // Greek alpha
char uni2 = '\U0001F600'; // 😀 emoji

// === STRING LITERALS ===
// Basic string
char* str1 = "Hello, world!";
char* str2 = "";                  // Empty string (s-char-sequenceopt)
char* str3 = "Multiple words 123";

// Escape sequences
char* str4 = "Line 1\nLine 2";     // \n newline
char* str5 = "Tab\tDelimited";     // \t tab
char* str6 = "Quote: \"text\"";    // \" escaped quote
char* str7 = "Backslash: \\";      // \\ backslash
char* str8 = "Bell\aBackspace\b";  // \a and \b
char* str9 = "FormFeed\fCarriage\rReturn";

// Octal and Hexadecimal escapes
char* str10 = "\123";             // Octal escape
char* str11 = "\x41";             // Hexadecimal escape (A)

// Universal character names (C99+)
char* str12 = "\u03B1";           // Greek alpha
char* str13 = "\U0001F600";       // 😀 emoji

// Wide string literals
wchar_t* wstr1 = L"Wide Hello";
wchar_t* wstr2 = L"\n\t\u03B1";

// Concatenated string literals (valid in C)
char* str14 = "Hello, " "world!";
wchar_t* wstr3 = L"Wide " L"concat";

// String with all escape types
char* str15 = "Mix: \a\b\f\n\r\t\v\\\'\"\123\x41\u03B1\U0001F600";

int main() {
    return 0;
}