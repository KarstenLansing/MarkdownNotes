
//  make request to https://swapi.dev/api/starships/3/ and print response without curl
#include <iostream>
#include <string>


using namespace std;

int main() {
    string url = "https://swapi.dev/api/people/1/";
    string cmd = "curl -s -X GET " + url;
    FILE *fp = popen(cmd.c_str(), "r");
    if (fp == NULL) {
        cout << "Failed to run command" << endl;
        return -1;
    }
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        cout << buffer;
    }
    pclose(fp);
    return 0;
}
