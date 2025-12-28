# Map concepts

Amazon Location Service provides comprehensive mapping capabilities that enable you to create customized, visually consistent maps for your applications. You can leverage AWS map styles and design principles to customize the look and feel of your maps, ensuring visual consistency and branding.

This topic covers essential mapping concepts including terminology, localization, internationalization, and map features.

## Features

Amazon Location Service enables you to customize maps with advanced styling features. Add topographic elements such as terrain and contour density, plus route-related features like traffic and travel modes (truck or transit). These customization options help you tailor map appearances for specific use cases, including logistics, transit, or outdoor terrain visualization.

| Feature name   | Description                                     | Supported values                                                                                                                         | Supported map styles               |
| -------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Color scheme   | Set color scheme for maps                       | `Light` and `Dark`                                                                                                                       | `Standard`, `Monochrome`           |
| Terrain        | Show topographic hillshade                      | `Hillshade`                                                                                                                              | `Standard`                         |
| ContourDensity | Show topographic elevation lines                | `Medium`                                                                                                                                 | `Standard`                         |
| Traffic        | Show real-time traffic conditions               | `All`                                                                                                                                    | `Standard`                         |
| TravelModes    | Optimize map style for travel modes             | `Transit` and `Truck`                                                                                                                    | `Standard`                         |
| Language       | Set local language                              | BCP47 language codes (e.g., en-US, es-ES, fr-CH)                                                                                         | `Standard`, `Monochrome`, `Hybrid` |
| PoliticalView  | Tailored geopolitical views of specific country | Argentina, Cyprus, Egypt, Georgia, Greece, Kenya, Morocco, Palestine, Serbia, Russia, Sudan, Suriname, Syria, Türkiye, Tanzania, Uruguay | `Standard`, `Monochrome`, `Hybrid` |

For more information about the Standard, Monochrome and Hybrid styles, see [Amazon Location Service map styles](map-styles.md "map-styles.md").

###### Topics

- [Maps terminology](maps-terminology.md "maps-terminology.md")
- [Color scheme](maps-color-scheme.md "maps-color-scheme.md")
- [Topography](maps-topographic-map.md "maps-topographic-map.md")
- [Navigation](maps-navigation-map.md "maps-navigation-map.md")
- [Localization and internationalization](maps-localization-internationalization.md "maps-localization-internationalization.md")
