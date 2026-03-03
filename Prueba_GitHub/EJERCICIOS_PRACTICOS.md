# Ejercicios Prácticos: Aprendiendo Git y GitHub 💻

Sigue estos ejercicios en orden. Cada uno construye sobre el anterior.

---

## EJERCICIO 1: Verificar tu Git inicial

**Objetivo:** Entender el estado actual de tu repositorio

```bash
# 1. Ve a tu carpeta padre
cd /home/catec/Pruebas_Codigo_Sprint1

# 2. Verifica que Git está inicializado
git status

# 3. Deberías ver algo como:
# "On branch master" o "On branch main"
# Esto significa que Git ya está inicializado aquí

# 4. Mira tu configuración
git config --global user.name
git config --global user.email

# Si ves tu nombre y email, ¡excelente!
# Si no ves nada, sigue los pasos de la sección "Configuración Inicial" del tutorial
```

**✓ Completado cuando:** Ves "On branch master/main" sin estado de error

---

## EJERCICIO 2: Configurar tu información personal

**Si ya has hecho esto, sáltalo. Si no:**

```bash
# Reemplaza con tu información real
git config --global user.name "Tu Nombre"
git config --global user.email "tu.correo@ejemplo.com"

# Verifica que se guardó
git config --global user.name
git config --global user.email
```

**✓ Completado cuando:** Ves tu nombre y email al ejecutar los comandos de verificación

---

## EJERCICIO 3: Hacer el primer commit

```bash
# 1. Ve a la carpeta padre (si no estás ya allí)
cd /home/catec/Pruebas_Codigo_Sprint1

# 2. Ve qué cambios sin guardar hay
git status

# 3. Agrega todos los cambios
git add .

# 4. Verifica que todo está agregado (deberían verse en verde)
git status

# 5. Haz el primer commit
git commit -m "Inicial: Agregar proyecto Prueba_GitHub"

# 6. Mira el historial
git log

# Deberías ver tu commit listado con tu nombre
```

**✓ Completado cuando:** Ves tu commit en `git log` con tu nombre y el mensaje

---

## EJERCICIO 4: Crear cuenta en GitHub (si no la tienes)

**Si ya tienes cuenta en GitHub, sáltalo:**

1. Ve a https://github.com
2. Haz clic en "Sign up"
3. Completa:
   - Correo electrónico
   - Contraseña
   - Nombre de usuario (recuérdalo, lo necesitarás)
4. Verifica tu correo
5. Listo, ya tienes cuenta

**✓ Completado cuando:** Puedas iniciar sesión en GitHub

---

## EJERCICIO 5: Crear tu primer repositorio en GitHub

```
⚠️ IMPORTANTE: Reemplaza TU_USUARIO con tu nombre de usuario de GitHub en 
TODOS los comandos y URLs siguientes
```

**En GitHub:**

1. Inicia sesión
2. Haz clic en tu avatar (esquina superior derecha)
3. Selecciona "Your repositories"
4. Haz clic en el botón verde "New"
5. Completa:
   - **Repository name:** `Prueba_GitHub`
   - **Description:** `Proyecto de prueba de Python con Chacha20`
   - **Public:** Elige (si es tu primer repo, elige "Public" para aprender)
   - **Initialize this repository:** NO marques nada
6. Haz clic en "Create repository"

**En tu terminal:**

```bash
# 1. Ve a tu carpeta padre si no estás allí
cd /home/catec/Pruebas_Codigo_Sprint1

# 2. Conecta tu repositorio local con GitHub
git remote add origin https://github.com/TU_USUARIO/Prueba_GitHub.git

# 3. Verifica que se conectó
git remote -v

# Deberías ver dos líneas con "origin" y tu URL
```

**✓ Completado cuando:** `git remote -v` muestra dos líneas con tu URL

---

## EJERCICIO 6: Cambiar nombre de rama y subir código

```bash
# 1. Cambia el nombre de "master" a "main" (estándar moderno)
git branch -M main

# 2. Sube tu código a GitHub por primera vez
git push -u origin main

# 3. Es posible que Git pida autenticación
# Opciones:
#   - Si pide usuario/contraseña: usa tu usuario y un Personal Access Token
#   - Instrucciones: https://docs.github.com/en/authentication
```

**Importante - Si tienes error de autenticación:**

GitHub ya no acepta contraseñas directas. Necesitas un "Personal Access Token":

1. Ve a https://github.com/settings/tokens
2. Haz clic en "Generate new token (classic)"
3. En "Select scopes", marca:
   - ☑ repo (acceso completo a repositorios)
4. Haz clic en "Generate token"
5. **Copia el token (aparece una sola vez)**
6. En la terminal, cuando pida contraseña, pega el token

**✓ Completado cuando:** Ves en GitHub tu código subido en https://github.com/TU_USUARIO/Prueba_GitHub

---

## EJERCICIO 7: Ver tu código en GitHub

