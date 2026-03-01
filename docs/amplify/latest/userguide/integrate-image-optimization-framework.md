# Image optimization integration for framework authors

Framework authors can integrate Amplify's image optimization feature by using the
Amplify Hosting deployment specification. To enable image optimization, your deployment
manifest must contain a routing rule that targets the image optimization service. The
following example demonstrates how to configure the routing rule.

```
// .amplify-hosting/deploy-manifest.json

{
  "routes": [
    {
      "path": "/images/*",
      "target": {
        "kind": "ImageOptimization",
        "cacheControl": "public, max-age=31536000, immutable"
      }
    }
  ]
}
```

For more information about configuring image optimization settings using the deployment
specification, see [Using the Amplify Hosting deployment specification to configure build output](ssr-deployment-specification.md "ssr-deployment-specification.md") .

## Understanding the Image optimization API

Image optimization can be invoked at runtime via an Amplify app's domain URL, at the
path defined by the routing rule.

```
GET https://{appDomainName}/{path}?{queryParams}
```

Image optimization imposes the following rules on images.

- Amplify can't optimize GIF, APNG and SVG formats or convert them to another
  format.
- SVG images aren't served unless the `dangerouslyAllowSVG` setting is
  enabled.
- The width or height of a source images can't exceed 11 MB or 9,000 pixels.
- The size limit of an optimized image is 4 MB.
- HTTPS is the only protocol supported for sourcing images with remote URLs.

### HTTP headers

The **Accept** request HTTP header is used to specify
the image formats, expressed as MIME types, allowed by the client (usually a web
browser). The image optimization service will attempt to convert the image to the
specified format. The value specified for this header will have a higher priority than
the format query parameter. For example, a valid value for the **Accept** header is `image/png, image/webp, */*` . The formats
setting specified in the Amplify deployment manifest will restrict the formats to
those in the list. Even if the **Accept** header asks for a
specific format, it will be ignored if the format isn't in the allow list.

### URI request parameters

The following table describes the URI request parameters for Image
optimization.

| Query parameter | Type                                                            | Required | Description                                                                                                                                                                                                    | Example                                            |
| --------------- | --------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| url             | String                                                          | Yes      | A relative path or absolute URL to the source image. For a remote URL,<br>only the https protocol is supported. Value must be URL encoded.                                                                     | `?url=https%3A%2F%2Fwww.example.com%2Fbuffalo.png` |
| width           | Number                                                          | Yes      | The width in pixels of the optimized image.                                                                                                                                                                    | `?width=800`                                       |
| height          | Number                                                          | No       | The height in pixels of the optimized image. If not specified, the image<br>will be auto scaled to match the width.                                                                                            | `?height=600`                                      |
| fit             | Enum values: `cover`, `contain`, `fill`,<br>`inside`, `outside` | No       | How the image is resized to fit the specified width and height.                                                                                                                                                | `?width=800&height=600&fit=cover`                  |
| position        | Enum values: `center`, `top`, `right`,<br>`bottom`, `left`      | No       | A position to be used when fit is `cover` or<br>`contain`.                                                                                                                                                     | `?fit=contain&position=centre`                     |
| trim            | Number                                                          | No       | Trims pixels from all edges that contain values similar to the specified<br>background color of the top-left pixel.                                                                                            | `?trim=50`                                         |
| extend          | Object                                                          | No       | Adds pixels to the edges of the image using the color derived from the<br>nearest edge pixels. The format is `{top}_{right}_{bottom}_{left}`<br>where each value is the number of pixels to add.               | `?extend=10_0_5_0`                                 |
| extract         | Object                                                          | No       | Crops the image to the specified rectangle delimited by top, left, width<br>and height. The format is {left}\_{top}\_{width}\_{right} where each value is the<br>number of pixels to crop.                     | `?extract=10_0_5_0`                                |
| format          | String                                                          | No       | The desired output format for the optimized image.                                                                                                                                                             | `?format=webp`                                     |
| quality         | Number                                                          | No       | The quality of the image, from 1 to 100. Only used when converting the<br>format of the image.                                                                                                                 | `?quality=50`                                      |
| rotate          | Number                                                          | No       | Rotates the image by the specified angle in number of degrees.                                                                                                                                                 | `?rotate=45`                                       |
| flip            | Boolean                                                         | No       | Mirrors the image vertically (up-down) on the x-axis. This always occurs<br>before rotation, if any.                                                                                                           | `?flip`                                            |
| flop            | Boolean                                                         | No       | Mirrors the image horizontally (left-right) on the y-axis. This always<br>occurs before rotation, if any.                                                                                                      | `?flop`                                            |
| sharpen         | Number                                                          | No       | Sharpening enhances the definition of edges in the image. Valid values are<br>between 0.000001 and 10.                                                                                                         | `?sharpen=1`                                       |
| median          | Number                                                          | No       | Applies a median filter. This removes noise or smoothes the edges of an<br>image.                                                                                                                              | `?sharpen=3`                                       |
| blur            | Number                                                          | No       | Applies a Gaussian blur of the specified sigma. Valid values are from 0.3<br>to 1,000.                                                                                                                         | `?blur=20`                                         |
| gamma           | Number                                                          | No       | Applies a gamma correction to improve the perceived brightness of a<br>resized image. Value must be between 1.0 and 3.0.                                                                                       | `?gamma=1`                                         |
| negate          | Boolean                                                         | No       | Inverts the colors of the image.                                                                                                                                                                               | `?negate`                                          |
| normalize       | Boolean                                                         | No       | Enhances image contrast by stretching its luminance to cover a full<br>dynamic range.                                                                                                                          | `?normalize`                                       |
| threshold       | Number                                                          | No       | Replaces any pixel in the image with a black pixel, if its intensity is<br>less than the specified threshold. Or with a white pixel if it's greater than<br>the threshold. Valid values are between 0 and 255. | `?threshold=155`                                   |
| tint            | String                                                          | No       | Tints the image using the provided RGB while preserving the image<br>luminance.                                                                                                                                | `?tint=#7743CE`                                    |
| grayscale       | Boolean                                                         | No       | Turns the image into grayscale (black and white).                                                                                                                                                              | `?grayscale`                                       |

### Response status codes

The following list describes the response status codes for image
optimization.

**Success - HTTP status code 200**

The request was fullfilled successfully.

**BadRequest - HTTP status code 400**

- An input query parameter was specified incorrectly.
- The remote URL is not listed as allowed in the `remotePatterns`
  setting.
- The remote URL doesn't resolve to an image.
- The requested width or height are not listed as allowed in the
  `sizes` setting.
- The image requested is SVG but the `dangerouslyAllowSvg`
  setting is disabled.

**Not Found - HTTP status code 404**

The source image was not found.

**Content too large - HTTP status code 413**

Either the source image or the optimized image exceed the maximum allowed size
in bytes.

### Understanding optimized image caching

Amplify Hosting caches optimized images on our CDN so that subsequent requests to
the same image, with the same query parameters, are served from the cache. The cache
Time to live (TTL) is controlled by the `Cache-Control` header. The following
list describes your options for specifying the `Cache-Control` header.

- Using the `Cache-Control` key within the routing rule that targets
  image optimization.
- Using custom headers defined in the Amplify app.
- For remote images, the `Cache-Control` header returned by the remote
  image is honored.

The `minimumCacheTTL` specified in the image optimization settings
defines the lower bound of the Cache-Control max-age directive. For
example, if a remote image URL responds with a `Cache-Control s-max-age=10`,
but the value of `minimumCacheTTL` is 60, then 60 is used.
