import array
import random

class Packet:
    # Constructor function for a packet
    def __init__(self, data: int):
        self.data = data
        self.path = []
        self.reverseBinary = ''
        # Reverse binary
        # Obtain the binary representation of the data
        while(data):
            rem = data % 2
            self.reverseBinary = self.reverseBinary + str(rem)
            # Divide with integral result and discard remainder
            data //= 2
        # Reverse the binary array
        self.reverseBinary = self.reverseBinary[: : -1]
        self.reverseBinary = self.reverseBinary.zfill(5)
    # Get packet data
    def getData(self):
        return self.data
    # Get packet data in binary, reversed
    def getReverseBinary(self):
        return self.reverseBinary
    # Get packet path array
    def getPath(self):
        return self.path
    # Add name of the node to the packet's path
    def addToPath(self, nodeName):
        self.path.append(nodeName)

class Switch:
    # Constructor function for a node/switch
    def __init__(self, name: str):
        self.name = name
        # Inputs 1 and 2
        self.input1 = None
        self.input2 = None
    # Get node name
    def getName(self):
        return self.name
    # Add node name to packet
    def add(self, packet: Packet):
        return packet.addToPath(self.name)
    # Get inputs
    def getInputs(self):
        if(self.input1):
            if(self.input2):
                return (self.input1.getData(), self.input2.getData())
    # Get Input Packets
    def getInputPackets(self):
        return(self.input1, self.input2)
    # Add input
    def addInput(self, input: Packet):
        if(self.input1 == None):
            self.input1 = input
            self.add(self.input1)
        else:
            if(self.input2 == None):
                self.input2 = input
                self.add(self.input2)
    # Using the two inputs, return the packet that has the larger number
    def up(self):
        if(self.input1):
            if(self.input2):
                n1 = self.input1.getData() 
                n2 = self.input2.getData()
                if(n1 < n2):
                    return(self.input2)
                else:
                    return(self.input1)
    # Using the two inputs, return the packet that has the smaller number
    def down(self):
        if(self.input1):
            if(self.input2):
                n1 = self.input1.getData() 
                n2 = self.input2.getData()
                if(n1 < n2):
                    return(self.input1)
                else:
                    return(self.input2)

# Interacting with the user:
val = input("Do you want to run built-in test cases? \nType 'y' to run pre-built test cases. Type 'n' to test random input: " )
if(val == 'y'):
    # Initializing 8 packets
    p1 = Packet(7)
    p2 = Packet(6)

    p3 = Packet(5)
    p4 = Packet(4)

    p5 = Packet(3)
    p6 = Packet(2)

    p7 = Packet(1)
    p8 = Packet(0)

    # Initializing 16 packets
    p1a = Packet(3)
    p2a = Packet(12)

    p3a = Packet(4)
    p4a = Packet(7)

    p5a = Packet(8)
    p6a = Packet(2)

    p7a = Packet(14)
    p8a = Packet(6)

    p9a = Packet(0)
    p10a = Packet(11)

    p11a = Packet(9)
    p12a = Packet(10)

    p13a = Packet(1)
    p14a = Packet(15)

    p15a = Packet(5)
    p16a = Packet(13)
elif (val == 'n'):
    # Initializing 8 packets
    p1 = Packet(random.randint(0, 7))
    p2 = Packet(random.randint(0, 7))

    p3 = Packet(random.randint(0, 7))
    p4 = Packet(random.randint(0, 7))

    p5 = Packet(random.randint(0, 7))
    p6 = Packet(random.randint(0, 7))

    p7 = Packet(random.randint(0, 7))
    p8 = Packet(random.randint(0, 7))

    # Initializing 16 packets
    p1a = Packet(random.randint(0, 15))
    p2a = Packet(random.randint(0, 15))

    p3a = Packet(random.randint(0, 15))
    p4a = Packet(random.randint(0, 15))

    p5a = Packet(random.randint(0, 15))
    p6a = Packet(random.randint(0, 15))

    p7a = Packet(random.randint(0, 15))
    p8a = Packet(random.randint(0, 15))

    p9a = Packet(random.randint(0, 15))
    p10a = Packet(random.randint(0, 15))

    p11a = Packet(random.randint(0, 15))
    p12a = Packet(random.randint(0, 15))

    p13a = Packet(random.randint(0, 15))
    p14a = Packet(random.randint(0, 15))

    p15a = Packet(random.randint(0, 15))
    p16a = Packet(random.randint(0, 15))

