# Память нашего общения

## Сессия 4 — 14.05.2026 (ПОЛНАЯ СЕССИЯ)

### Что сделано сегодня:

#### 1. OpenShorts запуск
- Frontend: http://localhost:5173
- Backend: `python -m uvicorn app:app --port 8000`
- Проблема: серверы падают при перезапуске, нужно переоткрывать терминал

#### 2. Пользователь хотел сделать шортс видео
- Видео: `C:\Users\Admin\Downloads\Telegram Desktop\IMG_0788.MP4`
- Цель: мужик с озонатором говорит про микробы и загрязнение воздуха
- OpenShorts НЕ умеет в voice replacement/lip sync — это отдельные инструменты
- Пользователь отменил задачу

#### 3. Изучены и установлены репозитории:
| Репозиторий | Stars | Статус |
|-------------|-------|--------|
| get-shit-done | 62k | ✅ Установлен в `~/.claude/skills/gsd-*/` |
| superpowers | 191k | ✅ plugin в opencode.json |
| reversa | 774 | ⚠️ Интерактивный установщик не работает |
| ralphex | 1.1k | ✅ `go install` |
| hermes-agent | 150k | ✅ `uv tool install` |
| free-claude-code | 24k | ✅ `uv tool install` |

#### 4. Multi-agent система
Создано 4 субагента в `.opencode/agent/`:
- `web-dev.md` — HTML, CSS, Tailwind, лендинги
- `python-dev.md` — FastAPI, боты, видеообработка
- `researcher.md` — анализ рынка, конкуренты
- `designer.md` — UI/UX, стилизация

#### 5. MCP серверы (8 штук)
Добавлены в `opencode.json`:
- `filesystem` — доступ к companies/ и openshorts/
- `everything` — поиск по всему
- `sequential-thinking` — последовательное мышление
- `webresearch` — web-исследования
- `npm-helper` — NPM помощник
- `npm-sentinel` — NPM безопасность
- `playwright` — browser automation
- `context7` — уже был (документация)

#### 6. Скиллы (23 штуки)
- **Дизайн:** canvas-design, image-enhancer, theme-factory, artifacts-builder, brand-guidelines
- **Документы:** xlsx, pdf, docx, pptx
- **Маркетинг:** competitive-ads-extractor, lead-research-assistant, content-research-writer, domain-name-brainstormer, internal-comms
- **Организация:** invoice-organizer, meeting-insights-analyzer

### Команды установленных инструментов:
- `hermes` — Hermes Agent
- `fcc-server` — Free Claude Code proxy
- `fcc-claude` — Claude Code через proxy
- `ralphex` — autonomous plan execution

### Проекты в работе:
1. **Ozonbox** — лендинг для агрохолдинга
2. **OpenShorts** — AI-генератор шортсов
3. **Open Design** — AI-дизайн инструмент

---

*Обновляй этот файл после каждой значимой сессии*

### Контекст проекта
- Проект: Лендинг Ozonbox для агрохолдинга
- Стек: Tailwind CSS v4, GSAP, AOS, Lenis, Bootstrap 5.3

### Ключевые решения
- Решено перенести все AGENTS файлы в папку Instructions для централизации
- Создан этот файл памяти для долгосрочного контекста

### Выполнено
- AGENTS файлы перенесены в Instructions/
- Обновлены ссылки в корневом AGENTS.md
- Исправлены ссылки в Instructions/AGENTS.md (было docs/)
- Удалены дубликаты из корня (AGENTS_WEB.md, AGENTS_D.md)
- Установлены дизайн-скилы:
  - canvas-design — визуальное искусство
  - image-enhancer — улучшение изображений
  - theme-factory — темы для артефактов
  - artifacts-builder — HTML компоненты
  - brand-guidelines — брендовые стили
- Установлены дизайн-скилы из awesome-opencode-skills:
  - canvas-design
  - image-enhancer
  - theme-factory
  - artifacts-builder
  - brand-guidelines

### 12.05.2026 — Скилы для анализа данных и маркетинга
- document-skills: xlsx, pdf, docx, pptx
- Маркетинг: competitive-ads-extractor, lead-research-assistant, content-research-writer, domain-name-brainstormer, internal-comms
- Организация: invoice-organizer, meeting-insights-analyzer

