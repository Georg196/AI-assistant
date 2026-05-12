# Структура проекта Ozonbox

## Быстрый старт

### Лендинг Ozonbox
```bash
npm install        # Установка зависимостей
npm run dev        # Development с watch
npm run build      # Production build
```

### Open Design (AI-дизайн)
```bash
cd open-design
pnpm install --link-workspace-packages=true
pnpm tools-dev run web
```

---

## Структура файлов

```
агрохолдинги/
├── index.html              # Главная страница (1395 строк, inline CSS)
├── package.json            # Зависимости npm
├── src/
│   ├── css/
│   │   └── styles.css      # Tailwind входной файл + @theme переменные
│   └── js/
│       └── main.js         # GSAP, AOS, Lenis инициализация
├── dist/
│   └── styles.css          # Скомпилированный CSS (из src/css)
├── open-design/            # Клонированный репозиторий Open Design
│   ├── apps/
│   │   ├── daemon/         # Локальный сервер (Express + SQLite)
│   │   ├── web/            # Next.js веб-интерфейс
│   │   ├── desktop/        # Electron shell
│   │   └── packaged/       # Packaged runtime
│   ├── skills/             # 31 навык дизайна
│   ├── design-systems/      # 72 дизайн-системы
│   └── tools/
│       ├── dev/            # Lifecycle control
│       └── pack/           # Packaged build
├── .AGENTS.md              # Python правила (aiogram)
├── AGENTS_D.md             # UI/UX правила
└── AGENTS_WEB.md           # Web правила (HTML/CSS/JS)
```

---

## Ключевые секции index.html

| Секция | Описание | Строка |
|--------|----------|--------|
| HERO | Главный баннер + статистика | ~843-898 |
| PAIN | Проблемы от санитарных сбоев | ~900-960 |
| PLANNING | Плановое vs аварийное внедрение | ~962-1012 |
| COMPARISON | Ozonator vs Система Ozonbox | ~1014-1060 |
| RESULTS | Что получит клиент | ~1062-1127 |
| LEVELS | 3 пакета внедрения (1.2М-5.5М) | ~1128-1259 |
| EQUIPMENT | Каталог оборудования | ~1261-1369 |

---

## Цветовая схема

```css
--primary: #1F32BF       /* Синий основной */
--primary-light: #2E4AE0
--accent: #00B4D8       /* Голубой акцент */
--accent-dark: #0284C7
--accent-green: #10B981  /* Зеленый успех */
--accent-orange: #F59E0B /* Оранжевый предупреждение */
--accent-red: #EF4444    /* Красный опасность */
--dark: #0D1117          /* Темный фон */
```

---

## Попапы Tilda

Для интеграции с Tilda использовать ссылки:
- `#zv1` — Оставить заявку
- `#zv6` — Рассчитать
- `#zvonok3` — Заказать звонок
- `#popup:myform1` — Получить решение
- `#popup:myform3` — Консультация