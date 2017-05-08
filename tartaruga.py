import turtle

def ajuda(funcao):
	'''Exibe a ajuda de uma função dada'''
	help(funcao)
	
def abaixar_caneta():
	'''Os próximos comandos de movimento da tartaruga deixarão rastro'''
	turtle.pendown()

def andar_ate(x, y):
	'''Move a tartaruga até a posição (coordenadas x e y) passada'''
	turtle.setpos(x, y)

def andar_horizontal(distancia):
	'''Move a tartaruga na horizontal pela distância dada'''
	turtle.setx(distancia)
	
def andar_vertical(y):
	'''Move a tartaruga na vertical pela distância dada'''
	turtle.sety(y)

def carimbar():
	'''Desenha uma cópia da tartaruga (como um carimbo)'''
	turtle.stamp()

def cor_caneta(cor):
	'''Muda a cor da caneta (cores possíveis: azul, amarelo, branco, 
		verde, vermelho, preto e rosa).'''		
	turtle.pencolor(converte_cor(cor))
	
def cor_preenchimento(cor):
	'''Mudar a cor de preenchimento (cores possíveis: azul, amarelo, branco, 
		verde, vermelho, preto e rosa).'''
	turtle.fillcolor(converte_cor(cor))

def direcao():
	'''Exibe a direção atual da tartaruga (ângulo)'''
	return turtle.heading()

def direita(angulo):
	'''Gira a tartaruga para a direita pelo ângulo dado'''
	turtle.right(angulo)
	
def escrever(texto):
	'''Escreve na tela o texto passado'''
	turtle.write(texto)

def esquerda(angulo):
	'''Gira a tartaruga para a esquerda pelo ângulo dado'''
	turtle.left(angulo)

def exibir():
	turtle.shape("turtle")
	turtle.showturtle()

def iniciar_preenchimento():
	'''Os desenhos seguintes passam a ser preenchidos'''
	turtle.begin_fill()
	
def levantar_caneta():
	'''Os próximos comandos de movimento da tartaruga não deixarão mais rastro'''
	turtle.penup()

def mudar_direcao(angulo):
	'''Muda a direção da tartaruga pelo ângulo dado'''
	turtle.setheading(angulo)

def parar_preenchimento():
	'''Os desenhos seguintes deixam de ser preenchidos'''
	turtle.end_fill()

def ponto():
	'''Desenha um ponto na tela'''
	turtle.dot()

def posicao():
	'''Exibe a posição atual da tartaruga'''
	return turtle.position()

def pra_frente(distancia):
	'''Move a tartaruga pra frente pela distância dada'''
	turtle.forward(distancia)

def pra_tras(distancia):
	'''Mover a tartaruga pra trás pela distância dada'''
	turtle.backward(distancia)

def reiniciar():
	'''Apaga os desenhos e retorna a tartaruga para a posição inicial'''
	turtle.reset()
	
def terminar():
	'''Termina o desenho (libera a janela de exibição)'''
	turtle.done()
	
def velocidade(valor):
	'''Altera a velocidade do desenho (valores de 1 a 10)'''
	turtle.speed(valor)

def voltar_casa():
	'''Retorna a tartaruga para a posição original (coordenadas 0,0)'''
	turtle.home()


# Funções auxiliares

def dic_cores():
	return {"azul":"blue", "amarelo":"yellow", "branco":"white", 
		"verde":"green", "vermelho":"red", "preto":"black", "rosa":"pink"}

def converte_cor(cor):
	cores = dic_cores()
	if cor in cores:
		cor = cores[cor]
	return cor
