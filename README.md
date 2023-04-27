# Rest

## INDICE

- [endpoints](#endpoints)
- ![uso](#uso)
- ![LICENSE](#license)
- ![autor](#autor)

- Api escrita en **_django Rest Framewrok_** en donde podras almacenar tus proyectos pendientes en tu planes de estudio, cumple con las operaciones **_CRUD_**

## endpoints

1. GET

- `/api/rest`: ruta principal

```json
[
  {
    "id": 1,
    "title": "proyecto en django",
    "description": "Desarrollar una Api en Django Rest Framework",
    "technology": "Python",
    "created_at": "2023-04-27T03:52:50.377336Z"
  },
  {
    "id": 2,
    "title": "proyecto en react",
    "description": "Desarrollar una Aplicacion en mobile con react native",
    "technology": "JavaScript",
    "created_at": "2023-04-27T03:53:22.715489Z"
  }
]
```

2. POST

- `/api/rest`: crea un proyecto

```json
{
  "id": 3,
  "title": "proyecto en Laravel",
  "description": "Desarrollar una api",
  "technology": "PHP",
  "created_at": "2023-04-27T03:53:22.715489Z"
}
```

3. PUT

- `/api/rest/<int:id>`: Actuliza por id

```json
{
  "id": 3,
  "title": "proyecto en typescript",
  "description": "Desarrollar una CLI con nodejs",
  "technology": "Typescript",
  "created_at": "2023-04-27T03:53:22.715489Z"
}
```

4. DELETE

- `/api/rest/<int:id>`: Elimina por id

```json
{}
```

## Uso

Para usar esta api puedes clonar el repositorio

```shell
git clone https://github.com/sebastian01w/Drf_rest.git
```

descarga las dependecias

```shell
pip install -r requirements.txt
```

ejecuta el comando:

```shell
python manage.py runserver
```

obtendras esta vista en el puerto 8080

![rest](https://i.postimg.cc/fLD3WQyF/rest.png)

## LICENSE

- Este proyecto esta bajo la `LILCENSE MIT` sientete libre de hacer con el lo que plazca mejoralo como te veas que es mejor

## Autor

- Johan Sebastian Castro Garcia
  <br>
  `github`: sebastian01w
  <br>
  `email`: johancs.mm@gmail.com
