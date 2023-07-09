def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    #x=[]
    #for i in data:
        #x.append (list(i))
    data=data.split( )
    return  (list(data))
# Read data from file
f = open("data/data01.txt", "r")
data = f.read()
f.close
print(main(data))