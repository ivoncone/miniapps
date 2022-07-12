roles = ['analista', 'analista', 'desarrollador', 'disenador',
'programador', 'programador', 'ejecutivo', 'ejecutivo', 'desarrollador']

# option 1
def contar(datos):
	result = {}
	for dato in datos:
		if dato not in result:
			result[dato] = 0
		result[dato] += 1
	return result

cuenta = contar(roles)

dic_inverso = {}
for dato, repeticiones in cuenta.items():
	if repeticiones not in dic_inverso:
		dic_inverso[repeticiones] = []
	dic_inverso[repeticiones].append(dato)
max_rep = max(dic_inverso)
roles_repetidos = (dic_inverso[max_rep])
print(roles_repetidos)

#option 2
def eliminar_duplicados(roles):
	n_lista = []
	for elemento in roles:
		if not elemento in n_lista:
			n_lista.append(elemento)
	return n_lista
sin_duplicados = eliminar_duplicados(roles)
print(sin_duplicados[:4])