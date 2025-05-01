#include <string>
#include <iostream>
#include <algorithm>


using namespace std;

class Solution {
    public:
        int minimumTimeToInitialState(string word, int k) {
            int sec = 0;
            int len_word = word.length();
            string start_word = word;
            while (true) {
                sec++;
                if (len_word - sec*k <= 0) {
                    break;
                }
                size_t part = len_word - sec*k + 1;
                word = word.substr(k);
                if (start_word.substr(0, min(part, word.length())) == word) {
                    break;
                }
            }
            return sec;
        }    
    };

int main() {
    Solution s;
    cout << s.minimumTimeToInitialState("abacaba", 3) << endl ;
}