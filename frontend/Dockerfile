# Этап сборки
FROM node:16-alpine AS build

WORKDIR /app

COPY frontend/package.json frontend/yarn.lock ./
RUN yarn install

COPY frontend/ .
RUN yarn build

# Этап сервировки с помощью Nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

# Опционально: копирование конфигурации Nginx
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
