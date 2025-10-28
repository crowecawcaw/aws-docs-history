# Geocode

Geocoding transforms textual addresses or place names into geographic coordinates, along
with detailed address components and additional information. This API supports flexible
queries, including both free-form text and structured queries with street names, postal
codes, and regions. Optional features include time zone data and political view
adjustments.

###### Note

Stored results incur higher Storage pricing. Use the `IntendedUse`
parameter to indicate single-use or storage. Refer to the [Places pricing](places-pricing.md "places-pricing.md") to understand cost implications for stored results.

For more information, see [Geocode](../APIReference/API_geoplaces_Geocode.md "../APIReference/API_geoplaces_Geocode.md") in the
_Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Geocode](how-to-geocode.md "how-to-geocode.md").

## Use cases

- **Add supplementary data to customer addresses:**
  Improve address records by including zip codes, coordinates, and utilizing
  persistent storage to support informed business and marketing decisions.
- **Address Data Standardization:** Apply geocoding
  in data pipelines or batch processes to standardize address data, utilizing
  persistent storage for ongoing reference.
- **Determine Time Zones:** Identify the time zone
  for cities or addresses to provide accurate timestamps for applications like
  travel, scheduling, and invoicing.

## Understand the request

The request accepts optional parameters, such as `AdditionalFeatures`,
`BiasPosition`, and `Filter`, to refine the search results.
Additional options, like `Language`, `MaxResults`, and
`PoliticalView`, provide further customization of the response. The
required parameter is `Query`, which can be provided as free-form text or
structured as `QueryComponents`. For more information, refer to the Geocode
API Reference.

The request includes the following key parameters:

**Authentication**

For authentication, the `Key` parameter is optional if other
methods are in use.

- `Key`: Optional parameter for authentication.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md")

**Querying and biasing**

Parameters used for querying and geographic biasing of results.

- `QueryText`: Free-form text query for searching
  locations.
- `QueryComponents`: Structured components such as
  address number, country, locality, or postal code for precise
  searching.
- `BiasPosition`: Geographic position to bias search
  results towards.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md")

**Refining Results**

Apply filters to refine the results.

- `Filter`: Filter to include specific countries or place
  types. For more information, see [Filtering](places-filtering.md "places-filtering.md").

**Internationalization and localization**

Specify language and apply political view for localized results.

- `Language`: Language for the results.
- `PoliticalView`: Applies a political view reflecting
  territorial claims.

For more information, see [Localization and
internationalization](places-localization-internationalization.md "places-localization-internationalization.md")

**Additional Features**

Request additional information like time zone details.

- `AdditionalFeatures`: Option to request additional
  details such as time zone. For more information, see [Additional features](additional-features.md "additional-features.md").

## Understand the response

The response provides `ResultItems`, which contain detailed location data
such as `Address`, `PlaceId`, `Position`, and other
relevant attributes. Additional features like `TimeZone` information or
`MatchScores` for each query component may also be included. Each
`ResultItem` represents a matched location or geocoding result based on
the specified request parameters. For further details, see the Geocode API
Reference.

The response includes the following key parameters:

**Address and related details**

Details about the returned location, including address components.

- `Address`: Full address including country, region,
  postal code, and street details.
- `PostalCodeDetails`: Additional information related to
  postal codes.
- `StreetComponents`: Street details including base name
  and type.

**Place types and categories**

Information on the type and category of place returned.

- `Categories`: List of categories describing the place,
  for example _Restaurants_,
  _Schools_.
- `PlaceType`: Specifies the type of place, such as city,
  address, or region.

**Result analysis**

Scores indicating how closely results match the input query.

- `MatchScores`: Scores for matching precision.
  - `Overall`: Measures how well an address search
    matches your input, on a scale from 0.0 to 1.0 (0% to 100%).
    A perfect score of 1.0 means every part of your search was
    found in the database. It's normal to see lower scores when
    including extra details like contact names or delivery
    instructions. These naturally reduce the score, but don't
    necessarily mean the address is wrong.
  - `Component Score`: Each address component (such
    as `AddressNumber` or `PostalCode`) is
    scored individually on a scale from 0.0 to 1.0 (0% to 100%).
    These scores indicate how accurately each part of the
    address matches the result. For example, if
    `AddressNumber`, `Street`, and
    `PostalCode` score close to 1.0, you can
    trust the match even if the overall score is lower due to
    other query details.

###### Note

When no score appears for a specific component (such as
`Street`), that component is counted as 0. This
helps identify parts of the address that might need
verification.

This scoring system helps balance between exact matches and
practical usability when dealing with real-world address
searches that often include extra information.

**Additional details**

Includes extra location-related information as needed.

- `AccessPoints`: Geographic coordinates representing
  access points.
- `TimeZone`: Time zone information for the
  location.