# 8 Input Batcher Sorter:
# Initializing all 24 switches in the Batcher sorter
a0 = Switch('a0')
a1 = Switch('a1')
a2 = Switch('a2')
a3 = Switch('a3')

b0 = Switch('b0')
b1 = Switch('b1')
b2 = Switch('b2')
b3 = Switch('b3')

c0 = Switch('c0')
c1 = Switch('c1')
c2 = Switch('c2')
c3 = Switch('c3')

d0 = Switch('d0')
d1 = Switch('d1')
d2 = Switch('d2')
d3 = Switch('d3')

e0 = Switch('e0')
e1 = Switch('e1')
e2 = Switch('e2')
e3 = Switch('e3')

f0 = Switch('f0')
f1 = Switch('f1')
f2 = Switch('f2')
f3 = Switch('f3')

print('8 Input Batcher Sorter (6 Stages with 4 Switches Each):')
# Stage a: Introducing the packets
a0.addInput(p1)
a0.addInput(p2)
print('a0 inputs: ' + str(a0.getInputs()))

a1.addInput(p3)
a1.addInput(p4)
print('a1 inputs: ' + str(a1.getInputs()))

a2.addInput(p5)
a2.addInput(p6)
print('a2 inputs: ' + str(a2.getInputs()))

a3.addInput(p7)
a3.addInput(p8)
print('a3 inputs: ' + str(a3.getInputs()))
print('\n')

# Stage b
b0.addInput(a0.down())
b0.addInput(a1.up())

b1.addInput(a0.up())
b1.addInput(a1.down())

b2.addInput(a2.down())
b2.addInput(a3.up())

b3.addInput(a2.up())
b3.addInput(a3.down())

# Stage c
c0.addInput(b0.down())
c0.addInput(b1.down())

c1.addInput(b0.up())
c1.addInput(b1.up())

c2.addInput(b2.up())
c2.addInput(b3.up())

c3.addInput(b2.down())
c3.addInput(b3.down())

# Stage d
d0.addInput(c0.down())
d0.addInput(c2.up())

d1.addInput(c0.up())
d1.addInput(c2.down())

d2.addInput(c1.down())
d2.addInput(c3.up())

d3.addInput(c1.up())
d3.addInput(c3.down())

# Stage e
e0.addInput(d0.down())
e0.addInput(d2.down())

e1.addInput(d1.down())
e1.addInput(d3.down())

e2.addInput(d0.up())
e2.addInput(d2.up())

e3.addInput(d1.up())
e3.addInput(d3.up())

# Stage f
f0.addInput(e0.down())
f0.addInput(e1.down())

f1.addInput(e0.up())
f1.addInput(e1.up())

f2.addInput(e2.down())
f2.addInput(e3.down())

f3.addInput(e2.up())
f3.addInput(e3.up())

# Printing Batcher Sorter Output Results
# and initializing the Banyan input
banyanInput = []

print(f0.down().getData())
print(f0.down().getPath())
banyanInput.append(f0.down())

print(f0.up().getData())
print(f0.up().getPath())
banyanInput.append(f0.up())

print(f1.down().getData())
print(f1.down().getPath())
banyanInput.append(f1.down())

print(f1.up().getData())
print(f1.up().getPath())
banyanInput.append(f1.up())

print(f2.down().getData())
print(f2.down().getPath())
banyanInput.append(f2.down())

print(f2.up().getData())
print(f2.up().getPath())
banyanInput.append(f2.up())

print(f3.down().getData())
print(f3.down().getPath())
banyanInput.append(f3.down())

print(f3.up().getData())
print(f3.up().getPath())
banyanInput.append(f3.up())
print('\n')

# Print the Banyan inputs
print('Banyan Delta Network Emulation (3 Stages with 4 Switches Each):')

# Banyan Network:
# Initializing banyan network switches and their upper and lower destinations
g0 = Switch('g0')
# Adding inputs to g0
g0.addInput(f0.down())
g0.addInput(f2.down())
# Print Inputs
print('g0 inputs: ' + str(g0.getInputs()))

g1 = Switch('g1')
# Adding inputs to g1
g1.addInput(f0.up())
g1.addInput(f2.up())
# Print Inputs
print('g1 inputs: ' + str(g1.getInputs()))

