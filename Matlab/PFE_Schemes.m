clear all
close all
clc

lam = 0.001;

A = [0 0 0; lam 0 0; lam lam 0];
b = [lam lam 1-2*lam];
c = [0 lam 2*lam];
rk.A = A;
rk.b = b';
rk.c = c';
[p,q] = rk_stabfun(rk);

rk_new = rk_opt(3,1,'erk','ssp',poly_coeff_ind=[2:3],poly_coeff_val=p(3:4));
[p1,q1] = rk_stabfun(rk_new);


disp('c');
disp(rk_new.c);
disp('A');
disp(rk_new.A);
disp('b');
disp(rk_new.b);

% disp('Original');
% disp(p);
% disp('New');
% disp(p1);


%%
bounds = [-50 1 -25 25];
% bounds = [-1/lam-100 5 -100 100];
plotstabreg(rk,bounds);
% plotstabreg_func(p,q,bounds);
