# Eorzea Collection CSS theme for MyAnimeList

## Preview
![Screenshot](Eorzea_Collection/preview/Snapshot.jpg?raw=true)

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

Select the default theme and paste the code into the Add custom CSS

```css
@import url('https://malcat-gen.appspot.com/series?template=.data.image a[href^="/$list/$id/"]:after{background-image:url($series_image)}');
@import url('https://murakumo-jp.github.io/MyAnimeList-CSS/Eorzea_Collection/Eorzea_Collection.css');
```
If you want to change the images in CSS then paste this after the code and replace the links to your.


```css
.list-container .cover-block {
    background-image: url("Here is a link to your images") !important;
}

.list-container .cover-block:before {
    background-image: url("Here is a link to your images") !important;
}

.list-container .cover-block:after {
    background-image: url("Here is a link to your images") !important;
}
```
