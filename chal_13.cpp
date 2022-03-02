#include <iostream>
#include <map>

#include "utils.h"


int challenge_3() {
  std::cout << "\nCHALLENGE 3 ..................\n";
  char src[] = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
  int n = strnlen(src, BUFSIZ);
  char* xor_dst = get_bufn(src, n);
  decode_single_char_xor(src, xor_dst, n);
  print_array("   ", xor_dst, n/2);

  std::cout << "\n";

  return 0;
}
 