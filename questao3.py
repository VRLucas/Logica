# Sequência a
sequencia_a = [1, 3, 5, 7]
sequencia_a.append(sequencia_a[-1] + 2)
print("a) Próximo elemento da sequência a:", sequencia_a[-1])

# Sequência b
sequencia_b = [2, 4, 8, 16, 32, 64]
sequencia_b.append(sequencia_b[-1] * 2)
print("b) Próximo elemento da sequência b:", sequencia_b[-1])

# Sequência c
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
sequencia_c.append(sequencia_c[-1] + (len(sequencia_c) ** 2))
print("c) Próximo elemento da sequência c:", sequencia_c[-1])

# Sequência d
sequencia_d = [4, 16, 36, 64]
sequencia_d.append(sequencia_d[-1] + ((len(sequencia_d) + 1) ** 2))
print("d) Próximo elemento da sequência d:", sequencia_d[-1])

# Sequência e
sequencia_e = [1, 1, 2, 3, 5, 8]
sequencia_e.append(sequencia_e[-1] + sequencia_e[-2])
print("e) Próximo elemento da sequência e:", sequencia_e[-1])

# Sequência f
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
sequencia_f.append(sequencia_f[-1] + 1)
print("f) Próximo elemento da sequência f:", sequencia_f[-1])
