
# Plugin Factoides para Errbot
**Factoides** es un plugin para [Errbot](http://errbot.io), un bot de chat basado en Python.
Permite a los usuarios crear "factoides", que el bot puede usar a demanda. 
Es la versión en español del plugin original hecho por [alimac](https://github.com/alimac/err-factoid).

## Instalación

Para instalar el plugin, abrir una ventana de chat privada con el bot e ingresar:

```
!repos install https://github.com/pgiu/err-factoid.git
```

## Configuración

No hay nada que configurar, por ahora.

A pesar de que no es requerido, recomiendo que descomenten las siguientes líneas del archivo de configuración `config.py`:

```
BOT_ALT_PREFIXES = ('Err',)
BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')
BOT_ALT_PREFIX_CASEINSENSITIVE = True
```

## Interacción

El plugin permite que el bot guarde y muestre "factoides". Los factoides tienen entre una y tres palabras y siguen la fórmula `algo es descripción`.

Ejemplos:

```
!agua es mojada
!agua caliente es mojada
!agua muy caliente es mojada y quema
```

### Agregar un nuevo factoide

```
!agua es mojada
```

O, si están habilitados los prefijos alternativos,

```
Err, agua es mojada
```

El robot debería responder:

```
Perfecto, agua es mojada
```

### Ask about a factoid

Para que el bot te cuente lo que le enseñaste, escribe:

```
agua?
que es agua?
```

El bot debería responder:

```
agua es mojada
```

### Remover un factoide

Para borrar un factoide, escribir lo siguiente

```
!olvidar agua
```

O, si están hablitados los prefijos alternativos,

```
Err, olvidar agua
Err, forget about agua
```

### Lest all factoids

Para listar todos los factoides, usar:

```
!listar factoides
```

El bot debería responder por una lista de las cosas que conoce.

```
Mi nombre es Err y conozco sobre:
agua, agua caliente, agua muy caliente
```
