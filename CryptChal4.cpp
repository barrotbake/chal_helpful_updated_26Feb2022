#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
#include "challenge_3.h"
#include "utils.h"

int challenge_5(){
    std::cout << "\nCHALLENGE 5 ..................\n";
    string cypherStr = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal";
    char cipher = 'b';
    for(int i; i < cypherStr.length(); i++){
        block_xor(cypherStr[i]); 
    } 
    return 0;
}