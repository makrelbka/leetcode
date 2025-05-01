#include <string>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        map<char, int> dict = {{'0', 0}, {'1', 1}, {'2', 2}, {'3', 3}, {'4', 4}, 
                              {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9}};
        long res = 0;
        int sign = 1;
        int i = 0;
        long max = pow(2, 31);
        while (i < s.size() && s[i] == ' ') {
            i++;
            continue;
        }
        if (s[i] == '+' || s[i] == '-') {
            if (s[i] == '-') {
                sign = -1;
            }
            i++;
        }
        
        while (i < s.size() && dict.count(s[i]) != 0 ) {
            res = res * 10 + dict.find(s[i])->second;
            i++;
            if (sign * res < -max) {
                return -max;
            } 
            if (sign * res > max - 1) {
                return max - 1; 
            }
        }  
        return sign * res;
    }
};