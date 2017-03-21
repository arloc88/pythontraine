from docx import Document

def main():
    ifState = 0
    conditionState = 0
    nestedIfState = 0
    endState = 0

    doc = Document('prova.docx')

    text = ""
    for para in doc.paragraphs:
        if (para.text.lower().startswith("if")):
            text = para.text + "\n"
            print(para.text)
            ifState = 1


if __name__ == "__main__":
    main()



