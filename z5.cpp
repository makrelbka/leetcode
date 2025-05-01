#include <string>
#include <iostream>


using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int start;
        int end;
        int max_len = -1;
        int len1;
        int len2;
        for (int i = 0; i < s.length(); i++) {
            len1 = pal_len(s, i, i);
            len2 = pal_len(s, i, i + 1);
            if (max_len < len1) {
                start = i - (len1 - 1) / 2;
                end = i + (len1 - 1) / 2;
                max_len = len1;
            }
            if (max_len < len2) {
                start = i - len2 / 2 + 1;
                end = i + len2 / 2;
                max_len = len2;
            }
        }
        string res = s.substr(start, end - start + 1);
        return res;
    }

private:
    int pal_len(string& s, int l, int r) {
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            l--;
            r++;
        }
        return r - l - 1;
    }
};

int main() {
    Solution a;
    cout << a.longestPalindrome("ababc") << endl;
}
