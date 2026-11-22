# Summit Planner

Learning project: a phone app that takes a position and a date and returns a ski-touring route, best start time and a personal summit chance, using my own ML models trained on raw weather and terrain data. Official avalanche bulletins are only used as labels for training and grading, never as model input.

## Status

Week 1: daily data pipeline. `src/save_daily.py` runs every day on GitHub Actions and saves that day's avalanche bulletins to `data/raw/<date>/`.

## Repo layout

```
src/save_daily.py                    daily download script (run by GitHub Actions)
.github/workflows/save_daily.yml     schedule: every day 09:47 UTC
explore/explore.py                   messy experiments
data/raw/<date>/<region>.json        raw bulletins, kept forever
```

## Data source

EAWS bulletin mirror, no API key, daily files since 2021-01-25:
`https://static.avalanche.report/eaws_bulletins/<DATE>/<DATE>-<REGION>.json`

- `<DATE>` is the day the bulletin is **valid for** (checked: the 2026-03-01 FR file has `mainDate: 2026-03-01`, published 2026-02-28 16:00).
- Unofficial mirror, no licence file found. Raw files are saved daily in case it disappears.
- Off-season the file simply doesn't exist (HTTP 404). The script skips it and continues.

## Region IDs

| Region | File | ID(s) | How found |
|---|---|---|---|
| Riksgränsen (Abisko/RGN Väst) | SE.json | SE-15 | `SE.json` has only IDs; names are in `SE.raw.json` (raw `area_id` N = SE-N) |
| Abisko/RGN Öst | SE.json | SE-16 | same |
| Courmayeur – Val Ferret | IT-23.json | IT-23-AO-14 | names in `IT-23.json` → `bulletins[].regions[]` |
| Courmayeur – Val Veny | IT-23.json | IT-23-AO-22 | same |
| Mont-Blanc | FR.json | FR-03 | `FR.json` has 36 IDs (FR-01…FR-23, FR-40, FR-41, FR-64…FR-74), no names; FR-NN matches Météo-France massif number NN (3 = Mont-Blanc, 6 = Haute-Tarentaise). Not yet verified against names. |
| Haute-Tarentaise | FR.json | FR-06 | same |

Other Swedish IDs: SE-01 V. Vindelfjällen, SE-03 S. Jämtlandsfjällen, SE-07 V. Härjedalsfjällen, SE-08 Kebnekaisefjällen, SE-09 S. Lapplandsfjällen.

#	Point |	Lat	| Lon	| Height	
1	 Riksgränsen station	| 68.4258	| 18.1273	| 521
2	 Riksgränsfjället (top lift)	| 68.4278	| 18.1222	| 909	
3  Nordalsfjället	| 68.4065	| 18.0893	| 1051
4	 Chamonix	| 45.9231	| 6.8697	| 1035
5	 Plan de l'Aiguille	| 45.9016	| 6.8849	| 2317
6	 Mont Blanc	| 45.8328	| 6.8650	| 4800	
7	 Val d'Isère	| 45.4480	| 6.9802	| 1850	
8	 Rocher de Bellevarde	| 45.4452	| 6.9511 | 2827	
9	 Grande Casse	| 45.4051	| 6.8276	| 3800	
10 Courmayeur	| 45.7966	| 6.9689	|1200	
11	Pavillon du Mont Fréty	| 45.8291	| 6.9509	| 2173	
12	Punta Helbronner	| 45.8458	| 6.9317	| 3462	
