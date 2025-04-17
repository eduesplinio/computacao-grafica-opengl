import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import numpy as np

def create_star_vertices():
    '''
    Vertices para desenhar uma estrela de 6 pontas
    A estrela é formada por dois triângulos sobrepostos
    '''
    lista_vertices = [
        # Primeiro triângulo (apontando para cima)
        [ 0.0,  4.0,  0.0],  # V1 (ponta superior)
        [-3.5, -2.0,  0.0],  # V2 (base esquerda)
        [ 3.5, -2.0,  0.0],  # V3 (base direita)
        
        # Segundo triângulo (apontando para baixo)
        [ 0.0, -4.0,  0.0],  # V4 (ponta inferior)
        [ 3.5,  2.0,  0.0],  # V5 (base direita)
        [-3.5,  2.0,  0.0],  # V6 (base esquerda)
    ]
    return np.array(lista_vertices, dtype=np.float32)

def display():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    
    vertices = create_star_vertices()
    
    # Modo de desenho atual (pode ser alterado com as teclas 1, 2, 3)
    global drawing_mode
    
    if drawing_mode == gl.GL_TRIANGLES:
        # Desenha a estrela usando triângulos
        gl.glColor3f(0.7, 0.7, 0.7)  # Cor cinza
        gl.glBegin(gl.GL_TRIANGLES)
        for vertex in vertices:
            gl.glVertex3fv(vertex)
        gl.glEnd()
    
    elif drawing_mode == gl.GL_LINES:
        # Desenha as linhas da estrela
        gl.glColor3f(0.0, 0.0, 1.0)  # Cor azul
        gl.glBegin(gl.GL_LINES)
        # Linhas do primeiro triângulo
        gl.glVertex3fv(vertices[0])  # V1
        gl.glVertex3fv(vertices[1])  # V2
        gl.glVertex3fv(vertices[1])  # V2
        gl.glVertex3fv(vertices[2])  # V3
        gl.glVertex3fv(vertices[2])  # V3
        gl.glVertex3fv(vertices[0])  # V1
        
        # Linhas do segundo triângulo
        gl.glVertex3fv(vertices[3])  # V4
        gl.glVertex3fv(vertices[4])  # V5
        gl.glVertex3fv(vertices[4])  # V5
        gl.glVertex3fv(vertices[5])  # V6
        gl.glVertex3fv(vertices[5])  # V6
        gl.glVertex3fv(vertices[3])  # V4
        gl.glEnd()
    
    elif drawing_mode == gl.GL_POINTS:
        # Desenha apenas os pontos dos vértices
        gl.glPointSize(10.0)
        gl.glColor3f(1.0, 0.0, 0.0)  # Cor vermelha
        gl.glBegin(gl.GL_POINTS)
        for vertex in vertices:
            gl.glVertex3fv(vertex)
        gl.glEnd()
    
    glut.glutSwapBuffers()

def reshape(width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-5, 5, -5, 5, -1, 1)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

def keyboard(key, x, y):
    global drawing_mode
    
    if key == b'\x1b':  # ESC
        sys.exit()
    elif key == b'1':
        drawing_mode = gl.GL_TRIANGLES
    elif key == b'2':
        drawing_mode = gl.GL_LINES
    elif key == b'3':
        drawing_mode = gl.GL_POINTS
    
    glut.glutPostRedisplay()

def main():
    global drawing_mode
    drawing_mode = gl.GL_TRIANGLES  # Modo inicial
    
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(800, 800)
    glut.glutCreateWindow(b"Estrela de 6 Pontas")
    
    # Habilita teste de profundidade
    gl.glEnable(gl.GL_DEPTH_TEST)
    
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutKeyboardFunc(keyboard)
    glut.glutMainLoop()

if __name__ == "__main__":
    main() 