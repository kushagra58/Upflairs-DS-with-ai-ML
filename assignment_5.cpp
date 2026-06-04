// peterson number

#include <iostream>
using namespace std;

int factorial(int n) {
    int fact = 1;
    for(int i = 1; i <= n; i++)
        fact *= i;
    return fact;
}

int main() {
    int num, temp, sum = 0;
    cin >> num;

    temp = num;

    while(temp > 0) {
        int digit = temp % 10;
        sum += factorial(digit);
        temp /= 10;
    }

    if(sum == num)
        cout << "Peterson Number";
    else
        cout << "Not a Peterson Number";

    return 0;
}


// circular prime number


#include <iostream>
#include <string>
using namespace std;

bool isPrime(int n) {
    if(n < 2) return false;

    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0)
            return false;
    }
    return true;
}

int main() {
    int num;
    cin >> num;

    string s = to_string(num);
    bool circularPrime = true;

    for(int i = 0; i < s.length(); i++) {
        int rotated = stoi(s);

        if(!isPrime(rotated)) {
            circularPrime = false;
            break;
        }

        s = s.substr(1) + s[0];
    }

    if(circularPrime)
        cout << "Circular Prime";
    else
        cout << "Not a Circular Prime";

    return 0;
}


// Harshad number


#include <iostream>
using namespace std;

int main() {
    int num, temp, sum = 0;
    cin >> num;

    temp = num;

    while(temp > 0) {
        sum += temp % 10;
        temp /= 10;
    }

    if(num % sum == 0)
        cout << "Harshad Number";
    else
        cout << "Not a Harshad Number";

    return 0;
}



// magic number


#include <iostream>
using namespace std;

int digitSum(int n) {
    int sum = 0;

    while(n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int num;
    cin >> num;

    while(num > 9) {
        num = digitSum(num);
    }

    if(num == 1)
        cout << "Magic Number";
    else
        cout << "Not a Magic Number";

    return 0;
}


// generate pascal triangle

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++) {
        int num = 1;

        for(int space = 0; space < n - i - 1; space++)
            cout << " ";

        for(int j = 0; j <= i; j++) {
            cout << num << " ";
            num = num * (i - j) / (j + 1);
        }

        cout << endl;
    }

    return 0;
}

// duck number


#include <iostream>
#include <string>
using namespace std;

int main() {
    string num;
    cin >> num;

    bool duck = false;

    for(int i = 1; i < num.length(); i++) {
        if(num[i] == '0') {
            duck = true;
            break;
        }
    }

    if(duck)
        cout << "Duck Number";
    else
        cout << "Not a Duck Number";

    return 0;
}