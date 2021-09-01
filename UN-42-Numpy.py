{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numpy\n",
    "\n",
    "**Numpy** es una libreria para la ciencia de los datos en Python. Proporciona un objeto **matriz** multidimensional de alto rendimiento y herramientas para trabajar con estas matrices. \n",
    "\n",
    "https://numpy.org/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Matrices\n",
    "\n",
    "Una matriz numpy es una cuadrícula de valores, todos del mismo tipo, y está indexada por una tupla de enteros no negativos. El número de dimensiones es el rango de la matriz; la forma de una matriz es una tupla de números enteros que dan el tamaño de la matriz a lo largo de cada dimensión.\n",
    "\n",
    "Podemos inicializar matrices numpy desde listas de Python anidadas y acceder a elementos usando corchetes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from numpy import random as r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Juan']\n"
     ]
    }
   ],
   "source": [
    "print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size= r.choice([1,2],p=[0.1,0.9]) , p=[0.5,0.2,0.2,0.1], replace=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "a = np.array([34, 25, 7])   # Crear una matriz de rango 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "print(type(a))            # Prints \"<class 'numpy.ndarray'>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3,)\n"
     ]
    }
   ],
   "source": [
    "print(a.shape)            # Prints \"(3,)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34 25 7\n"
     ]
    }
   ],
   "source": [
    "print(a[0], a[1], a[2])   # Prints \"1 2 3\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "a[0] = 5                  # Cambiar un elemento de la matriz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 5 25  7]\n"
     ]
    }
   ],
   "source": [
    "print(a)                  # Prints \"[5, 2, 3]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = np.array([[1,2,3],[4,5,6]])    # Crear una matriz de rango 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n"
     ]
    }
   ],
   "source": [
    "print(b.shape)                     # Prints \"(2, 3)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 4\n"
     ]
    }
   ],
   "source": [
    "print(b[0, 0], b[0, 1], b[1, 0])   # Prints \"1 2 4\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy también proporciona muchas funciones para crear matrices:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0.]\n",
      " [0. 0. 0.]\n",
      " [0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros\n",
    "print(matriz)              # Prints \"[[ 0.  0.]\n",
    "                      #          [ 0.  0.]]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "b = np.ones((1,2))    # Crear un conjunto de todos ellos\n",
    "print(b)              # Prints \"[[ 1.  1.]]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[7 7]\n",
      " [7 7]]\n"
     ]
    }
   ],
   "source": [
    "c = np.full((2,2), 7)  # Crear una matriz constante\n",
    "print(c)               # Prints \"[[ 7.  7.]\n",
    "                       #          [ 7.  7.]]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0.]\n",
      " [0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "d = np.eye(2)         # Crear una matriz de identidad 2x2\n",
    "print(d)              # Prints \"[[ 1.  0.]\n",
    "                      #          [ 0.  1.]]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.00175892 0.12706911]\n",
      " [0.03101381 0.71757546]]\n"
     ]
    }
   ],
   "source": [
    "e = np.random.random((2,2))  # Crear una matriz llena de valores aleatorios\n",
    "print(e)                     # Podría imprimir \"[[ 0.91940167  0.08143941]\n",
    "                             #               [ 0.68744134  0.87236687]]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Puede leer sobre otros métodos de creación de matrices en la documentación de Numpy\n",
    "\n",
    "https://numpy.org/doc/stable/user/basics.creation.html#arrays-creation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Indexación de matrices\n",
    "\n",
    "Numpy ofrece varias formas de indexar en matrices.\n",
    "\n",
    "# Rebanar\n",
    "\n",
    "Similar a las listas de Python, las matrices numpy se pueden cortar. Dado que las matrices pueden ser multidimensionales, debe especificar un segmento para cada dimensión de la matriz:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Crear la siguiente matriz de rango 2 con forma (3, 4)\n",
    "# [[ 1  2  3]\n",
    "#  [ 5  6  7]\n",
    "#  [ 9 10 11 ]]\n",
    "a = np.array([[1,2,3], [5,6,7], [9,10,11]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 3]\n",
      " [6 7]]\n"
     ]
    }
   ],
   "source": [
    "# Usar el rebanado para sacar el subconjunto que consiste en las 2 primeras filas\n",
    "# y las columnas 1 y 2; b es el siguiente conjunto de forma (2, 2):\n",
    "# [[2 3]\n",
    "#  [6 7]]\n",
    "b = a[:2, 1:3]\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 3  2  1]\n",
      " [ 7  6  5]\n",
      " [11 10  9]]\n"
     ]
    }
   ],
   "source": [
    "print(np.fliplr(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "# Una rebanada de una matriz es una vista en los mismos datos, por lo que modificarla\n",
    "# modificará la matriz original.\n",
    "print(a[0, 1])   # Prints \"2\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [],
   "source": [
    "b[0, 0] = 77     # b[0, 0] es la misma pieza de datos que a[0, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "77\n"
     ]
    }
   ],
   "source": [
    "print(a[0, 1])   # Prints \"77\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "También puede mezclar la indexación de enteros con la indexación de sectores. Sin embargo, al hacerlo, se obtendrá una matriz de rango más bajo que la matriz original."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Crear la siguiente matriz de rango 2 con forma (3, 4)\n",
    "# [[ 1  2  3  4]\n",
    "#  [ 5  6  7  8]\n",
    "#  [ 9 10 11 12]]\n",
    "a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dos formas de acceder a los datos de la fila del medio de la matriz.\n",
    "# Mezclando la indexación de enteros con rebanadas se obtiene una matriz de rango inferior,\n",
    "# mientras que usando sólo rebanadas se obtiene un conjunto del mismo rango que el\n",
    "# La matriz original:\n",
    "row_r1 = a[1, :]    # Rank 1 view of the second row of a\n",
    "row_r2 = a[1:2, :]  # Rank 2 view of the second row of a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5 6 7 8] (4,)\n",
      "[[5 6 7 8]] (1, 4)\n"
     ]
    }
   ],
   "source": [
    "print(row_r1, row_r1.shape)  # Prints \"[5 6 7 8] (4,)\"\n",
    "print(row_r2, row_r2.shape)  # Prints \"[[5 6 7 8]] (1, 4)\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  6 10] (3,)\n",
      "[[ 2]\n",
      " [ 6]\n",
      " [10]] (3, 1)\n"
     ]
    }
   ],
   "source": [
    "# Podemos hacer la misma distinción al acceder a las columnas de una matriz:\n",
    "col_r1 = a[:, 1]\n",
    "col_r2 = a[:, 1:2]\n",
    "print(col_r1, col_r1.shape)  # Prints \"[ 2  6 10] (3,)\"\n",
    "print(col_r2, col_r2.shape)  # Prints \"[[ 2]\n",
    "                             #          [ 6]\n",
    "                             #          [10]] (3, 1)\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Indexación de matrices de enteros: \n",
    "\n",
    "Cuando indexa matrices de números utilizando la división, la vista de matriz resultante siempre será una submatriz de la matriz original. Por el contrario, la indexación de matrices de enteros le permite construir matrices arbitrarias utilizando los datos de otra matriz. Aquí hay un ejemplo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "a = np.array([[1,2], [3, 4], [5, 6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 2)\n",
      "[1 4 5]\n"
     ]
    }
   ],
   "source": [
    "# Un ejemplo de indexación de arreglos enteros.\n",
    "# La matriz devuelta tendrá forma (3,2) y\n",
    "print(a.shape)\n",
    "print(a[[0, 1, 2], [0, 1, 0]])  # Prints \"[1 4 5]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 4 5]\n"
     ]
    }
   ],
   "source": [
    "# El ejemplo anterior de indexación de arreglos enteros es equivalente a esto:\n",
    "print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints \"[1 4 5]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 2]\n"
     ]
    }
   ],
   "source": [
    "# Cuando se usa la indexación de arreglos enteros, se puede reutilizar el mismo\n",
    "# elemento de la matriz de la fuente:\n",
    "print(a[[0, 0], [1, 1]])  # Prints \"[2 2]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 2]\n"
     ]
    }
   ],
   "source": [
    "# Equivalente al ejemplo anterior de indexación de arreglos enteros\n",
    "print(np.array([a[0, 1], a[0, 1]]))  # Prints \"[2 2]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Un truco útil con la indexación de matrices enteras es seleccionar o mutar un elemento de cada fila de una matriz:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7  8  9]\n",
      " [10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Crear una nueva matriz de la cual seleccionaremos elementos\n",
    "a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "\n",
    "print(a)  # prints \"array([[ 1,  2,  3],\n",
    "          #                [ 4,  5,  6],\n",
    "          #                [ 7,  8,  9],\n",
    "          #                [10, 11, 12]])\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11 16 17 21]\n"
     ]
    }
   ],
   "source": [
    "# Crear una serie de índices\n",
    "b = np.array([0, 2, 0, 1])\n",
    "\n",
    "# Selecciona un elemento de cada fila de a usando los índices de b\n",
    "print(a[np.arange(4), b])  # Prints \"[ 1  6  7 11]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[21  2  3]\n",
      " [ 4  5 26]\n",
      " [27  8  9]\n",
      " [10 31 12]]\n"
     ]
    }
   ],
   "source": [
    "# Muta un elemento de cada fila de a usando los índices de b\n",
    "a[np.arange(4), b] += 10\n",
    "\n",
    "print(a)  # prints \"array([[11,  2,  3],\n",
    "          #                [ 4,  5, 16],\n",
    "          #                [17,  8,  9],\n",
    "          #                [10, 21, 12]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Indexación de matriz booleana: \n",
    "\n",
    "La indexación de matriz booleana le permite seleccionar elementos arbitrarios de una matriz. Con frecuencia, este tipo de indexación se utiliza para seleccionar los elementos de una matriz que satisfacen alguna condición. Aquí hay un ejemplo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "a = np.array([[1,2], [3, 4], [5, 6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "bool_idx = (a > 2)  # Encuentra los elementos de a que son más grandes que 2; \n",
    "                    # esto devuelve un conjunto numérico de Booleans de la misma \n",
    "                    # forma que a, donde cada ranura de bool_idx dice\n",
    "                    # si ese elemento de a es > 2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[False False]\n",
      " [ True  True]\n",
      " [ True  True]]\n"
     ]
    }
   ],
   "source": [
    "print(bool_idx)      # Prints \"[[False False]\n",
    "                     #          [ True  True]\n",
    "                     #          [ True  True]]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "# Usamos la indexación de arreglos booleanos para construir un arreglo de rango 1\n",
    "# que consiste en los elementos de un correspondiente a los valores Verdaderos\n",
    "# de bool_idx\n",
    "\n",
    "print(a[bool_idx])  # Prints \"[3 4 5 6]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "# Podemos hacer todo lo anterior en una sola declaración concisa:\n",
    "print(a[a > 2])     # Prints \"[3 4 5 6]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Por brevedad, hemos omitido muchos detalles sobre la indexación de matrices numpy; si quieres saber más debes leer la documentación .  \n",
    "\n",
    "https://numpy.org/doc/stable/reference/arrays.indexing.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Tipos de datos\n",
    "\n",
    "Cada matriz numpy es una cuadrícula de elementos del mismo tipo. Numpy proporciona un gran conjunto de tipos de datos numéricos que puede utilizar para construir matrices. Numpy intenta adivinar un tipo de datos cuando crea una matriz, pero las funciones que construyen matrices generalmente también incluyen un argumento opcional para especificar explícitamente el tipo de datos. Aquí hay un ejemplo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int32\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "x = np.array([1, 2])   # Dejar que numpy elija el tipo de datos\n",
    "print(x.dtype)         # Prints \"int64\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "float64\n"
     ]
    }
   ],
   "source": [
    "x = np.array([1.0, 2.0])   # Dejar que numpy elija el tipo de datos\n",
    "print(x.dtype)             # Prints \"float64\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int64\n"
     ]
    }
   ],
   "source": [
    "x = np.array([1, 2], dtype=np.int64)   # Forzar un tipo de datos en particular\n",
    "print(x.dtype)                         # Prints \"int64\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Puede leer todo sobre numerosos tipos de datos en la documentación .\n",
    "\n",
    "https://numpy.org/doc/stable/reference/arrays.dtypes.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Matemáticas de matriz\n",
    "\n",
    "Las funciones matemáticas básicas operan por elementos en matrices y están disponibles como sobrecargas de operador y como funciones en el módulo numpy:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "x = np.array([[1,2],[3,4]], dtype=np.float64)\n",
    "y = np.array([[5,6],[7,8]], dtype=np.float64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 6.  8.]\n",
      " [10. 12.]]\n",
      "[[ 6.  8.]\n",
      " [10. 12.]]\n"
     ]
    }
   ],
   "source": [
    "# Suma de elementos; ambos producen la matriz\n",
    "# [[ 6.0  8.0]\n",
    "#  [10.0 12.0]]\n",
    "print(x + y)\n",
    "print(np.add(x, y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-4. -4.]\n",
      " [-4. -4.]]\n",
      "[[-4. -4.]\n",
      " [-4. -4.]]\n"
     ]
    }
   ],
   "source": [
    "# Diferencia de elementos (resta); ambos producen la matriz\n",
    "# [[-4.0 -4.0]\n",
    "#  [-4.0 -4.0]]\n",
    "print(x - y)\n",
    "print(np.subtract(x, y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5. 12.]\n",
      " [21. 32.]]\n",
      "[[ 5. 12.]\n",
      " [21. 32.]]\n"
     ]
    }
   ],
   "source": [
    "# Producto de elementos; ambos producen la matriz\n",
    "# [[ 5.0 12.0]\n",
    "#  [21.0 32.0]]\n",
    "print(x * y)\n",
    "print(np.multiply(x, y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.2        0.33333333]\n",
      " [0.42857143 0.5       ]]\n",
      "[[0.2        0.33333333]\n",
      " [0.42857143 0.5       ]]\n"
     ]
    }
   ],
   "source": [
    "# División de elemetos; ambos producen la matriz\n",
    "# [[ 0.2         0.33333333]\n",
    "#  [ 0.42857143  0.5       ]]\n",
    "print(x / y)\n",
    "print(np.divide(x, y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.         1.41421356]\n",
      " [1.73205081 2.        ]]\n"
     ]
    }
   ],
   "source": [
    "# Raíz cuadrada de elemtos; produce la matriz\n",
    "# [[ 1.          1.41421356]\n",
    "#  [ 1.73205081  2.        ]]\n",
    "print(np.sqrt(x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Tenga en cuenta que **es una multiplicación por elementos, no una multiplicación de matrices**. En cambio, usamos la dotfunción para calcular productos internos de vectores, para multiplicar un vector por una matriz y para multiplicar matrices. dot está disponible como función en el módulo numpy y como método de instancia de objetos de matriz:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "x = np.array([[1,2],[3,4]])\n",
    "y = np.array([[5,6],[7,8]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "v = np.array([9,10])\n",
    "w = np.array([11, 12])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "219\n",
      "219\n"
     ]
    }
   ],
   "source": [
    "# Producto interno de los vectores; ambos producen 219\n",
    "print(v.dot(w))\n",
    "print(np.dot(v, w))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[29 67]\n",
      "[29 67]\n"
     ]
    }
   ],
   "source": [
    "# Matriz / producto vectorial; ambos producen la matriz de rango 1 [29 67]\n",
    "print(x.dot(v))\n",
    "print(np.dot(x, v))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[19 22]\n",
      " [43 50]]\n",
      "[[19 22]\n",
      " [43 50]]\n"
     ]
    }
   ],
   "source": [
    "# Matriz / producto de la matriz; ambos producen la matriz de rango 2\n",
    "# [[19 22]\n",
    "#  [43 50]]\n",
    "print(x.dot(y))\n",
    "print(np.dot(x, y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy proporciona muchas funciones útiles para realizar cálculos en matrices; uno de los más útiles es sum:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "x = np.array([[1,2],[3,4]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "[4 6]\n",
      "[3 7]\n"
     ]
    }
   ],
   "source": [
    "print(np.sum(x))  # Calcular la suma de todos los elementos; imprime \"10\"\n",
    "print(np.sum(x, axis=0))  # Calcula la suma de cada columna; imprime \"[4 6]\"\n",
    "print(np.sum(x, axis=1))  # Calcula la suma de cada fila; imprime \"[3 7]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Puede encontrar la lista completa de funciones matemáticas proporcionadas por numpy en la documentación.\n",
    "\n",
    "https://numpy.org/doc/stable/reference/routines.math.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Además de calcular funciones matemáticas utilizando matrices, con frecuencia necesitamos remodelar o manipular datos en matrices. El ejemplo más simple de este tipo de operación es la transposición de una matriz; para transponer una matriz, simplemente use el **T** atributo de un objeto de matriz:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]]\n",
      "[[1 3]\n",
      " [2 4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "x = np.array([[1,2], [3,4]])\n",
    "print(x)    # Prints \"[[1 2]\n",
    "            #          [3 4]]\"\n",
    "print(x.T)  # Prints \"[[1 3]\n",
    "            #          [2 4]]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n",
      "[1 2 3]\n"
     ]
    }
   ],
   "source": [
    "# Note que tomar la transposición de una matriz de rango 1 no hace nada:\n",
    "v = np.array([1,2,3])\n",
    "print(v)    # Prints \"[1 2 3]\"\n",
    "print(v.T)  # Prints \"[1 2 3]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy proporciona muchas más funciones para manipular matrices; puedes ver la lista completa en la documentación.\n",
    "https://numpy.org/doc/stable/reference/routines.array-manipulation.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Broadcasting\n",
    "\n",
    "El Broadcasting es un mecanismo poderoso que permite a numpy trabajar con matrices de diferentes formas al realizar operaciones aritméticas. Con frecuencia tenemos una matriz más pequeña y una matriz más grande, y queremos usar la matriz más pequeña varias veces para realizar alguna operación en la matriz más grande.\n",
    "\n",
    "Por ejemplo, suponga que queremos agregar un vector constante a cada fila de una matriz. Podríamos hacerlo así:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Añadiremos el vector v a cada fila de la matriz x,\n",
    "# almacenando el resultado en la matriz y\n",
    "x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "v = np.array([1, 0, 1])\n",
    "y = np.empty_like(x)   # Crear una matriz vacía con la misma forma que x\n",
    "\n",
    "# Agrega el vector v a cada fila de la matriz x con un bucle explícito\n",
    "for i in range(4):\n",
    "    y[i, :] = x[i, :] + v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  2  4]\n",
      " [ 5  5  7]\n",
      " [ 8  8 10]\n",
      " [11 11 13]]\n"
     ]
    }
   ],
   "source": [
    "# Ahora y es lo siguiente\n",
    "# [[ 2  2  4]\n",
    "#  [ 5  5  7]\n",
    "#  [ 8  8 10]\n",
    "#  [11 11 13]]\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Esto funciona; sin embargo, cuando la matriz x es muy grande, calcular un bucle explícito en Python podría ser lento. Tenga en cuenta que agregar el vector va cada fila de la matriz x es equivalente a formar una matriz vv apilando múltiples copias de v verticalmente, luego realizando la suma de elementos de x y vv. Podríamos implementar este enfoque de esta manera:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0 1]\n",
      " [1 0 1]\n",
      " [1 0 1]\n",
      " [1 0 1]]\n",
      "[[ 2  2  4]\n",
      " [ 5  5  7]\n",
      " [ 8  8 10]\n",
      " [11 11 13]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Añadiremos el vector v a cada fila de la matriz x,\n",
    "# almacenando el resultado en la matriz y\n",
    "x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "v = np.array([1, 0, 1])\n",
    "vv = np.tile(v, (4, 1))   # Amontonar 4 copias de V una encima de la otra\n",
    "print(vv)                 # Prints \"[[1 0 1]\n",
    "                          #          [1 0 1]\n",
    "                          #          [1 0 1]\n",
    "                          #          [1 0 1]]\"\n",
    "y = x + vv  # Agrega x y vv elementalmente\n",
    "print(y)  # Prints \"[[ 2  2  4\n",
    "          #          [ 5  5  7]\n",
    "          #          [ 8  8 10]\n",
    "          #          [11 11 13]]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El Broadcasting Numpy nos permite realizar este cálculo sin crear realmente múltiples copias de v. Considere esta versión, usando transmisión:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0]\n",
      " [3 0]]\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# We will add the vector v to each row of the matrix x,\n",
    "# storing the result in the matrix y\n",
    "x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
    "v = np.array([[1, 0],[3, 0]])\n",
    "print(v)\n",
    "print(3 in np.sum(v,axis=0))\n",
    "#y = x + v  # Añada v a cada fila de x utilizando la radiodifusión\n",
    "#print(y)  # Prints \"[[ 2  2  4]\n",
    "          #          [ 5  5  7]\n",
    "          #          [ 8  8 10]\n",
    "          #          [11 11 13]]\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La línea y = x + v funciona aunque x tiene forma (4, 3) y v tiene forma (3,) debido a la transmisión; esta línea funciona como si v realmente tuviera forma (4, 3), donde cada fila era una copia de v, y la suma se realizó por elementos."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# El Broadcasting de dos matrices juntas sigue estas reglas:\n",
    "\n",
    "1. Si las matrices no tienen el mismo rango, anteponga 1 a la forma de la matriz de rango inferior hasta que ambas formas tengan la misma longitud.\n",
    "\n",
    "2. Se dice que las dos matrices son compatibles en una dimensión si tienen el mismo tamaño en la dimensión, o si una de las matrices tiene el tamaño 1 en esa dimensión.\n",
    "\n",
    "3. Los arreglos se pueden transmitir juntos si son compatibles en todas las dimensiones.\n",
    "\n",
    "3. Después de la transmisión, cada matriz se comporta como si tuviese una forma igual al máximo de formas de las dos matrices de entrada.\n",
    "\n",
    "5. En cualquier dimensión donde una matriz tiene un tamaño 1 y la otra matriz tiene un tamaño mayor que 1, la primera matriz se comporta como si se hubiera copiado a lo largo de esa dimensión.\n",
    "\n",
    "Ver\n",
    "\n",
    "https://numpy.org/doc/stable/user/basics.broadcasting.html\n",
    "http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc\n",
    "\n",
    "Las funciones que apoyan el Broadcasting se conocen como funciones universales. Puede encontrar la lista de todas las funciones universales en la documentación.\n",
    "\n",
    "https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs\n",
    "\n",
    "Estas son algunas aplicaciones del Broadcasting:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 4  5]\n",
      " [ 8 10]\n",
      " [12 15]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Calcular el producto exterior de los vectores\n",
    "v = np.array([1,2,3]) # v tiene forma (3,)\n",
    "w = np.array([4,5]) # w tiene forma (2,)\n",
    "# Para calcular un producto exterior, primero reformamos v para que sea una columna\n",
    "# vector de forma (3, 1); podemos entonces emitirlo contra w para rendir\n",
    "# una salida de la forma (3, 2), que es el producto exterior de v y w:\n",
    "# [[ 4 5]\n",
    "# [ 8 10]\n",
    "# [12 15]]\n",
    "print(np.reshape(v, (3, 1)) * w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 4 6]\n",
      " [5 7 9]]\n"
     ]
    }
   ],
   "source": [
    "# Agregar un vector a cada fila de una matriz\n",
    "x = np.array([[1,2,3], [4,5,6]])\n",
    "# x tiene forma (2, 3) y v tiene forma (3,) por lo que transmiten a (2, 3),\n",
    "# dando la siguiente matriz:\n",
    "# [[2 4 6]\n",
    "# [5 7 9]]\n",
    "print(x + v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5  6  7]\n",
      " [ 9 10 11]]\n"
     ]
    }
   ],
   "source": [
    "# Agregar un vector a cada columna de una matriz\n",
    "# La x tiene forma (2, 3) y la w tiene forma (2,).\n",
    "# Si transponemos x entonces tiene forma (3, 2) y puede ser difundida\n",
    "# contra w para obtener el resultado de la forma (3, 2); transponiendo este resultado\n",
    "# produce el resultado final de la forma (2, 3) que es la matriz x con\n",
    "# el vector w añadido a cada columna. Da la siguiente matriz:\n",
    "# [[ 5 6 7]\n",
    "# [ 9 10 11]]\n",
    "print((x.T + w).T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 5  6  7]\n",
      " [ 9 10 11]]\n"
     ]
    }
   ],
   "source": [
    "# Otra solución es remodelar la w para que sea un vector de forma de la columna (2, 1);\n",
    "# podemos entonces emitirlo directamente contra x para producir la misma\n",
    "# salida.\n",
    "print(x + np.reshape(w, (2, 1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  4  6]\n",
      " [ 8 10 12]]\n"
     ]
    }
   ],
   "source": [
    "# Multiplica una matriz por una constante:\n",
    "# x tiene forma (2, 3). Numpy trata los escalares como matrices de forma ();\n",
    "# estos pueden ser emitidos juntos a la forma (2, 3), produciendo el\n",
    "# Siguiendo la matriz:\n",
    "# [[ 2 4 6]\n",
    "# [ 8 10 12]]\n",
    "print(x * 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "El Broadcasting suele hacer que su código sea más conciso y rápido, por lo que debe esforzarse por utilizarlo siempre que sea posible.\n",
    "\n",
    "Documentación Numpy\n",
    "Esta breve descripción general ha abordado muchas de las cosas importantes que necesita saber sobre numpy, pero está lejos de ser completa. Consulte la referencia de numpy para obtener más información sobre numpy.\n",
    "\n",
    "https://numpy.org/doc/stable/reference/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Ejercicio Triqui (tres en linea, juego de la vieja, tres en raya, etc.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def displayInicialTriqui():\n",
    "    for i in range(0,3):\n",
    "        for j in range(0,3):\n",
    "            print(\"|_\",end=\"\")\n",
    "        print(\"|\")\n",
    "\n",
    "def displayTriqui(matriz):\n",
    "    for i in range(0,3):\n",
    "        for j in range(0,3):\n",
    "            if matriz[i,j]==1:\n",
    "                print(\"|X\", end=\"\")\n",
    "            else:\n",
    "                if matriz[i,j]==10:\n",
    "                    print(\"|O\",end=\"\")\n",
    "                else:\n",
    "                    print(\"|_\",end=\"\")\n",
    "        print(\"|\")\n",
    "        \n",
    "def estadoDelJuego(matriz)->int:\n",
    "    #devuelve 1 si gana la X\n",
    "    if 3 in np.sum(matriz, axis=0) or 3 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==3 or np.sum(np.diagonal(np.fliplr(matriz)))==3:\n",
    "        salida = 1\n",
    "    else:\n",
    "        #devuelve 2 si gana la Y\n",
    "        if 30 in np.sum(matriz, axis=0) or 30 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==30 or np.sum(np.diagonal(np.fliplr(matriz)))==30:\n",
    "            salida = 2\n",
    "        else:\n",
    "            #devuelve 3 si no hay ganador\n",
    "            if np.sum(matriz)==45 or np.sum(matriz)==54:\n",
    "                salida = 3\n",
    "            else:\n",
    "                #devuelve 4 si aun hay juego\n",
    "                salida = 4\n",
    "    return salida\n",
    "\n",
    "def jugarTriqui():\n",
    "    #seleccionar aleatoriamente un jugador\n",
    "    turno=False\n",
    "    if np.random.rand()<0.5:\n",
    "        turno=True\n",
    "    #inicializar las variables del juego\n",
    "    displayInicialTriqui()\n",
    "    matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros\n",
    "    estado=4\n",
    "    while(estado==4):\n",
    "        #atrapar el movimiento de los jugadores\n",
    "        tupla= tuple(input(\"Ingrese la casilla a jugar, ej: la casilla superior derecha es 1,3: \"))\n",
    "        #convertir la notacion de los jugadores a los indices de la matriz\n",
    "        x=int(tupla[0])-1\n",
    "        y=int(tupla[2])-1\n",
    "        #validar movimiento dentro del tablero\n",
    "        if x>=0 and x<= 2 and y>=0 and y<=2:\n",
    "            #validar movimiento no antes hecho\n",
    "            if matriz[x,y]==0:\n",
    "                if turno:\n",
    "                    matriz[x,y]=1\n",
    "                else:\n",
    "                    matriz[x,y]=10\n",
    "                #llamar la funcion del estado del juego\n",
    "                estado = estadoDelJuego(matriz)\n",
    "                #llamar el visualizador\n",
    "                displayTriqui(matriz)\n",
    "                #cambiar de turno\n",
    "                turno=not(turno)\n",
    "            else:\n",
    "                print(\"Recuerde jugar en casillas vacias!\")\n",
    "        else:\n",
    "            print(\"Recuerda que el tablero es de 3 por 3!  ej: la casilla inferior izquierda es 3,1\")\n",
    "    # Publicar el resultado del juego\n",
    "    if estado == 1 :\n",
    "        print(\"El jugador X ha ganado!\")\n",
    "    else:\n",
    "        if estado == 2 :\n",
    "            print(\"El jugador O ha ganado!\")\n",
    "        else:\n",
    "            print(\"No hubo ganadores!\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
