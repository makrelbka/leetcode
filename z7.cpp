#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        long res = 0;
        bool flag = false;
        if (x < 0) {
            flag = true;
            x *= -1;
        }
        while (x > 0) {
            res = (res * 10) + (x % 10);
            x /= 10;   
        }
        if (flag) {
            res *= -1;
        }
        if (res < -(1LL << 31) || res > ((1LL << 31) - 1)) {
            return 0;
        }
        return res;
    }
};

int main() {
    Solution a;
    cout << a.reverse(-123);
}