**Всего установлено 23 скила**

### Заметки

### 12.05.2026 — Логи работы (перенесены в память 14.05.2026)

#### [2026-05-12] init | Структура wiki создана

#### [2026-05-12] research | Глубокое исследование Ozonbox
- Изучен сайт ozonbox.pro (страницы: О нас, Каталог, Зернохранилища)
- Создано резюме компании с анализом рынка и конкурентов
- Добавлены статьи: технология холодной генерации, озонирование зернохранилищ
- Загружен скилл content-research-writer для научной работы

#### [2026-05-12] catalog | Изучен каталог продукции
- Изучены категории: Озонаторы Air, UV системы, Шкафы, Нейтрализаторы
- Собрана информация о пищевых производствах (полный разбор решения)
- Создан подробный каталог оборудования (8 категорий, серии, применение)
- Составлены отраслевые решения (10 отраслей)

### 12.05.2026 — Структура для мульти-компаний
- Создана папка `companies/` с шаблоном
- Структура: `[slug]/company-info.md` + `projects/` + `context/`
- **Все файлы Ozonbox перемещены в `companies/ozonbox/`**

---

## Сессия 2 — 14.05.2026

### Запрос пользователя
Пользователь попросил создать базу данных для хранения истории общения, чтобы я "помнил все о чем мы с тобой говорим и что ты мне отвечаешь".

### Действие
Обновлён файл `Instructions/memory.md` — это и есть база данных нашего общения.

### Структура памяти
- Хронологические сессии с датами
- Контекст проекта (лендинг Ozonbox)
- Ключевые решения и выполненные задачи
- Важные заметки

### Формат ведения записей
После каждой значимой сессии добавляю:
1. Дату и номер сессии
2. Запрос пользователя
3. Что сделано
4. Важные детали для контекста

## Сессия 3 — 14.05.2026 (часть 2)

### Изучены репозитории
1. **get-shit-done** (62k stars) — meta-prompting система для Claude Code/OpenCode
2. **superpowers** (191k stars) — agentic skills framework + методология
3. **reversa** (774 stars) — reverse engineering фреймворк для legacy систем
4. **ralphex** (1.1k stars) — autonomous plan execution с Claude Code

### Установлено
- ✅ **get-shit-done**: Установлен в `~/.claude/skills/gsd-*/`
- ✅ **superpowers**: Добавлен в `opencode.json` plugin
- ⚠️ **reversa**: Интерактивный установщик не работает в терминале
- ⚠️ **ralphex**: Требует Go для сборки

### OpenShorts
- Frontend запущен на http://localhost:5173
- Backend: `python -m uvicorn app:app --port 8000`

### Установлены агенты
- **hermes-agent** (150k stars) — uv tool install, self-improving AI agent
- **free-claude-code** (24k stars) — fcc-server, Claude Code прокси

### Добавлены MCP серверы
- `filesystem` — доступ к companies/ и openshorts/
- `everything` — поиск по всему
- `sequential-thinking` — последовательное мышление
- `webresearch` — web-исследования
- `npm-helper` — NPM помощник
- `npm-sentinel` — NPM безопасность
- `playwright` — browser automation

### Репозитории изучены сегодня
1. **hermes-agent** (150k stars)
2. **free-claude-code** (24k stars)
3. **get-shit-done** (62k stars)
4. **superpowers** (191k stars)
5. **reversa** (774 stars)
6. **ralphex** (1.1k stars)

---

## Сессия 3 — 14.05.2026

### Запуск OpenShorts
- Запущены серверы: frontend (:5173), backend (:8000)
- Возникли проблемы с перезапуском — нужно переоткрывать терминал

### Настройка Multi-agent системы
Создано 4 субагента в `.opencode/agent/`:

| Агент | Назначение |
|-------|------------|
| `web-dev.md` | HTML, CSS, Tailwind, лендинги |
| `python-dev.md` | Python: FastAPI, боты, видеообработка, OpenShorts |
| `researcher.md` | Анализ рынка, конкуренты, маркетинг |
| `designer.md` | UI/UX, стилизация, компоненты |

Обновлён `opencode.json` с конфигурацией агентов.

---

*Обновляй этот файл после каждой значимой сессии*