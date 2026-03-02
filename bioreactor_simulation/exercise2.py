import numpy as np
import matplotlib.pyplot as plt

t_start = np.array([0.00, 0.54, 0.90, 1.23, 1.58, 1.95, 2.33])
t_end   = np.array([0.54, 0.90, 1.23, 1.58, 1.95, 2.33, 2.70])

X_start = np.array([15.5, 23.0, 30.0, 38.8, 48.5, 58.3, 61.3])
X_end   = np.array([23.0, 30.0, 38.8, 48.5, 58.3, 61.3, 62.5])

S_const = np.array([137.0, 114.0, 90.0, 43.0, 29.0, 9.0, 2.0])

t_X = np.concatenate(([t_start[0]], t_end))
X_t = np.concatenate(([X_start[0]], X_end))

t_S = np.ravel(np.column_stack([t_start, t_end]))
S_t = np.ravel(np.column_stack([S_const, S_const]))


plt.figure(figsize=(7,4.5))
plt.plot(t_X, X_t, marker="o", linewidth=2)
plt.xlabel("Time $t$ (h)")
plt.ylabel("Cell concentration $X$ (g/L)")
plt.title("Cell concentration $X(t)$")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("X_vs_time.png", dpi=300)
plt.show()

plt.figure(figsize=(7,4.5))
plt.step(t_S, S_t, where="post", linewidth=2)
plt.xlabel("Time $t$ (h)")
plt.ylabel("Lactose concentration $S$ (g/L)")
plt.title("Lactose concentration $S(t)$")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("S_vs_time.png", dpi=300)
plt.show()