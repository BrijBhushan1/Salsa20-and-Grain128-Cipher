****************  Python program of Salsa20 cipher:*********************

list1 = [211,159,13,115,76,55,82,183,3,117,222,37,191,187,234,136,49,237,179,48,1,106,178,219,175,199,166,48,86,16,179,207,
31,240,32,63,15,83,93,161,116,147,48,113,238,55,204,36,
79,201,235,79,3,81,156,47,203,26,244,243,88,118,104,54];
list3 = [];
i=0;
while i<64:
list3.append('{0:08b}'.format(list1[i]))
i=i+1;
# rotation function
def rotation(strg,n):
return strg[:2]+strg[n:] + strg[2:n]
# littteendian functiom
listword = [];
j=0;
while j<64:
listword.append('{0:032b}'.format(list1[j]+pow(2,8)*list1[j+1]+pow(2,16)*list1[j+2]+pow(2,24)*list1[j+3]));
j=j+4;
zz=listword[:];
def quarterround(x,y,z,w):
#z[1]=y1^((y1+y3)<<<7), z[2]=y2^((z1+y0)<<<9)
#z[3]=y3^((z2+y1)<<<13), z[0]=y0^((z3+z2)<<<18)
zz[y]='{0:032b}'.format(int(zz[y],2) ^ int((rotation(bin(int(zz[y],2)+int(zz[w],2)),-7)),2))
zz[z]='{0:032b}'.format(int(zz[z],2) ^ int((rotation(bin(int(zz[y],2)+int(zz[x],2)),-9)),2))
zz[w]='{0:032b}'.format(int(zz[w],2) ^ int((rotation(bin(int(zz[z],2)+int(zz[y],2)),-13)),2))
zz[x]='{0:032b}'.format(int(zz[x],2) ^ int((rotation(bin(int(zz[w],2)+int(zz[z],2)),-18)),2))
def rowround():
#(z0,z1,z2,z3)
quarterround(x=0,y=1,z=2,w=3);
#(z4,z5,z6,z7) = quarterround(y4,y5,y6,y7)
quarterround(x=4,y=5,z=6,w=7);
#(z8,z9,z10,z11) = quarterround(y8,y9,y10,y11)
quarterround(x=8,y=9,z=10,w=11);
#(z12,z13,z14,z15) = quarterround(y12,y13,y14,y15)
quarterround(x=12,y=13,z=14,w=15);
Page 10
def columnround():
#(y0,y4,y8, y12) = quarterround(x0,x4,x8,x12)
quarterround(x=0,y=4,z=8,w=12);
#(y5,y9,y13, y1) = quarterround(x5,x9,x13,x1)
quarterround(x=5,y=9,z=13,w=1);
#(y10,y14,y2, y6) = quarterround(x10,x14,x2,x6)
quarterround(x=10,y=14,z=2,w=6);
#(y15,y3,y7, y11) = quarterround(x15,x3,x7,x11)
quarterround(x=15,z=3,y=7,w=11);
def doubleround():
# doubleround(x)=
rowround(columnround());
# Calling 10 time doubleround function
i=0;
while i<10
columnround();
rowround();
i=i+1;
keybin=[];
keydec=[];
#Calculating back the 64 byte sequence
i=0;
while i<16:
a=zz[i];
j=0;
while j<32:
keybin.append(a[j:j+7]);
keydec.append(int(a[j:j+7],2));
j=j+8;
i=i+1;
k=0;
while k<64:
print((keydec[k]));
k=k+1;