

# resultado = []
# for x in palavras:
#      n = x.upper()
#      if n == x and len(x) > 4:
#          resultado.append()
palavras = ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
novo = [x for x in palavras if x == x.upper() and len(x)> 3]
print(novo)
