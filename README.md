# Первое задание

## Инструкция по запуску:

1. После клонирования репозитория, перейти в папку <i>task1</i>
2. Создать docker network:

```
docker network create lexicom
```

3. Используя Docker Compose, запустить веб приложение и Redis:

```
docker-compose up --build
```

или

```
docker compose up --build
```

4. Приложение будет запущено на локалхосте (localhost:8000). Сваггером можно воспользоваться через эндпоинт /docs.

## Комментарии по имплементации

1. Всего реализовано 3 ручки:
    1. POST write_data
    2. PUT write_data
    3. GET check_data

Реализовано именно 3 ручки для того, чтобы получить идемпотентность PUT и GET методов, согласно
Restful API, и отделить создание новой записи в отдельный эндпоинт (POST write_data).

Через PUT write_data возможно обновить информацию о уже существующем клиенте, иначе 404.

Через POST write_data возможно только создать нового клиента, если в системе уже есть клиент с таким номером телефона,
то также 400.

Через GET check_data возможно получить адрес клиента, указав его номер.

На всех эндпоинтах установлена валидация через Pydantic. Согласно ей, номер телефона состоит из 11 цифр.

В приложении применена слоистая архитектура и абстракции для возможного изменения и масштабирования.

# Второе задание

1 Вариант: Использовать UPDATE c JOIN

```
UPDATE full_names fn
SET status = sn.status
FROM short_names sn
WHERE fn.name LIKE sn.name || '.%'
  AND sn.status IS NOT NULL;
```

2 Вариант: Использование Common Table Expression

```
WITH temp_status AS (
  SELECT fn.name, sn.status
  FROM full_names fn
  JOIN short_names sn
  ON fn.name LIKE sn.name || '.%'
  WHERE sn.status IS NOT NULL
)
UPDATE full_names fn
SET status = ts.status
FROM temp_status ts
WHERE fn.name = ts.name;

```

3 Вариант: Использование подзапроса в UPDATE

```
UPDATE full_names
SET status = (
  SELECT sn.status
  FROM short_names sn
  WHERE full_names.name LIKE sn.name || '.%'
  LIMIT 1
)
WHERE EXISTS (
  SELECT 1
  FROM short_names sn
  WHERE full_names.name LIKE sn.name || '.%'
);
```