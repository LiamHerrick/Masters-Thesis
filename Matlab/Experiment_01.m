clear all
close all
clc

%% RK_Opt 1/3 Scheme
rk_base = rk_opt(3,1,'erk','ssp');
[p,q] = rk_stabfun(rk_base);
disp(p);
plotstabreg(rk_base);
% disp(rk_base);


%% Adjusting coefficients
val = [0.0925, 0.0023];
rk1 = rk_opt(3,1,'erk','ssp',poly_coeff_ind=[2:3],poly_coeff_val=val(1:2));
[p1,q1] = rk_stabfun(rk1);
disp(p1);
bounds = [-20 5 -10 10];
plotstabreg(rk1,bounds);
disp(rk1.A);





%% Standard lambda scheme
lam = 0.05;
A = [0 0 0; lam 0 0; lam lam 0];
b = [lam lam 1-2*lam];
c = [0 lam 2*lam];
rk.A = A;
rk.b = b';
rk.c = c';
[p0,q0] = rk_stabfun(rk);
disp(p0);
bounds = [-40 1 -10 10];
plotstabreg(rk,bounds);
% plotstabreg_func(p0,q0,bounds);

%%
% vals = [0.17 0.8];
vals = [0.0 0.8];
rk2 = rk_opt(3,1,'erk','ssp',poly_coeff_ind=[2:3],poly_coeff_val=p0(3:4));
[p2,q2] = rk_stabfun(rk2);
disp(p2);
plotstabreg(rk2,bounds);
