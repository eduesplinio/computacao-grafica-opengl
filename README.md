# Exercícios Práticos - OpenGL
**Computação Gráfica**

**Aluno:** Eduardo Esplinio  
**Matrícula:** 06003445

## Assuntos
- Formas geométricas em 2D
- Primitivas OpenGL
- Transformações geométricas

## Descrição
Este projeto contém implementações de geometrias básicas usando OpenGL em Python. O projeto inclui dois exemplos:
1. Hexágono com vértices específicos
2. Estrela de 6 pontas com diferentes modos de visualização

## Estrutura do Projeto
```
.
├── README.md
├── requirements.txt
├── src/
│   ├── hexagono.py
│   └── estrela.py
```

## Requisitos
- Python 3.x
- PyOpenGL
- NumPy

## Instalação
1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

### Hexágono
```bash
python src/hexagono.py
```
- Pressione ESC para sair

### Estrela de 6 Pontas
```bash
python src/estrela.py
```
- Tecla 1: Modo triângulos (preenchido)
- Tecla 2: Modo linhas
- Tecla 3: Modo pontos
- ESC: Sair

## Detalhes da Implementação

### Hexágono (hexagono.py)
- Implementa um hexágono usando triângulos
- Vértices específicos conforme requisitos
- Desenha pontos nos vértices

### Estrela (estrela.py)
- Implementa uma estrela de 6 pontas usando dois triângulos
- Três modos de visualização diferentes
- Demonstra diferentes primitivas do OpenGL 