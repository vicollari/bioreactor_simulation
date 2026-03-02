import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Data from the table
# -----------------------------
# Time interval bounds (h)
t_start = np.array([0.00, 0.54, 0.90, 1.23, 1.58, 1.95, 2.33])
t_end   = np.array([0.54, 0.90, 1.23, 1.58, 1.95, 2.33, 2.70])

# Cell concentration X ranges (g/L): X goes from X_i to X_f in each interval
X_i = np.array([15.5, 23.0, 30.0, 38.8, 48.5, 58.3, 61.3])
X_f = np.array([23.0, 30.0, 38.8, 48.5, 58.3, 61.3, 62.5])

# Lactose concentration S (g/L): constant within each interval
S = np.array([137.0, 114.0, 90.0, 43.0, 29.0, 9.0, 2.0])

# -----------------------------
# Build piecewise profiles
# -----------------------------
# For X(t): straight lines in each interval; we can plot just endpoints
t_X = np.r_[t_start[0], np.repeat(t_end, 1)]   # [0, 0.54, 0.9, ...]
X_t = np.r_[X_i[0], X_f]                       # [15.5, 23, 30, ...]

# For S(t): step function (constant per interval)
# We'll create "stairs" coordinates
t_S = np.ravel(np.column_stack([t_start, t_end]))  # [t0, t1, t1, t2, ...]
S_t = np.ravel(np.column_stack([S, S]))            # [S1, S1, S2, S2, ...]

# -----------------------------
# Plot
# -----------------------------
fig, ax1 = plt.subplots(figsize=(8,5))

# X(t)
ax1.plot(t_X, X_t, marker='o', linewidth=2)
ax1.set_xlabel('Time t (h)')
ax1.set_ylabel('Cell concentration X (g/L)')
ax1.grid(True, alpha=0.3)

# S(t) on a second y-axis
ax2 = ax1.twinx()
ax2.step(t_S, S_t, where='post', linewidth=2)
ax2.set_ylabel('Lactose concentration S (g/L)')

plt.title('Batch growth data: X(t) and S(t)')
plt.tight_layout()
plt.show()