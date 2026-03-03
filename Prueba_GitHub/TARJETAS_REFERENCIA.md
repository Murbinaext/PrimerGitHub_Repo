# Git & GitHub - Tarjetas de Referencia Rápida 🎴

## TARJETA 1: Configuración Inicial (Se hace UNA sola vez)

```bash
# Tu identidad (reemplaza con tu info)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Verificar
git config --global user.name
git config --global user.email
```

---

## TARJETA 2: Crear Repositorio (Se hace UNA sola vez por proyecto)

```bash
# OPCIÓN A: Nuevo repositorio (comando git init)
git init
git add .
git commit -m "Commit inicial"
git remote add origin https://github.com/TU_USUARIO/nombre.git
git branch -M main
git push -u origin main

# OPCIÓN B: Clonar un repositorio existente
git clone https://github.com/usuario/repo.git
cd repo
```

---

## TARJETA 3: El Ciclo Diario (Esto lo harás cien veces)

```
Esta es tu rutina normal:

┌─────────────────────────────┐
│       EDITAR ARCHIVOS       │
│  (Usando tu editor normal)  │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│   git status                │ ← Ver qué cambió
│   (opcional: git diff)      │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│   git add .                 │ ← Preparar cambios
│   (o git add archivo.txt)   │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│  git commit -m "mensaje"    │ ← Guardar cambios
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│      git push               │ ← Subir a GitHub
│  (o git push origin main)   │
└─────────────────────────────┘
```

**Comandos:**
```bash
git status          # Ver qué cambió
git diff            # Ver diferencias en detalle
git add .           # Agregar TODO
git add archivo.txt # Agregar archivo específico
git commit -m "Descripción clara del cambio"
git push            # Subir a GitHub
```

---

## TARJETA 4: Ver Historial

```bash
# El commit más reciente
git log -1

# Los últimos 5 commits en una línea
git log -5 --oneline

# Todos los commits
git log

# Versión visual (el mejor para entender)
git log --all --oneline --graph

# Ver cambios en un commit específico
git show abc1234  # Donde abc1234 es el ID del commit
```

---

## TARJETA 5: Deshacer Cambios (UN POCO PELIGROSO)

```bash
# ❌ Cambios que AÚN NO HAS AGREGADO (git add)
git checkout -- archivo.txt    # Deshacer un archivo
git checkout -- .              # Deshacer TODO

# ⚠️ CAMBIOS QUE SÍ AGREGASTE (git add) pero NO commitiste
git reset archivo.txt          # Quitar archivo, guardar cambios
git reset                      # Quitar todo, guardar cambios

# ⚠️⚠️ COMMITS (PELIGROSO - PIERDES CAMBIOS)
git reset --soft HEAD~1        # Deshacer último commit, guardar cambios
git reset --hard HEAD~1        # Deshacer último commit, PERDER cambios
                               # NO HAGAS ESTO sin saber qué haces

# 💡 Si metiste la pata con reset --hard
# Intenta: git reflog (muestra todo lo que Git hizo)
```

**Regla de oro:** Si tienes dudas, NUNCA uses `reset --hard`. Usa `reset --soft`.

---

## TARJETA 6: Trabajar con Ramas

**¿Por qué ramas?** Para trabajar sin romper el código en `main`

```bash
# Ver todas tus ramas
git branch           # Solo locales
git branch -a        # Incluyendo remotas en GitHub

# Crear rama y cambiar a ella
git checkout -b feature/mi-funcionalidad

# Cambiar a una rama existente
git checkout main
git checkout feature/mi-funcionalidad

# Borrar rama local (después de confirmar que no la necesitas)
git branch -d feature/mi-funcionalidad

# Borrar rama en GitHub
git push origin --delete feature/mi-funcionalidad

# Mezclar (merge) rama a main
git checkout main              # Asegúrate estar en main
git pull                       # Actualiza
git merge feature/mi-funcionalidad
git push
```

**Flujo recomendado:**
```
main (estable) ← siempre funciona
  ↑
  └─── feature/nueva-funcionalidad ← trabajas aquí
         ↑
         Cuando terminas, haces merge a main
```

---

## TARJETA 7: Sincronizar con GitHub

```bash
# Descargar cambios de otros
git pull

# Subir tus cambios
git push

# Subir rama nueva a GitHub
git push -u origin feature/mi-rama

# Crear rama local basada en rama remota
git checkout --track origin/feature/existente
```

---

## TARJETA 8: Mensajes de Commit Buenos vs Malos

✅ BUENOS Mensajes:
```
Feature: Agregar validación de email
Fix: Corregir bug en cálculo de impuestos
Docs: Actualizar README con instrucciones
Chore: Actualizar dependencias
Refactor: Simplificar función de login
```

❌ MALOS Mensajes:
```
asdfgh
cambios
actualizar
fix
arreglé el bug
muchos cambios varios
```

**Estructura sugerida:**
```
[Tipo]: [Descripción breve]

Descripción más larga (opcional)
- Punto 1
- Punto 2
```

**Tipos comunes:**
- `Feature` o `Feat` - Funcionalidad nueva
- `Fix` - Arreglaste un bug
- `Docs` - Cambios en documentación
- `Chore` - Mantenimiento (actualizar dependencias, etc)
- `Refactor` - Reorganizar código sin cambiar funcionalidad
- `Test` - Agregar o modificar tests

