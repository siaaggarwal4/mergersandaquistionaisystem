def ris_norms(type, text):
    text=text.lower()
    s = 0
    reason = ["reason for the score"]
    

    if type == "Liability" or type == "Liability cap":

        if inchec("unlimited liability", text):
            s+=3
            reason.append("unlimited liability")
            # return "high", ["unlimited liability"]
        
        if inchec("no limitation", text):
            s+= 3
            reason.append("no limitation")

        if "cap" in text:
            s+=1
            reason.append("low capacity")
            # return "low", ["cap"]
        
        # return "med", []

    elif type=="Termnation for Convience":
        
        if inchec("immediately", text):
            s+= 3
            reason.append("immediate termination allowed")

        if inchec("either party", text) is False:
            s+=2
            reason.append("one-sided termination")
        
        if inchec("30 days", text) or inchec("60 days", text):
            s+=1
            reason.append("reasonable notice period")
        # if "immediate termnation" in text or "immediately":
            # return "high", ["immediate termnation", "immediately"]
        # if "30 days":
            # return "low", ["30 days"]
        # return "med", []
    
    elif type == "Change of control":
        if inchec("terminate", text):
            s+=3
            reason.append("termination on change of control")
        
        if inchec("consent", text):
            s+=2
            reason.append("requires consent")

    elif type == "Competitive Restriction Exception":
        if inchec("cannont compete", text):
            s+= 3
            reason.append("stops from competetion")
        
        if inchec("can compete", text):
            s+= 1
            reason.append("cannot compete with rules")

    elif type == "Exclusivity":
        if inchec("exclusive", text):
            s+=2
            reason.append("exclusive agreemen")
        
        if inchec("all customers", text) or inchec("all products", text):
            s+=2
            reason.append("broad scope")
        
        if inchec("years", text):
            s+=2
            reason.append("long time dur")
    
    elif type == "No Disparagement":
        if inchec("perptual", text) or inchec("forever", text):
            s+=2
            reason.append("no time limit")
        # if employee or officier in reason applie broad s+=1


    elif type == "No Solicit of Customers":
        if inchec("any customer", text) or inchec("prospective customer", text):
            s+=2
            reason.append("broad restriction")
        
        if inchec("years", text):
            s+=2
            reason.append("long restriction time dur")

    elif type == "Non-Compete":
        if inchec("cannot compete", text):
            s+=2
            reason.append("restriction for competetion")
        if inchec("years", text):
            s+=2
            reason.append("long time dur for non compete")
    
    elif type == "Post-Termination Services":
        if inchec("non compensation", text):
            s+=3
            reason.append("no payement for service") 
    
    elif type == "Price Restrictions":
        if inchec("fixed price", text):
            s+=3
            reason.append("fixed priceing")
        if inchec("not change price", text):
            s+=2
            reason.append("price lock cannot change")

    elif type == "Revenue/Profit sharing":
        if inchec("audit", text):
            s+=1
            reason.append("overly restriction")
    
    print(s, reason)
    if s>= 3:
        s = "high"
        # return "high", reason
    elif s>=2:
        s = "med"
        # return "med", reason
    elif s>=1:
        s="low"
    elif s==0:
        s = "risk not computed"

    return s, reason
        #return "low" , reason   
    # return "mediuym"


def inchec(w1,w2):
    return w1 in w2