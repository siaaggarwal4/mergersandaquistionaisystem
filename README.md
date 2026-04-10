MERGERS AND AQUISTION AI SYSTEM

updating repo

It takes a contract, extract clauses, identify clauses from finetuned model and show the risk norms.

Reading hundreds of contracts during a merger is slow and easy to get wrong.
I built a simple AI system that reads contracts and highlights risks instantly.
 
What it does
	•	Upload a contract\
	•	The system breaks it into clauses\
	•	AI identifies important legal terms\
	•	Flags risks like:\
	    •	change of control\
    	•	termination\
    	•	restrictions\
    •	Shows a risk score + confidence


How it works\

Think of it like:\ “Ctrl + F for legal risk — but smarter”\
	1.	Contract → text\
	2.	Text → clauses\
	3.	AI model reads each clause\
	4.	Outputs calculated on logic:\
	•	what the clause is\
	•	how risky it is

Tech used
	•	Flask (backend)
    •	(React Frontend)
	•	Legal-BERT (AI model)
	•	PyTorch + HuggingFace 
	•	AWS EC2 (deployment)

Why it matters

Instead of manually reviewing everything, this helps:
	•	spot risky contracts faster
	•	focus on what actually matters

Future Improvements:
    Edge cases to risk norms
    Integrate features like risk calculation with agreement
    Employee Data analysis
    Companies background information to score for mergers and agreement
    
