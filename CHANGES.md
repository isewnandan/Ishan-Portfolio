# Wat is er gewijzigd

## ✅ Bestandsnamen aangepast

Alle 5 project-pagina's zijn hernoemd naar `index.html`:

| Voor | Na |
|---|---|
| `projects/logistics-monitor/logistics.html` | `projects/logistics-monitor/index.html` |
| `projects/housing-forecast/housing.html` | `projects/housing-forecast/index.html` |
| `projects/energy-optimizer/energy.html` | `projects/energy-optimizer/index.html` |
| `projects/churn-prediction/churn.html` | `projects/churn-prediction/index.html` |
| `projects/labour-market/labour.html` | `projects/labour-market/index.html` |

Hierdoor werken de links in de homepage automatisch (die linkten al naar `projects/<naam>/index.html`).

## ✅ Top nav-links gefixed (alle 5 pagina's)

```html
<!-- Voor -->
<a href="index.html" class="nav-id">
<a href="index.html" class="nav-back">

<!-- Na -->
<a href="../../index.html" class="nav-id">
<a href="../../index.html" class="nav-back">
```

## ✅ Prev/Next footer-links gefixed (4 pagina's met footer)

| Pagina | Previous | Next |
|---|---|---|
| **001** logistics-monitor | (geen prev/next, alleen "Back to portfolio") | |
| **002** housing-forecast | `../logistics-monitor/index.html` | `../energy-optimizer/index.html` |
| **003** energy-optimizer | `../housing-forecast/index.html` | `../churn-prediction/index.html` |
| **004** churn-prediction | `../energy-optimizer/index.html` | `../labour-market/index.html` |
| **005** labour-market | `../churn-prediction/index.html` | `../../index.html` (homepage) |

## ✅ Wat NIET gewijzigd is

- De homepage (`index.html` in root) — die linkte al correct
- Alle styling, content, secties, animaties op alle pagina's
- Alle notebooks en data-bestanden

## 🧪 Test checklist

Open de root `index.html` met Live Server in VSCode en test:

1. Klik elk van de 5 projecten op de homepage → moet de juiste pagina openen
2. Op elke project-pagina, klik linksboven "Back to portfolio" → terug naar homepage
3. Op pagina 002, 003, 004 → klik "Previous project" en "Next project" → moet door alle pagina's heen kunnen
4. Op pagina 005 → "Next" gaat terug naar homepage
5. Op pagina 001 → alleen "Back to portfolio" knop (geen prev/next, dat is design-keuze)

## 🚀 Naar Vercel

Na lokaal testen:

```bash
git add .
git commit -m "Fix: nav links between project pages"
git push
```

Vercel deployt automatisch. URLs worden netjes:
- `ishan-portfolio.vercel.app/projects/logistics-monitor/`
- `ishan-portfolio.vercel.app/projects/housing-forecast/`
- enz.

(Dankzij `index.html` hoeft de bestandsnaam niet eens in de URL te staan.)
