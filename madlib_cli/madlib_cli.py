import re
def welcome_msg():
    try:
        print("""
    ****************************************
             Welcome to madlib            
     This is a phrasal template word game 
     where one player prompts others for  
     a list of words to substitute for    
     blanks in a story before reading     
      aloud.                              
    ****************************************
    """)
    except Exception as e :
        print(f"THERE IS AN ERROR in welcome_msg, IS {e}")
    return print


def read_template():
   
    try:
        with open('./files/test.txt','r') as file :
            contents=file.read()
        print("Is the file Closed? " , file.closed)
        return contents

    except Exception as e:
        print(f"THERE IS AN ERROR in read_template, IS {e}")
    

def read_template2(path):
   
    try:
        with open(path,'r') as file :
            contents=file.read()
        print("Is the file Closed? " , file.closed)
        return contents

    except Exception as e:
        print(f"THERE IS AN ERROR in read_template, IS {e}")

def copy_file():
  
    try:
        with open('./files/example-copy.txt','w') as file2 :
            file2.write(read_template())
        print("Is the file Closed? " , file2.closed)
        return print("\ncopy_file:\n",file2.write(read_template()))
    except Exception as e:
        print(f"THERE IS AN ERROR in copy_file, IS {e}")


def parse(text):
    placeholders = re.findall(r"\{(.*?)\}", text)
    words = re.sub(r"\{(.*?)\}", "$", text)
    return words, placeholders

def  merge(words, user_words):
    for word in user_words:
        words = words.replace("$", word, 1)
    return(words)


if __name__ == "__main__":
    text = read_template()
    words, placeholders = parse(text)
    user_words = []
    for placeholder in placeholders:
        user_words.append(input(f"Enter a {placeholder}: "))
    result = merge(words, user_words)
    f = open("./files/result.txt", "w")
    f.write(result)
    print("******* The result : ************")
    print(result)