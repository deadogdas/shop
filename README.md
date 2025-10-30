# 🛍️ Shop — Full-Stack Интернет-Магазин

Полноценное приложение интернет-магазина с фронтендом на **Vue 3 (Vite)** и бэкендом на **FastAPI (Python)**.  
Проект полностью контейнеризован с помощью **Docker Compose**.

---

## 🚀 Стек технологий

**Frontend**
- ⚡ Vue 3 + Vite
- 🎨 CSS + компонентный дизайн
- 🔄 Axios (в `src/services/api.js`) для работы с API
- 🧭 Vue Router

**Backend**
- 🐍 FastAPI
- 🗄️ SQLAlchemy
- 🧱 PostgreSQL
- 🧰 Слои: models / repositories / services / routes / schemas

**DevOps**
- 🐳 Docker + Docker Compose

---

## 📂 Структура проекта

```
shop/
├── docker-compose.yml
├── backend/
│   ├── app/
│   │   ├── models/ — модели БД
│   │   ├── routes/ — REST API
│   │   ├── services/ — бизнес-логика
│   │   ├── repositories/ — взаимодействие с БД
│   │   └── schemas/ — Pydantic-схемы
└── frontend/
    ├── src/
    │   ├── components/ — Vue-компоненты
    │   ├── router/ — маршруты
    │   └── services/api.js — взаимодействие с беком
```

---

## ⚙️ Установка и запуск

### 🐳 Вариант 1 — через Docker

```bash
# Клонируем проект
git clone https://github.com/deadogdas/shop.git
cd shop

# Запускаем контейнеры
docker-compose up --build
```

После сборки приложение будет доступно:
- Фронтенд: [http://localhost:5173](http://localhost:5173)
- Бэкенд API: [http://localhost:8000](http://localhost:8000/docs)

---

### 💻 Вариант 2 — ручной запуск

#### Backend

```bash
cd backend
pip install -r requirements.txt
python run.py
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🧩 Основной функционал

- Просмотр каталога товаров  
- Фильтрация по категориям  
- Добавление товаров в корзину  
- Управление заказами  
- REST API с документацией Swagger (`/docs`)