g2 = Switch('g2')
# Adding inputs to g2
g2.addInput(f1.down())
g2.addInput(f3.down())
# Print Inputs
print('g2 inputs: ' + str(g2.getInputs()))

g3 = Switch('g3')
# Adding inputs to g3
g3.addInput(f1.up())
g3.addInput(f3.up())
# Print Inputs
print('g3 inputs: ' + str(g3.getInputs()))

h0 = Switch('h0')
h1 = Switch('h1')
h2 = Switch('h2')
h3 = Switch('h3')

i0 = Switch('i0')
i1 = Switch('i1')
i2 = Switch('i2')
i3 = Switch('i3')

# Emulate 3 x 4 Banyan network
for i in range(0, len(banyanInput)):
    shortenedReverseBinary = banyanInput[i].getReverseBinary()[-3:]
    # print(shortenedReverseBinary)
    # For g0
    if (banyanInput[i].getPath()[-1] == 'g0'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput[i].addToPath('h0')
        else:
            banyanInput[i].addToPath('h2')
    # For g1
    if (banyanInput[i].getPath()[-1] == 'g1'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput[i].addToPath('h1')
        else:
            banyanInput[i].addToPath('h3')
    # For g2
    if (banyanInput[i].getPath()[-1] == 'g2'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput[i].addToPath('h0')
        else:
            banyanInput[i].addToPath('h2')
    # For g3
    if (banyanInput[i].getPath()[-1] == 'g3'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput[i].addToPath('h1')
        else:
            banyanInput[i].addToPath('h3')
    # print(banyanInput[i].getPath())

for i in range(0, len(banyanInput)):
    shortenedReverseBinary = banyanInput[i].getReverseBinary()[-3:]
    # print(shortenedReverseBinary)
    # For h0
    if (banyanInput[i].getPath()[-1] == 'h0'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput[i].addToPath('i0')
        else:
            banyanInput[i].addToPath('i1')
    # For h1
    if (banyanInput[i].getPath()[-1] == 'h1'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput[i].addToPath('i0')
        else:
            banyanInput[i].addToPath('i1')
    # For h2
    if (banyanInput[i].getPath()[-1] == 'h2'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput[i].addToPath('i2')
        else:
            banyanInput[i].addToPath('i3')
    # For h3
    if (banyanInput[i].getPath()[-1] == 'h3'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput[i].addToPath('i2')
        else:
            banyanInput[i].addToPath('i3')
    # print(banyanInput[i].getPath())

print('\n')
for i in range(0, len(banyanInput)):
    shortenedReverseBinary = banyanInput[i].getReverseBinary()[-3:]
    print(banyanInput[i].getData(), end=' -> Binary = ')
    print(shortenedReverseBinary, end=': ')
    # For i0
    if (banyanInput[i].getPath()[-1] == 'i0'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput[i].addToPath('i0 UP')
        else:
            banyanInput[i].addToPath('i0 DOWN')
    # For i1
    if (banyanInput[i].getPath()[-1] == 'i1'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput[i].addToPath('i1 UP')
        else:
            banyanInput[i].addToPath('i1 DOWN')
    # For i2
    if (banyanInput[i].getPath()[-1] == 'i2'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput[i].addToPath('i2 UP')
        else:
            banyanInput[i].addToPath('i2 DOWN')
    # For i3
    if (banyanInput[i].getPath()[-1] == 'i3'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput[i].addToPath('i3 UP')
        else:
            banyanInput[i].addToPath('i3 DOWN')
    print(banyanInput[i].getPath())

print('\n*********************************************************')
# 16 x 10 Batcher Sorter:
# Initializing all 80 switches in the Batcher sorter
j0 = Switch('j0')
j1 = Switch('j1')
j2 = Switch('j2')
j3 = Switch('j3')
j4 = Switch('j4')
j5 = Switch('j5')
j6 = Switch('j6')
j7 = Switch('j7')

k0 = Switch('k0')
k1 = Switch('k1')
k2 = Switch('k2')
k3 = Switch('k3')
k4 = Switch('k4')
k5 = Switch('k5')
k6 = Switch('k6')
k7 = Switch('k7')

l0 = Switch('l0')
l1 = Switch('l1')
l2 = Switch('l2')
l3 = Switch('l3')
l4 = Switch('l4')
l5 = Switch('l5')
l6 = Switch('l6')
l7 = Switch('l7')

m0 = Switch('m0')
m1 = Switch('m1')
m2 = Switch('m2')
m3 = Switch('m3')
m4 = Switch('m4')
m5 = Switch('m5')
m6 = Switch('m6')
m7 = Switch('m7')

n0 = Switch('n0')
n1 = Switch('n1')
n2 = Switch('n2')
n3 = Switch('n3')
n4 = Switch('n4')
n5 = Switch('n5')
n6 = Switch('n6')
n7 = Switch('n7')

o0 = Switch('o0')
o1 = Switch('o1')
o2 = Switch('o2')
o3 = Switch('o3')
o4 = Switch('o4')
o5 = Switch('o5')
o6 = Switch('o6')
o7 = Switch('o7')

p0 = Switch('p0')
p1 = Switch('p1')
p2 = Switch('p2')
p3 = Switch('p3')
p4 = Switch('p4')
p5 = Switch('p5')
p6 = Switch('p6')
p7 = Switch('p7')

q0 = Switch('q0')
q1 = Switch('q1')
q2 = Switch('q2')
q3 = Switch('q3')
q4 = Switch('q4')
q5 = Switch('q5')
q6 = Switch('q6')
q7 = Switch('q7')

r0 = Switch('r0')
r1 = Switch('r1')
r2 = Switch('r2')
r3 = Switch('r3')
r4 = Switch('r4')
r5 = Switch('r5')
r6 = Switch('r6')
r7 = Switch('r7')

s0 = Switch('s0')
s1 = Switch('s1')
s2 = Switch('s2')
s3 = Switch('s3')
s4 = Switch('s4')
s5 = Switch('s5')
s6 = Switch('s6')
s7 = Switch('s7')

print('\n16 Input Batcher Sorter (10 Stages with 8 Switches Each):')
# Stage J: Introducing the packets
j0.addInput(p1a)
j0.addInput(p2a)
print('j0 inputs: ' + str(j0.getInputs()))

j1.addInput(p3a)
j1.addInput(p4a)
print('j1 inputs: ' + str(j1.getInputs()))

j2.addInput(p5a)
j2.addInput(p6a)
print('j2 inputs: ' + str(j2.getInputs()))

j3.addInput(p7a)
j3.addInput(p8a)
print('j3 inputs: ' + str(j3.getInputs()))

j4.addInput(p9a)
j4.addInput(p10a)
print('j4 inputs: ' + str(j4.getInputs()))

j5.addInput(p11a)
j5.addInput(p12a)
print('j5 inputs: ' + str(j5.getInputs()))

j6.addInput(p13a)
j6.addInput(p14a)
print('j6 inputs: ' + str(j6.getInputs()))

j7.addInput(p15a)
j7.addInput(p16a)
print('j7 inputs: ' + str(j7.getInputs()))

# Stage k
k0.addInput(j0.down())
k0.addInput(j1.up())
# print('k0 inputs: ' + str(k0.getInputs()))

k1.addInput(j0.up())
k1.addInput(j1.down())
# print('k1 inputs: ' + str(k1.getInputs()))

k2.addInput(j2.down())
k2.addInput(j3.up())
# print('k2 inputs: ' + str(k2.getInputs()))

k3.addInput(j2.up())
k3.addInput(j3.down())
# print('k3 inputs: ' + str(k3.getInputs()))

k4.addInput(j4.down())
k4.addInput(j5.up())
# print('k4 inputs: ' + str(k4.getInputs()))

k5.addInput(j4.up())
k5.addInput(j5.down())
# print('k5 inputs: ' + str(k5.getInputs()))

k6.addInput(j6.down())
k6.addInput(j7.up())
# print('k6 inputs: ' + str(k6.getInputs()))

k7.addInput(j6.up())
k7.addInput(j7.down())
# print('k7 inputs: ' + str(k7.getInputs()))

# Stage l
l0.addInput(k0.down())
l0.addInput(k1.down())
# print('l0 inputs: ' + str(l0.getInputs()))

l1.addInput(k0.up())
l1.addInput(k1.up())
# print('l1 inputs: ' + str(l1.getInputs()))

l2.addInput(k2.up())
l2.addInput(k3.up())
# print('l2 inputs: ' + str(l2.getInputs()))

l3.addInput(k2.down())
l3.addInput(k3.down())
# print('l3 inputs: ' + str(l3.getInputs()))

l4.addInput(k4.down())
l4.addInput(k5.down())
# print('l4 inputs: ' + str(l4.getInputs()))

l5.addInput(k4.up())
l5.addInput(k5.up())
# print('l5 inputs: ' + str(l5.getInputs()))

l6.addInput(k6.up())
l6.addInput(k7.up())
# print('l6 inputs: ' + str(l6.getInputs()))

l7.addInput(k6.down())
l7.addInput(k7.down())
# print('l7 inputs: ' + str(l7.getInputs()))

# Stage m
m0.addInput(l0.down())
m0.addInput(l2.up())
# print('m0 inputs: ' + str(m0.getInputs()))

m1.addInput(l0.up())
m1.addInput(l2.down())
# print('m1 inputs: ' + str(m1.getInputs()))

m2.addInput(l1.down())
m2.addInput(l3.up())
# print('m2 inputs: ' + str(m2.getInputs()))

m3.addInput(l1.up())
m3.addInput(l3.down())
# print('m3 inputs: ' + str(m3.getInputs()))

m4.addInput(l4.down())
m4.addInput(l6.up())
# print('m4 inputs: ' + str(m4.getInputs()))

m5.addInput(l4.up())
m5.addInput(l6.down())
# print('m5 inputs: ' + str(m5.getInputs()))

m6.addInput(l5.down())
m6.addInput(l7.up())
# print('m6 inputs: ' + str(m6.getInputs()))

m7.addInput(l5.up())
m7.addInput(l7.down())
# print('m7 inputs: ' + str(m7.getInputs()))

# Stage n
n0.addInput(m0.down())
n0.addInput(m2.down())
# print('n0 inputs: ' + str(n0.getInputs()))

n1.addInput(m1.down())
n1.addInput(m3.down())
# print('n1 inputs: ' + str(n1.getInputs()))

n2.addInput(m0.up())
n2.addInput(m2.up())
# print('n2 inputs: ' + str(n2.getInputs()))

n3.addInput(m1.up())
n3.addInput(m3.up())
# print('n3 inputs: ' + str(n3.getInputs()))

n4.addInput(m4.up())
n4.addInput(m6.up())
# print('n4 inputs: ' + str(n4.getInputs()))

n5.addInput(m5.up())
n5.addInput(m7.up())
# print('n5 inputs: ' + str(n5.getInputs()))

n6.addInput(m4.down())
n6.addInput(m6.down())
# print('n6 inputs: ' + str(n6.getInputs()))

n7.addInput(m5.down())
n7.addInput(m7.down())
# print('n7 inputs: ' + str(n7.getInputs()))

# Stage o
o0.addInput(n0.down())
o0.addInput(n1.down())
# print('o0 inputs: ' + str(o0.getInputs()))

o1.addInput(n0.up())
o1.addInput(n1.up())
# print('o1 inputs: ' + str(o1.getInputs()))

o2.addInput(n2.down())
o2.addInput(n3.down())
# print('o2 inputs: ' + str(o2.getInputs()))

o3.addInput(n2.up())
o3.addInput(n3.up())
# print('o3 inputs: ' + str(o3.getInputs()))

o4.addInput(n4.up())
o4.addInput(n5.up())
# print('o4 inputs: ' + str(o4.getInputs()))

o5.addInput(n4.down())
o5.addInput(n5.down())
# print('o5 inputs: ' + str(o5.getInputs()))

o6.addInput(n6.up())
o6.addInput(n7.up())
# print('o6 inputs: ' + str(o6.getInputs()))

o7.addInput(n6.down())
o7.addInput(n7.down())
# print('o7 inputs: ' + str(o7.getInputs()))

# Stage p
p0.addInput(o0.down())
p0.addInput(o4.up())
# print('p0 inputs: ' + str(p0.getInputs()))

p1.addInput(o0.up())
p1.addInput(o4.down())
# print('p1 inputs: ' + str(p1.getInputs()))

p2.addInput(o1.down())
p2.addInput(o5.up())
# print('p2 inputs: ' + str(p2.getInputs()))

p3.addInput(o1.up())
p3.addInput(o5.down())
# print('p3 inputs: ' + str(p3.getInputs()))

p4.addInput(o2.down())
p4.addInput(o6.up())
# print('p4 inputs: ' + str(p4.getInputs()))

p5.addInput(o2.up())
p5.addInput(o6.down())
# print('p5 inputs: ' + str(p5.getInputs()))

p6.addInput(o3.down())
p6.addInput(o7.up())
# print('p6 inputs: ' + str(p6.getInputs()))

p7.addInput(o3.up())
p7.addInput(o7.down())
# print('p7 inputs: ' + str(p7.getInputs()))

# Stage q
q0.addInput(p0.down())
q0.addInput(p4.down())
# print('q0 inputs: ' + str(q0.getInputs()))

q1.addInput(p1.down())
q1.addInput(p5.down())
# print('q1 inputs: ' + str(q1.getInputs()))

q2.addInput(p2.down())
q2.addInput(p6.down())
# print('q2 inputs: ' + str(q2.getInputs()))

q3.addInput(p3.down())
q3.addInput(p7.down())
# print('q3 inputs: ' + str(q3.getInputs()))

q4.addInput(p0.up())
q4.addInput(p4.up())
# print('q4 inputs: ' + str(q4.getInputs()))

q5.addInput(p1.up())
q5.addInput(p5.up())
# print('q5 inputs: ' + str(q5.getInputs()))

q6.addInput(p2.up())
q6.addInput(p6.up())
# print('q6 inputs: ' + str(q6.getInputs()))

q7.addInput(p3.up())
q7.addInput(p7.up())
# print('q7 inputs: ' + str(q7.getInputs()))

# Stage r
r0.addInput(q0.down())
r0.addInput(q2.down())
# print('r0 inputs: ' + str(r0.getInputs()))

r1.addInput(q1.down())
r1.addInput(q3.down())
# print('r1 inputs: ' + str(r1.getInputs()))

r2.addInput(q0.up())
r2.addInput(q2.up())
# print('r2 inputs: ' + str(r2.getInputs()))

r3.addInput(q1.up())
r3.addInput(q3.up())
# print('r3 inputs: ' + str(r3.getInputs()))

r4.addInput(q4.down())
r4.addInput(q6.down())
# print('r4 inputs: ' + str(r4.getInputs()))

r5.addInput(q5.down())
r5.addInput(q7.down())
# print('r5 inputs: ' + str(r5.getInputs()))

r6.addInput(q4.up())
r6.addInput(q6.up())
# print('r6 inputs: ' + str(r6.getInputs()))

r7.addInput(q5.up())
r7.addInput(q7.up())
# print('r7 inputs: ' + str(r7.getInputs()))

# Stage s
s0.addInput(r0.down())
s0.addInput(r1.down())
# print('s0 inputs: ' + str(s0.getInputs()))

s1.addInput(r0.up())
s1.addInput(r1.up())
# print('s1 inputs: ' + str(s1.getInputs()))

s2.addInput(r2.down())
s2.addInput(r3.down())
# print('s2 inputs: ' + str(s2.getInputs()))

s3.addInput(r2.up())
s3.addInput(r3.up())
# print('s3 inputs: ' + str(s3.getInputs()))

s4.addInput(r4.down())
s4.addInput(r5.down())
# print('s4 inputs: ' + str(s4.getInputs()))

s5.addInput(r4.up())
s5.addInput(r5.up())
# print('s5 inputs: ' + str(s5.getInputs()))

s6.addInput(r6.down())
s6.addInput(r7.down())
# print('s6 inputs: ' + str(s6.getInputs()))

s7.addInput(r6.up())
s7.addInput(r7.up())
# print('s7 inputs: ' + str(s7.getInputs()))
print('\n')

# Printing Batcher Sorter Output Results
# and initializing the Banyan input
banyanInput16 = []

print(s0.down().getData())
print(s0.down().getPath())
banyanInput16.append(s0.down())

print(s0.up().getData())
print(s0.up().getPath())
banyanInput16.append(s0.up())

print(s1.down().getData())
print(s1.down().getPath())
banyanInput16.append(s1.down())

print(s1.up().getData())
print(s1.up().getPath())
banyanInput16.append(s1.up())

print(s2.down().getData())
print(s2.down().getPath())
banyanInput16.append(s2.down())

print(s2.up().getData())
print(s2.up().getPath())
banyanInput16.append(s2.up())

print(s3.down().getData())
print(s3.down().getPath())
banyanInput16.append(s3.down())

print(s3.up().getData())
print(s3.up().getPath())
banyanInput16.append(s3.up())

print(s4.down().getData())
print(s4.down().getPath())
banyanInput16.append(s4.down())

print(s4.up().getData())
print(s4.up().getPath())
banyanInput16.append(s4.up())

print(s5.down().getData())
print(s5.down().getPath())
banyanInput16.append(s5.down())

print(s5.up().getData())
print(s5.up().getPath())
banyanInput16.append(s5.up())

print(s6.down().getData())
print(s6.down().getPath())
banyanInput16.append(s6.down())

print(s6.up().getData())
print(s6.up().getPath())
banyanInput16.append(s6.up())

print(s7.down().getData())
print(s7.down().getPath())
banyanInput16.append(s7.down())

print(s7.up().getData())
print(s7.up().getPath())
banyanInput16.append(s7.up())
print('\n')

# Print the Banyan inputs (16)
print('Banyan Delta Network Emulation (4 Stages with 8 Switches Each):')

# Banyan Network (16):
# Initializing banyan network switches and their upper and lower destinations

# Adding inputs to t0
t0 = Switch('t0')
t0.addInput(s0.down())
t0.addInput(s4.down())
print('t0 inputs: ' + str(t0.getInputs()))

# Adding inputs to t1
t1 = Switch('t1')
t1.addInput(s0.up())
t1.addInput(s4.up())
print('t1 inputs: ' + str(t1.getInputs()))

# Adding inputs to t2
t2 = Switch('t2')
t2.addInput(s1.down())
t2.addInput(s5.down())
print('t2 inputs: ' + str(t2.getInputs()))

# Adding inputs to t3
t3 = Switch('t3')
t3.addInput(s1.up())
t3.addInput(s5.up())
print('t3 inputs: ' + str(t3.getInputs()))

# Adding inputs to t4
t4 = Switch('t4')
t4.addInput(s2.down())
t4.addInput(s6.down())
print('t4 inputs: ' + str(t4.getInputs()))

# Adding inputs to t5
t5 = Switch('t5')
t5.addInput(s2.up())
t5.addInput(s6.up())
print('t5 inputs: ' + str(t5.getInputs()))

# Adding inputs to t6
t6 = Switch('t6')
t6.addInput(s3.down())
t6.addInput(s7.down())
print('t6 inputs: ' + str(t6.getInputs()))

# Adding inputs to t7
t7 = Switch('t7')
t7.addInput(s3.up())
t7.addInput(s7.up())
print('t7 inputs: ' + str(t7.getInputs()))

print('\n')
# Emulate 16 x 3 Banyan network
for i in range(0, len(banyanInput16)):
    shortenedReverseBinary = banyanInput16[i].getReverseBinary()[-4:]
    # print(shortenedReverseBinary)
    # For t0
    if (banyanInput16[i].getPath()[-1] == 't0'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u0')
        else:
            banyanInput16[i].addToPath('u4')
    # For t1
    if (banyanInput16[i].getPath()[-1] == 't1'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u1')
        else:
            banyanInput16[i].addToPath('u5')
    # For t2
    if (banyanInput16[i].getPath()[-1] == 't2'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u2')
        else:
            banyanInput16[i].addToPath('u6')
    # For t3
    if (banyanInput16[i].getPath()[-1] == 't3'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u3')
        else:
            banyanInput16[i].addToPath('u7')
    # For t4
    if (banyanInput16[i].getPath()[-1] == 't4'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u0')
        else:
            banyanInput16[i].addToPath('u4')
    # For t5
    if (banyanInput16[i].getPath()[-1] == 't5'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u1')
        else:
            banyanInput16[i].addToPath('u5')
    # For t6
    if (banyanInput16[i].getPath()[-1] == 't6'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u2')
        else:
            banyanInput16[i].addToPath('u6')
    # For t7
    if (banyanInput16[i].getPath()[-1] == 't7'):
        if(shortenedReverseBinary[0] == '0'):
            banyanInput16[i].addToPath('u3')
        else:
            banyanInput16[i].addToPath('u7')
    # print(banyanInput16[i].getPath())

for i in range(0, len(banyanInput16)):
    shortenedReverseBinary = banyanInput16[i].getReverseBinary()[-4:]
    # print(shortenedReverseBinary)
    # For u0
    if (banyanInput16[i].getPath()[-1] == 'u0'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v0')
        else:
            banyanInput16[i].addToPath('v2')
    # For u1
    if (banyanInput16[i].getPath()[-1] == 'u1'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v1')
        else:
            banyanInput16[i].addToPath('v3')
    # For u2
    if (banyanInput16[i].getPath()[-1] == 'u2'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v0')
        else:
            banyanInput16[i].addToPath('v2')
    # For u3
    if (banyanInput16[i].getPath()[-1] == 'u3'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v1')
        else:
            banyanInput16[i].addToPath('v3')
    # For u4
    if (banyanInput16[i].getPath()[-1] == 'u4'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v4')
        else:
            banyanInput16[i].addToPath('v6')
    # For u5
    if (banyanInput16[i].getPath()[-1] == 'u5'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v5')
        else:
            banyanInput16[i].addToPath('v7')
    # For u6
    if (banyanInput16[i].getPath()[-1] == 'u6'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v4')
        else:
            banyanInput16[i].addToPath('v6')
    # For u7
    if (banyanInput16[i].getPath()[-1] == 'u7'):
        if(shortenedReverseBinary[1] == '0'):
            banyanInput16[i].addToPath('v5')
        else:
            banyanInput16[i].addToPath('v7')
    # print(banyanInput16[i].getPath())

for i in range(0, len(banyanInput16)):
    shortenedReverseBinary = banyanInput16[i].getReverseBinary()[-4:]
    # print(shortenedReverseBinary)
    # For v0
    if (banyanInput16[i].getPath()[-1] == 'v0'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w0')
        else:
            banyanInput16[i].addToPath('w1')
    # For v1
    if (banyanInput16[i].getPath()[-1] == 'v1'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w0')
        else:
            banyanInput16[i].addToPath('w1')
    # For v2
    if (banyanInput16[i].getPath()[-1] == 'v2'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w2')
        else:
            banyanInput16[i].addToPath('w3')
    # For v3
    if (banyanInput16[i].getPath()[-1] == 'v3'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w2')
        else:
            banyanInput16[i].addToPath('w3')
    # For v4
    if (banyanInput16[i].getPath()[-1] == 'v4'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w4')
        else:
            banyanInput16[i].addToPath('w5')
    # For v5
    if (banyanInput16[i].getPath()[-1] == 'v5'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w4')
        else:
            banyanInput16[i].addToPath('w5')
    # For v6
    if (banyanInput16[i].getPath()[-1] == 'v6'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w6')
        else:
            banyanInput16[i].addToPath('w7')
    # For v7
    if (banyanInput16[i].getPath()[-1] == 'v7'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w6')
        else:
            banyanInput16[i].addToPath('w7')
    # print(banyanInput16[i].getPath())

for i in range(0, len(banyanInput16)):
    shortenedReverseBinary = banyanInput16[i].getReverseBinary()[-4:]
    print(banyanInput16[i].getData(), end=' -> Binary = ')
    print(shortenedReverseBinary, end=': ')
    # For w0
    if (banyanInput16[i].getPath()[-1] == 'w0'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w0 UP')
        else:
            banyanInput16[i].addToPath('w0 DOWN')
    # For w1
    if (banyanInput16[i].getPath()[-1] == 'w1'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w1 UP')
        else:
            banyanInput16[i].addToPath('w1 DOWN')
    # For w2
    if (banyanInput16[i].getPath()[-1] == 'w2'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w2 UP')
        else:
            banyanInput16[i].addToPath('w2 DOWN')
    # For w3
    if (banyanInput16[i].getPath()[-1] == 'w3'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w3 UP')
        else:
            banyanInput16[i].addToPath('w3 DOWN')
    # For w4
    if (banyanInput16[i].getPath()[-1] == 'w4'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w4 UP')
        else:
            banyanInput16[i].addToPath('w4 DOWN')
    # For w5
    if (banyanInput16[i].getPath()[-1] == 'w5'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w5 UP')
        else:
            banyanInput16[i].addToPath('w5 DOWN')
    # For w6
    if (banyanInput16[i].getPath()[-1] == 'w6'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w6 UP')
        else:
            banyanInput16[i].addToPath('w6 DOWN')
    # For w7
    if (banyanInput16[i].getPath()[-1] == 'w7'):
        if(shortenedReverseBinary[2] == '0'):
            banyanInput16[i].addToPath('w7 UP')
        else:
            banyanInput16[i].addToPath('w7 DOWN')
    print(banyanInput16[i].getPath())