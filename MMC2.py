import numpy as np

lam = -10000.0
T = 1.0
tol = 1e-10
u0 = 1.0

def solve_u(lam, T, tau):
    n = int(T / tau)
    u = np.zeros(n + 1)
    x = np.linspace(0, T, n + 1)
    u[0] = u0
    for i in range(n):
        u[i + 1] = (u[i] + tau * (1 - lam * x[i + 1])) / (1 - tau * lam)
    return x, u

reached_tolerance = False
for tau in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    x, u_num = solve_u(lam, T, tau)
    u_exact = np.exp(lam * x) + x
    err = np.max(np.abs(u_num - u_exact))
    print(f"tau = {tau:.1e}, max error = {err:.2e}")
    if err <= tol:
        print(f"Required tolerance reached at tau = {tau:.1e}")
        reached_tolerance = True
        break

if not reached_tolerance:
    print(f"Tolerance {tol:.1e} was not reached for the listed step sizes.")
