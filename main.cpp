#include "challenge_1.h"
#include "challenge_2.h"
#include "challenge_3.h"
#include "challenge_4.h"
#include "challenge_5.h"
#include "utils.h"

#include <cstdlib>
#include <iostream>

void run_conversion_tests() { 
  test_tobinary_8();  
  test_toascii_frombinary();
  test_HexToBinary();
  test_BinaryToHex();
  test_AsciiToBinary();
  test_BinaryToText();
  test_BinaryToBase64();
}


int main(int argc, const char* argv[]) {
  if (argc != 2) { 
    std::cerr << "Usage: ./main <1-5>\n";  
    exit(-1); 
  }
  int choice = atoi(argv[1]); 

  switch(choice) { 
    case 1:  challenge_1();  break;
    case 2:  challenge_2();  break;
    // case 3:  challenge_3();  break;
    // case 4:  challenge_4();  break;
    // case 5:  challenge_5();  break;
    default: std::cerr << "Error -- choice " << choice << "not recognized\n";  break;
  } 

  // run_conversion_tests();

  return 0;
}
