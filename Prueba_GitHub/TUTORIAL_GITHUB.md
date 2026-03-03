# Tutorial Completo: Aprendiendo GitHub 📚

## 📋 Tabla de Contenidos
1. [Conceptos Básicos](#conceptos-básicos)
2. [Configuración Inicial](#configuración-inicial)
3. [Trabajar Localmente](#trabajar-localmente)
4. [Conectar con GitHub](#conectar-con-github)
5. [Operaciones Esenciales](#operaciones-esenciales)
6. [Flujo de Trabajo Recomendado](#flujo-de-trabajo-recomendado)
7. [Consejos y Buenas Prácticas](#consejos-y-buenas-prácticas)

---

## Conceptos Básicos

### ¿Qué es Git?
Git es un sistema de control de versiones que te permite:
- **Guardar cambios** en tu código (versiones)
- **Volver atrás** si algo sale mal
- **Colaborar** con otros desarrolladores
- **Rastrear** quién hizo qué cambios y cuándo

### ¿Qué es GitHub?
GitHub es una plataforma en línea donde puedes:
- **Almacenar** tus repositorios Git en la nube
- **Compartir** código con otros
- **Colaborar** en equipo
- **Documentar** tus proyectos

### Conceptos Clave

| Término | Descripción |
|---------|-------------|
| **Repository (Repo)** | Carpeta que contiene tu proyecto y el historial de cambios |
| **Commit** | Foto de tu código en un momento específico (con un mensaje) |
| **Branch** | Rama del proyecto donde trabajas sin afectar el código principal |
| **Remote** | Ubicación remota (GitHub) donde está tu repositorio |
| **Push** | Enviar tus cambios locales a GitHub |
| **Pull** | Descargar cambios de GitHub a tu máquina |
| **Merge** | Combinar cambios de diferentes ramas |

---

## Configuración Inicial

### Paso 1: Verificar que Git esté instalado

Abre la terminal y escribe:
```bash
git --version
```

Debes ver algo como: `git version 2.34.1`

Si no lo ves, instala Git desde https://git-scm.com/

### Paso 2: Configurar tu nombre y email

Esta información aparecerá en todos tus commits. Es importante para que GitHub sepa quién eres.

```bash
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu.email@ejemplo.com"
```

Verifica que se guardó correctamente:
```bash
git config --global user.name
git config --global user.email
```

**Nota:** El `--global` significa que estas configuraciones se aplicarán a TODOS tus proyectos. Si quieres configurar solo para un proyecto específico, omite `--global`.

### Paso 3: Crear una cuenta en GitHub

1. Ve a https://github.com
2. Haz clic en "Sign up" (Registrarse)
3. Completa los datos (nombre de usuario, correo, contraseña)
4. Verifica tu correo electrónico

---

## Trabajar Localmente

### Paso 1: Entender tu situación actual

Ya has hecho `git init` en tu carpeta padre. Esto creó un repositorio en esa ubicación.

Para verificar el estado:
```bash
cd /home/catec/Pruebas_Codigo_Sprint1
git status
```

### Paso 2: Verificar la historia de commits

```bash
git log
```

Esto muestra todos los commits que has hecho (probablemente aún no haya ninguno).

### Paso 3: Trabajar en la carpeta Prueba_GitHub

Navega a ella:
```bash
cd /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub
```

Verifica qué archivos hay:
```bash
ls -la
```

### Paso 4: Los primeros cambios

#### 4.1 Verificar qué cambios sin guardar hay
```bash
git status
```

Verás una salida como:
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        chacha20.cpp
        chacha20.h
        chacha20_timing.cpp
        chacha20_timing.py
        README.md

nothing added to commit but untracked files present (tracking files)
```

Esto significa que hay archivos que Git no está siguiendo aún.

#### 4.2 Agregar archivos para commit
Hay dos maneras:

**Opción A: Agregar todos los archivos**
```bash
git add .
```

**Opción B: Agregar archivos específicos**
```bash
git add chacha20.cpp
git add README.md
# ... etc
```

#### 4.3 Verificar que se agregaron
```bash
git status
```

Ahora verás los archivos en color verde con "Changes to be committed"

#### 4.4 Hacer el primer commit
```bash
git commit -m "Primer commit: Agregar archivos iniciales del proyecto"
```

**Buenas prácticas para mensajes de commit:**
- Es corto pero descriptivo
- Usa presente ("Agregar" no "Agregué")
- Empieza con mayúscula
- Evita caracteres especiales

---

## Conectar con GitHub

### Paso 1: Crear un repositorio en GitHub

1. Inicia sesión en GitHub
2. Haz clic en el ícono "+" en la esquina superior derecha
3. Selecciona "New repository"
4. Completa:
   - **Repository name**: `Prueba_GitHub` (debe coincidir con tu carpeta)
   - **Description**: Una breve descripción del proyecto
   - **Public or Private**: Elige según lo desees
   - NO marques "Initialize this repository with..." (ya tienes uno local)
5. Haz clic en "Create repository"

### Paso 2: Conectar tu repositorio local con GitHub

GitHub te mostrará instrucciones. Sigue estas:

En tu terminal, dentro de la carpeta del proyecto:
```bash
git remote add origin https://github.com/TU_USUARIO/Prueba_GitHub.git
```

Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub.

### Paso 3: Verificar que se conectó
```bash
git remote -v
```

Debes ver:
```
origin  https://github.com/TU_USUARIO/Prueba_GitHub.git (fetch)
origin  https://github.com/TU_USUARIO/Prueba_GitHub.git (push)
```

### Paso 4: Cambiar el nombre de la rama principal

Por defecto, Git crea una rama llamada `master`, pero GitHub usa `main`. Hazlo:

```bash
git branch -M main
```

### Paso 5: Subir tu código a GitHub por primera vez

```bash
git push -u origin main
```

**¿Qué significa esto?**
- `push`: Enviar cambios
- `-u`: Recordar esta configuración para próximas veces
- `origin`: El nombre de tu repositorio remoto (GitHub)
- `main`: La rama a la que envías

**Nota sobre autenticación:** Dependiendo de tu configuración, Git puede pedirte:
- Usuario y contraseña (método antiguo, no recomendado)
- Personal Access Token (recomendado)
- SSH Key (más avanzado)

Si tienes problemas, consulta: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

---

## Operaciones Esenciales

### 1. Ver el estado de tu repositorio
```bash
git status
```

Esto te muestra:
- En qué rama estás
- Cambios sin guardar
- Cambios que serán subidos al próximo push

### 2. Ver el historial de cambios
```bash
git log
```

Para una vista más compacta:
```bash
git log --oneline
```

Para ver cambios de los últimos 5 commits:
```bash
git log -5 --oneline
```

### 3. Hacer cambios y guardarlos

**Edita un archivo** (por ejemplo, README.md), luego:

```bash
# Ver cambios sin guardar
git diff

# Agregar cambios
git add nombre_del_archivo.txt

# O agregar todos
git add .

# Crear commit
git commit -m "Descripción del cambio"
```

### 4. Subir cambios a GitHub
```bash
git push
```

(Ya no necesitas `-u origin main` porque lo establecimos antes)

### 5. Descargar cambios de GitHub
```bash
git pull
```

Esto es útil si:
- Otros han hecho cambios y quieres bajarlos
- Hiciste cambios desde otra máquina

### 6. Ver cambios antes de commitear
```bash
git diff
```

### 7. Deshacer cambios sin guardar
```bash
# Si NO has hecho "git add" aún
git checkout -- nombre_archivo.txt

# O para todos los archivos
git checkout -- .
```

### 8. Deshacer un commit (cuidado)
```bash
# Ver los últimos 5 commits
git log --oneline -5

# Deshacer el último commit (pero guardar los cambios localmente)
git reset --soft HEAD~1

# Deshacer el último commit (perder los cambios)
git reset --hard HEAD~1
```

---

## Flujo de Trabajo Recomendado

Este es el flujo típico día a día:

### Ciclo Diario: EDITAR → COMMIT → PUSH

```bash
# 1. Navega a tu proyecto
cd /home/catec/Pruebas_Codigo_Sprint1/Prueba_GitHub

# 2. Edita tus archivos (usando tu editor favorito)
# Por ejemplo, edita chacha20.cpp o crea nuevos archivos

# 3. Verifica qué cambió
git status

# 4. Ver diferencias detalladas (opcional)
git diff

# 5. Agregar cambios
git add .

# 6. Crear commit con mensaje descriptivo
git commit -m "Feature: Mejorar función de encriptación"

# 7. Subir a GitHub
git push

# 8. Verifica en GitHub que los cambios están allí
# Abre https://github.com/TU_USUARIO/Prueba_GitHub
```

### Trabajar con Ramas (Intermedio)

Las ramas te permiten trabajar en feature sin afectar el código principal:

```bash
# Crear una rama nueva
git branch feature/nueva-funcionalidad

# Cambiar a esa rama
git checkout feature/nueva-funcionalidad

# O hacer ambas cosas a la vez
git checkout -b feature/nueva-funcionalidad

# Ver todas tus ramas
git branch

# Hacer cambios y commits normalmente...
git add .
git commit -m "Agregar nueva funcionalidad"

# Subir la rama a GitHub
git push -u origin feature/nueva-funcionalidad

# Cuando termines, puedes hacer un "Pull Request" en GitHub
# para que otros revisen antes de mezclar (merge) a main
```

---

## Consejos y Buenas Prácticas

### ✅ Haz (DO's)

1. **Commit frecuentemente**
   - Haz commits pequeños y lógicos
   - Cada commit debe representar una idea clara

2. **Escribe buenos mensajes de commit**
   - ✅ Bien: "Fix: Corregir bug en validación de entrada"
   - ❌ Mal: "asdfgh" o "cambios varios"

3. **Sincronízate regularmente**
   ```bash
   git pull  # Antes de empezar a trabajar
   git push  # Al terminar
   ```

4. **Crea un .gitignore**
   - Para ignorar archivos que no quieres subir a GitHub
   - Ejemplo:
   ```
   __pycache__/
   *.o
   *.exe
   .DS_Store
   node_modules/
   ```

5. **Usa ramas para features**
   - No trabajes siempre en `main`
   - Usa: `feature/mi-funcionalidad`, `bugfix/mi-bug`

### ❌ No Hagas (DON'Ts)

1. **No hagas push sin test**
   - Verifica que tu código funciona antes

2. **No comitees archivos innecesarios**
   - No subas: `.exe`, `__pycache__`, archivos de compilación, etc.

3. **No usos mensajes de commit genéricos**
   - ❌ "Cambios", "Actualización", "Fix"
   - ✅ "Fix: Corregir overflow en cálculo de suma"

4. **No olvides hacer pull antes de trabajar**
   - Si colaboras, otros pueden haber hecho cambios

5. **No hagas reset --hard** sin saber qué haces
   - Pierdes cambios permanentemente

---

## Comandos Rápidos de Referencia

```bash
# CONFIGURACIÓN
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# CREAR Y CLONAR
git init                          # Crear repo nuevo
git clone URL                     # Copiar un repo existente

# ESTADO Y DIFERENCIAS
git status                        # Ver estado
git diff                          # Ver cambios sin guardar
git log                           # Ver historial
git log --oneline                 # Historial compacto

# AGREGAR Y COMMITEAR
git add .                         # Agregar todos los cambios
git add archivo.txt               # Agregar archivo específico
git commit -m "mensaje"           # Crear commit
git commit --amend                # Modificar ultimo commit

# REMOTOS
git remote -v                     # Ver repositorios remotos
git remote add origin URL         # Agregar remoto
git push                          # Subir cambios
git pull                          # Descargar cambios
git push origin main              # Subir rama específica

# RAMAS
git branch                        # Ver ramas
git branch -a                     # Ver todas (locales y remotas)
git checkout -b nombre            # Crear y cambiar a rama
git checkout nombre               # Cambiar a rama
git merge nombre                  # Mezclar rama a la actual

# DESHACER
git checkout -- archivo           # Deshacer cambios en archivo
git reset --soft HEAD~1           # Deshacer último commit, guardar cambios
git reset --hard HEAD~1           # Deshacer último commit, perder cambios
```

---

## Próximos Pasos

1. **Practica lo básico**: Haz al menos 5 commits pequeños
2. **Aprende ramas**: Crea una rama `feature/prueba` y experimenta
3. **Colabora**: Invita a un amigo: 
   - En GitHub: Settings → Collaborators → Agregar persona
4. **Aprende Pull Requests**: Útil cuando colaboras con otros
5. **Explora GitHub**: Búsca proyectos interesantes, aprende releyendo su historial

---

## Recursos Útiles

- **Documentación Oficial Git**: https://git-scm.com/doc
- **Documentación GitHub**: https://docs.github.com
- **Visualizador de ramas**: `git log --all --oneline --graph`
- **Practica en línea**: https://learngitbranching.js.org

---

## Cheat Sheet Visual

```
Tu Máquina (Local)          Internet             GitHub
┌─────────────────┐                          ┌──────────┐
│  Carpeta Local  │                          │ Servidor │
│                 │      git push            │          │
│  (modificas) →  ├─────────────────────────→│          │
│  git add .      │                          │          │
│  git commit -m  │      git pull            │          │
│  "cambios"      │←─────────────────────────┤          │
│                 │                          │          │
└─────────────────┘                          └──────────┘
```

¡Listo! Ya tienes todo lo que necesitas para empezar. 🚀
