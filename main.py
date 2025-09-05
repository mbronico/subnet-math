ip=input("Enter IP Address(x.x.x.x/x): ")

splitter=ip.split("/")
subnet_mask=int(splitter[1])
workable_octets=splitter[0].split(".")

incrementor = False


if subnet_mask in (1, 9, 17, 25):
    incrementor = 128
elif subnet_mask in (2, 10, 18, 26):
    incrementor = 64
elif subnet_mask in (3, 11, 19, 27):
    incrementor = 32
elif subnet_mask in (4, 12, 20, 28):
    incrementor = 16
elif subnet_mask in (5, 13, 21, 29):
    incrementor = 8
elif subnet_mask in (6, 14, 22, 30):
    incrementor = 4
elif subnet_mask in (7, 15, 23, 31):
    incrementor = 2 
elif subnet_mask in (8, 16, 24, 32):
    incrementor = 1
else:
    incrementor = ("incorrect")



print(workable_octets)
print(subnet_mask)
print(incrementor)


net_add=("0.0.0.1")
first_host=("0.0.0.2")
last_host=("0.0.0.3")
broadcast=("0.0.0.4")
next_net=("0.0.0.5")


print("""
      IP Address: {}

      Network Address: {}
      First Host: {}
      Last Host: {}
      Broadcast Address: {}
      Next Network Address: {}
      """.format(ip, net_add, first_host, last_host, broadcast, next_net))
