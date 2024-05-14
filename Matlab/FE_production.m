clear all
close all
clc

%% FE scheme stability region
lam = spectrum2('disk',10);
bounds=[-5 1 -5 5];
s=1;
p=1;
[h,poly_coeff] = opt_poly_bisect(lam,s,p,'chebyshev');

x = real(lam);
y = imag(lam);
plot(x,y,'x','MarkerSize',10,'LineWidth',2);
axis(bounds);
hold
plotstabreg_func(poly_coeff,bounds=bounds);

%% Reproduce FE scheme
indices=[2];
rk_fe = rk_opt(s,p,'erk','ssp');%,poly_coeff_ind=indices,poly_coeff_val=poly_coeff);
disp(rk_fe)

%% Slightly expanded FE scheme
lam = 2*spectrum2('disk',10);
bounds=[-5 1 -5 5];
s=2;
p=1;
[h,poly_coeff] = opt_poly_bisect(lam,s,p,'chebyshev');

x = real(lam);
y = imag(lam);
plot(x,y,'x','MarkerSize',10,'LineWidth',2);
axis(bounds);
hold
plotstabreg_func(poly_coeff,bounds=bounds);

%%
indices = [2];
rk_fe2 = rk_opt(s,p,'erk','ssp',poly_coeff_ind=indices,poly_coeff_val=poly_coeff);
disp(rk_fe2);
% rk_fe2s = rk_opt(s,p,'erk','ssp');
% disp(rk_fe2s);

%% RK4 Reproduction
lam = spectrum2('imagaxis', 500);
s = 4;
p = 4;
bounds = [-25 5 -15 15];
[h,poly_coeff] = opt_poly_bisect(lam,s,p,'rotated chebyshev');
plotstabreg_func(poly_coeff);
hold
plot_lam(lam,bounds);
indices = [5];
rk4 = rk_opt(s,p,'erk','ssp');
[p,q]=rk_stabfun(rk4);
disp(p);
rk42 = rk_opt(s,p,'erk','ssp');%,poly_coeff_ind=indices,poly_coeff_val=poly_coeff);

%%
lam1 = spectrum2('disk', 10);
lam2 = lam1 - 10;
lam = [lam1' lam2'];
s = 2;
p = 1;
bounds = [-25 5 -15 15];
% disp(lam);
% plot_lam(lam, bounds)
[h,poly_coeff] = opt_poly_bisect(lam,s,p,'rotated chebyshev');
plotstabreg_func(poly_coeff,bounds=bounds);
hold
plot_lam(lam,bounds);
s2 = 10;
solution = rk_opt(s2,p,'erk','ssp');
[p,q]=rk_stabfun(solution);
disp(p);
plotstabreg(solution);
%%
plot_lam(lam,[-30 5 -15 15])

function plot_lam(lam,bounds)
    x = real(lam);
    y = imag(lam);
    plot(x,y,'x','MarkerSize',10,'LineWidth',2);
    axis(bounds);
end