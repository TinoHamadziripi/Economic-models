import matplotlib.pyplot as plt


class SolowModel(object):
    """
    Parameters
    ==========

    n = population growth
    s = savings rate
    delta = depreciation rate
    alpha = share of labor
    z = productivity parameter
    k = current capital stock

    """

    def __init__(self, n=0.001, s=0.25, delta=0.2,
                 alpha=0.2, z=2.0, k=1.0):
        self.n = n
        self.s = s
        self.delta = delta
        self.alpha = alpha
        self.z = z
        self.k = k

    @property
    def solow_func(self):
        lhs = (self.s * self.z * self.k ** self.alpha +
               (1 - self.delta) * self.k) / (1 - self.n)
        return lhs

    def update(self) -> object:
        self.k = self.solow_func

    @property
    def steady_state(self):
        new_capital: float = ((self.s * self.z) / (self.n + self.delta)
                              ) ** (1 / (1 - self.alpha))
        return new_capital

    def generate_timeseries(self, t: object) -> object:
        seq = []
        for i in range(t):
            seq.append(self.k)
            self.update()
        return seq


# plot model
s_mod = SolowModel()
s_mod1 = SolowModel(k=8.0)
T = 50
fig, ax = plt.subplots(figsize=(9, 6))
ax.plot([s_mod.steady_state] * T, 'k-', linestyle='dashed', label='steady state')

for i in s_mod, s_mod1:
    lab = 'Capital from initial state %s' % i.k
    ax.plot(i.generate_timeseries(T), 'o-', alpha=0.8, label=lab)

ax.legend()
ax.set_ylabel("Capital")
ax.set_xlabel("Time")
ax.set_title("Solow Growth Model - Steady State Capital")
plt.show()
