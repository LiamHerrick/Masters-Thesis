% clear all
% % Define a polynomial representing the complex domain
% % polynomial = [1, 0, -1];  % Example: z^2 - 1
% % Input is coefficients of polynomial
% polynomial = [2, (3+0.5i), 5, (-4+2i)];
% 
% % Number of points to sample
% N = 100;
% 
% % Generate sampled values within the complex domain
% sampled_values = spectrum_from_polynomial(polynomial, N);
% 
% % Display the sampled values
% % disp(sampled_values);
% 
% plot(real(sampled_values), imag(sampled_values), 'o');
% xlabel('Real part');
% ylabel('Imaginary part')
% grid on;

function lamda = spectrum_from_polynomial(polynomial, N)
% Function to generate discrete values sampled within a complex domain
% defined by a polynomial.
%
% Inputs:
% - polynomial: A polynomial representing the complex domain.
% - N: Number of points to sample.
%
% Output:
% - lamda: Array of complex values sampled within the complex domain.

% Generate parameter values
t_values = linspace(0, 2*pi, N);  % Sample parameter values evenly
polynomial_values = polyval(polynomial, exp(1i*t_values));  % Evaluate polynomial at parameter values

% Return sampled values as complex numbers
lamda = polynomial_values.';
end
