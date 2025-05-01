#include <string>
#include <map>
#include <iostream>

using namespace std;


class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        long y = 1;
        int len = 1;
        while (x >= y * 10) {
            y = y * 10;
            len++;
        }
        
        len = len / 2;
        while (len > 0) {
            if (x / y != x % 10) {
                return false;
            } else {
                x = (x % y) / 10;
                y /= 100;
                len--;
            }
        }
        return true;   
    }
};

int main() {
    Solution s;
    cout << s.isPalindrome(99999) << endl;
    return 0;
}