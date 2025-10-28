# Suggest

Suggest provides predictions or recommendations based on user input or context, such as
relevant places, points of interest, query terms, or search categories. It assists users in
finding places, points of interest, or identifying follow-up queries based on incomplete or
misspelled input. The API returns a list of possible matches or refinements, which can be
used to formulate a more accurate query. Users can select the appropriate suggestion for
further searching. The API supports filtering results by location and other attributes and
offers additional features like phonemes and time zones. The response includes refined query
terms and detailed place information.

###### Note

By default, the Suggest API returns only `ID` and `Title`
fields, providing a cost-effective option. Additional address components and highlights
can be requested by setting `additionalFeatures` to `Core`. Refer
to [Places pricing](places-pricing.md "places-pricing.md") for cost implications related to stored
results.

For more information, see [Suggest](../APIReference/API_geoplaces_Suggest.md "../APIReference/API_geoplaces_Suggest.md") in the
_Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
Suggest](suggest-how-to.md "suggest-how-to.md").

## Use cases

- **Ride-Hailing Services:** Provide real-time
  suggestions to quickly complete addresses for pick-up and drop-off locations,
  ensuring accuracy and faster ride booking.
- **Travel and Navigation Services:** Offer
  real-time predictions for locations or landmarks, even for misspelled or
  partially entered terms, such as "Eifel" for "Eiffel Tower." The API refines
  suggestions to offer relevant nearby points of interest, helping users locate
  places accurately.
- **Restaurant Search Assistance:** Anticipate
  users' interests in restaurants and suggest nearby dining options, enhancing the
  search experience.

## Understand the request

The Suggest API request uses parameters to generate suggestions based on user input.
Optional parameters allow for refined search results using location bias and filtering
criteria. For more details, refer to the Suggest API Reference.

The request includes the following key parameters:

**Authentication**

The `Key` parameter is optional if other authentication methods
are used.

- `Key`: API key for authorization.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md")

**Querying**

Defines the free-text search and location bias.

- `QueryText`: Free-form text for generating suggestions.
  (required)
- `BiasPosition`: Prioritizes suggestions near a specific
  longitude and latitude.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md")

**Refining results**

Filters results to narrow down search criteria.

- `Filter`: Allows filtering by bounding box or circular
  area to limit search results.

For more details, see [Filtering](places-filtering.md "places-filtering.md")

**Internationalization and Localization**

Options for customizing the language and applying a political view to the
results.

- `Language`: Specifies the language of the
  results.
- `PoliticalView`: Applies a political view reflecting
  territorial claims.

For more information, see [Localization and
internationalization](places-localization-internationalization.md "places-localization-internationalization.md")

**Additional features**

Requests extra data, such as time zone information.

- `AdditionalFeatures`: Option to request additional
  details such as time zone or phonetic data.

For more information, see [Additional features](additional-features.md "additional-features.md")

**Limiting results**

Sets limits on the number of results or query refinements returned.

- `MaxQueryRefinements`: Limits the number of query
  refinement terms returned.
- `MaxResults`: Limits the number of suggestions
  returned.

## Understand the response

The response provides suggested addresses or places based on the input query, with
attributes such as location, address details, business chains, contacts, phonemes, time
zone, and opening hours. The API returns `ResultItems`, representing possible
matches for completing the input query. There are two types of results, identified by
`SuggestResultItemType`: results of type `Query` suggest a
follow-up category or chain query, which can be used to obtain focused results for a
specified category by passing the `QueryID` to the SearchText API. Results of
type `Place` provide a final result with an address and additional
information about the place. For further details, refer to the API Reference for Suggest
API.

The response includes the following key data:

**Result analysis**

Provides information on refining the input query.

- `QueryRefinements`: Terms that can be used to refine
  the search query.
- `Highlights`: Highlights parts of the address or title
  that match the query.

**Place types and categories**

Describes the type and category of the place.

- `Categories`: Categories describing the place, such as
  _Restaurants_ or
  _Schools_.
- `PlaceType`: Specifies the type of place, such as a
  city, address, or region.
- `BusinessChains`: Indicates any associated business
  chains.

**Additional details**

Additional information about the place, as specified in the
request.

- `Contacts`: Provides emails, phone numbers, and
  websites.
- `OpeningHours`: Operational hours of the place.
- `AccessPoints`: Geographic coordinates associated with
  the place.
- `Phonemes`: Phonetic representations of address
  components.
- `TimeZone`: Time zone information, including
  offset.
