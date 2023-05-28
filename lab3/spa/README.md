### Клиентское часть приложения для раскрашивания черно-белых изображений на основе [DeOldify](https://github.com/jantic/DeOldify).

В качестве SPA фреймворка используется [Vue.js 3](https://vuejs.org/).

#### 1. Команда проекта
 - Наймушин Алексей

#### 2. Запуск приложения
 - устанавливаем пакеты ```npm i```;
 - запускаем сервер разрабоки ```npm run watch```

#### 3. Запуск в [docker](https://www.docker.com/)
Собираем приложение ```npm run build```

Создаем контейнер
```
docker build . -t nginx --progress=plain
```

Запускаем контейнер
```
docker run -p 80:80 nginx
```