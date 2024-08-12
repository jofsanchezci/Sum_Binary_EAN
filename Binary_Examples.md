
# Ejemplos de Suma de Números Binarios y Uso de Complemento a Dos

## 1. Ejemplos de Suma de Números Binarios

**Ejemplo 1:**
- **Binario 1**: `1010` (10 en decimal)
- **Binario 2**: `0011` (3 en decimal)
- **Suma**: `1101` (13 en decimal)

**Ejemplo 2:**
- **Binario 1**: `1101` (13 en decimal)
- **Binario 2**: `0110` (6 en decimal)
- **Suma**: `10011` (19 en decimal, ignorando el acarreo adicional)

**Ejemplo 3:**
- **Binario 1**: `1111` (15 en decimal)
- **Binario 2**: `0001` (1 en decimal)
- **Suma**: `10000` (16 en decimal)

## 2. Ejemplos de Resta usando Complemento a Dos

**Ejemplo 1: Restar 5 (`0101`) de 9 (`1001`)**

Paso 1: Encuentra el complemento a dos de 5 (`0101`).
- Complemento a uno de 5: `1010`
- Complemento a dos de 5: `1011`

Paso 2: Suma `1001` (9 en binario) y `1011` (complemento a dos de 5).
```
   1001  (9 en decimal)
+  1011  (complemento a dos de 5)
--------
  10100  (ignora el acarreo extra)
```
Resultado: `0100` (4 en decimal)

**Ejemplo 2: Restar 7 (`0111`) de 10 (`1010`)**

Paso 1: Encuentra el complemento a dos de 7 (`0111`).
- Complemento a uno de 7: `1000`
- Complemento a dos de 7: `1001`

Paso 2: Suma `1010` (10 en binario) y `1001` (complemento a dos de 7).
```
   1010  (10 en decimal)
+  1001  (complemento a dos de 7)
--------
  10011  (ignora el acarreo extra)
```
Resultado: `0011` (3 en decimal)

**Ejemplo 3: Restar 3 (`0011`) de 8 (`1000`)**

Paso 1: Encuentra el complemento a dos de 3 (`0011`).
- Complemento a uno de 3: `1100`
- Complemento a dos de 3: `1101`

Paso 2: Suma `1000` (8 en binario) y `1101` (complemento a dos de 3).
```
   1000  (8 en decimal)
+  1101  (complemento a dos de 3)
--------
  10101  (ignora el acarreo extra)
```
Resultado: `0101` (5 en decimal)
