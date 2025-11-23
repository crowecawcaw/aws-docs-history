# Style dynamic maps

Amazon Location Service provides two options for styling your dynamic maps: using predesigned AWS
Map Styles or customizing the map style using style descriptors.

For more information, see [GetStyleDescriptor](../APIReference/API_geomaps_GetStyleDescriptor.md "../APIReference/API_geomaps_GetStyleDescriptor.md") in the _Amazon Location Service API
Reference_.

## Use predesigned AWS map styles

AWS map styles are predefined styles that adhere to industry standards to
deliver a sophisticated, professional aesthetic. By leveraging these styles in
Amazon Location Service, you can reduce time-to-market and eliminate the need for dedicated
cartographers to create map styles from scratch.

For more information, see [AWS map styles and features](map-styles.md "map-styles.md").

To learn more about predefined map styles, see:

- [Standard map style](map-styles.md#standard-map "map-styles.md#standard-map")
- [Monochrome map style](map-styles.md#monochrome-map "map-styles.md#monochrome-map")
- [Hybrid map style](map-styles.md#hybrid-map "map-styles.md#hybrid-map")
- [Satellite map style](map-styles.md#satellite-map "map-styles.md#satellite-map")

## Benefits of using AWS map styles

- **Time and resource efficiency**: AWS Map
  Styles allow you to bypass the time-consuming and resource-intensive process
  of designing map styles from scratch. This allows you to focus on core
  functionalities while providing visually appealing maps.
- **Professional and consistent aesthetics**:
  Skilled cartographers have meticulously crafted AWS Map Styles, following
  industry best practices. Every detail, from color palettes to label
  placements, has been optimized for clarity and legibility.
- **Seamless integration**: AWS Map Styles
  integrate seamlessly with your application's design language, providing a
  polished and consistent mapping experience for your end-users.

## Get started with AWS map

styles

- **Check the AWS map styles offering**: In
  the Amazon Location Service console, navigate to the **Map** section to
  explore the available styles.
- **Choose the style that matches your needs**:
  Select the style that best aligns with your application's design and user
  experience requirements.
- **Integrate the style**: Follow the provided
  documentation to integrate the chosen style into your application using
  Amazon Location Service APIs or SDKs.

Learn more about [How to display a map](how-to-display-a-map.md "how-to-display-a-map.md").

## Use cases

- Customizing map styles based on color schemes like "Light" or
  "Dark".
- Displaying maps according to specific political views or geographic
  boundaries.
- Optimizing map styles for different use cases, such as logistics, outdoor
  activities, navigation with traffic data, and transportation-specific
  routing.

## Understand the request

The request supports parameters like `ColorScheme`, `Key`,
and `PoliticalView` to define the map's style and presentation. The
`Style` parameter is required to specify the desired map
style.

- **`ColorScheme`**: Sets the map's
  color tone, such as "Light" or "Dark".
- **`PoliticalView`**: Specifies the
  political view for map visualization.
- **`Style`**: Defines the style of
  the map, like "Standard" or "Monochrome".
- **`Terrain`**: Displays
  topographic features through elevation shading and geographic
  highlighting.
- **`ContourDensity`**: Shows
  terrain shape and steepness using elevation contour lines at varying density
  levels.
- **`Traffic`**: Overlays real-time
  traffic conditions on the map.
- **`TravelMode`**: Displays
  transportation information including public transit systems or truck routing
  with road restrictions.

## Understand the response

The response provides headers like `CacheControl`,
`ContentType`, and `ETag`, and contains the style
descriptor as a JSON blob. The headers give caching information, content format
details, and versioning for style changes.

- **`CacheControl`**: Controls
  caching configurations for the style descriptor.
- **`ContentType`**: Indicates the
  response format as JSON.
- **`ETag`**: Provides a version
  identifier for the style descriptor.
- **`Blob`**: Contains the body of
  the style descriptor in JSON format.

## Customize style descriptors

To customize map styles, you must understand the structure of the style
descriptor, which is usually a JSON object defining the visual representation of map
elements. The style descriptor comprises several layers, each controlling the style
for a specific type of map element, such as roads, parks, buildings, or
labels.

- **Use a predefined style descriptor as a
  base**: You can either start with a predefined style descriptor
  or create one from scratch using map style editors such as [Maputnik](https://maputnik.github.io/ "https://maputnik.github.io/").
- **Understand the structure**: The style
  descriptor is a hierarchical JSON object that contains layers, each
  representing a different map element. Each layer has properties that control
  the visual appearance of that element, such as color, opacity, and line
  width.
- **Modify styles for layers**: Depending on
  the map style editor you’re using, you can change existing layers or add new
  ones to customize the style. For example, you can adjust the color of roads,
  modify the font size of labels, or add custom icons for specific
  locations.
- **Define styles for different zoom levels**:
  Map style editors allow you to define different styles for different zoom
  levels, which is useful for controlling the level of detail and visibility
  based on user zoom interactions.
- **Test and iterate**: After modifying or
  creating the style descriptor, test the customized style on a map to ensure
  it displays as intended. Iterate and adjust until you achieve the desired
  visual style.
