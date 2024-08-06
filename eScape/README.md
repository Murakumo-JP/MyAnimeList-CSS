# eScape CSS Theme for MyAnimeList

● Design and Code by MurakumoJP.

## ☆ Preview

![Screenshot](eScape.jpg?raw=true)

## ☆ Features

* Supports Anime/Manga
* Uses MAL Modern Theme

## ☆ Anime List Settings

- [ ] ☆ Common
    - [X] Numbers
    - [X] Score
    - [X] Type
    - [X] Episodes
    - [X] Tags
- [ ] ☆ Modern Only
    - [X] Image
    - [X] Premiered
    - [X] Studios

## ☆ Layout Code

```css
@\import "https://malscraper.azurewebsites.net/covers/auto/presets/dataimagelinkafter";
@\import "https://murakumo-jp.github.io/MyAnimeList-CSS/eScape/Style.min.css";
```

* Edit Background

```css
:root {
  --body-bg: url("Your link to the images");
}
```


## ☆ Censorship Hentai

```css
@\import "https://murakumo-jp.github.io/MALCensorship/R18Cover.min.css";
```