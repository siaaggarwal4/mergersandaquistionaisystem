# MERGERS AND AQUISTION AI SYSTEM

updating repo


## What this is

Reading hundreds of contracts during a merger is slow and easy to get wrong.
I have built an AI system that reads contracts, extract and identify ttype of clauses and highlights risky with confidence.


## What it does

* Upload a contract (USER)
* System extracts text (works  with pdf, text, doc,)(OCR)
* The system breaks it into clauses
* Finetuned LegalBERT identifies type of clauses
* Types of clauses like:
    * change of control
    * termination
    * restrictions and more ( 12 total!)
* Shows a risk score + confidence


## How it works (_the simple_ idea)

Think of it like:

-> “Ctrl + F for legal risk — but smarter”

1. Contract → text
2. Text → clauses
3. AI model reads each clause
4. Outputs:
    * what the clause is
    * how risky it is

## **Tech used**

* FastAPI (backend)
* React (frontend)
* Legal-BERT (Finetuned AI model) from HuggingFace
* Tesseract and pymupdf (OCR)
* pandas (for data pre processing)
⸻

### Dataset for finetuning:
*Atticus Open Contract Dataset*
Contract Understanding Atticus Dataset (CUAD) v1 is a dataset of more than 13,000 labels in 510 commercial legal contracts that have been manually labeled by The Atticus Project to identify 41 categories of important clauses that lawyers look for when reviewing contracts.
I have preprocessed the data to extract clauses for main clauses types.

The 12 types this system can catergorize clauses to are:



## **Why it matters**

Instead of manually reviewing everything, this helps:

* Spot risky contracts faster
* Focus on what actually matters
* Reduce human error
* Support faster, smarter decisions in M&A

## **Key Highlights**

* Built an end-to-end AI pipeline from raw documents to structured insights
* Applied transformer-based NLP to real-world legal problems
* Designed a simple risk scoring system for decision-making

## **What I Learned**

* Fine-tuning transformer models for domain-specific tasks
* Handling long, unstructured documents
* Designing AI systems that connect to real business impact
* Deploying ML systems in production environments (currently)
