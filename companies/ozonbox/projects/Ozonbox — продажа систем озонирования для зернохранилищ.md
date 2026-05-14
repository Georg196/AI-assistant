# 🖥️ Лендинг Ozonbox

## Описание
Одностраничный лендинг для агрохолдинга Ozonbox — продажа систем озонирования для зернохранилищ.

## Статус
🟢 Активен

## Стек
- Tailwind CSS v4
- GSAP (анимации)
- AOS (scroll-animations)
- Lenis (smooth scroll)
- Bootstrap 5.3

## Структура проекта
```
агрохолдинги/
├── index.html
├── package.json
├── src/css/styles.css
├── src/js/main.js
├── dist/
└── open-design/
```

## Секции лендинга
| Секция | Строки | Описание |
|--------|--------|----------|
| HERO | ~843-898 | Главный баннер + статистика |
| PAIN | ~900-960 | Проблемы от санитарных сбоев |
| PLANNING | ~962-1012 | Плановое vs аварийное |
| COMPARISON | ~1014-1060 | Ozonator vs Ozonbox |
| RESULTS | ~1062-1127 | Что получит клиент |
| LEVELS | ~1128-1259 | 3 пакета (1.2М-5.5М) |
| EQUIPMENT | ~1261-1369 | Каталог оборудования |

## Команды
```bash
npm run dev    # Development с watch
npm run build  # Production build
```

## Инструкции
- `Instructions/AGENTS_WEB.md` — Web правила
- `Instructions/AGENTS_DESIGN.md` — UI/UX правила

## TODO
- [ ] Собрать информацию о компании
- [ ] Добавить контакты
- [ ] Проработать УТП