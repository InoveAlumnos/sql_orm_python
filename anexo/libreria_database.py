###################################################

# ESTE SCRIPT SE CREO PARA GENEARAR LA BASE DE DATOS
# DE "libreria.db" PARA SU USO EN LOS EJERCICIOS

###################################################

import sqlite3


conn = sqlite3.connect('libreria.db')
c = conn.cursor()
c.execute("""
            DROP TABLE IF EXISTS autor;
        """)
c.execute("""
            CREATE TABLE autor(
            id               INTEGER  NOT NULL PRIMARY KEY,
            name             TEXT NOT NULL
            );
        """)

c.execute("""
            DROP TABLE IF EXISTS libro;
        """)
c.execute("""
            CREATE TABLE libro(
            id               INTEGER  NOT NULL PRIMARY KEY,
            titulo           TEXT NOT NULL,
            cantidad_paginas INTEGER  NOT NULL,
            [autor_id] INTEGER NOT NULL REFERENCES autor(id)
            );
        """)

conn.commit()

c.execute("INSERT INTO autor(id, name) VALUES (1, 'Gabriel Garcia Marquez');")
c.execute("INSERT INTO autor(id, name) VALUES (2, 'Jorge Luis Borges');")
c.execute("INSERT INTO autor(id, name) VALUES (3, 'Jose Saramago');")
c.execute("INSERT INTO autor(id, name) VALUES (4, 'Ernesto Sabato');")
c.execute("INSERT INTO autor(id, name) VALUES (5, 'Manuel Puig');")


c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (1,'Cien anios de soledad',471,1);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (2,'El Aleph',146,2);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (3,'El libro de Arena',181,2);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (4,'Las intermitencias de la muerte',214,3);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (5,'Relato de un naufrago',141,1);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (6,'El amor en los tiempos del colera',464,1);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (7,'La caverna',454,3);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (8,'El tunel',184,4);")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor_id) VALUES (9,'Boquitas pintadas',218,5);")

conn.commit()
conn.close()