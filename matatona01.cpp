#include <iostream>
using namespace std;
#define MAXN 100000
int p[MAXN+1], dp[MAXN+1]; 
int main() {
    int n, x, q, m, max_x = 0;    
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> x;
        p[x]++;
        max_x = max(max_x, x);
    }
    for(int i = 0; i < max_x; i++) {
        dp[i+1] = p[i+1] + dp[i];
    }
    cin >> q;
    while(q--) {
        cin >> m;
        if(m <= max_x) {
            cout << dp[m] << "\n";
        }
        else {
            cout << dp[max_x] << "\n";
        }
    }
    return 0;
}