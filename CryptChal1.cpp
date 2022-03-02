#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

#include "utils.h"


int challenge_1() {
  std::cout << "\nCHALLENGE 1 ..................\n";

  char hexbuf[] = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
  char decbuf[BUFSIZ];
  char base64_buf[BUFSIZ];

  memset(decbuf, 0, sizeof(decbuf));
  memset(base64_buf, 0, sizeof(base64_buf));
  int n = strlen(hexbuf);
  hex_decoded(hexbuf, decbuf, n);

  // for (int i = 0, j = 0; i < n; i += 2, ++j) { 
  //   decbuf[j] = dec_value(hexbuf[i]) << 4 | dec_value(hexbuf[i + 1]); 
  // }
  // std::cout << "\nOriginal data...\n";
  // for (int i = 0; i < n; ++i) { 
  //   std::cout << hexbuf[i];  
  //   if (i % 6 == 5) { 
  //     std::cout << " "; 
  //   } 
  // }  

  // std::cout << "\n\nHex conversion... (hexbuf[0] << 4 | hexbuf[1]  hexbuf[2] << 4 | hexbuf[3])...)\n";
  // for (int i = 0; i < n/2; ++i) { 
  //   std::cout << tobinary_8(decbuf[i]) << " "; 
  // }  
  // std::cout << "\n";
  
  // std::cout << "strlen(decbuf) is: " << strlen(decbuf) << "\n";
  std::cout << "\nBase64 conversion...\n";
  convert_to_base64(decbuf, base64_buf, strlen(decbuf));
  std::cout << base64_buf << "\n\n";
  
  return 0;
}

