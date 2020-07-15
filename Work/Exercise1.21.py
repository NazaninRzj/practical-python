#Exercise 1.21
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')

print("AIG" in symlist)
print("AA" in symlist)
print("CAT" not in symlist)

#Exercise 1.22
symlist.append("RHT")
symlist.insert(1,"AA")
symlist.remove("MSFT")
symlist.append("YHOO")
print(symlist.index("YHOO"))

count = 0
for name in range (len(symlist)):
    if symlist[name] == "YHOO":
        count += 1
print(count)

symlist.remove("YHOO")
print(symlist)

