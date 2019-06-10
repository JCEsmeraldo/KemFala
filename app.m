[x,fa]=audioread('/mnt/5084755F8475488C/Projetos/KemFala/Samples/ze1.wav');
n=length(x);
X = abs(fft(x))/(n/2);
#n=length(x);
f=0:fa/(n-1):fa;
subplot(2,1,1)
plot(f(1:n/2),X(1:n/2))
hold on
fc=1800;
Wc=(2*pi*fc/fa)/pi; %frequencia de corte em tempo discreto
num = fir1(30,Wc);
[h,w]=freqz(num,1,512,fa); %Calcula a resposta em frequencia do filtro
subplot(2,1,1)
plot(w,abs(h),'r')
y = filter(num,1,x);
Y = abs(fft(y))/(n/2);
subplot(2,1,2)
plot(f(1:n/2),Y(1:n/2))
audiowrite('/mnt/5084755F8475488C/Projetos/KemFala/Samples/filtrado.wav',y,fa)
sound(y,fa)