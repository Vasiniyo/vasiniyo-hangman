# vasiniyo-hangman

`vasiniyo-hangman` - Игра [Виселица](https://ru.wikipedia.org/wiki/Виселица_(игра)), написанная на `python 3.11`

## TL;DR
В коренной директории находится файл run.sh, который собирает и запускает контейнер.

## Установка
Установите Docker для своей системы: https://docs.docker.com/get-started/get-docker/<br>
Получите последний образ:

```bash
    docker pull ghcr.io/vasiniyo/vasiniyo-hangman:latest
```

Также вы можете собрать образ из исходников:<br>
Скачайте репозиторий<br>
Сделать это можно, например, вот так:
```bash
  git clone git@github.com:Vasiniyo/vasiniyo-hangman.git
```
```bash
  git clone https://github.com/Vasiniyo/vasiniyo-hangman.git
```
Перейдите в коренную директорию с игрой и пропишите команду
```bash
  docker build -t "vasiniyo-hangman" --no-cache .
```
После этого создастся образ с именем `vasiniyo-hangman`, который можно будет использовать, чтобы поднять контейнер


## Использование
```bash
    docker run -it --rm ghcr.io/vasiniyo/vasiniyo-hangman:latest
```
Либо просто запустите run.sh в коренной директории, чтобы выполнить сборку образа и поднять контейнер автоматически.
По умолчанию имя контейнера будет `vasiniyo-hangman`
```bash
    ./run.sh
```

Вы прекрасны, игра успешно работает

## Содействие

Вы можете внести свой вклад в разработку. Для этого можете открыть имеющиеся `issues`,
либо придумывать свои и отправлять`Pull Request`с соответствующими изменениями.
Обязательно создавайте новый issue, если вы обнаружили баг, либо у вас есть крутые идеи.
