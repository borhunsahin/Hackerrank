using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int N = int.Parse(Console.ReadLine());
        
        for(int i=0; i<N; i++)
        {
            string S = Console.ReadLine();
            
            string odd = "";
            string even = "";
            
            int counter = 0;
            
            foreach(char ch in S)
            {
                if(counter%2==0)
                {
                    even += ch;
                }
                else
                {
                    odd += ch;
                }
                
                counter++;
            }
            
            Console.WriteLine(even+" "+odd);
        }
    }
}
