%%Parcial1
%Ignacio Alvarado Reyes A01656149
% Clear the enviroment
clear all
close all
clc

% Cargar los datos
estatura  = xlsread('Datos.xlsx',1,'A2:A227');
talla = xlsread('Datos.xlsx',1,'B2:B227');

% Medidas de tendencia central (media y desviación estándar)
mediaEstatura = median(estatura);
mediaTalla = median(talla);

desviacionEstatura = std(estatura);
desviacionTalla = std(talla);

% Funciones 
yEstatura= @(x) (1/(11.1693*sqrt(2*pi)))*exp(-((((x-169)^2)/(2*(11.1693)^2))));
yTalla= @(x) (1/(1.8465*sqrt(2*pi)))*exp(-((((x-26)^2)/(2*(1.8465)^2))));

% Gráfica PDF función normal

pEs = makedist('Normal','mu',169,'sigma',11.1693);
pTal = makedist('Normal','mu',26,'sigma',1.8465);

%plot(pEs)
%plot(pTal)

% Histogramas

%histogram(estatura)
%histogram(talla)

% Datos Separados por Género

estaturaMasc  = xlsread('DatosMasc.xlsx',1,'A2:A130');
tallaMasc = xlsread('DatosMasc.xlsx',1,'B2:B130');

estaturaFem  = xlsread('DatosFem.xlsx',1,'A2:A96');
tallaFem = xlsread('DatosFem.xlsx',1,'B2:B96');
