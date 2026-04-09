from legalmodelberttrain import LegalBert
from parser import get_text, clean_text
from extract_clauses import extract_clause
from risknorms import ris_norms

fh = open("datafile.txt", "w")
def run_sys(input_file_path, model_path):
    print("got file", input_file_path)
    # print("got model", model_path)
    text = get_text(input_file_path)
    # print(text)
    text=clean_text(text)
    # for line in text:
    fh.write(text)
    clauses = extract_clause(text)
    # print(clauses)
    classify = LegalBert(model_path)

    out= []
    f=open("clanalyze.txt", "w")
    
    for i in clauses:
        # print(i)
        labe = classify.predict(i)
        labe["review"] = False
        # print(labe)

        if labe["confidence"] < 0.60:
            labe["review"] = True

        labe["text"] = i
        labe["risk"], labe["reason"] = ris_norms(labe["predictiontype"], i)
        f.write(str(labe)+"\n")
        out.append(labe)

    return out


if __name__ == "__main__":
    print(run_sys("/Users/siaaggarwal/Downloads/Law_Insider_tombstone-technologies-inc_amended-agreement-and-plan-of-merger-and-reorganization_Filed_05-11-2010_Contract.pdf", "/Users/siaaggarwal/Downloads/bert:model"))
