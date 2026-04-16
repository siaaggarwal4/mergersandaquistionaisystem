import re
import regex
def extract_clause(text):

    fh = open("datafile1", "w")
    # fh.write(text)
    # with open("datafile.txt", "w") as fh:
        # fh.write(text)

    clauses = []
    
    claus = re.split(r'\ns*\n', text)
    # print(claus[1])
    claus = [j.strip().replace("\\n", " ") for j in claus if len(j)>80]
    clauses = claus
    # print(len(claus[0].split("\n")))pip

    # print(claus[1])
    # print("c", claus)
    # for j in claus:
    #     fh.write("j:"+j)
        # print("j", j, "\n")
        # print("first 10", j[:10])
    
    patern = r"((?<!Inc|INC|Corp|Corp|Dr|DR)\.)"
    if len(claus) == 1:
        clauses = []
        claus = re.split(r'(?=\b\d+\.\s+[A-Z])', text) # gives list of paragraphs
        # print(type(claus))
        for j in claus:
            lines = regex.split(patern, j)
            # fh.write()
            for line in lines:
            #     lines1 = l.split("\n")
            #     for line in lines1:
                    if len(line.strip()) > 80:
                        # if len(line.split()) > 300:
                        #      clauses.append(line[:600])
                        #      clauses.append(lines[500:])
                        # else :
                            linen = re.sub(r"\s+", " ", line).strip() #line.replace(r"\n", " ")
                            # print(linen)
                            # print("yes 12")
                            fh.write("line:"+ line.strip())
                            clauses.append(linen)

    fh = open("line.txt", "w")
    for i in clauses:
          fh.write("line: "+ str(len(i)) + i)
          fh.write("\n\n")
          
        # claus = [j.strip() for j in claus if len(j)>20]
            # for jl in lines:
            #     fh.write("j:"+jl)
    
    return claus

    # clauses =   [j for j in text.split("\n") if len(j) > 20]
    # copy = clauses[:]
    # for i in range(len(copy)):
    #     if len(copy[i]) < 20:
    #         clauses.pop(i)
    
    # return clauses
