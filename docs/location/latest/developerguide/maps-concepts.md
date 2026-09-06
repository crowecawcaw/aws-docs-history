

# Map concepts
<a name="maps-concepts"></a>

Amazon Location Service provides comprehensive mapping capabilities that enable you to create customized, visually consistent maps for your applications. You can leverage AWS map styles and design principles to customize the look and feel of your maps, ensuring visual consistency and branding.

For customers in `ap-southeast-1` and `ap-southeast-5`, supported request and response fields may differ. Refer to the [Maps API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) for details.

This topic covers essential mapping concepts including terminology, localization, internationalization, and map features.

## Features
<a name="maps-concepts-features"></a>

With Amazon Location Service, you can customize maps with advanced styling features. Add topographic elements such as terrain and contour density, route-related features like traffic and travel modes (truck or transit), and point-of-interest (POI) controls including density and category filtering. These customization options help you tailor map appearances for specific use cases, including logistics, transit, outdoor terrain visualization, or location-based discovery.


| Feature name | Description | Supported values | Supported map styles | 
| --- | --- | --- | --- | 
| Color scheme | Set color scheme for maps | Light and Dark | Standard, Monochrome, Hybrid, Satellite | 
| Terrain | Show topographic hillshade | Hillshade and Terrain3D | Standard, Monochrome, Hybrid (Terrain3D), Satellite (Terrain3D) | 
| ContourDensity | Show topographic elevation lines | Low, Medium, High | Standard, Monochrome, Hybrid | 
| Traffic | Show real-time traffic conditions | All, Congestion | Standard, Monochrome, Hybrid | 
| Buildings | Show three-dimensional building structures | Buildings3D | Standard, Monochrome | 
| TravelModes | Optimize map style for travel modes | Transit and Truck | Standard, Monochrome, Hybrid | 
| Language | Set local language | BCP47 language codes (e.g., en-US, es-ES, fr-CH) | Standard, Monochrome, Hybrid | 
| PoliticalView | Tailored geopolitical views of specific country | Argentina, Cyprus, Egypt, Georgia, Greece, Kenya, Morocco, Palestine, Serbia, Russia, Sudan, Suriname, Syria, Türkiye, Tanzania, Uruguay | Standard, Monochrome, Hybrid | 
| PoiDensity | Control how many POIs render on the map | Off, VerySparse, Sparse, Default, Dense, VeryDense | Standard, Hybrid | 
| PoiCategories | Show only specified POI categories | FoodAndDrink, Entertainment, SightsAndMuseums, Transportation, Accommodations, LeisureAndOutdoor, Shopping, BusinessAndServices, FacilitiesAndBuildings | Standard, Hybrid | 

For more information about the Standard, Monochrome and Hybrid styles, see [Amazon Location Service map styles](https://docs.aws.amazon.com/location/latest/developerguide/map-styles.html).

**Topics**
+ [Features](#maps-concepts-features)
+ [Maps terminology](maps-terminology.md)
+ [Color scheme](maps-color-scheme.md)
+ [Topography](maps-topographic-map.md)
+ [Navigation](maps-navigation-map.md)
+ [Localization and internationalization](maps-localization-internationalization.md)
+ [3D Features](maps-3d-map.md)