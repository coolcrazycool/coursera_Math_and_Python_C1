# # HW Week4
# 
# ## Рассмотрим логистическое распределение
# 
# Среднее: $$E[x]= \frac{k*x_m}{k-1}, при  k>1$$
# Дисперсия: $$D[x]=(\frac{x_m}{k-1})^2*\frac{k}{k-2}, при k>2$$

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
import math

# Найдем E и D, xm по умолчанию = 1, k=b - коэффициент кривизны, возьмем 3(3>2)
xm = 1.
k = 3.

# Тогда посчитаем E и D по формулам выше
E = (xm * k) / (k - 1)
D = (E ** 2) * (k / (k - 2))

# Сгенерируем выборку объема 1000
pareto = sts.pareto(b=3)
sample = pareto.rvs(1000)


# Построим гистограмму выборки, теоретическую плотность
x = np.linspace(1, 10, 1000)
pdf = pareto.pdf(x)
plt.plot(x, pdf, label='theoretical pdf', color='red', alpha=0.5)
plt.hist(sample, bins=50, range=(1, 10), density=True)
plt.legend()

plt.ylabel('fraction of samples')
plt.xlabel('$x$')
plt.show()


# Сгенерируем массив выборочных средних для n=5
sample_5 = [pareto.rvs(5).mean() for _ in range(1000)]

# Вычислим математическое ожидание, дисперсию и среднее квадратичное
E_5 = E
D_5 = D / 5
g_5 = math.sqrt(D_5)

# Нормальное распределение Парето
n_5 = sts.norm(E_5, g_5)

# Найдем плотность распределения
pdf_5 = n_5.pdf(x[:600])

# Построим гистограмму
plt.plot(x[:600], pdf_5, label='theoretical pdf, n=5', color='red', alpha=0.5)
plt.hist(sample_5, bins=50, range=(1, 6), density=True)
plt.legend()

plt.ylabel('fraction of samples')
plt.xlabel('$x$')
plt.show()


# Повторим предыдущую ячейку для n = 10
# Сгенерируем массив выборочных средних для n=10
sample_10 = [pareto.rvs(10).mean() for _ in range(1000)]

# Вычислим математическое ожидание, дисперсию и среднее квадратичное
E_10 = E
D_10 = D / 10
g_10 = math.sqrt(D_10)

# Нормальное распределение Парето
n_10 = sts.norm(E_10, g_10)

# Найдем плотность распределения
pdf_10 = n_10.pdf(x[:400])

# Построим гистограмму
plt.plot(x[:400], pdf_10, label='theoretical pdf, n=10', color='red', alpha=0.5)
plt.hist(sample_10, bins=50, range=(1, 4), density=True)
plt.legend()

plt.ylabel('fraction of samples')
plt.xlabel('$x$')
plt.show()


# Повторим предыдущую ячейку для n = 50
# Сгенерируем массив выборочных средних для n=50
sample_50 = [pareto.rvs(50).mean() for _ in range(1000)]

# Вычислим математическое ожидание, дисперсию и среднее квадратичное
E_50 = E
D_50 = D / 50
g_50 = math.sqrt(D_50)

# Нормальное распределение Парето
n_50 = sts.norm(E_50, g_50)

# Найдем плотность распределения
pdf_50 = n_50.pdf(x[:300])

# Построим гистограмму
plt.plot(x[:300], pdf_50, label='theoretical pdf, n=50', color='red', alpha=0.5)
plt.hist(sample_50, bins=50, range=(1, 3), density=True)
plt.legend()

plt.ylabel('fraction of samples')
plt.xlabel('$x$')
plt.show()


# При увеличении n - увеличивается точность апроксимации выборочного среднего значения непрерывной случайной
# величины, которая описана распределением Парето. Распеределение Парето заметно скошено при малых n. Функция
# сходится медленно. Максимальную симметричность достигнет при очень больших n.
