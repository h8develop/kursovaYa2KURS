# Ad Management System

Система управления рекламными кампаниями с кластерной архитектурой на Kubernetes и CI/CD с использованием GitHub Actions.

## **Структура Проекта**

```
.github/
  workflows/
    ci-cd.yml         # Настройки CI/CD для GitHub Actions
backend/
  app/
    routers/          # Роуты для API FastAPI
    metrics.py        # Метрики Prometheus
    models.py         # Модели базы данных
    schemas.py        # Схемы Pydantic для API
  Dockerfile          # Dockerfile для backend
  main.py             # Точка входа в приложение FastAPI
frontend/
  src/                # Исходный код React приложения
  public/             # Статические файлы
  Dockerfile          # Dockerfile для frontend
  nginx.conf          # Конфигурация Nginx
infrastructure/
  grafana/            # Настройки Grafana
  loki/               # Настройки Loki
  prometheus/         # Настройки Prometheus
k8s/                  # Kubernetes манифесты для развертывания
  backend-deployment.yaml  # Deployment backend
  frontend-deployment.yaml # Deployment frontend
  ingress.yaml             # Ingress маршрутизация
  ...
docker-compose.yml     # Файл для локальной разработки
README.md              # Документация проекта
```

## **Компоненты**

- **Frontend**: React приложение, обслуживаемое через Nginx.
- **Backend**: FastAPI приложение для обработки API запросов.
- **PostgreSQL**: База данных для хранения данных рекламных кампаний.
- **Prometheus**: Система мониторинга.
- **Grafana**: Платформа для визуализации метрик и логов.
- **Loki**: Система логирования.
- **Ingress Controller**: Управляет внешним доступом к сервисам.

## **Требования**

- Docker и Docker Compose (для локальной разработки).
- Kubernetes кластер (локально с Minikube или в облаке).
- kubectl установлен и настроен для взаимодействия с вашим кластером.
- GitHub репозиторий с настройками CI/CD.

## **Локальная Разработка с Docker Compose**

### **Шаг 1: Сборка и Запуск Контейнеров**

```bash
docker-compose up --build -d
```

### **Шаг 2: Проверка Запущенных Сервисов**

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend: [http://localhost:8000](http://localhost:8000)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3001](http://localhost:3001)

## **Развёртывание в Kubernetes**

### **Шаг 1: Запуск Minikube**

```bash
minikube start
```

### **Шаг 2: Применение Манифестов Kubernetes**

```bash
kubectl apply -f k8s/
```

### **Шаг 3: Настройка Ingress**

После применения манифеста `ingress.yaml` убедитесь, что DNS настроен правильно. Используйте `minikube tunnel`, чтобы перенаправить запросы:

```bash
minikube tunnel
```

Доступ к сервисам:
- Frontend: [http://frontend.local](http://frontend.local)
- Backend: [http://backend.local](http://backend.local)
- Grafana: [http://grafana.local](http://grafana.local)
- Prometheus: [http://prometheus.local](http://prometheus.local)

## **CI/CD с GitHub Actions**

- **Сборка Docker-образов**:
  - Используется `Dockerfile` для backend и frontend.
  - Автоматическая загрузка образов в Docker Hub.

- **Деплой в Kubernetes**:
  - Применяются манифесты из папки `k8s/`.

## **Мониторинг и Логирование**

- **Prometheus**:
  - Сбор метрик с backend и других сервисов.
  - Пример: количество созданных объявлений, время обработки API.

- **Grafana**:
  - Визуализация метрик из Prometheus.
  - Настроенные дашборды для аналитики.

- **Loki**:
  - Система логирования для анализа логов контейнеров.
