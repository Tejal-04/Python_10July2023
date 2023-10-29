'''# Write Mode
f = open('F:\\Data_Science\\Advance Python\\funny.txt','w')   
print('Successfully File Open in Writing Mode...')
f.write('I Love Python')
print('Successfully Write the Msg in File')
f.close()
print('Successfully File Close...')

# Append Mode
f = open('F:\\Data_Science\\Advance Python\\funny.txt','a')
print('Successfully Open the File in Append Mode...')
f.write(' I Love C++')
print('Successfully Append the Msg in File')
f.close()
print('Successfully Close the File...')

# Word Count in TXT File
f = open('F:\\Data_Science\\Advance Python\\funny.txt','r')
print('Successfully Open the File in Reading Mode...')
print(f.read())
print('Successfully Read the Words in File')
f.close()

# Read Line in file
f = open('F:\\Data_Science\\Advance Python\\funny1.txt','r')
print('Successfully Open the File in Reading Mode...')
for line in f:
    print(line)
print('Successfully Read the Lines in File')
f.close()

# Splitting Lines into the Array of Words
f = open('F:\\Data_Science\\Advance Python\\funny1.txt','r')
for line in f:
    tokens = line.split(' ')   
    #print(tokens)
    print(str(tokens))   # Returns array of words
    print(len(tokens))   # Returns len of words in array
f.close()''' 

f_out = open('F:\\Data_Science\\Advance Python\\funny1.txt','w')
print(f_out.write('I Love Python'))
f =  open('F:\\Data_Science\\Advance Python\\funny1.txt','r')
for line in f:
    tokens = line.split(' ')
    print(f_out.write('\nWord Count : ' + str(len(tokens)) + ' ' + line))
f.close()
f_out.close()

'''# With Statement(No need of f.close() flag write. It automatically closed the file.)
with open('F:\\Data_Science\\Advance Python\\funny1.txt','r') as f:
    print(f.read())
print(f.closed)   # This flag tells you if the file is closed or still open'''