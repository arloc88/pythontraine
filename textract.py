from textblob import TextBlob
import docx2txt

def main():

#prova = textract.process('prova.docx')
# extract text
    doc = docx2txt.process("prova.docx")

    blob = TextBlob(doc)

    for s in blob.words:
        print(s)


if __name__ == "__main__":
    main()

