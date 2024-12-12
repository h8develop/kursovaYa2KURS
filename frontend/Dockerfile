# Этап сборки
FROM node:16-alpine AS build

WORKDIR /app

# Копируем только необходимые файлы для установки зависимостей
COPY ./frontend/package.json ./frontend/yarn.lock ./
RUN yarn install

# Копируем все файлы проекта во временный контейнер
COPY ./frontend/ ./
RUN yarn build

# Этап сервировки с помощью Nginx
FROM nginx:alpine

# Копируем сборку React в Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Создаем корректный файл конфигурации Nginx
RUN echo 'server {\n\
    listen 80;\n\
    server_name localhost;\n\
\n\
    location / {\n\
        root /usr/share/nginx/html;\n\
        index index.html;\n\
        try_files $uri /index.html;\n\
    }\n\
}' > /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
