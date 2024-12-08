# Этап сборки
FROM node:16-alpine AS build

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Копируйте package.json и yarn.lock для установки зависимостей
COPY package.json yarn.lock ./

# Установите зависимости
RUN yarn install

# Копируйте остальной код приложения
COPY . .

# Соберите приложение для продакшена
RUN yarn build

# Этап сервировки с помощью Nginx
FROM nginx:alpine

# Удалите стандартный сайт Nginx
RUN rm -rf /usr/share/nginx/html/*

# Копируйте собранные файлы в директорию Nginx для обслуживания
COPY --from=build /app/build /usr/share/nginx/html

# Копируйте пользовательскую конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Откройте порт 80 для доступа
EXPOSE 80

# Запустите Nginx в фоновом режиме
CMD ["nginx", "-g", "daemon off;"]
