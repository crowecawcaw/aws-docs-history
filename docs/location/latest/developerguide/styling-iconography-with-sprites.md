

# Style iconography with sprites
<a name="styling-iconography-with-sprites"></a>

A sprite is a Portable Network Graphic (PNG) image file that contains small raster images such as icons, markers, and other elements rendered on a map. Sprites can be customized based on parameters like style, color scheme, and variant. Amazon Location Service provides a sprite sheet through the `GetSprites` API. You can also use custom icons by either loading your own icon set (see [How to add an icon on the map](how-to-add-icon-on-map.md)) or customizing the style descriptor to load your custom sprites.

For more information, see [GetSprites](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetSprites.html) in the *Amazon Location Service API Reference*.

## Use cases
<a name="use-cases"></a>
+ Rendering custom map elements using sprite sheets for specific styles and color schemes.
+ Fetching sprites for various map styles such as Standard, Monochrome, or Hybrid.
+ Customizing iconography on the map by modifying sprites.

## Understand the request
<a name="styling-understand-the-request"></a>

The request requires URI parameters such as `ColorScheme`, `FileName`, and `Style`. These parameters allow for the customization of the sprite sheet based on the map's color scheme, style, and the specific sprite file required.
+ **`ColorScheme`**: Defines the color scheme for the sprites, such as "Light" or "Dark".
+ **`FileName`**: The name of the sprite file to retrieve, which could be a PNG or JSON file.
+ **`Style`**: Specifies the map style, such as "Standard" or "Monochrome".

## Understand the response
<a name="styling-understand-the-response"></a>

The response contains headers such as `CacheControl`, `ContentType`, and `ETag`, and returns the sprite data as either a binary blob or a JSON file. These headers provide caching information, the content type of the response, and version control for the sprite data.
+ **`CacheControl`**: Caching configurations for the sprite file.
+ **`ContentType`**: The format of the response, indicating whether it contains PNG or JSON data.
+ **`ETag`**: Identifier for the sprite's version, used for cache validation.
+ **`Blob`**: Contains the body of the sprite sheet or the JSON offset file.

------
#### [ Standard Light ]

![Sprite sheet of map icons for the Amazon Location Service Standard Light style, including colored point-of-interest markers, road shields, and navigation symbols.](http://docs.aws.amazon.com/location/latest/developerguide/images/styling-standard-light.png)


------
#### [ Standard Dark ]

![Sprite sheet of map icons for the Amazon Location Service Standard Dark style, including colored point-of-interest markers, road shields, and navigation symbols.](http://docs.aws.amazon.com/location/latest/developerguide/images/styling-standard-dark.png)


------
#### [ Monochrome Light ]

![Sprite sheet of map icons for the Amazon Location Service Monochrome Light style, showing light-colored point-of-interest markers, road shields, and traffic signs on a light background.](http://docs.aws.amazon.com/location/latest/developerguide/images/styling-monochrome-light.png)


------
#### [ Monochrome Dark ]

![Sprite sheet of map icons for the Amazon Location Service Monochrome Dark style, showing light-colored point-of-interest markers, road shields, and traffic signs on a dark background.](http://docs.aws.amazon.com/location/latest/developerguide/images/styling-monochrome-dark.png)


------
#### [ Hybrid ]

![Sprite sheet of map icons for the Amazon Location Service Hybrid (Satellite) style, including road shields, traffic signs, and navigation markers used on satellite imagery.](http://docs.aws.amazon.com/location/latest/developerguide/images/styling-hybrid.png)


------