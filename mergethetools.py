def merge_the_tools(string, k):
    # your code goes here
    s = int(len(string)/k)
    string = list(string)
    st = []
    for i in range(0, len(string), k):
        st = []
        for j in range(i, i+k):
            a = string[j]
            if(a not in st):
                st.append(a)
        print(*st,sep='')

        
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