```bash
# 1. Abre en tu navegador:
# https://github.com/TU_USUARIO/Prueba_GitHub

# Deberías ver:
# - Tu repositorio
# - El botón "main" (tu rama)
# - Todos tus archivos (chacha20.cpp, README.md, etc.)
# - El commit que hiciste
```

**✓ Completado cuando:** Ves todos tus archivos en GitHub

---

## EJERCICIO 8: Editar archivo local y subir cambios

```bash
# 1. Edita el archivo README.md
# Abre: /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub/README.md
# Reemplaza "# Prueba_GitHub" con esto:

cat > /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub/README.md << 'EOF'
# Prueba_GitHub

Proyecto de prueba para aprender Git y GitHub.

## Descripción
Este proyecto contiene implementaciones del algoritmo Chacha20 de encriptación.

## Archivos
- `chacha20.cpp` - Implementación en C++
- `chacha20.h` - Headers para C++
- `chacha20_timing.cpp` - Test de timing en C++
- `chacha20_timing.py` - Test de timing en Python

## Cómo ejecutar
```
g++ chacha20_timing.cpp -o chacha20_timing
./chacha20_timing
```

## Autor
Tu Nombre

## Fecha de Creación
Marzo 2026
EOF

# 2. Verifica que cambió
git status

# 3. Ver exactamente qué cambió
git diff

# 4. Agrega el cambio
git add README.md

# 5. Haz un commit con un mensaje claro
git commit -m "Docs: Actualizar README con información del proyecto"

# 6. Sube el cambio a GitHub
git push

# Verifica en GitHub.com que el cambio está allí
```

**✓ Completado cuando:** Ves el README actualizado en https://github.com/TU_USUARIO/Prueba_GitHub

---

## EJERCICIO 9: Hacer 3 commits pequeños

El objetivo es que entiendas que los commits deben ser pequeños y lógicos.

```bash
# 1. Crea un nuevo archivo
cat > /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub/config.txt << 'EOF'
# Configuración del proyecto
KEY_SIZE = 256
BLOCK_SIZE = 64
EOF

# 2. Haz un commit
git add config.txt
git commit -m "Config: Agregar archivo de configuración"

# 3. Edita un archivo existente (por ejemplo, chacha20.h)
# Puedes añadir un comentario al principio:
sed -i '1i // Last updated: Marzo 2026\n' /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub/chacha20.h

# 4. Haz otro commit
git add chacha20.h
git commit -m "Chore: Agregar timestamp en header"

# 5. Sube todos los cambios
git push

# 6. Verifica el historial
git log --oneline

# Deberías ver los últimos 5 commits aproximadamente
```

**✓ Completado cuando:** `git log --oneline` muestra 3+ commits después del inicial

---

## EJERCICIO 10: Trabajar con ramas

Las ramas son fundamentales para no romper el código principal.

```bash
# 1. Verifica en qué rama estás
git status

# 2. Crea una nueva rama para una feature
git checkout -b feature/mejorar-readme

# 3. Verifica que cambiaste de rama
git branch

# El asterisco (*) muestra dónde estás

# 4. Edita algo en esta rama
cat > /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub/CHANGELOG.md << 'EOF'
# Changelog

## [0.1.0] - 2026-03-03
### Added
- Configuración inicial del proyecto
- Documentación básica

### Changed
- Actualización del README
EOF

# 5. Haz un commit en esta rama
git add CHANGELOG.md
git commit -m "Docs: Agregar archivo CHANGELOG"

# 6. Sube esta rama a GitHub
git push -u origin feature/mejorar-readme

# 7. Cambia de vuelta a main
git checkout main

# 8. Verifica que volviste a main
git status

# Nota: El CHANGELOG.md NO está aquí, está solo en la rama feature

# 9. Mira ambas ramas
git branch -a
```

**✓ Completado cuando:** Ves dos ramas en GitHub: "main" y "feature/mejorar-readme"

---

## EJERCICIO 11: Crear un .gitignore

El `.gitignore` le dice a Git qué archivos ignorar (no subir).

```bash
# 1. Ve a tu carpeta
cd /home/catec/Pruebas_Codigo_Sprint1

# 2. Crea un archivo .gitignore
cat > /home/catec/Pruebas_Codigo_Sprint1/.gitignore << 'EOF'
# Archivos de compilación C++
*.o
*.obj
*.out
*.exe
*.so
*.dll
*.dylib

# Archivos Python
__pycache__/
*.py[cod]
*.egg-info/
.Python
venv/
env/

# Sistema operativo
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Build
build/
dist/
.build/
EOF

# 3. Agrega el .gitignore
git add .gitignore

# 4. Haz un commit
git commit -m "Config: Agregar .gitignore"

# 5. Sube los cambios
git push
```

**✓ Completado cuando:** Ves `.gitignore` en tu repositorio de GitHub

---

## EJERCICIO 12: Ver el historial completo

