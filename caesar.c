#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

string encipher(int y, string x);

int main(int argc, string argv[])
{

    if (argc == 2)
    {
        for(int i=0;i<strlen(argv[1]);i++)
        {
            if(isdigit(argv[1][i])==0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }

        }
        int key=atoi(argv[1]);
        string plain=get_string("plaintext: ");
        string cipher=encipher(key, plain);
        printf("ciphertext: %s\n", cipher);
    }

    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

}

string encipher(int y, string x)
{
    for(int i=0;i<strlen(x);i++)
    {
        if(islower(x[i])!=0)
        {
             x[i]-=97;
             x[i]=(x[i]+ y)%26;
             x[i]+=97;
        }
        else if(isupper(x[i])!=0)
        {
             x[i]-=65;
             x[i]=(x[i]+ y)%26;
             x[i]+=65;
        }
    }
    return x;
    printf("%s\n", x);
}
