#include <iostream>
using namespace std;
int fibonacci_naive(int n) {
    if (n <= 1)
        return n;

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

int fibonacci_fast(int n) {
    int prev = 0, next = 1, ans;
    if(n==0) return prev;
    for(int i=2; i<=n ; i++){
        ans = prev + next;
        prev = next;
        next = ans;
    }

    return next;
}

int main() {
    int n = 0;
    cin >> n;
    cout << fibonacci_fast(n) << '\n';
    return 0;
}
