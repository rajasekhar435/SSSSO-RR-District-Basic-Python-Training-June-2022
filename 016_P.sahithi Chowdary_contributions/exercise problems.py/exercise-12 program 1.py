t1 = ("pulsar","duke","shine")
print("the total number of items present in the tuple is",len(t1))
print("The index of the shine in the tuple is",t1.index("shine"))
t1 = list(t1)
print(t1)
t1.append("splendor")
t1.remove("duke")
t1 = tuple(t1)
print(t1)