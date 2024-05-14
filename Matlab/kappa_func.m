function lam_func = kappa_func()
    lam_func = @(kappa) spectrum('rectangle',100,kappa,10);
end