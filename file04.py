def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x=[]
    i=0
    num=['0','1','2','3','4','5','6','7','8','9']
    for i in data:
        if i not in num:
            x.append(i)
    return x
    
# Read data from file
f=open("data/data04.txt","r")
data=f.read()
f.close
print(main(data))