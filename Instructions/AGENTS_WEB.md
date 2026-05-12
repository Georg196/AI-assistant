# AGENTS.md — Web правила (HTML/CSS/JS, production-ready)

## Общие принципы

- **Простота превыше всего** — минимальное усложнение, которое не даёт ценности, не стоит того.
- Сначала думай → потом кодь (Think Before Coding).
- Явно проговаривай предположения и trade-offs.
- Делай **хирургические изменения** — минимум диффа.
- Читаемость и простота > «умный» код.
- Сначала рабочий код → потом рефакторинг и улучшения.

## Поиск информации

- Используй `context7` MCP для изучения документации библиотек.
- Используй `websearch` для актуальных решений.

## Стек (2026)

### CSS/Дизайн
- **Tailwind CSS v4** — утилитарный CSS для кастомных дизайнов
- **Bootstrap 5.3** — готовые компоненты, grid, утилиты
- **daisyUI** — компоненты на Tailwind (опционально)
- **Bootstrap Icons** — иконки к Bootstrap
- **Animate.css** — простые CSS анимации
- **AOS** — scroll-reveal анимации
- **GSAP** — сложные timeline, scroll-triggered
- **Lenis** — плавный скролл

### JavaScript
- **Vanilla JS** — предпочитай без фреймворка для статики
- **ES Modules** — современный import/export
- **PostCSS** — обработка CSS
- **cssnano** — минификация CSS

### Линтинг/Форматирование
- **ESLint** — JS линтинг
- **Prettier** — форматирование (HTML, CSS, JS, JSON)
- **Stylelint** — CSS линтинг
- **HTML-validate** — валидация HTML

### Сборка
- **Tailwind CLI** — компиляция Tailwind
- **PostCSS CLI** — обработка PostCSS

## Код-стиль

### HTML
- Семантические теги (`<header>`, `<main>`, `<section>`, `<footer>`)
- Доступность (ARIA-labels, alt на картинках, focus-visible)
- `<!DOCTYPE html>`, `<html lang="ru">`, viewport meta

### CSS
- CSS Custom Properties (variables) для темы
- Mobile-first подход (`@media (min-width: ...)`)
- ≤ 80 символов в строке
- Комментарии на русском/английском
- Tailwind utilities + кастомные стили в отдельном файле

### JavaScript
- ES6+ (`const`, `let`, arrow functions, template literals)
- Деструктуризация, optional chaining (`?.`)
- Модули (`<script type="module">`)
- `document.addEventListener('DOMContentLoaded', ...)`
- Никаких `var`, `eval()`

### Именование
- CSS: kebab-case (`.hero-section`, `.btn-primary`)
- JS: camelCase для переменных, kebab-case для data-атрибутов
- Файлы: kebab-case (`.btn-primary`, `main-menu.js`)

## Структура проекта

```
project/
├── src/
│   ├── css/
│   │   ├── styles.css          # Tailwind входной файл
│   │   ├── components.css      # Компоненты
│   │   └── custom.css          # Кастомные стили
│   ├── js/
│   │   ├── main.js             # Главный JS
│   │   ├── components/        # JS модули
│   │   └── utils/             # Утилиты
│   └── img/                    # Исходные изображения
├── dist/                       # Продакшн файлы
├── index.html
├── package.json
├── tailwind.config.js
├── postcss.config.js
├── .eslintrc.json
├── .prettierrc
├── .stylelintrc
└── README.md
```

## Хорошие практики

- Responsive дизайн (mobile-first)
- Lazy loading изображений (`loading="lazy"`)
- предзагрузка критических ресурсов
- Минификация CSS/JS для продакшна
- CSS variables для темы ( легко менять цвета)
- BEM-подобное именование для кастомных компонентов

## Запрещено

- `innerHTML` без sanitization
- `document.write()`
- Inline стили (кроме динамических)
- `!important` без веской причины
- Глубокая вложенность селекторов (> 3 уровня)
- Синхронные скрипты в `<head>` без `defer`

## Анимации

- Анимируй только `transform` и `opacity` (GPU-ускорение)
- GSAP для сложных timeline
- AOS/Animate.css для простых scroll-reveal
- `prefers-reduced-motion` support
- will-change только для активных анимаций

## Оптимизация

- Image optimization (WebP, responsive srcset)
- CSS purging (Tailwind удаляет неиспользуемое)
- Critical CSS inline
- Fonts preconnect + font-display: swap

## Workflow с AI (Claude/GPT)

1. Проанализируй дизайн-макет или требования
2. Создай структуру проекта
3. Настрой зависимости
4. Напиши рабочую HTML/CSS/JS версию
5. Проверь валидатором и линтерами
6. Оптимизируй (минификация, изображения)
7. Протестируй (разные размеры экранов)

## Команды сборки

```bash
# Установка зависимостей
npm install

# Development (watch mode)
npm run dev

# Production build
npm run build

# Линтинг
npm run lint:css
npm run lint:js

# Форматирование
npm run format

# Валидация HTML
npm run validate
```