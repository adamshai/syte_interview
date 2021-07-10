# README

A service to maintain a to do list

## Set up

### One time setup

```
docker volume create todo-list-db
```

### Start the service

```
docker compose up
```

An item in the list has two fields:

- text: string
- done: boolean

CRUD interface:

| Action | HTTP request type | URL            | Description                     |
| ------ | ----------------- | -------------- | ------------------------------- |
| Create | POST              | /api/item      | Adds an item to the list        |
| Read   | GET               | /api/item/{id} | Returns item with id {id}       |
| Read   | GET               | /api/item      | Returns all items               |
| Update | PUT               | /api/item/{id} | Updates item {id} in the list   |
| Delete | DELETE            | /api/item/{id} | Deletes item {id} from the list |

- HTTP request format should be JSON

## Examples:

### Get all items

```
[GET] /api/item
response =
[
    {
        "done": false,
        "id": 2,
        "text": "item 2"
    },
    {
        "done": false,
        "id": 3,
        "text": "item 3"
    }
]
```

### Get item 2

```
[GET] /api/item/2
response =
{
    "done": false,
    "id": 2,
    "text": "item 2"
}
```

### Add an item

```
[POST] /api/item
request =
{
    "text": "Go to the supermarket"
}
response =
{
    "done": false,
    "id": 4,
    "text": "Go to the supermarket"
}
```

### Set item 1 as done

```
[PUT] /api/item/1
request =
{
    "done": true
}
response =
{
    "done": true,
    "id": 1,
    "text": "item 1"
}
```

### Delete item 1

```
[DELETE] /api/item/1
response =
1
```
