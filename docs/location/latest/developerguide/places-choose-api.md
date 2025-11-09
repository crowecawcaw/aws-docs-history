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

| **Business<br>need**                                                                                                                                       | **Useful API**                                                                         | **Examples**                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Add a neighbourhood business<br>information in an application**<br>Also returns business information, such as categories and food<br>types.              | `SearchNearBy`                                                                         |                                                                                                                                                  |
| **Proximity Search for business<br>chain**<br>Also returns business information, such as categories, food<br>types, and access points.                     | Search Text Suggest                                                                    |                                                                                                                                                  |
| **Search by phone name**<br>Also returns business information, such as categories, food<br>types, and access points.                                       | Search Text Suggest                                                                    |                                                                                                                                                  |
| **Search by name of place, POI,<br>category**<br>Also returns business information, such as categories, food<br>types, and access points.                  | Search Text Suggest                                                                    | [How to search for a place, POI,<br>or business using a name](how-to-search-for-place-poi-business.md "how-to-search-for-place-poi-business.md") |
| **Predict suggestions as user key<br>query**<br>Also returns business information, such as categories, food<br>types, and access points.                   | Suggest                                                                                | [How to predict suggestions based on<br>input](how-to-predict-suggestions.md "how-to-predict-suggestions.md")                                    |
| **Autocomplete or suggest for autofill<br>an address on checkout page**Normalizes and<br>standardizes addresses.                                           | Autocomplete, Suggest                                                                  | [How to complete an address](how-to-complete-address.md "how-to-complete-address.md")                                                            |
| **Convert a specific address to<br>longitude and latitude coordinates**<br>Normalizes and standardizes addresses.                                          | Geocode                                                                                |                                                                                                                                                  |
| **Convert longitude and latitude<br>coordinates into a corresponding address**<br>Normalizes and standardizes addresses.                                   | Reverse Geocode                                                                        | [How to reverse geocode for a<br>position](how-to-reverse-geocode-position.md "how-to-reverse-geocode-position.md")                              |
| **Get Timezone of a City**<br>Supports UTC offset and time zone name.                                                                                      | Geocode                                                                                |                                                                                                                                                  |
| **Get Timezone for longitude and<br>latitude**<br>Supports UTC offset and time zone name.                                                                  | Reverse Geocode                                                                        |                                                                                                                                                  |
| **Get place by place id**<br>Returns business information, such as categories, contacts,<br>opening hours, and access points.                              | Get Place                                                                              | [How to get results for a PlaceId](how-to-get-place-by-id.md "how-to-get-place-by-id.md")                                                        |
| **Get name, contacts, and opening hours<br>of a point of interest**<br>Returns business information, such as categories, food types,<br>and access points. | Search Text, Search Nearby, Suggestion                                                 |                                                                                                                                                  |
| **Provide places type for a place name**<br>Supports pre-filtering.                                                                                        | Geocode Autocomplete                                                                   |                                                                                                                                                  |
| **Provide places type for a<br>latitude/longitude coordinates**<br>Supports pre-filtering.                                                                 | Reverse Geocode                                                                        |                                                                                                                                                  |
| **Provide poi categories (such as<br>hospital, store, museum and 500 more) for an address or<br>POI**<br>Supports pre-filtering.                           | Search Text, Search Nearby, Suggestion                                                 |                                                                                                                                                  |
| **Add the type-ahead search behavior<br>for completion or predictions**<br>Supports cost efficient, label-only, and address<br>component.                  | Autocomplete Suggest                                                                   | [How to predict suggestions based on<br>input](how-to-predict-suggestions.md "how-to-predict-suggestions.md")                                    |
| \*_Visualize Places search and/or<br>geocode result on a map_<br>• All APIs return<br>geocoordinates, except autocomplete.                                 | `GetTile` and `GetStyleDescriptor` with<br>rendering engine (MapLibre) with Places API |                                                                                                                                                  |
| **Enhance, clean, normalize and<br>standardize your address database**Supports<br>address label, components, timezone, and more.                           | Geocode, Reverse Geocode                                                               |                                                                                                                                                  |
