srt1=str(input("enter the string:"))
srt2=str(input("enter the another string:"))
if len(srt1)>len(srt2):
    print(f"the srt1 is longer than the srt2")
elif len(srt2)>len(srt1):
     print(f"the srt2 is longer than the srt1")
else:
     print(f"both strings are equal")