```bash
# 1. Ver solo el último commit
git log -1

# 2. Ver últimos 5 commits en una línea
git log -5 --oneline

# 3. Ver todos los commits
git log

# 4. Ver todos los commits con graph (visual)
git log --all --oneline --graph

# Deberías ver algo como:
# * 1a2b3c4 Config: Agregar .gitignore
# * 5d6e7f8 Docs: Agregar archivo CHANGELOG
# | * 9g0h1i2 Docs: Actualizar README
# |/
# * 3j4k5l6 Chore: Agregar timestamp en header
# * 7m8n9o0 Config: Agregar archivo de configuración
# * pq1r2s3 Docs: Actualizar README con información del proyecto
# * tu4v5w6 Inicial: Agregar proyecto Prueba_GitHub
```

**✓ Completado cuando:** Ves tu historial de commits

---

## EJERCICIO 13: Sincronizar cambios

```bash
# 1. Baja los cambios más recientes de GitHub
git pull

# (En este caso no hay cambios de otros, pero es buena práctica)

# 2. Verifica que estás actualizado
git status

# Deberías ver: "Your branch is up to date with 'origin/main'"
```

**✓ Completado cuando:** No ves mensajes de "diverged" o cambios sin sincronizar

---

## EJERCICIO 14: Merge de ramas

Cuando terminas una feature, la mezclas (merge) con main.

```bash
# 1. Estamos en main? Verifica
git status

# Si no, cambia a main
git checkout main

# 2. Mezcla la rama feature
git merge feature/mejorar-readme

# 3. Verifica que el merge fue exitoso
git log --oneline

# Deberías ver los commits de ambas ramas

# 4. Sube los cambios
git push

# 5. (Opcional) Borra la rama feature si ya no la necesitas
git branch -d feature/mejorar-readme
git push origin --delete feature/mejorar-readme
```

**✓ Completado cuando:** El merge se completa sin conflictos y ves los cambios en GitHub

---

## EJERCICIO 15: Crear un .gitignore apropiado para tu carpeta padre

Ahora que tienes múltiples proyectos, queremos ignorar cosas innecesarias:

```bash
# 1. Ve a la carpeta padre
cd /home/catec/Pruebas_Codigo_Sprint1

# 2. Ve qué state tiene git
git status

# 3. Actualiza el .gitignore (si lo creaste)
# O créalo si aún no lo hiciste

cat > /home/catec/Pruebas_Codigo_Sprint1/.gitignore << 'EOF'
# Sistema operativo
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDEs y editors
.vscode/
.idea/
*.swp
*.swo
*~
.sublime-project
.sublime-workspace

# Python
__pycache__/
*.py[cod]
*.egg-info/
.Python
venv/
env/
.venv
ENV/

# C++
*.o
*.obj
*.out
*.exe
*.so
*.dll
*.dylib
*.a
.o
build/

# Jupyter
.ipynb_checkpoints/

# Node (si aplica)
node_modules/
npm-debug.log

# Archivos de sistema
.env
.env.local
.env.*.local
EOF

# 4. Agrega
git add .gitignore

# 5. Commit
git commit -m "Config: Actualizar .gitignore global"

# 6. Push
git push
```

**✓ Completado cuando:** El .gitignore se actualiza en GitHub

---

## EJERCICIO BONUS: Clonar tu repositorio

Practica clonar tu repo (como si fuera otra persona):

```bash
# 1. Crea una carpeta temporal
mkdir /tmp/test_clone

# 2. Ve allí
cd /tmp/test_clone

# 3. Clona tu repositorio
git clone https://github.com/TU_USUARIO/Prueba_GitHub.git

# 4. Ve al directorio clonado
cd Prueba_GitHub

# 5. Verifica que todo está
git log --oneline
ls -la

# 6. Limpia la carpeta temporal (opcional)
# cd /tmp && rm -rf test_clone
```

**✓ Completado cuando:** Ves todos tus archivos y commits en la carpeta clonada

---

## 🎉 ¡FELICIDADES!

Has completado los ejercicios básicos de Git y GitHub. Ahora sabes:

- ✅ Configurar Git
- ✅ Hacer commits
- ✅ Subir código a GitHub
- ✅ Trabajar con ramas
- ✅ Ver el historial
- ✅ Usar .gitignore

### Próximos Pasos

1. **Practica diario:** Haz pequeños cambios y commits
2. **Aprende Pull Requests:** Útil para colaborar
3. **Explora otros repos:** Lee el código de proyectos que te interesen
4. **Colabora:** Invita a alguien a tu proyecto

### Comandos que deberías entender ahora:

```bash
git init              # Crear repositorio nuevo
git add .            # Preparar cambios
git commit -m "msg"  # Guardar cambios
git push             # Subir a GitHub
git pull             # Descargar de GitHub
git checkout -b rama # Crear rama
git merge rama       # Mezclar rama
git log              # Ver historial
```

¡Sigue practicando! 🚀
