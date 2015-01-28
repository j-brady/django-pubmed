from Bio import Entrez, Medline

def GetPubMedEntries(email,search_term):
  Entrez.email = email 
  handle = Entrez.esearch(db="pubmed", term=search_term, retmax=500)
  record = Entrez.read(handle)
  idlist = record["IdList"]

  handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
  records = Medline.parse(handle)
  records = list(records)  
  return records

def convert_to_string(record,field):
    r = record.get(field,"?")
    string = ''
    for num,i in enumerate(r):
      last = len(r)-1
      if field =="AU" and num !=last:
        string+='%s, '%i
      elif field =="AU" and num == last:
        string+='%s'%i
      else:
        string+='%s'%i
    return str(string)


if __name__ == "__main__":

  email = "jacob.brady0449@gmail.com"
  #search_term="schnell jr OR (schnell j AND wright pe)"
  search_term="brady jacob p OR (brady jacob AND  matthews sj)"
  records =  GetPubMedEntries(email,search_term)  
  for record in records:
    #r = record.get("AU","?")
    #string = ''
    print(convert_to_string(record,"AU"))

