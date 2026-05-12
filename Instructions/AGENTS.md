# AGENTS.md — Агрохолдинги

## Инструкции для AI агентов

Все инструкции находятся в папке `Instructions/`:

| Файл | Назначение |
|------|------------|
| [AGENTS_MAIN.md](AGENTS_MAIN.md) | Главная навигация по проекту |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Структура проекта с описанием секций |
| [AGENTS_PYTHON.md](AGENTS_PYTHON.md) | Python правила (aiogram, FastAPI, etc.) |
| [AGENTS_DESIGN.md](AGENTS_DESIGN.md) | UI/UX правила и дизайн система |
| [AGENTS_WEB.md](AGENTS_WEB.md) | Web правила (HTML/CSS/JS, Tailwind) |
| [memory.md](memory.md) | Память нашего общения |
| [CHANGELOG.md](CHANGELOG.md) | История изменений проекта |

## Быстрый старт

### Лендинг Ozonbox
```bash
npm install        # Установка зависимостей
npm run dev         # Development с watch
npm run build       # Production build
```

### Open Design (AI-дизайн инструмент)
```bash
cd open-design
pnpm install --link-workspace-packages=true
pnpm tools-dev run web
# Откроется на http://127.0.0.1:51458/
```

## Структура проекта

```
агрохолдинги/
├── index.html              # Лендинг Ozonbox
├── package.json            # npm зависимости
├── src/
│   ├── css/styles.css      # Tailwind входной файл
│   └── js/main.js          # GSAP + AOS + Lenis
├── dist/                   # Скомпилированный CSS
├── docs/                   # Инструкции AGENTS
│   ├── AGENTS_MAIN.md      # Этот файл
│   ├── AGENTS_PYTHON.md    # Python правила
│   ├── AGENTS_DESIGN.md    # UI/UX правила
│   ├── AGENTS_WEB.md       # Web правила
│   └── PROJECT_STRUCTURE.md
├── open-design/            # AI-дизайн инструмент
└── .env                    # Переменные окружения
```

## Ключевые секции index.html

| Секция | Строки | Описание |
|--------|--------|----------|
| HERO | ~843-898 | Главный баннер + статистика |
| PAIN | ~900-960 | Проблемы от санитарных сбоев |
| PLANNING | ~962-1012 | Плановое vs аварийное внедрение |
| COMPARISON | ~1014-1060 | Ozonator vs Система Ozonbox |
| RESULTS | ~1062-1127 | Что получит клиент |
| LEVELS | ~1128-1259 | 3 пакета внедрения (1.2М-5.5М) |
| EQUIPMENT | ~1261-1369 | Каталог оборудования |