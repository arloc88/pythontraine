from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import docx2txt


def main():

    # extract text
    doc = docx2txt.process("prova.docx")
    #create a blob
    blob = TextBlob(doc)

    count=0
    for s in blob.sentences:
        if(s.lower().startswith('if')):
            count += 1
            print(" \n***** Nuovo If trovato: *****\n")
            print(s)

    print ('\n*******************************************')
    print("\n Sono stati trovati " + str(count)+ " if " )


    #print(doc)
    #print ('+++++++++++++++++++++++++++++++++++++++++++++')
    #print(blob)

if __name__ == "__main__":
    main()

