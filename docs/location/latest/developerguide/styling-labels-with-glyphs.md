

# Style labels with glyphs
<a name="styling-labels-with-glyphs"></a>

Glyphs are binary files containing encoded Unicode characters, which are used by a map renderer to display labels. Amazon Location Service enables the retrieval of specific glyphs from a font stack for use in map rendering through the `GetGlyphs` API.

For more information, see [GetGlyphs](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetGlyphs.html) in the *Amazon Location Service API Reference*.

## Use cases
<a name="glyphs-use-cases"></a>
+ Rendering custom text on maps with specific fonts and styles.
+ Fetching glyphs for localized map text rendering.
+ Using Unicode character ranges to display map labels and symbols.
+ Optimizing map font rendering based on font stacks and glyph ranges.

## Supported fonts in API
<a name="supported-fonts"></a>

The following fonts are supported in the API:
+ Amazon Ember Bold
+ Amazon Ember Bold Italic
+ Amazon Ember Bold,Noto Sans Bold
+ Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
+ Amazon Ember Condensed RC BdItalic
+ Amazon Ember Condensed RC Bold
+ Amazon Ember Condensed RC Bold Italic
+ Amazon Ember Condensed RC Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
+ Amazon Ember Condensed RC Light
+ Amazon Ember Condensed RC Light Italic
+ Amazon Ember Condensed RC LtItalic
+ Amazon Ember Condensed RC Regular
+ Amazon Ember Condensed RC Regular Italic
+ Amazon Ember Condensed RC Regular,Noto Sans Regular
+ Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
+ Amazon Ember Condensed RC RgItalic
+ Amazon Ember Condensed RC ThItalic
+ Amazon Ember Condensed RC Thin
+ Amazon Ember Condensed RC Thin Italic
+ Amazon Ember Heavy
+ Amazon Ember Heavy Italic
+ Amazon Ember Light
+ Amazon Ember Light Italic
+ Amazon Ember Medium
+ Amazon Ember Medium Italic
+ Amazon Ember Medium,Noto Sans Medium
+ Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium
+ Amazon Ember Regular
+ Amazon Ember Regular Italic
+ Amazon Ember Regular Italic,Noto Sans Italic
+ Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
+ Amazon Ember Regular,Noto Sans Regular
+ Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
+ Amazon Ember Thin
+ Amazon Ember Thin Italic
+ AmazonEmberCdRC\_Bd
+ AmazonEmberCdRC\_BdIt
+ AmazonEmberCdRC\_Lt
+ AmazonEmberCdRC\_LtIt
+ AmazonEmberCdRC\_Rg
+ AmazonEmberCdRC\_RgIt
+ AmazonEmberCdRC\_Th
+ AmazonEmberCdRC\_ThIt
+ AmazonEmber\_Bd
+ AmazonEmber\_BdIt
+ AmazonEmber\_He
+ AmazonEmber\_HeIt
+ AmazonEmber\_Lt
+ AmazonEmber\_LtIt
+ AmazonEmber\_Md
+ AmazonEmber\_MdIt
+ AmazonEmber\_Rg
+ AmazonEmber\_RgIt
+ AmazonEmber\_Th
+ AmazonEmber\_ThIt
+ Noto Sans Black
+ Noto Sans Black Italic
+ Noto Sans Bold
+ Noto Sans Bold Italic
+ Noto Sans Extra Bold
+ Noto Sans Extra Bold Italic
+ Noto Sans Extra Light
+ Noto Sans Extra Light Italic
+ Noto Sans Italic
+ Noto Sans Light
+ Noto Sans Light Italic
+ Noto Sans Medium
+ Noto Sans Medium Italic
+ Noto Sans Regular
+ Noto Sans Semi Bold
+ Noto Sans Semi Bold Italic
+ Noto Sans Thin
+ Noto Sans Thin Italic
+ NotoSans-Bold
+ NotoSans-Italic
+ NotoSans-Medium
+ NotoSans-Regular
+ Open Sans Regular,Arial Unicode MS Regular

## Understand the request
<a name="glyphs-understand-the-request"></a>

The request accepts two required URI parameters, `FontStack` and `FontUnicodeRange`, which determine the font and the Unicode range for glyphs. The `FontStack` parameter specifies which font to use, while the `FontUnicodeRange` defines the character range to fetch. The request does not include a body, focusing only on the URI parameters for its functionality.
+ **`FontStack`**: Specifies the name of the font stack to retrieve. Example: "Amazon Ember Bold, Noto Sans Bold".
+ **`FontUnicodeRange`**: A Unicode range of characters to download glyphs for. The range must be multiples of 256. Example: "0-255".

## Understand the response
<a name="glyphs-understand-the-response"></a>

The response returns glyph data as a binary blob, along with HTTP headers for caching, content type, ETag, and pricing information. The glyph data is returned as a binary blob to be rendered on maps, and the headers provide additional metadata for handling the response effectively.
+ **`CacheControl`**: Instructs the client on caching configurations for the response.
+ **`ContentType`**: Specifies the format of the response body, indicating the type of glyph data returned.
+ **`ETag`**: An identifier for the glyph's version, used for cache validation.
+ **`PricingBucket`**: Indicates the pricing tier associated with the request.
+ **`Blob`**: The glyph data returned as a binary blob, used to render map text.