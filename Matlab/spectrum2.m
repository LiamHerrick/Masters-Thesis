test = spectrum('gap', 500);

plot(real(test), imag(test), 'o');
xlabel('Real part');
ylabel('Imaginary part')
grid on;


% lam = spectrum('realaxis',500);
% s = 10; p = 2;
% [h,poly_coeff] = opt_poly_bisect(lam,s,p,'chebyshev');
% 
% lam_func = @(kappa) spectrum('rectangle',100,kappa,10);
% [h,poly_coeff] = opt_poly_bisect(lam,20,1,'chebyshev','lam_func',lam_func);
% plotstabreg_func(poly_coeff,[1]);

function lamda = spectrum(name,N,kappa,beta)
% function lamda = spectrum(name,N,kappa,beta)
%
% Return N discretely sampled values from certain sets in the complex plane.
%
% Acceptable values for name:
%       * 'realaxis':     `[-1,0]`
%       * 'imagaxis':     `[-i,i]`
%       * 'disk':         `{z : |z+1|=1}`
%       * 'rectangle':    `{x+iy : -\beta \le y \le \beta, -\kappa \le x \le 0}`
%       * 'Niegemann-ellipse' and 'Niegemann-circle':  See :cite:`niegemann2011`
%       * 'gap':          Spectrum with a gap; see :cite:`2012_optimal_stability_polynomials`
%
% kappa and beta are used only if name == 'rectangle'

if nargin<4 beta=0; end
if nargin<3 kappa=1; end

switch name
  case 'realaxis'
    lamda = -linspace(0,1,N).';
  case 'imagaxis'
    lamda = 1i*linspace(0,1,N).';
  case 'disk'
    theta = linspace(0,pi,N);
    lamda = (-1+cos(theta) + 1i*sin(theta)).';
  case 'rectangle'
    imag_lim = beta;
    l1 = 1i*linspace(0,imag_lim,50);
    l2 = 1i*imag_lim + linspace(-kappa,0,N);
    l3 = -kappa + 1i*linspace(0,imag_lim,50);
    lamda = [l1 l2 l3].';
  case 'Niegemann-ellipse'
    lamda_0 = sqrt(3.)/2; % = cos(arcsin(0.5))
    theta = linspace(0,2*pi,N);
    lamda = (min(-0.5*(lamda_0+cos(theta)),0.) + 1i*sin(theta)).';
  case 'Niegemann-circle'
    labda_0 = sqrt(3.)/2; % = cos(arcsin(0.5))
    theta = linspace(0,2*pi,N);
    lamda = (min(-(labda_0+cos(theta)),0.) + 1i*sin(theta)).';
  case 'gap'
    % gap = 20;
    gap = 5;
    d   = 1;
    z1= 1i*linspace(0,1,N);
    theta=linspace(pi/2.,pi,N);
    z2 = cos(theta)+1i*sin(theta);
    theta=linspace(0,pi,N);
    z3 = d*(cos(theta)+1i*sin(theta))-gap;
    lamda = [z1 z2 z3].';
end
end