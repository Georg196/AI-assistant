# Ozonbox — производство инженерных систем очистки и обеззараживания

## О проекте

Лендинг для компании Ozonbox — система управления санитарными процессами в десятках отраслях

## Технологии

- **HTML5** + семантическая разметка
- **Tailwind CSS v4** — утилитарный CSS
- **Bootstrap 5.3** — компоненты и grid
- **Vanilla JavaScript** — ES6+
- **GSAP** — анимации
- **AOS** — scroll-reveal
- **PostCSS** — обработка CSS
- **ESLint/Prettier/Stylelint** — линтинг и форматирование

## Структура

```
├── src/
│   ├── css/
│   │   └── styles.css      # Tailwind входной файл
│   └── js/
│       └── main.js         # Главный скрипт
├── dist/                   # Продакшн файлы
├── index.html             # Главная страница
├── package.json
└── *.config.js            # Конфиги линтеров
```

## Команды

```bash
# Установка зависимостей
npm install

# Development (с watch)
npm run dev

# Production build
npm run build

# Линтинг CSS
npm run lint:css

# Линтинг JS
npm run lint:js

# Форматирование
npm run format

# Валидация HTML
npm run validate
```

## Разработка

1. Клонировать репозиторий
2. `npm install`
3. `npm run dev` — запустить watch mode
4. Редактировать файлы в `src/`
5. Результат в `dist/styles.css`

## Продакшн

```bash
npm run build  # Минификация CSS
```

## Зависимости

### Core
- `tailwindcss@4.0` — CSS framework
- `bootstrap@5.3` — UI components
- `bootstrap-icons` — иконки

### Анимации
- `gsap` — timeline анимации
- `aos` — scroll-reveal
- `animate.css` — CSS анимации

### Утилиты
- `@fontsource/ibm-plex-sans` — шрифт
- `lenis` — плавный скролл

### Dev
- `eslint` — JS linting
- `prettier` — форматирование
- `stylelint` — CSS linting
- `postcss` — CSS processing
- `autoprefixer` — vendor prefixes
- `cssnano` — минификация