from transformers import BertForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer, DataCollatorWithPadding
from datasets import Dataset
from typenum import typetonum, numtotype
import torch

class LegalBert:

    def __init__(self, model_path, data_path=""):
        self.data = " " # Dataset.from_csv("filtered copy.csv")
        self.model = BertForSequenceClassification.from_pretrained(model_path, num_labels=12)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.trainer = None

    def data_type_labelling(self, data_path="filerdata.csv"):
        self.data = Dataset.from_csv(data_path)
        nums = [typetonum[i["Type"]] for i in self.data]
        print(nums)
        self.data = self.data.add_column("label", nums)
        print(self.data[6])
        # self.data.remove_columns("Type")

        textch = [self.tokenize(text) for text in self.data]
        input_ids = [i["input_ids"] for i in textch]
        attn_mask = [i["attention_mask"] for i in textch]
        # label = [i["label"] for i i]
        self.data = self.data.add_column("input_ids", input_ids)
        self.data = self.data.add_column("attention_mask", attn_mask)
        self.data =  self.data.remove_columns("Unnamed: 0")
        self.data =  self.data.remove_columns("Contract")
        self.data =  self.data.remove_columns("Type")
        return self.data


    def tokenize(self, exampl):
        input_ids = self.tokenizer(exampl["Contract"], padding=True, truncation=True, max_length=256)
        input_ids["label"]= exampl["label"]
        return input_ids

    def train(self):
        data = self.data_type_labelling() # "filtereddata.csv")
        evaldata = self.data_type_labelling()#"filterdata2.csv")

        trainer_ = TrainingArguments(output_dir="./model", num_train_epochs=2, per_device_train_batch_size=4, logging_dir="./logs")
        datac = DataCollatorWithPadding(tokenizer=self.tokenizer)
        self.trainer = Trainer(model=self.model, args=trainer_, data_collator=datac,  train_dataset=data, eval_dataset=evaldata)
        self.trainer.train()
        
        return self.trainer
    
        # tokenize()

    def predict(self, text):
        # output = self.model(**self.tokenizer("The computation of the rebates received by licensee shall be expressed as a fixed percentage (15%) of  billable platform fees paid by licensee to licensor.', 'during the term of the non-exclusive license agreement, licensor shall receive from licensee one third (33%) of the gross  amounts earned by the licensee from third parties applicable to the following areas of the licensed technology usage (if any),  (""supplemental payments""):\n\n(a) clearing fees\n\n(b) banking rebates (""give-up fees"")\n\n(c) processing of half pips\n\n(d) swap rates (swap interest rate differential)\n\n(e) currency spreads', ""the rebates shall be payable in shares of licensor's common stock; priced at $.25  cents per share.", return_tensors = "pt").to(self.model.device))
        output = self.model(**self.tokenizer(text, return_tensors="pt", max_length=256).to(self.model.device))

        logits = output.logits
        prob = torch.softmax(logits, dim=-1)
        confidenc, prediction_type = torch.max(prob, dim=-1)
        # predictiontype = numtotype[int(logits.argmax(dim=1))]
        # confidenc =  torch.softmax(logits, dim=-1)[0]
         
        return {"predictiontype": numtotype[prediction_type.item()], "confidence": confidenc.item()} 
