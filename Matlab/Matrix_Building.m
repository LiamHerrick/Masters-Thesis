% clear all
% close all
% clc

%% Full Scheme
function [A_block, b_block] = PI_Scheme(A, b, S, K, lam)
    A_block = gen_A_matrix(A,lam,S,K);
    b_block = gen_b_matrix(S,b,lam,K);
end

%% PFEasRK
function [A b] = PFEasRK(lam,K)
    A = zeros(K+1);
    counter = 0;
    for i = 1:K+1
        for j = 1:counter
            A(i,j) = 1;
        end
        counter = counter + 1;
    end
    A = A * lam;

    b = ones(K+1,1);
    b(K) = (1/lam) - K;
    b = b * lam;
end

%% c_values
function c = get_c_values(A)
    K = size(A);
    K = K(1);
    % c = zeros(1,K);
    c = zeros(K,1);
    for i = 1:K
       c(i) = sum(A(i,:));
    end
end

%% Almost zeros
function Z = almost_zero_mat(S,lam,K,A,L)
    c = get_c_values(A);
    Z = zeros(K+1,K+1);
    Z(:,end) = (c(S)/lam-(K+1))*(A(S,L)/c(S));
    Z = Z * lam;
end

%% Lambda Matrix
function lam_mat = gen_lam_mat(S,lam,K,A)
    c = get_c_values(A);
    lam_mat = ones(K+1);
    lam_mat(:,end) = 1 + ((c(S)/lam) - (K+1))*(A(S,1)/c(S));
    lam_mat = lam_mat * lam;
end

%% Zero Matrix
function empty_mat = gen_zeros(K)
    empty_mat = zeros(K+1);
end

%% Zero Vector
function empty_vec = gen_zeros_vec(K)
    empty_vec = zeros(K+1,1);
end

%% b1 Vector
function b1 = b1_vec(b,lam,K)
    b1 = ones(K+1,1);
    b1(K+1) = b(1) * ((1/lam)-(K+1)) + 1;
    b1 = b1 * lam;
end

%% Full b matrix
function b_structure = gen_b_matrix(S,b,lam,K)
    b_structure = [];
    b_structure = [b_structure; b1_vec(b,lam,K)];
    % b_structure = [b1_vec(b,lam,K)];
    for i = 2:S
        b_list = gen_zeros_vec(K);
        b_list(K+1) = ((1/lam)-(K+1))*b(i);
        b_list = b_list * lam;
        b_structure = [b_structure; b_list];
    end
    % b_structure = cat(b_structure);
end

%% A Matrix
function block_structure = gen_A_matrix(A, lam, S, K)
    N = (K+1)*S;
    block_structure = zeros(N,N);
    
    % First row
    [A_t, ~] = PFEasRK(lam,K);
    block_structure(1:K+1,1:K+1) = A_t;

    % Main loop from 2 to S
    for i=2:S
        % Diagonal entries
        block_structure((i-1)*(K+1)+1:i*(K+1),(i-1)*(K+1)+1:i*(K+1)) = PFEasRK(lam,K);
        if i > 2
            for j=2:i-1
                block_structure(i*(K+1)-K:i*(K+1),j*(K+1)-K:j*(K+1)) = almost_zero_mat(i,lam,K,A,j);
            end
        end
        block_structure((i-1)*(K+1)+1:(i-1)*(K+1)+1+K,1:K+1) = gen_lam_mat(i,lam,K,A);
    end
    % disp(block_structure);
    % disp(size(block_structure));
end

%% Full Scheme
% function [A_block, b_block] = PI_Scheme(A, b, S, K, lam)
%     A_block = gen_A_matrix(A,lam,S,K);
%     b_block = gen_b_matrix(S,b,lam,K);
% end

%% Testing area
lam = 0.01;

% Heun
A = [0 0; 1 0];
b = [1/2 1/2];
K = 3;
S = 2;

[A_block, b_block] = PI_Scheme(A,b,S,K,lam);
disp(A_block);
disp(b_block);

% RK Base
rk.A = A_block;
rk.b = b_block;
[p,q] = rk_stabfun(rk);
disp(p);
bounds = [-100 5 -10 10];
plotstabreg(rk,bounds);

%% RK4
A = [0 0 0 0; 0.5 0 0 0; 0 0.5 0 0; 0 0 1 0];
b = [1/6 1/3 1/3 1/6];
K = 2;
S = 4;
lam = 0.01;

[A_block, b_block] = PI_Scheme(A,b,S,K,lam);
% disp(A_block);
% disp(b_block);

% RK Base
rk.A = A_block;
rk.b = b_block;
[p,q] = rk_stabfun(rk);
% disp('Poly Coeffs');
% disp(p);
bounds = [-100 5 -10 10];
% plotstabreg(rk,bounds);

% rk2 = rk_opt(3,1,'erk','ssp',poly_coeff_ind=[2:3],poly_coeff_val=p0(3:4));
rk_test = rk_opt(S*(K+1),4,'erk','ssp',poly_coeff_ind=[4:12],poly_coeff_val=p(5:13));
plotstabreg(rk_test,bounds);