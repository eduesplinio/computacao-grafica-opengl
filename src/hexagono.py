import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import numpy as np

def create_hex_vertices():
    '''
    Vertices para desenhar Hexagono com as coordenadas especificadas
    '''
    lista_vertices = [
        [ 1.0,  4.0,  0.0],  # V1
        [ 4.0,  2.0,  0.0],  # V2
        [ 4.0, -1.0,  0.0],  # V3
        [ 1.0, -4.0,  0.0],  # V4
        [-4.0, -2.0,  0.0],  # V5
        [-3.0,  3.0,  0.0]   # V6
    ]
    return np.array(lista_vertices, dtype=np.float32)

def display():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    
    vertices = create_hex_vertices()
    
    # Desenha o hexágono usando triângulos
    gl.glColor3f(0.7, 0.7, 0.7)  # Cor cinza
    gl.glBegin(gl.GL_TRIANGLES)
    
    # T1: V5, V6, V1
    gl.glVertex3fv(vertices[4])  # V5 (-4, -2)
    gl.glVertex3fv(vertices[5])  # V6 (-3, 3)
    gl.glVertex3fv(vertices[0])  # V1 (1, 4)
    
    # T2: V6, V1, V2
    gl.glVertex3fv(vertices[5])  # V6 (-3, 3)
    gl.glVertex3fv(vertices[0])  # V1 (1, 4)
    gl.glVertex3fv(vertices[1])  # V2 (4, 2)
    
    # T3: V6, V2, V3
    gl.glVertex3fv(vertices[5])  # V6 (-3, 3)
    gl.glVertex3fv(vertices[1])  # V2 (4, 2)
    gl.glVertex3fv(vertices[2])  # V3 (4, -1)
    
    # T4: V6, V3, V4
    gl.glVertex3fv(vertices[5])  # V6 (-3, 3)
    gl.glVertex3fv(vertices[2])  # V3 (4, -1)
    gl.glVertex3fv(vertices[3])  # V4 (1, -4)
    
    # T5: V6, V4, V5
    gl.glVertex3fv(vertices[5])  # V6 (-3, 3)
    gl.glVertex3fv(vertices[3])  # V4 (1, -4)
    gl.glVertex3fv(vertices[4])  # V5 (-4, -2)
    
    gl.glEnd()
    
    # Desenha os pontos nos vértices
    gl.glPointSize(5.0)
    gl.glColor3f(0.0, 0.0, 0.0)  # Cor preta
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
    if key == b'\x1b':  # ESC
        sys.exit()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(800, 800)
    glut.glutCreateWindow(b"Hexagono")
    
    # Habilita teste de profundidade
    gl.glEnable(gl.GL_DEPTH_TEST)
    
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutKeyboardFunc(keyboard)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()