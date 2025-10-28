# GetPlace

GetPlace retrieves detailed information about a place using its unique
`PlaceId`. The request supports optional parameters for additional features,
such as time zone data or phonemes, and language localization. The API returns information
like address, coordinates, business details, contact methods, and time zone
information.

###### Note

If results are stored, they will be billed at the higher Storage pricing tier. Use the
`IntendedUse` parameter to specify whether the results are for single use
or storage. Refer to [Places pricing](places-pricing.md "places-pricing.md") for cost details associated with
stored results.

For more information, see [GetPlace](../APIReference/API_geoplaces_GetPlace.md "../APIReference/API_geoplaces_GetPlace.md") in the
_Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How to use
GetPlace](get-place-how-to.md "get-place-how-to.md").

## Use cases

- **Refresh stored data:** Regularly refresh stored
  data to ensure your application provides accurate, current information. Use the
  GetPlace API to update details about businesses and places, ensuring users have
  the latest information. For example, refresh opening hours, contact details, and
  user reviews for local restaurants or shops to enhance user trust and
  application functionality.
- **Retrieve place details after typeahead
  suggestions:** Improve user experience by integrating the GetPlace
  API with autocomplete or suggestion features. As users type an address, business
  name, or point of interest, suggestions provide relevant places, and GetPlace
  enables access to more detailed information once a selection is made.

## Understand the request

The GetPlace API request requires specific parameters, such as the
`PlaceId`, and supports optional parameters for additional features or
language localization. These parameters help tailor the results based on language,
intended use, and geographic context. For more details, refer to the GetPlace API
Reference.

The request accepts the following key parameters:

**Authentication**

The `Key` parameter is optional if other authentication methods
are used.

- `Key`: API key for authorization.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md").

**Querying**

Defines the unique identifier for retrieving place information.

- `PlaceId`: The unique identifier for the place.
  (required)

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md").

**Internationalization and Localization**

Options to customize the language and apply a political view to the
results.

- `Language`: Specifies the language of the
  results.
- `PoliticalView`: Applies a political view reflecting
  territorial claims.

For more information, see [Localization and
internationalization](places-localization-internationalization.md "places-localization-internationalization.md").

**Additional Features**

Requests additional data, such as time zone details.

- `AdditionalFeatures`: Option to request additional
  information like time zone or phoneme details.

For more information, see [Additional features](additional-features.md "additional-features.md").

## Understand the response

The response from the GetPlace API includes basic data, such as the address,
coordinates, and business details, as well as additional data based on the request
parameters. Information like access restrictions, time zones, and phoneme details for
pronunciation can also be provided. For further details, refer to the GetPlace API
Reference.

The response includes the following key data:

**Address and Related Details**

Provides complete address details for the location.

- `Address`: Full address information, including country,
  region, and postal code.
- `PostalCodeDetails`: Additional information about
  postal codes and authorities.

**Place Types and Categories**

Describes the type and category of the place.

- `BusinessChains`: Information on any associated
  business chains.
- `Categories`: Categories to which the place belongs,
  such as food or retail.
- `PlaceType`: Type of the place, such as point of
  interest or locality.

**Additional Details**

Provides additional data about the place, as specified in the
request.

- `Contacts`: Contact methods, including phone numbers,
  emails, and websites.
- `OpeningHours`: Business hours or access times.
- `AccessPoints`: Geographic coordinates (longitude and
  latitude) of access points.
- `Phonemes`: Pronunciations for various address
  components.
- `TimeZone`: Time zone information, including
  offset.
