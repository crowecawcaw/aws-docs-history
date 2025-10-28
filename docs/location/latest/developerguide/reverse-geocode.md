# Reverse Geocode

Reverse Geocode converts geographic coordinates into a human-readable address or place. It
provides detailed address components, place type, category, and street information, with
filtering options based on place type to refine results. The API can also include additional
features, such as time zone information and political view adjustments.

###### Note

If results are stored, they will be billed at the higher Storage pricing tier. Use the
`IntendedUse` parameter to specify whether the results are for single use
or storage. Refer to [Places pricing](places-pricing.md "places-pricing.md") for cost implications associated
with stored results.

For more information, see [ReverseGeocode](../APIReference/API_geoplaces_ReverseGeocode.md "../APIReference/API_geoplaces_ReverseGeocode.md") in the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Reverse Geocode](reverse-geocode-how-to.md "reverse-geocode-how-to.md").

## Use cases

- **Add supplementary data to customer position
  data:** Improve position data records by including zip codes,
  coordinates, and utilizing persistent storage to support informed business and
  marketing decisions.
- **Position data standardization:** Apply
  geocoding in data pipelines or batch processes to standardize position data,
  utilizing persistent storage for ongoing reference.
- **Determine time zones:** Identify the time zone
  for cities or addresses to provide accurate timestamps for applications like
  travel, scheduling, and invoicing.

## Understand the request

The Reverse Geocode API request accepts a combination of required and optional
parameters to customize results. The required parameter `QueryPosition`
(longitude and latitude) specifies the coordinates to reverse geocode. Optional
parameters include `AdditionalFeatures` for extra data, `Filter`
to refine results, and `MaxResults` to limit the number of returned results.
Additional options like `Language`, `PoliticalView`, and
`IntendedUse` allow for further customization. For more details, refer to
the Reverse Geocode API Reference.

The request accepts the following key parameters:

**Authentication**

The `Key` parameter is optional if other authentication methods
are used.

- `Key`: Optional parameter for authentication.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md").

**Querying**

Parameters used for defining the geographic location and search
radius.

- `QueryPosition`: Specifies the longitude and latitude
  for the reverse geocode request.
- `QueryRadius`: Defines the search radius around the
  coordinates.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md").

**Refining results**

Apply filters to limit the search results to specific countries or place
types.

- `Filter`: Filter for results based on country or place
  type.

For more details, see [Filtering](places-filtering.md "places-filtering.md").

**Internationalization and localization**

Options to customize the language and apply a political view to the
results.

- `Language`: Specifies the language of the
  results.
- `PoliticalView`: Applies a political view reflecting
  territorial claims.

For more information, see [Localization and
internationalization](places-localization-internationalization.md "places-localization-internationalization.md").

**Additional features**

Requests extra data, such as time zone information.

- `AdditionalFeatures`: Option to request additional data
  such as time zone details.

For more information, see [Additional features](additional-features.md "additional-features.md").

## Understand the response

The response from the Reverse Geocode API provides detailed information about
locations at the specified coordinates. The `ResultItems` array includes a
list of place objects, each containing address details, categories, and geographic
position. Additional data such as `TimeZone`, `FoodTypes`, and
`PostalCodeDetails` offer further context. The response also includes
bounding box information for mapping and the distance from the query position. For more
details, see the Reverse Geocode API Reference.

The response includes the following key data:

**Address and related details**

Detailed address information for the returned location.

- `Address`: Complete address information, including
  country, region, postal code, and street details.
- `PostalCodeDetails`: Additional details related to
  postal codes, such as classifications and postal authorities.
- `StreetComponents`: Additional details about the
  street, including base name and type.

**Place types and categories**

Describes the type and category of the returned place.

- `Categories`: Categories describing the place, such as
  _Restaurants_ or
  _Schools_.
- `PlaceType`: Specifies the type of place, such as a
  city, address, or region.

**Result analysis**

Information on how closely each result matches the input query.

- `MatchScores`: Scores indicating the accuracy of each
  match to the input query.

**Additional details**

Provides extra location-related data.

- `TimeZone`: Time zone information for the
  location.
- `AccessPoints`: Geographic coordinates representing
  entry points to the location.
