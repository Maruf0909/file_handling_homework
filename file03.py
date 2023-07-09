def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    i=0
    for i in data:
        if i>='0' and i<='9':
            list.append(i)
    return list


# Read data from file
f = open("data/data03.txt",encoding='utf8')
data = f.read()
f.close
print(main(data))
