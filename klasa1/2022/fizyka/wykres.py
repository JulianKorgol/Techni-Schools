import matplotlib.pyplot as plt
#Made by Julian Korgol
#

# Tutaj wprowadzamy dane
firstDatax = 1
secondDatax = 1
thirdDatax = 1
firstDatay = 1
secondDatay = 1
thirdDatay = 1

# Tutaj wprowadzamy nazwy x i y.
xjkname = 'Test' # x
yjkname = 'Test' # y

plt.plot([firstDatax, secondDatax, thirdDatax], [firstDatay, secondDatay, thirdDatay], 'o')
plt.xlabel(xjkname)
plt.ylabel(yjkname)
plt.show()
