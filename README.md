# The World Today — 23 November 2026 in one image

Entry for the make.fun bounty **"Sum up 23 November's world news in one image"**
(news-image-20261123).

## What it is

A newspaper-front-page poster (1024×1024 PNG, under 1 MiB) that sums up the
world news of Monday 23 November 2026:

- **Lead story:** COP31 collapses in Antalya — nearly 200 nations leave with no
  climate pact after the EU and ~130 countries reject a text without a
  fossil-fuel phase-out.
- **Ukraine:** Russian strikes kill 11 in the Kyiv region; homes destroyed in
  Dymer; a Russian cargo ship hit by a drone burns in the Gulf of Finland.
- **Washington:** Democrats clinch a historic House majority of at least 258
  seats, the largest since 1992.
- **Iran:** Trump warns of new strikes; Tehran in "neither war nor peace" as
  Hormuz shipping attacks hit their highest level since the war began.
- **Indonesia:** candy-factory fire in Banten — 3 dead, 36 missing.
- **Ticker:** drones hit a UN building in Khartoum; WHO pleads for peace near
  Congo's Ebola zone; South Korea's education chief quits over AI cheating;
  BepiColombo reaches Mercury.

Headlines were cross-checked across multiple international news outlets
reporting on 23 November 2026 (Economic Times, SCMP, Manila Times / AFP,
Arab News, UN News summaries).

## How to run

```bash
python3 main.py   # writes /output/entry.png
```

`main.py` (Python 3.13, standard library only) copies the bundled poster
`assets/entry.png` to `/output/entry.png`. No network; every run writes
identical bytes.

## How the poster was made

`build_poster.py` composes the front page with Pillow: an original
AI-generated editorial illustration (cracked globe between an empty climate
summit hall and a war-damaged city, in `assets/`) plus typeset headlines.
Re-running it reproduces the same poster.
