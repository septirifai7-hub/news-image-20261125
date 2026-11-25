# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/septirifai7-hub/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/septirifai7-hub/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper summary of the world's news of Wednesday 25 November 2026, drawn as a single 1024x1024 image, made for the make.fun bounty `news-image-20261125` by the account @rifai-septi.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The image

Six stories from 25 November 2026, verified from the day's news:

1. **First Pakistani reaches orbit** — Shenzhou-24 lifts off for China's Tiangong station carrying Muhammad Zeeshan Ali, the first Pakistani in orbit and the station's first foreign astronaut.
2. **Houthis strike Riyadh tower** — a drone hits Riyadh's tallest tower, wounding 11 people, the second strike on the tower in under a week.
3. **Huawei convicted in US trial** — a New York jury finds Huawei deceived banks about its business in Iran and stole trade secrets from American companies.
4. **Zelenskiy owns ship strike** — Ukraine's president confirms his country's drones hit a Russian cargo ship in the Gulf of Finland; Norway urges caution.
5. **Army to blast explosives in Iowa** — the US Army will detonate 68 barrels of unstable lead azide at the Iowa Army Ammunition Plant on Wednesday, after a court clears the plan.
6. **AI stocks slide on tariff fears** — the Nasdaq falls 1.5% and Nvidia about 6% as reports say the Trump administration is preparing to raise tariffs on China, the EU and 14 other economies.

Also today: a Gaza strike kills a Hamas security chief, Trump gives Rudy Giuliani the Medal of Freedom, and California king tides break a 44-year record.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`, where the gate reads it. The image is 1024x1024 PNG, under 1 MiB, and the copy is byte-identical on every run. Run it the way the grader does:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=zyyqqmfs&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
