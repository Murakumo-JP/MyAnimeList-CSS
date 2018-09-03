# Eorzea Collection CSS theme for MyAnimeList

Original page design from http://ffxiv.eorzeacollection.com/ by Edeon Vails.

List CSS and adaption by MurakumoJP.

## Preview
https://myanimelist.net/animelist/MurakumoJP

![Screenshot](Eorzea_Collection/preview/Snapshot.png?raw=true)

## Features

* Supports anime and manga
* Uses MAL Modern Theme
* All controls still in place and fully functional

## List Settings
On the List page, do the following.
https://myanimelist.net/editprofile.php?go=listpreferences

Anime List

![Screenshot](Eorzea_Collection/preview/ListSettings/AnimeList.png?raw=true)

Manga List

![Screenshot](Eorzea_Collection/preview/ListSettings/MangaList.png?raw=true)

After setting the list, go to the list Style Design page and move the slider from classic to modern.
https://myanimelist.net/ownlist/style

![Screenshot](Eorzea_Collection/preview/ListSettings/StyleEdit.png?raw=true)

Go to your list style editing page, and turn off these options.
https://myanimelist.net/ownlist/style/theme/1
![Screenshot](https://i.imgur.com/1pVzKRM.png?raw=true)

On the same page, in the Add Custom CSS field, paste the code shown below.

```css
@import "https://malscraper.azurewebsites.net/covers/auto/presets/dataimagelinkafter";
@import "https://murakumo-jp.github.io/MyAnimeList-CSS/Eorzea_Collection/Eorzea_Collection.css";
```
## Image Сhanges

If you want to change the images in CSS then paste this after the code and replace the links to your.

I recommend images with resolutions of 1053px250

```css
.list-container .cover-block {
    background-image: url("your images") !important;
}
```
## MIT License

Copyright (c) 2018 Murakumo-JP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
