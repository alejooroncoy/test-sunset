<h1 align="center">Prueba Sunset</h1>

Este proyecto consiste en la creación de una **API REST** que interactúe con una base de datos gestionada en **Turso**. El objetivo es proporcionar un endpoint para cada tabla presente en la base de datos, permitiendo la gestión de los datos a través de operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

---

## Requisitos

### Tablas en la base de datos
La base de datos Turso contiene las siguientes tablas con las estructuras detalladas:

### Tabla `User`
| Column Name | Type     | Default Value |
|-------------|----------|---------------|
| id          | INTEGER  | NULL          |
| name        | STRING   | NULL          |
| password    | STRING   | NULL          |
| email       | STRING   | NULL          |
| store_id    | STRING   | NULL          |
| brand_id    | STRING   | NULL          |

### Tabla `Store`
| Column Name      | Type     | Default Value |
|------------------|----------|---------------|
| id               | INTEGER  | NULL          |
| social_networks  | STRING   | NULL          |
| website          | STRING   | NULL          |

### Tabla `Brand`
| Column Name | Type     | Default Value |
|-------------|----------|---------------|
| id          | INTEGER  | NULL          |
| fiscal_data | STRING   | NULL          |
| iban        | STRING   | NULL          |

---

## Tareas a realizar

1. **Creación de la API REST**:
   - Implementar un endpoint independiente para cada una de las tablas (`User`, `Store`, `Brand`).
   - Permitir realizar las operaciones básicas: **Crear, Leer, Actualizar y Eliminar**.

2. **Conexión con la base de datos Turso**:
   - Utilizar el **SDK oficial de Turso** para conectar la API a la base de datos. Guías disponibles:
     - [SDK Turso (JavaScript)](https://docs.turso.tech/sdk/ts/quickstart).
     - [Prisma con Turso](https://docs.turso.tech/sdk/ts/orm/prisma).
     - [SQLAlchemy con Turso](https://docs.turso.tech/sdk/python/orm/sqlalchemy).

3. **Gestión del proyecto con Gitflow**:
   - Seguir la metodología de trabajo **Gitflow** para la gestión de ramas. Para más información, consulta:
     - [Introducción a Gitflow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=%C2%BFQu%C3%A9%20es%20Gitflow%3F,vez%20y%20quien%20lo%20populariz%C3%B3.).
     - [Cheat Sheet de Gitflow](https://danielkummer.github.io/git-flow-cheatsheet/index.es_ES.html).

4. **Documentación de endpoints**:
   - Crear una documentación clara y concisa para los endpoints implementados, indicando los métodos HTTP utilizados y ejemplos de solicitudes/respuestas.

---

## Herramientas recomendadas

- **ORM**:
  - Para TypeScript/JavaScript: [Prisma](https://docs.turso.tech/sdk/ts/orm/prisma).
  - Para Python: [SQLAlchemy](https://docs.turso.tech/sdk/python/orm/sqlalchemy).
- **SDK de Turso**:
  - Utiliza el [SDK oficial de Turso](https://docs.turso.tech/sdk/ts/quickstart) para la conexión a la base de datos.
- **Gestión de ramas con Gitflow**:
  - Apóyate en la [guía Gitflow Cheat Sheet](https://danielkummer.github.io/git-flow-cheatsheet/index.es_ES.html) para una implementación efectiva del flujo de trabajo.

---

## Estructura del proyecto

1. **Endpoints**:
   - `GET /users`: Obtener todos los usuarios.
   - `POST /users`: Crear un nuevo usuario.
   - `PUT /users/:id`: Actualizar un usuario existente.
   - `DELETE /users/:id`: Eliminar un usuario.

   - `GET /stores`: Obtener todas las tiendas.
   - `POST /stores`: Crear una nueva tienda.
   - `PUT /stores/:id`: Actualizar una tienda existente.
   - `DELETE /stores/:id`: Eliminar una tienda.

   - `GET /brands`: Obtener todas las marcas.
   - `POST /brands`: Crear una nueva marca.
   - `PUT /brands/:id`: Actualizar una marca existente.
   - `DELETE /brands/:id`: Eliminar una marca.

2. **Ramas Gitflow**:
   - `main`: Versión estable y lista para producción.
   - `develop`: Desarrollo principal.
   - `feature/<nombre>`: Nuevas funcionalidades.
   - `release/<nombre>`: Preparación para un lanzamiento.
   - `hotfix/<nombre>`: Correcciones rápidas en producción.

---

## Cómo empezar

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. Configura Gitflow:
   ```bash
   git flow init
   ```

3. Instala las dependencias necesarias (ejemplo con Node.js y Prisma):
   ```bash
   npm install
   npm install prisma
   ```

4. Configura la conexión con la base de datos Turso en el archivo `.env`:
   ```env
   TURSO_URL=<tu-url-de-turso>
   TURSO_API_KEY=<tu-api-key>
   ```

5. Desarrolla nuevas funcionalidades siguiendo la metodología Gitflow.

---

## Recursos adicionales

- [Documentación oficial de Turso](https://docs.turso.tech/).
- [Metodología Gitflow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow).
- [Cheat Sheet de Gitflow](https://danielkummer.github.io/git-flow-cheatsheet/index.es_ES.html).
- [Prisma y Turso](https://docs.turso.tech/sdk/ts/orm/prisma).
- [SQLAlchemy y Turso](https://docs.turso.tech/sdk/python/orm/sqlalchemy).

¡Feliz codificación!