---

## TARJETA 9: Crear y Usar .gitignore

```bash
# Crear archivo .gitignore en la carpeta raíz
nano .gitignore
# (O edítalo con tu editor favorito)
```

**Contenido típico para Python/C++:**
```
# Python
__pycache__/
*.pyc
venv/
.env

# C++
*.o
*.out
*.exe

# Sistema
.DS_Store
.vscode/
.idea/

# Jupyter
.ipynb_checkpoints/
```

Después:
```bash
git add .gitignore
git commit -m "Config: Agregar .gitignore"
git push
```

---

## TARJETA 10: Emergencias - Comandos de Rescate

```bash
# "¿Qué pasó?" - Ver TODO
git status
git log --oneline -10
git diff

# "Cambié accidentalmente un archivo" 
git checkout -- archivo.txt  # Deshace cambios

# "Agregué un archivo por accidente"
git reset archivo.txt  # Lo quita del staging

# "Hice un commit con mensaje malo"
git commit --amend -m "Mensaje correcto"
git push --force-with-lease origin main

# "Subí algo que no quería"
# (para borrar del historio, es más complejo)
# Mejor: cometeloide siguiente commit que lo borre

# "¿Qué contenía este archivo en el commit abc1234?"
git show abc1234:ruta/archivo.txt

# "Quiero ver TODO lo que Git ha hecho"
git reflog
```

---

## TARJETA 11: Colaborar con Otros

**Dar acceso a otros:**
1. GitHub → Settings → Collaborators → Add people
2. Envía el nombre de usuario

**Cuando colaboras:**
```bash
# SIEMPRE empieza con
git pull

# Haz tus cambios
# ...

# Antes de push, verifica que no hay conflictos
git pull

# Si hay conflictos, resuélvelos y hace commit
# Si no hay conflictos
git push
```

**Para evitar conflictos:**
- No edites archivos al mismo tiempo que otros
- Comunícate con el equipo
- Usa ramas diferentes para features diferentes

---

## TARJETA 12: Cheat Sheet Ultra Compacto

```bash
# SETUP (una sola vez)
git config --global user.name "Nombre"
git config --global user.email "email"

# DÍA A DÍA
git status
git add .
git commit -m "mensaje"
git push
git pull

# RAMAS
git branch -a
git checkout -b feature/nombre
git checkout main
git merge feature/nombre

# HISTORIAL
git log --oneline
git log --all --oneline --graph

# EMERGENCIAS
git checkout -- archivo.txt        # Deshacer archivo
git reset --soft HEAD~1            # Deshacer commit
git commit --amend -m "mensaje"    # Corregir último commit
```

---

## TARJETA 13: Preguntas Frecuentes

**P: ¿Cuándo debo hacer commit?**
R: Cuando completaste una pequeña característica. Regla: Si no puedes describirlo en una frase, es muy grande.

**P: ¿Qué es origin?**
R: Es el nombre del repositorio remoto en GitHub. Puedes tener varios ("origin", "upstream", etc).

**P: ¿Qué es main vs master?**
R: Lo mismo. GitHub cambió al predeterminado de "main" en 2020. Son equivalentes.

**P: ¿Debería tener muchas ramas?**
R: No. Solo crea ramas cuando trabajes en una feature importante. Bórrala después de mergear.

**P: ¿Cómo colaboro si no tengo permiso de escritura?**
R: Haz un "Fork" (copia) del repo, haz cambios en tu copia, y luego un "Pull Request" para que el dueño lo revise.

**P: ¿Qué es un Pull Request (PR)?**
R: Una solicitud para mezclar tu código. Otros pueden revisar y comentar antes de mergear.

**P: ¿Cómo actualizo mi repo si alguien cambió algo en GitHub?**
R: `git pull`

**P: Borré un archivo, ¿puedo recuperarlo?**
R: Sí: `git checkout -- archivo` (si no hiciste commit aún) o restaurar de un commit anterior.

**P: ¿Puedo trabajar offline?**
R: Sí. Git funciona localmente. Cuando tengas internet: `git push`

**P: ¿Qué significa "Your branch is ahead of origin/main"?**
R: Que hiciste commits que NO has subido aún. Solución: `git push`

---

## TARJETA 14: Recursos en Internet

- **Git Official Docs:** https://git-scm.com/doc
- **GitHub Docs:** https://docs.github.com
- **Aprende visualmente:** https://learngitbranching.js.org
- **Visualiza tu historial:** `git log --all --oneline --graph | head -20`

---

## TARJETA 15: Tu Primera Semana (Plan de Estudio)

**Día 1:** 
- Haz el Ejercicio 1-3 (configuración básica y primer commit)

**Día 2:**
- Haz el Ejercicio 4-6 (conectar con GitHub y subir código)

**Día 3:**
- Haz el Ejercicio 7-8 (editar y subir cambios)

**Día 4:**
- Haz el Ejercicio 9-10 (múltiples commits y ramas)

**Día 5-7:**
- Haz el Ejercicio 11-14 (todo junto)
- Borr y vuelve a crear ramas de práctica
- Haz pequeños cambios y commitéalos todos los días

**Meta:** Al final de la semana, deberían ser tan natural que dejes de pensar en ello.

---

¡Imprime estas tarjetas de referencia! (O guarda este archivo) 🎴
