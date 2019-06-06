s = tf('s');
g = tf(1, [0.01, 0.11, 0.1])
T = 0.18;
gc = 5 + 0.3*s + 5/(s*T);
% gc = (5*T*s + 0.3*T*s^2 + 5)/(s*T);

step(g)

denominator = 1 + g*gc;
% denominator = 1 +  (5*T*s + 0.3*T*s^2 + 5)/(s*T*(0.01*s^2 + 0.11*s + 0.1)) == 0;
% denominator = T*(0.01*s^3 + 0.11*s^2 + 0.1*s + 5*s + 0.3*s^2) + 5 == 0;
% denominator = T*(0.01*s^3 + 0.41*s^2 + 5.1*s) + 5 == 0;
% denominator = 1 + T*(0.002*s^3 + 0.082*s^2 + 1.02*s) == 0;
% eq = 1 + T*(0.002*s^2 + 0.082*s^1 + 1.02)*s;
r = roots([0.002 0.082 1.02]);
f = @(x) 0.002*x^2 + 0.082*x^1 + 1.02;
f(r(1));
f(r(2));
desired = -8.7 + 8.7i; %desired
sym t;
d = desired;

eq = 1 + (5*t*d + 0.3*t*d^2 + 5)/(d*t*(0.01*d^2 + 0.11*d + 0.1)) == 0;
eq2 = 1 + t*(0.002*d^2 + 0.082*d + 1.02)*d == 0;

% T_approx = -1/(0.002*desired^2 + 0.082*desired + 1.02)*desired
% zero at s = 0, -20.5000 + 9.4736i, -20.5000 - 9.4736i
double(solve(eq2, t))
double(solve(eq, t))


closed = feedback(g*gc, 1)



