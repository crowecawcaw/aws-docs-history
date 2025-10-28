# Search Nearby

The Search Nearby API allows developers to query for points of interest within a specified
radius from central coordinates. The API provides place results with optional filters,
including categories, business chains, food types, and more. Response details include place
name, address, phone, category, food type, contact, and opening hours. Additional features,
such as phonemes, time zones, and others, are available based on requested
parameters.

###### Note

If results are stored, they will be billed at the higher Storage pricing tier. Use the
`IntendedUse` parameter to specify whether the results are for single use
or storage. Refer to [Places pricing](places-pricing.md "places-pricing.md") for cost implications associated
with stored results.

For more information, see [SearchNearby](../APIReference/API_geoplaces_SearchNearby.md "../APIReference/API_geoplaces_SearchNearby.md")
in the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Search Nearby](search-nearby-how-to.md "search-nearby-how-to.md").

## Use cases

- **Real Estate Applications:** Provide potential
  homebuyers or renters with a list of amenities and services near a property,
  such as schools, hospitals, and shopping centers.
- **Local Business Discovery:** Enable users to
  locate businesses, restaurants, or shops within a specific radius from their
  current location. For example, a food delivery app can display nearby
  restaurants based on real-time location.
- **Travel and Tourism Apps:** Help travelers
  explore attractions, landmarks, hotels, and services near their location or a
  destination. A travel app might suggest nearby points of interest such as
  museums, parks, and historic sites.
- **Emergency Services:** Assist users in finding
  the nearest hospitals, police stations, or pharmacies during emergencies,
  especially valuable for apps focused on health, safety, or disaster
  response.
- **Transportation and Logistics:** Help users find
  the nearest gas stations, EV charging points, or public transit stops.
  Ride-hailing services can display nearby available drivers.

## Understand the request

The Search Nearby API request includes required parameters such as
`QueryPosition` and optional parameters like filters to refine the
search. Additional options, like `Language` and `PoliticalView`,
customize results for specific needs. For more information, refer to the Search Nearby
API Reference.

The request includes the following key parameters:

**Authentication**

The `Key` parameter is optional if other authentication methods
are used.

- `Key`: API key for authorization.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md")

**Querying**

Defines the location and search radius for the query.

- `QueryPosition`: Specifies the longitude and latitude
  coordinates.
- `QueryRadius`: Defines the search radius around the
  specified coordinates.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md")

**Refining Results**

Filters results to narrow down search criteria.

- `Filter`: Applies filters such as categories, business
  chains, or food types.

For more details, see [Filtering](places-filtering.md "places-filtering.md")

**Internationalization and Localization**

Options to customize the language and apply a political view to the
results.

- `Language`: Specifies the language of the
  results.
- `PoliticalView`: Applies a political view reflecting
  territorial claims.

For more information, see [Localization and
internationalization](places-localization-internationalization.md "places-localization-internationalization.md")

**Additional Features**

Requests additional data, such as time zone information.

- `AdditionalFeatures`: Option to request additional
  details like time zone information.

For more information, see [Additional features](additional-features.md "additional-features.md")

## Understand the response

The response from the Search Nearby API provides detailed results matching the query,
including location, address details, business chains, contacts, phonemes, time zone, and
opening hours. For more details, refer to the Search Nearby API Reference.

The response includes the following key data:

**Address and Related Details**

Comprehensive address information for the returned location.

- `Address`: Includes full address details, such as
  country and street.

**Place Types and Categories**

Describes the type and category of the returned place.

- `Categories`: Categories describing the place, such as
  _Restaurants_ or
  _Schools_.
- `FoodTypes`: Types of food available at restaurants or
  eateries.
- `BusinessChains`: Indicates any associated business
  chains.

**Additional Details**

Additional information related to the place, as requested.

- `Contacts`: Lists emails, phone numbers, and
  websites.
- `OpeningHours`: Specifies operational hours for the
  place.
- `Phonemes`: Provides phonetic representations of
  address components.
- `TimeZone`: Includes time zone information for the
  place.
