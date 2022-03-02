#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

#include "utils.h"

int challenge_3(){
    std::cout << "\nCHALLENGE 3 ..................\n";
    char hexbuf[] = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
    char decmsg[BUFSIZ];
    for(int i = 0; i < 256; i++){
        decode_single_char_xor(hexbuf, decmsg, 1);
    }
    cout << decmsg;
    return 0;
}