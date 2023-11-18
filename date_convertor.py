month_num={"january":"1","february":"2","march":"3","april":"4","may":"5","june":"6","july":"7","august":"8","september":"9","october":"10","november":"11","december":"12"}
months="january"

date_us=input("enter the date in us form: ")

a=""
if "january" in date_us or "march" in date_us or "february" in date_us or "april" in date_us or "may" in date_us or "june" in date_us or "july" in date_us or "august" in date_us or "september" in date_us or "october" in date_us or "november" in date_us or "december" in date_us:
   list=[]
   for i in date_us:
     if i==",":
       list.append(a)
       a=""
     if i==" ":
       list.append(month_num.get(a))
       a=""
     if i!=" " and i!=",":
       a+=i
   list.append(a)
  
   
   date_euro=list[1]+"/"+list[0]+"/"+list[2]
 
   print("the date in europe form is:"+date_euro) 
   
         

      

   
else:
   
 list=[]
 for i in date_us:
    
   
      
       
       



    
       
     if i=="/":
        
        
        list.append(a)

        
      
        
        a=""
        
        


        
     if i!="/":



      a+=i
    
    
  
   
 list.append(a)    
     
    
 



 date_euro=list[1]+"/"+list[0]+"/"+list[2]
 
 print("the date in europe form is:"+date_euro) 