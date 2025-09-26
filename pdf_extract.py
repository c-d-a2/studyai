from pypdf import PdfReader

import fitz

def topic_parser(infile):
    doc = fitz.open(infile)
    toc = doc.get_toc()  

    
    sections = []
    chapters = []
    for level, title, page in toc:
        if level == 1:
            sections.append({
                "title": title,
                "page": page
            })
        else:
            if level == 2:
                chapters.append({
                    "title": title,
                    "page": page
                })
    return {
        "Sections": sections,
        "Chapters": chapters
    }

            
def print_toc(toc):
    for chp in toc["Chapters"]:
        print(f"{chp} ")
    
    
    




def extract_text(sections):
    pass








def chunkenize(text):
    chunker = RecursiveChunker()
    chunks = chunker("Process Memory")

    for chunk in chunks:
        print(f"Chunk: {chunk}")
        print(f"Tokens: {chunk.token_count}")


toc2 = topic_parser("OperatingSystems.pdf")
toc  = topic_parser("CCNP.pdf")         
print(print_toc(toc))
print(print_toc(toc2))
#  Use topic and page marker on top of page
#  Delimeter would be a summary
#  using table of contents to guide 
#  offset  
#  how are the link formatted so that the pdf client can jump to the correct page? We can use this 

