# Places APIs

Places enable applications to search, find, and retrieve details about points of
interest, addresses, and specific locations. These capabilities enhance location-based
services by providing context and improving user experience in search functions.

- **Geocode**: Converts addresses or place names
  into geographic coordinates (longitude, latitude), supporting applications that
  require address-to-location transformation for mapping and spatial analysis. For
  more information, see [Reverse Geocode](reverse-geocode.md "reverse-geocode.md").
- **Reverse Geocode**: Converts geographic
  coordinates to the nearest address or place name, providing context for a
  location. For more information, See [Reverse Geocode](reverse-geocode.md "reverse-geocode.md").
- **Autocomplete**: Suggests potential completions
  for user-entered text, improving efficiency in search input. For more
  information, See [Autocomplete](autocomplete.md "autocomplete.md").
- **GetPlace**: Retrieves detailed information
  about a specified place, including attributes like address, contact details, and
  opening hours. For more information, See [GetPlace](get-place.md "get-place.md").
- **SearchNearby**: Finds places within a specified
  radius of a given geographic point, suitable for "near me" searches. For more
  information, See [Search Nearby](search-nearby.md "search-nearby.md").
- **SearchText**: Allows text-based searching for
  places or points of interest based on a keyword or phrase, ideal for finding
  locations by name or description. For more information, See [Search Text](search-text.md "search-text.md").
- **Suggest**: Provides search term suggestions as
  users type, enhancing search relevance and user experience. For more
  information, See [Suggest](suggest.md "suggest.md").
  The following table presents a number of business use cases that are best solved with
  Places APIs.

## Places use cases

The following section presents a number of business use cases that are best solved
with Places APIs.

| **Business need**                                                                                                                                 | **Useful API**                                                                      | **Examples**                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Add a neighbourhood business information in an application** Also returns business information, such as categories and food types.              | `SearchNearBy`                                                                      |                                                                                                                                               |
| **Proximity Search for business chain** Also returns business information, such as categories, food types, and access points.                     | Search Text Suggest                                                                 |                                                                                                                                               |
| **Search by phone name** Also returns business information, such as categories, food types, and access points.                                    | Search Text Suggest                                                                 |                                                                                                                                               |
| **Search by name of place, POI, category** Also returns business information, such as categories, food types, and access points.                  | Search Text Suggest                                                                 | [How to search for a place, POI, or business using a name](how-to-search-for-place-poi-business.md "how-to-search-for-place-poi-business.md") |
| **Predict suggestions as user key query** Also returns business information, such as categories, food types, and access points.                   | Suggest                                                                             | [How to predict suggestions based on input](how-to-predict-suggestions.md "how-to-predict-suggestions.md")                                    |
| **Autocomplete or suggest for autofill an address on checkout page**Normalizes and standardizes addresses.                                        | Autocomplete, Suggest                                                               | [How to complete an address](how-to-complete-address.md "how-to-complete-address.md")                                                         |
| **Convert a specific address to longitude and latitude coordinates** Normalizes and standardizes addresses.                                       | Geocode                                                                             |                                                                                                                                               |
| **Convert longitude and latitude coordinates into a corresponding address** Normalizes and standardizes addresses.                                | Reverse Geocode                                                                     | [How to reverse geocode for a position](how-to-reverse-geocode-position.md "how-to-reverse-geocode-position.md")                              |
| **Get Timezone of a City** Supports UTC offset and time zone name.                                                                                | Geocode                                                                             |                                                                                                                                               |
| **Get Timezone for longitude and latitude** Supports UTC offset and time zone name.                                                               | Reverse Geocode                                                                     |                                                                                                                                               |
| **Get place by place id** Returns business information, such as categories, contacts, opening hours, and access points.                           | Get Place                                                                           | [How to get results for a PlaceId](how-to-get-place-by-id.md "how-to-get-place-by-id.md")                                                     |
| **Get name, contacts, and opening hours of a point of interest** Returns business information, such as categories, food types, and access points. | Search Text, Search Nearby, Suggestion                                              |                                                                                                                                               |
| **Provide places type for a place name** Supports pre-filtering.                                                                                  | Geocode Autocomplete                                                                |                                                                                                                                               |
| **Provide places type for a latitude/longitude coordinates** Supports pre-filtering.                                                              | Reverse Geocode                                                                     |                                                                                                                                               |
| **Provide poi categories (such as hospital, store, museum and 500 more) for an address or POI** Supports pre-filtering.                           | Search Text, Search Nearby, Suggestion                                              |                                                                                                                                               |
| **Add the type-ahead search behavior for completion or predictions** Supports cost efficient, label-only, and address component.                  | Autocomplete Suggest                                                                | [How to predict suggestions based on input](how-to-predict-suggestions.md "how-to-predict-suggestions.md")                                    |
| **Visualize Places search and/or geocode result on a map** All APIs return geocoordinates, except autocomplete.                                   | `GetTile` and `GetStyleDescriptor` with rendering engine (MapLibre) with Places API |                                                                                                                                               |
| **Enhance, clean, normalize and standardize your address database**Supports address label, components, timezone, and more.                        | Geocode, Reverse Geocode                                                            |                                                                                                                                               |
