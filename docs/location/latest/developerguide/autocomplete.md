# Autocomplete

The Autocomplete API completes potential places and addresses as the user types, based on
partial input. It enhances the efficiency and accuracy of address entry by completing
queries with valid address information after a few keystrokes. Additionally, Autocomplete
supports result filtering based on geographic location, country, or specific place types and
can be tailored using optional parameters such as language and political view.

By default, Autocomplete returns only the `ID` and `Title` fields,
providing a cost-effective option. Additional address components and highlights can be
requested by setting `additionalFeatures` to `Core`.

###### Note

- Refer to [Places pricing](places-pricing.md "places-pricing.md") for cost details associated with
  stored results.
- Autocomplete does not return geocodes.
- Autocomplete does not support premium Japan data.
  For more information, see [Autocomplete](../APIReference/API_geoplaces_Autocomplete.md "../APIReference/API_geoplaces_Autocomplete.md")
  in the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How
to use Autocomplete](autocomplete-how-to.md "autocomplete-how-to.md").

## Use cases

- **Enhance checkout experience:** Provide
  real-time address completion as customers enter their location on websites or
  apps. Ensure that delivery or pickup locations match known addresses to
  streamline address validation, reduce errors, and create a seamless checkout
  experience.
- **Support customer services:** Offer real-time
  address suggestions for customer services such as contact centers or emergency
  services, streamlining the process of locating accurate addresses and improving
  user satisfaction by reducing the time needed to obtain correct address
  information.

## Understand the request

The Autocomplete request uses optional parameters to refine search results. For more
details, refer to the Autocomplete API Reference.

The request accepts the following key parameters:

**Authentication**

The `Key` parameter is optional if other authentication methods
are used.

- `Key`: Optional parameter for authentication.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md")

**Querying**

Defines the partial text query and geographic bias for result
suggestions.

- `QueryText`: The free-form text query used to find
  location results, this parameter is required.
- `BiasPosition`: Suggests results closest to specified
  longitude and latitude coordinates, this parameter is
  optional.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md")

**Refine results**

Applies filters to restrict results to specific countries or place
types.

- `Filter`: Allows filtering based on specified countries
  or place types.

For more details, see [Filtering](places-filtering.md "places-filtering.md")

## Understand the response

The Autocomplete API returns results as `ResultItems`, each representing a
matched location based on the request parameters. For further details, refer to the
Autocomplete API Reference.

The response includes the following key data:

**Address and related details**

Contains detailed address components for each location.

- `Address`: Provides full address components, including
  street, postal code, and country.

**Result analysis**

Provides analysis data for each result in relation to the input
query.

- `Distance`: Distance from the specified bias position
  to the result.
- `Highlights`: Highlights portions of the query within
  the result for clarity.
