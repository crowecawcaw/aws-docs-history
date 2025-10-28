# Search Text

Search Text allows you to query location data using a single free-form text input,
returning place results with optional filters like country, geographic circle, or bounding
box. The API also enables searching by `QueryId` returned from the Suggest API.
The response includes details such as place name, address, phone number, category, food
type, contact information, and opening hours. Optional features like phonemes, time zones,
and more are also available based on specified parameters.

###### Note

If results are stored, they will be billed at the higher Storage pricing tier. Use the
`IntendedUse` parameter to specify whether the results are for single use
or storage. Refer to [Places pricing](places-pricing.md "places-pricing.md") for cost implications associated
with stored results.

For more information, see [SearchText](../APIReference/API_geoplaces_SearchText.md "../APIReference/API_geoplaces_SearchText.md") in
the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Search Text](SearchText-how-to.md "SearchText-how-to.md").

## Use cases

- **Neighborhood search by text:** Help customers
  locate the nearest relevant place. Customers can find the closest address,
  business, or attraction such as museums, shops, or parks.
- **Business discovery:** Allow users to find
  specific businesses or types of places by entering keywords like "Italian
  restaurant" or "coffee shop." This feature is particularly useful for food
  delivery or restaurant recommendation apps.
- **Place search in travel apps:** Enable users to
  search for locations, landmarks, or businesses using free-form text, such as
  "hotels near Eiffel Tower," to receive relevant suggestions quickly.
- **Educational institutions search:** Allow users
  to search for schools, colleges, or training centers (for example, "elementary
  schools" or "universities"), a helpful tool for parents or students.

## Understand the request

The Search Text API request allows various parameters to refine the search. Optional
parameters enable additional features, location biasing, filtering criteria, language
preferences, and result limits. For more details, refer to the Search Text API
Reference.

The request includes the following key parameters:

**Authentication**

The `Key` parameter is optional if other authentication methods
are used.

- `Key`: API key for authorization.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md").

**Querying**

Parameters used for specifying the text search and location bias.

- `QueryText`: Free-form text for searching
  places.
- `QueryId`: Enables completion of suggested queries from
  the Suggest API.
- `BiasPosition`: Prioritizes results near a specific
  longitude and latitude.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md").

**Refining Results**

Filters results to narrow down search criteria.

- `Filter`: Allows filtering by bounding box or circular
  area to limit search results.

For more details, see [Filtering](places-filtering.md "places-filtering.md").

**Internationalization and Localization**

Options for customizing the language and applying a political view to the
results.

- `Language`: Specifies the language of the
  results.
- `PoliticalView`: Applies a political view reflecting
  territorial claims.

For more information, see [Localization and
internationalization](places-localization-internationalization.md "places-localization-internationalization.md").

**Additional Features**

Requests extra data such as time zone information.

- `AdditionalFeatures`: Option to request additional data
  such as time zone details.

For more information, see [Additional features](additional-features.md "additional-features.md").

## Understand the response

The response from the Search Text API includes detailed results that match the query,
with information on location, address details, business chains, contacts, phonemes, time
zone, and opening hours. For more details, refer to the Search Text API
Reference.

The response includes the following key data:

**Address and Related Details**

Comprehensive address information for the returned location.

- `Address`: Includes country, street, and other address
  details.

**Place Types and Categories**

Describes the type and category of the place.

- `Categories`: A list of categories describing the
  place, such as _Restaurants_ or
  _Schools_.
- `PlaceType`: Specifies the type of place, such as a
  city, address, or region.
- `BusinessChains`: Indicates any associated business
  chains.

**Additional Details**

Additional data related to the place, as requested.

- `Contacts`: Provides emails, phone numbers, and
  websites.
- `OpeningHours`: Operational hours of the place.
- `AccessPoints`: Geographic coordinates associated with
  the place.
- `Phonemes`: Phonetic representations of address
  components.
- `TimeZone`: Time zone information, including
  offset.
