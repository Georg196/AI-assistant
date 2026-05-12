# AGENTS.md — Агрохолдинги проект

## Структура

```
агрохолдинги/
├── index.html              # Лендинг Ozonbox (1395 строк)
├── package.json            # npm зависимости
├── src/
│   ├── css/
│   │   └── styles.css      # Tailwind входной файл
│   └── js/
│       └── main.js         # GSAP + AOS + Lenis
├── dist/                   # Скомпилированный CSS
├── open-design/            # AI-дизайн инструмент
├── PROJECT_STRUCTURE.md    # Подробная структура
├── .AGENTS.md              # Python правила
├── AGENTS_D.md             # UI/UX правила
└── AGENTS_WEB.md          # Web правила
```

## Быстрые команды

### Лендинг
```bash
npm run dev    # Development
npm run build  # Production
```

### Open Design
```bash
cd open-design
pnpm install --link-workspace-packages=true
pnpm tools-dev run web
```

## Ключевые файлы

| Файл | Назначение |
|------|------------|
| `index.html:843-898` | HERO секция |
| `index.html:900-960` | PAIN проблемы |
| `index.html:1014-1060` | Сравнение Ozonator vs Ozonbox |
| `src/css/styles.css` | CSS переменные + Tailwind |
| `src/js/main.js` | Анимации GSAP/AOS/Lenis |

## Правила

1. **Лендинг** → `AGENTS_WEB.md`
2. **Дизайн** → `AGENTS_D.md`
3. **Python/боты** → `.AGENTS.md`
4. **Open Design** → запускать из `open-design/`