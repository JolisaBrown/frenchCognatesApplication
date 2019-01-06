from PyDictionary import PyDictionary
dictionary= PyDictionary()
from pylev import pylev
import difflib
import sys
#from xgoogle.translate import Translator
#from difflib_data import*

#BeautifulSoup(html, "html.parser")

######make all the error messages temporarily disappear so stufff can be pretty
class DevNull:
    def write(self, msg):
       pass
sys.stderr = DevNull()


#import goslate
#gs = goslate.Goslate()
#print(gs.translate('hello world', 'fr'))


print ("Bonjour le monde")
#english= input("Put in an english word for the translation and a cognate:  ")
#translate= Translator().translate
#print (translate(english, lang_to="fr"))


french= input("Put in a french word for an english cognate:  ")


##french translation

##########wishful thiinking! CANNNN BEE SALVAGED!##
#english= input("Put in an english word for the translation and a cognate:  ")
#print (dictionary.meaning(english))
#dictionary.translate(english,'fr')
#french= dictionary.translate(english,'fr')


liresults=[]
with open('wordsEng.txt', 'r')as inputfile:
    for line in inputfile:
        liresults.append(line.strip().split(','))
        #print (liresults)

#list of 26 brackets to represent each letter of the alphabet, "a" has a value of 1
words = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for result in liresults:
    #determine the letter that the word in list Eng begins with and then add words to that list at the beginning
    words[ord(result[0][0])-ord('a')].append(result[0])





########time to start the comparisons

formerdistance=30
#open the list with the matching first letter and begin the comparison
candidates= []
for word in words[(ord(french[0])-ord('a'))]:
    # get the distance from your word
    distance = pylev.levenshtein(french, word)
    # if the edit distance is less than the lowest edit distance
    if distance< formerdistance:
        # set the lowest edit distance to be this edit distance
        formerdistance=distance
        # add this word to a NEW list of candidates (as opposed to the old list)
        candidates=[word]
    # if the edit distance is equal to the lowest edit distance
    elif distance==formerdistance:                    
        # add this word to the current list of candidates
        candidates.append(word)
    # else the edit distance is greater than the lower edit distance and we just want to move on
    else:
        continue
print ("")
print(candidates)
print ("")

# now that we have a list of candidates, let's show what the difference is

for candidate in candidates:
    d=difflib.Differ()
    diff=d.compare(french,candidate)
    print ('  '.join(diff))
    print (dictionary.meaning(candidate))
    print ('')
    #for line in difflib.context_diff(french, candidate):
     #   sys.stdout.write(line)         


##example

#def comparison(french,a_words[i]):
    #set_french= Counter(french)
    #set_a_words[i]=Counter(a_words[i])
    #common= set_french &set_a_words[i]
    

#if len(a_words[i])>7:
    #comparison(french,a_words[i])
    #if common>=4:
        #print (a_words[i])


    #while french[1,2,3,4]== a_words[i][1,2,3,4]

#if a_words.contains(french[1])and a_words.contains(french[2]) and a_words.contains(french[3]):
   



            


        

    

































#as inputfile
#compare=open(filename,'r')




    #fp.seek (key[0]==individualletters:
        #write key 



    #get key in dictionary with 
    #searchphrase=



    #searchfile= open(dictionary)
    #for line in searchfile:
        #line= line.write
    
    
    
    
