tic
lam = spectrum2('gap',500); % Returns N values in the complex plane
s = 2;
p = 2;

[h,poly_coeff] = opt_poly_bisect(lam,s,p,'chebyshev');

fprintf('h is %d.\n', h);
disp('poly_coeff is')
disp(size(poly_coeff));
disp(poly_coeff);
% plotstabreg_func(poly_coeff,[1]);

opt1 = rk_opt(s,p,'erk','ssp',poly_coeff_val = poly_coeff);

lam = spectrum2('gap',6400); % Returns N values in the complex plane
s = 2;
p = 2;

[h,poly_coeff] = opt_poly_bisect(lam,s,p,'chebyshev');

fprintf('h is %d.\n', h);
disp('poly_coeff is')
disp(size(poly_coeff));
disp(poly_coeff);
% plotstabreg_func(poly_coeff,[1]);

opt2 = rk_opt(s,p,'erk','ssp',poly_coeff_val = poly_coeff);
disp('N = 500')
disp('A')
disp(opt1.A)
disp('b')
disp(opt1.b)
disp('c')
disp(opt1.c)

disp('N = 6400')
disp('A')
disp(opt2.A)
disp('b')
disp(opt2.b)
disp('c')
disp(opt2.c)

disp("Finished");
toc