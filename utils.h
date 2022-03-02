#ifndef __UTILS_H__
#define __UTILS_H__

#include <string>

std::string AsciiToBinary(std::string Ascii);

std::string BinaryToBase64(std::string Binary); 

std::string BinaryToHex(std::string Binary);

std::string BinaryToText(std::string Binary);

std::string HexToBinary(std::string Hex);

void print_array(const char* msg, const char* s, int n);

void print_binary_dec_ascii(unsigned x);

void print_binary_dec_base64(const char* msg, unsigned x);

void print_binary_dec(const char* msg, unsigned x);

void print_binary(const char* msg, unsigned x);


int getbit(unsigned x, unsigned n);

char* tobinary(unsigned long x, int bits);
char* tobinary_4(unsigned long x);
char* tobinary_8(unsigned long x);
char* tobinary_16(unsigned long x);
char* tobinary_24(unsigned long x);
char* tobinary_32(unsigned long x);

char tobase64(char c); 
void convert_to_base64(const char* src, char* dst, int n);

char hex_char(char value);
char dec_value(char hex);

char toascii_frombinary(char* s);

void hex_decoded(const char* src, char* dst, int n, bool show=true);
void block_xor(const char* src1, const char* src2, char* dst, int n);
void key_xor(const char* src, char* dst, char key, int n);

char* get_bufn(const char* s, int n);

bool unlikely_chars(char c);

int character_count(const char* s, int n);


char decode_single_char_xor(const char* src, char* dst, int n);


void test_character_count();


void test_base64();
void test_hex_char();
void test_dec_value();
void test_hexdecoded();

void test_AsciiToBinary();
void test_BinaryToText();
void test_BinaryToBase64();

void test_tobinary_8();
void test_toascii_frombinary() ;

void test_BinaryToHex();
void test_HexToBinary();

#endif