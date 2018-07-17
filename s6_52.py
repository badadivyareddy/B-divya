def fun1(x):
 if(x//10==2 or x//10==3 or x //10==5):
   if(x //10==2):
     print("twenty ");
   if(x //10==3):
     print("thirty ");
   if(x //10==5):
     print("fifty ");
   word(x%10);
 else:
  word(x //10);
  if((x //10)==4 or(x //10)==6 or(x //10)==7 or(x //10)==9):
   print("ty ");
  if((x //10)==8):
   print("y ");
  word((x%10));

def fun2(x):
 word(x //100);
 if((x%100)!=0):
  print(" hundred and ");
 else:
  print(" hundred ");
 fbasic(x%100);

def fun3(x):
 fbasic(x //1000);
 print(" thousand ");
 fbasic(x%1000);

def fun4(x):
  fbasic(x //100000);
  print(" lakhs ");
  fbasic(x%100000);

def fun6(x):
 fbasic(x //10000000);
 print(" crores ");
 fbasic(x%10000000);
