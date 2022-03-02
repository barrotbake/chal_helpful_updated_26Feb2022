#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

#include "utils.h"


int challenge_2() { 
  std::cout << "\nCHALLENGE 2 ..................\n";
  char src1[] = "1c0111001f010100061a024b53535009181c";
  char src2[] = "686974207468652062756c6c277320657965";

  char hexsrc1[BUFSIZ];
  char hexsrc2[BUFSIZ];
  memset(hexsrc1, 0, sizeof(hexsrc1));
  memset(hexsrc2, 0, sizeof(hexsrc2));
  hex_decoded(src1, hexsrc1, strnlen(src1, BUFSIZ));
  hex_decoded(src2, hexsrc2, strnlen(src2, BUFSIZ));

  char result[BUFSIZ];
  memset(result, 0, sizeof(result));

  char xor_dst[BUFSIZ];
  memset(xor_dst, 0, sizeof(xor_dst));

  int n = strnlen(src1, BUFSIZ);
  block_xor(hexsrc1, hexsrc2, xor_dst, n);

  // convert two nibbles (4 bits each) back to two hex characters
  // e.g., the eight bit character:  01110100 splits to
  //       0111 0100 --->  '7' and '4'
  int mask = 15;                                      // only want 4 bits at a time
  for (int i = 0; i < n/2; ++i) { 
    // std::cout << tobinary_8(xor_dst[i]) << "\n";
    result[2 * i] = hex_char((xor_dst[i] >> 4) & mask);     // convert to hex
    result[2 * i + 1] = hex_char(xor_dst[i] & mask);
  }

  std::cout << "\nAfter block_xor...\n";
  std::cout << result << "\n\n";

  return 0;
}
