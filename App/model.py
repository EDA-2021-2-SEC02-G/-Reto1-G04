﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    
    catalog = {'obras': None,
               'artistas': None}

    catalog['obras'] = lt.newList()

    catalog['artistas'] = lt.newList('ARRAY_LIST',cmpfunction = None)

    return catalog

# Funciones para agregar informacion al catalogo

def addObra(catalog,obra):

    # Se adiciona la obra a la lista de obras

    lt.addLast(catalog['obras'],obra)

def addArtistas(catalog,artista):

    # Se adiciona la obra a la lista de obras

    lt.addLast(catalog['artistas'],artista)

def ultimosDatos(catalog):

    for x in range(lt.size(catalog['obras']) -2, lt.size(catalog['obras']) +1):

        print(lt.getElement(catalog['obras'],x)['Title'])


def ultimosArtistas(catalog):
    for x in range(lt.size(catalog['artistas']) -2, lt.size(catalog['artistas']) + 1):

        print(lt.getElement(catalog['artistas'],x)['DisplayName'])

   





    







    










# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento