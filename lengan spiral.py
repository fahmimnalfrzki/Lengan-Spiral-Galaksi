from numpy import*
from matplotlib.pyplot import*

#Membuka data
file1=open('melnik95.txt','r')
file2=open('novocc.tsv','r')
mel=file1.readlines()
nov=file2.readlines()

#Definisikan variabel dan konstanta
l_mel=[]
b_mel=[]
l_nov=[]
b_nov=[]
d_mel=[]
d_nov=[]
logt_nov=[]

X0=8
derad=pi/180

#Membaca data dan memasukan data ke variabel
for i in range(45,len(mel)):
    if len(mel[i].split())==7:
        l_mel.append(float(mel[i].split()[4]))
        b_mel.append(float(mel[i].split()[5]))
        d_mel.append(float(mel[i].split()[6]))
    if len(mel[i].split())==8:
        l_mel.append(float(mel[i].split()[5]))
        b_mel.append(float(mel[i].split()[6]))
        d_mel.append(float(mel[i].split()[7]))

for i in range(43,len(nov)):
    if len(nov[i].split())==4:
        l_nov.append(float(nov[i].split()[0]))
        b_nov.append(float(nov[i].split()[1]))
        d_nov.append(float(nov[i].split()[2]))
        logt_nov.append(float(nov[i].split()[3]))

#Menghitung koordinat galaktosentris (No.1)
l_mel=array(l_mel)
b_mel=array(b_mel)
d_mel=array(d_mel)
l_nov=array(l_nov)
b_nov=array(b_nov)
d_nov=array(d_nov)/1000

X_mel=X0-d_mel*cos(b_mel*derad)*cos(l_mel*derad)
Y_mel=d_mel*cos(b_mel*derad)*sin(l_mel*derad)
Z_mel=d_mel*sin(b_mel*derad)
X_nov=X0-d_nov*cos(b_nov*derad)*cos(l_nov*derad)
Y_nov=d_nov*cos(b_nov*derad)*sin(l_nov*derad)
Z_nov=d_nov*sin(b_nov*derad)

#Plot Z terhadap l (No. 2)
fi=figure(0)
f=fi.add_subplot(111)
f.scatter(l_nov,Z_nov,c='r',marker='x',label='Gugus Terbuka')
f.scatter(l_mel,Z_mel,c='b',marker='o',label='OB')
f.set_title('Hubungan Z dan l')
f.set_xlabel('l (deg)')
f.set_ylabel('Z (kpc)')
f.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#pilah objek Z<0.3 (No. 3)
X1_mel=[]
Y1_mel=[]
X1_nov=[]
Y1_nov=[]
logt=[]
for i in range(len(Z_mel)):
    if Z_mel[i]<0.3:
        X1_mel.append(X_mel[i])
        Y1_mel.append(Y_mel[i])
for i in range(len(Z_nov)):
    if Z_nov[i]<0.3:
        X1_nov.append(X_nov[i])
        Y1_nov.append(Y_nov[i])
        logt.append(logt_nov[i])

X1_mel=array(X1_mel)
Y1_mel=array(Y1_mel)
X1_nov=array(X1_nov)
Y1_nov=array(Y1_nov)
logt=array(logt)

#Plot X vs Y Gugus Terbuka (No. 4)
X1=[]
Y1=[]
Yn=[]

for i in range(len(X1_nov)):
    if X1_nov[i] < 12:
        X1.append(X1_nov[i])
    if Y1_nov[i] > -6 and Y1_nov[i] < 6:
        Y1.append(Y1_nov[i])
for i in range(len(X1)):
    Yn.append(Y1[i])
        
fi2=figure(2)
f=fi2.add_subplot(111)
f.scatter(Yn,X1,c='r',marker='x')
f.set_title('Plot X terhadap Y Gugus Terbuka')
f.set_xlabel('Y (kpc)')
f.set_ylabel('X (kpc)')

theta=linspace(-0.2*pi,0.2*pi)
r1=2.1*exp(-0.6*theta+1.13)
r2=2.1*exp(-0.6*theta+1.38)
r3=2.1*exp(-0.65*theta+1.68)
xf=r1*cos(theta)
yf=r1*sin(theta)
xf1=r2*cos(theta)
yf1=r2*sin(theta)
xf2=r3*cos(theta)
yf2=r3*sin(theta)

#Plot X dan Y untuk 7.5<logt<8.5 (No. 5)
X2=[]
Y2=[]
Y1n=[]
logt=array(logt)

for i in range(len(X1_nov)):
    if X1_nov[i] < 12:
        if logt[i]>7.5 and logt[i]<8.5:
            X2.append(X1_nov[i])
    if Y1_nov[i] > -6 and Y1_nov[i] < 6:
        if logt[i]>7.5 and logt[i]<8.5:
            Y2.append(Y1_nov[i])
for i in range(len(X2)):
    Y1n.append(Y2[i])
        
fi3=figure(3)
f=fi3.add_subplot(111)
f.scatter(Y1n,X2,c='r',marker='x')
'''f.plot(yf,xf,c='k')
f.plot(yf1,xf1,c='k')
f.plot(yf2,xf2,c='k')'''
f.set_title(r'Plot X terhadap Y Gugus Terbuka untuk 7.5 < $\log t$ <8.5')
f.set_xlabel('Y (kpc)')
f.set_ylabel('X (kpc)')


#Plot X dan Y untuk logt<7.5 (No. 5)
X3=[]
Y3=[]
Y2n=[]

for i in range(len(X1_nov)):
    if X1_nov[i] < 12:
        if logt[i]<7.5:
            X3.append(X1_nov[i])
    if Y1_nov[i] > -6 and Y1_nov[i] < 6:
        if logt[i]<7.5:
            Y3.append(Y1_nov[i])
for i in range(len(X3)):
    Y2n.append(Y3[i])

fi4=figure(4)
f=fi4.add_subplot(111)
f.scatter(Y2n,X3,c='r',marker='x')
'''f.plot(yf,xf,c='k')
f.plot(yf1,xf1,c='k')
f.plot(yf2,xf2,c='k')'''
f.set_title(r'Plot X terhadap Y Gugus Terbuka untuk $\log t$ < 7.5')
f.set_xlabel('Y (kpc)')
f.set_ylabel('X (kpc)')


#Plot X dan Y bintang OB No.7
Xo=[]
Yo=[]
Xon=[]

for i in range(len(X_mel)):
    if X_mel[i] < 12:
        Xo.append(X_mel[i])
    if Y_mel[i] > -6 and Y_mel[i] < 6:
        Yo.append(Y_mel[i])
for i in range(len(Yo)):
    Xon.append(Xo[i])
        
fi6=figure(6)
f=fi6.add_subplot(111)
f.scatter(Yo,Xon,c='b',marker='o')
f.plot(yf,xf,c='k')
f.plot(yf1,xf1,c='k')
f.plot(yf2,xf2,c='k')
f.set_title('Plot X terhadap Y Bintang OB')
f.set_xlabel('Y (kpc)')
f.set_ylabel('X (kpc)')

#Plot X dan Y bintang OB No.7