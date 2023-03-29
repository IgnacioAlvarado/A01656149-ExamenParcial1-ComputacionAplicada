%%matlabSol
% Ignacio Alvarado Reyes A01656149

syms a b c
potasio = 0.25*a + 0.15*b  == 1.5;
nitrato = 0.45*a + 0.5*b + 0.75*c == 5;
fosfato = 0.3*a + 0.35*b + 0.25*c == 3;

compuestos = solve([potasio, nitrato, fosfato], [a, b, c]);

compA = double(compuestos.a)
compB = double(compuestos.b)
compC = double(compuestos.c)
