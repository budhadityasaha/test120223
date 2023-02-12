
import sys,os
  
print("This is the name of the program:", sys.argv[0])
  
print("Argument List:", str(sys.argv))

print("sys.argv[1]:", sys.argv[1])

#print(os.path.dirname(__file__))		#this won't print anything (as the path is same as dir)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())


print(f'@@@@@@@@@ sys.path: {sys.path}')

fpath = os.path.join(os.path.dirname(__file__), 'schemas')
sys.path.append(fpath)

print(f'@@@@@@@@@ sys.path: {sys.path}')

print('script ends...')