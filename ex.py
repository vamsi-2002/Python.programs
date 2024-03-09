#s1={1,2,3,4,5,6}
#s2={6,7,4,2,5,8}
#print(s1&s2)
#print((s1) .intersection (s2))
#s3={2,4,5,1,8}
#print(s1.intersection (s2) .intersection(s3))

#day1={"mon","tue","wed","thu"}
#day2={"tue","wed","fri","sat","sun"}
#print(day1.difference(day2))
#rint(day1==day2)
#print(day1<day2)
#print(day1!=day2)
#day3={"mon","sat","fri","tue","wed","mon"}
#print(day1 .difference(day2,day3))
#print(day1 .difference(day2).difference (day3))

#frozen set
#set1=frozenset([1,2,3,4,5])
#print(type(set1))
#set1.add(10)

#issuperset
#set1={'a','b','c','d','e'}
#set2={'b','s','f','e'}
#set3={'b','x','z','w'}
#issubset=set1>set2
#print(issubset)
#issubset=set1<set2
#print(issubset)
#issubset=set1=set2
#print(issubset)
#issubset=set!=set2+
#print(issubset)

#people=[("vamsi",10),("vam",2),("era",3)]
#sorted_tup=sorted(people, key=lambda x:x[1])
#print(sorted_tup)

#def value(*args):
 #   total=0
  #  for num in args:
   #     total+=num
    #return total
#result=value(1,2,3,4,5)
#print(result)
        
#add=lambda x,y:x+y
#result= add(3,5)
#print(result)

#func=lambda arg1,arg2:arg1+arg2
#print("values:",func(10,20))
#print("values:",func(20,40))   
