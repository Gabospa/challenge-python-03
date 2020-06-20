# Resolve the problem!!
import re   




def run():
    # Start coding here
    text = ''
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        text= f.read()
        
    message = re.findall(r'[a-z]+', text)    
    print(message)


if __name__ == '__main__':
    run()
