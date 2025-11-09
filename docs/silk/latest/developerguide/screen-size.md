# Learn about screen resolution

When you're developing web content for Amazon Silk (or any other mobile browser), it's a
good idea to be aware of devices' screen resolution and related specifications. The following
table shows screen size, product model, resolution, and scale factor for Fire tablets and phone.
For full device specs, see [Tablet Device Specifications](https://developer.amazon.com/docs/fire-tablets/ft-device-and-feature-specifications.html "https://developer.amazon.com/docs/fire-tablets/ft-device-and-feature-specifications.html").

| **Device**                    | **Screen size**  | **Product model**                     | **Screen resolution (px)** | **Scale factor** |
| ----------------------------- | ---------------- | ------------------------------------- | -------------------------- | ---------------- |
| Fire 7 (9th Gen)              | 7-inch screen    | KFMUWI — Wi-Fi                        | 1024 x 600                 | 1.0 (mdpi)       |
| Fire HD 8 (8th Gen)           | 8-inch screen    | KFKAWI — Wi-Fi                        | 1280 x 800                 | (tdvpi)          |
| Fire HD 10 (7th Gen)          | 10.1-inch screen | KFSUWI — Wi-Fi                        | 1920 x 1200                | (hdpi)           |
| Fire 7 (7th Gen)              | 7-inch screen    | KFAUWI — Wi-Fi                        | 1024 x 600                 | (mdpi)           |
| Fire HD 8 (7th Gen)           | 8-inch screen    | KFDOWI — Wi-Fi                        | 1280 x 800                 | (tvdpi)          |
| Fire HD 8 (6th Gen)           | 8-inch screen    | KFGIWI — Wi-Fi                        | 1280 x 800                 | (tvdpi)          |
| Fire HD 10 (5th Gen)          | 10.1-inch screen | KFTBWI — Wi-Fi                        | 1280 x 800                 | 1.0 (mdpi)       |
| Fire HD 8 (5th Gen)           | 8-inch screen    | KFMEWI — Wi-Fi                        | 1280 x 800                 | 1.3 (tvdpi)      |
| Fire (5th Gen)                | 7-inch screen    | KFFOWI — Wi-Fi                        | 1024 x 600                 | 1 (mdpi)         |
| Fire HDX 8.9 (4th Gen)        | 8.9-inch screen  | KFSAWI — Wi-FiKFSAWA — Wi-Fi + 4G LTE | 2560 x 1600                | 2.0 (xhdpi)      |
| Fire HD 7 (4th Gen)           | 7-inch screen    | KFASWI — Wi-Fi                        | 1280 x 800                 | 1.5 (hdpi)       |
| Fire HD 6 (4th Gen)           | 6-inch screen    | KFARWI — Wi-Fi                        | 1280 x 800                 | 1.5 (hdpi)       |
| Fire Phone                    | 4.7-inch screen  | SD4930UR                              | 1280 x 720                 | 2.0 (xhdpi)      |
| Kindle Fire HDX 8.9 (3rd Gen) | 8.9-inch screen  | KFAPWI — Wi-FiKFAPWA — Wi-Fi + 4G LTE | 2560 x 1600                | 2.0 (xhdpi)      |
| Kindle Fire HDX 7 (3rd Gen)   | 7-inch screen    | KFTHWI — Wi-FiKFTHWA — Wi-Fi + 4G LTE | 1920 x 1200                | 2.0 (xhdpi)      |
| Kindle Fire HD 7 (3rd Gen)    | 7-inch screen    | KFSOWI — Wi-Fi                        | 1280 x 800                 | 1.5 (hdpi)       |
| Kindle Fire HD 8.9 (2nd Gen)  | 8.9-inch screen  | KFJWI — Wi-FiKFJWA — Wi-Fi + 4G LTE   | 1920 x 1200                | 1.5 (hdpi)       |
| Kindle Fire HD 7 (2nd Gen)    | 7-inch screen    | KFTT — Wi-Fi                          | 1280 x 800                 | 1.5 (hdpi)       |
| Kindle Fire (2nd Gen)         | 7-inch screen    | KFOT — Wi-Fi                          | 1024 x 600                 | 1.0 (mdpi)       |
| Kindle Fire (1st Gen)         | 7-inch screen    | KFOT — Wi-Fi                          | 1024 x 600                 | 1.0 (mdpi)       |

You can use the Silk user agent strings to detect a particular Fire device and target the
user experience accordingly. For more information about the Silk user agent string, see [Learn about user agent strings](user-agent.md "user-agent.md").

Keep in mind the following when developing web content for Silk and Fire devices:

- The viewport is the portion of the browser dedicated to displaying the webpage.
  Viewport size and screen size for mobile devices are not necessarily identical. They
  differ because the browser uses up some screen real estate to show its chrome. You can use
  the [viewport meta element](css3.md#viewport "css3.md#viewport") to specify attributes of the
  viewport, including width and height.
- With a mobile form factor, HTML forms can be challenging for users to complete. You
  can use HTML5 [input types](html5-elements.md#input-types "html5-elements.md#input-types") to make forms more
  responsive.
- You can use [media queries](css3.md#media-queries "css3.md#media-queries") to style your site for
  a specific screen resolution.
  For more information about Fire device specifications, see the [Device and Feature
  Specifications](https://developer.amazon.com/sdk/fire/specifications.html "https://developer.amazon.com/sdk/fire/specifications.html") (tablets) page on the Amazon Apps & Games Developer Portal. To
  learn more about scale factor, see [Screen Layout and Resolution](https://developer.amazon.com/docs/fire-tablets/ft-screen-layout-and-resolution.html "https://developer.amazon.com/docs/fire-tablets/ft-screen-layout-and-resolution.html").
