---
title: Ozonbox Design System
type: design-system
version: 1.0
created: 2026-05-14
industry: industrial-equipment
target: b2b-agro
---

# Ozonbox Design System

## 1. Visual Theme & Atmosphere

Промышленный B2B-стиль для агрохолдингов. Техническая эстетика, точность, надёжность.

**Tone:** Professional, industrial, trustworthy
**Density:** Comfortable, data-rich but scannable
**Mood:** Clean industrial precision, не перегружено

## 2. Color Palette & Roles

### Primary Colors

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Deep Blue | `#1F32BF` | CTAs, links, headers |
| Primary Light | Electric Blue | `#2E4AE0` | Hover states |
| Primary Dark | Navy | `#141A6E` | Footer, backgrounds |

### Accent Colors

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Accent | Cyan | `#00B4D8` | Highlights, icons |
| Accent Dark | Ocean | `#0284C7` | Secondary actions |
| Success | Emerald | `#10B981` | Positive stats, success |
| Warning | Amber | `#F59E0B` | Warnings |
| Error | Red | `#EF4444` | Errors, critical |

### Neutrals

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Dark | Charcoal | `#0D1117` | Text, headers |
| Dark Alt | Slate | `#1A1A2E` | Cards, sections |
| Gray Dark | Steel | `#374151` | Body text |
| Gray | Concrete | `#6B7280` | Secondary text |
| Gray Light | Mist | `#9CA3AF` | Placeholders |
| Border | Line | `#E5E7EB` | Dividers |
| Background | White | `#FFFFFF` | Main bg |
| Background Alt | Cloud | `#F9FAFB` | Section bg |

## 3. Typography

### Font Stack

```css
--font-main: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
--font-display: 'IBM Plex Sans', sans-serif;
--font-mono: 'IBM Plex Mono', monospace;
```

### Type Scale

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| H1 | 48px (clamp 32-48px) | 700 | 1.25 |
| H2 | 36px (clamp 26-36px) | 700 | 1.25 |
| H3 | 22px (clamp 18-22px) | 600 | 1.4 |
| H4 | 18px | 600 | 1.4 |
| Body Large | 18px | 400 | 1.6 |
| Body | 16px | 400 | 1.6 |
| Body Small | 14px | 400 | 1.5 |
| Caption | 12px | 500 | 1.4 |

### Type Treatment

- **Headings:** Letter-spacing: -0.02em
- **Body:** Normal tracking
- **Monospace:** For technical specs, numbers

## 4. Component Stylings

### Buttons

```css
/* Primary */
--btn-primary-bg: #1F32BF;
--btn-primary-color: #FFFFFF;
--btn-primary-radius: 4px;
--btn-primary-padding: 14px 24px;

/* Secondary */
--btn-secondary-bg: transparent;
--btn-secondary-border: 2px solid #1F32BF;
--btn-secondary-color: #1F32BF;

/* Accent */
--btn-accent-bg: #00B4D8;
--btn-accent-color: #FFFFFF;
```

### Cards

- Background: `#FFFFFF`
- Border: 1px solid `#E5E7EB`
- Border-radius: 8px
- Shadow: `0 1px 3px rgba(0,0,0,0.08)`
- Padding: 24px

### Form Inputs

- Height: 48px
- Border: 1px solid `#E5E7EB`
- Border-radius: 4px
- Focus: 2px solid `#1F32BF`
- Padding: 12px 16px

## 5. Layout Principles

### Container

```css
--container-max: 1160px;
--container-padding: 20px;
```

### Grid

- 12-column grid
- Gap: 24px (mobile), 32px (desktop)
- Section spacing: 80px (mobile), 120px (desktop)

### Spacing Scale

| Token | Value |
|-------|-------|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 32px |
| 2xl | 48px |
| 3xl | 64px |
| 4xl | 96px |

## 6. Depth & Elevation

```css
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
--shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);
--shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
--shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.15);
```

### Layering

- Background: z-index -1
- Default content: z-index 1
- Sticky header: z-index 100
- Modal: z-index 1000

## 7. Do's and Don'ts

### Do

- ✅ Использовать IBM Plex Sans для читаемости
- ✅ Синие акценты для доверия B2B
- ✅ Чёткая типографика для технических данных
- ✅ Достаточно whitespace для scanability
- ✅ Контрастные CTAs для конверсии

### Don't

- ❌ Избыточные градиенты (не фотореалистичный)
- ❌ Много анимаций (промышленный tone)
- ❌ Декоративные элементы без функции
- ❌ Яркие пёстрые цвета (не B2C)
- ❌ Мелкий текст (техническая аудитория читает specs)

## 8. Responsive Behavior

### Breakpoints

```css
--mobile: 576px;
--tablet: 768px;
--desktop: 992px;
--wide: 1200px;
```

### Touch Targets

- Minimum: 44px × 44px
- Button padding: 14px 24px minimum

### Collapsed Navigation

- Mobile: Hamburger menu
- Tablet: Condensed nav
- Desktop: Full nav

## 9. Agent Prompt Guide

Для генерации страниц в стиле Ozonbox:

```
Используй дизайн-систему Ozonbox:
- Primary: #1F32BF (Deep Blue)
- Accent: #00B4D8 (Cyan)
- Font: IBM Plex Sans
- Стиль: Промышленный B2B, технический, точный
- Компоненты: карточки с тенями, кнопки с radius 4px
```

---

## Related Files

- [[wiki/entities/Ozonbox|Ozonbox — компания]]
- [[wiki/summaries/Ozonbox-исследование|Deep Research]]
- [[Страницы/агрохолдинг.html|Landing Page]]