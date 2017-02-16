import turtle

def ajuda(funcao):
	'''Exibe a ajuda de uma função dada'''
	help(funcao)

def pra_frente(distancia):
	'''Move a tartarugra pra frente pela distância dada'''
	turtle.forward(distancia)

def pra_tras(distancia):
	'''Mover a tartaruga pra trás pela distância dada'''
	turtle.backward(distancia)

def posicao():
	'''Exibe a posição atual da tartaruga'''
	return turtle.position()

def direita(angulo):
	'''Gira a tartaruga para a direita pelo angulo dado'''
	turtle.right(angulo)

def esquerda(angulo):
	'''Gira a tartaruga para a direita pelo angulo dado'''
	turtle.left(angulo)

def andar_horizontal(distancia):
	'''Move a tartaruga na horizontal pela distância dada'''
	turtle.setx(distancia)
	
def andar_vertical(y):
	'''Move a tartaruga na vertical pela distância dada'''
	turtle.sety(y)
	
def andar_ate(x, y):
	'''Move a tartaruga até a posição (coordenadas x e y) passada'''
	turtle.setpos(x, y)

def mudar_direcao(angulo):
	'''Muda a direção da tartaruga pelo ângulo dado'''
	turtle.setheading(angulo)

def direcao():
	'''Exibe a direção atual da tartaruga (ângulo)'''
	return turtle.heading()
	
def voltar_casa():
	'''Retorna a tartaruga para a posição original (coordenadas 0,0)'''
	turtle.home()
