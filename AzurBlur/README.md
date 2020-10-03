# Azur Blur CSS theme for MyAnimeList

MyAnimeList Forum: https://myanimelist.net/forum/?topicid=1868018

Design and Code by MurakumoJP.

## Preview
![Screenshot](AzurBlur.jpg?raw=true)

## Features

* Supports anime
* Uses MAL Modern Theme

## ► Installation and Settings

To configure it, open the next page and check the boxes as shown in the screenshot below.

https://myanimelist.net/editprofile.php?go=listpreferences

![Screenshot](Settings/AnimeListSettings.jpg?raw=true)

After setting up, go to the style settings page.

https://myanimelist.net/ownlist/style

After setting up the list, go to the List style Design page and move the slider from Classic to Modern.

![Screenshot](preview/ListSettings/StyleEdit.png?raw=true)

Go to your list style editing page, and turn off these options.

https://myanimelist.net/ownlist/style/theme/1
![Screenshot](Settings/BgOff.jpg?raw=true)

You can upload a cover image of any height and width.

On the same page, open the add custom CSS field and paste the code that is listed below.

```css
@\import "https://malscraper.azurewebsites.net/covers/auto/presets/dataimagelinkafter";
@\import "https://murakumo-jp.github.io/MyAnimeList-CSS/AzurBlur/Style_min.css";
```

