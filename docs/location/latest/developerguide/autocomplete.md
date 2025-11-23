# Autocomplete

`Autocomplete` returns complete addresses and address components based on partial input.
Key use cases include address form auto-filling and typeahead address completion
(completing the address interactively while the end user is typing it).

###### Note

By default, only the place ID, place type, and label attributes are returned for each result.
Rich additional detail, including the full address breakdown and input highlight ranges for interactive
use cases can be obtained by setting the `AdditionalFeatures` input attribute, but note that requesting
additional features may impact [Places pricing](places-pricing.md "places-pricing.md")

###### Note

Japanese addresses are not supported.

Results are always addresses, or address components such as streets, postal codes, and countries. Points of interest are never returned.
Results do not include geocodes, since `Autocomplete` is focused on address completion, not geocoding.
To get address geocode coordinates, use the [Geocode](geocode.md "geocode.md") operation.Results can be filtered by geographic area.
They can also be filtered by place type, for example to include only localities or only postal codes.

For full details on all the Autocomplete request and response attributes, please, see[Autocomplete](../APIReference/API_geoplaces_Autocomplete.md "../APIReference/API_geoplaces_Autocomplete.md")
in the _Amazon Location Service API Reference_.

For example requests, responses, cURL, and CLI commands for this API, see [How
to use Autocomplete](autocomplete-how-to.md "autocomplete-how-to.md").

## Use cases

- **Enhance checkout experience:** Provide real-time address completion as customers enter their addresses
  in e-commerce checkout experiences and other address entry experiences on websites or apps.
  Ensure that delivery or pick-up locations match known addresses, reducing costly errors and increasing customer satisfaction.
- **Support customer services:** Give real-time address suggestions to customer service representatives
  in fields such as contact centers and emergency service dispatching, streamlining the process of collecting accurate address information and
  improving user satisfaction by reducing the time needed to obtain correct address information.

## Understand the request

The `Autocomplete` operation supports many optional request attributes to refine the search results.
For the complete list of request attributes, refer to [Autocomplete](../APIReference/API_geoplaces_Autocomplete.md "../APIReference/API_geoplaces_Autocomplete.md")
in the _Amazon Location Service API Reference_.

The request accepts the following key parameters:

**Authentication**

The Autocomplete API operation supports two alternative authentication modes.
You can authenticate either by signing the request with a [SigV4 signature](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
or by providing an [API Key](access.md "access.md").

- If you are making requests using a language-specific AWS SDK or using the AWS CLI, your request will normally be signed with SigV4 by default.
- In some use cases, for example, making requests from a web browser
  or using some other non-AWS SDK client, API keys are a more appropriate form of authentication.
  Use the optional Key request attribute to provide an API key for authenticating to `Autocomplete`.

For more information, see [Authenticate with Amazon Location Service](access.md "access.md")
in the _Amazon Location Service API Reference_.

**Specifying the address to query**

- Use the mandatory `QueryText` request attribute to provide the free-form text to query.
- `BiasPosition`: Use the optional `BiasPosition` request attribute to provide a pin position, as a `[longitude, latitude]` coordinate pair, to improve the relevance of the returned results.

For more information, see [Querying and biasing](places-querying-biasing.md "places-querying-biasing.md")
in the _Amazon Location Service API Reference_.

**Including all response attributes**

Set the optional field AdditionalFeatures to the value ["Core"]
to include all available result attributes in the response, including the full address breakdown and interactive highlight locations.
Note that requesting these extra attributes may impact [pricing](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/")

**Refine results**

Use the Filter attribute to filter the returned results based on specific countries,
place types, or geographic areas. For more details, see [Filtering](places-filtering.md "places-filtering.md")
in the
_Amazon Location Service Developer Guide_.

## Understand the response

The response object contains an array attribute named `ResultItems` that contains the list of results ranked in ascending order of relevance.
For the full list of result item attributes, refer to [Autocomplete](../APIReference/API_geoplaces_Autocomplete.md "../APIReference/API_geoplaces_Autocomplete.md")
in the _Amazon Location Service API Reference_.

The following is a short list of some of the more important result item attributes.

**Address and related details**

- `PlaceType` contains the place type of the result, which tells us whether the address represents a point address, a street, etc. Results returned by
  `Autocomplete` will always have a place type that represents either a complete address or a component of an address,
  like a street or postal code. Results will never include points of interest.
- `Address` contains the result label and, if `["Core"]` is specified for `AdditionalFeatures`,
  it also contains the full breakdown of the address into structured fields including house number, street name, postal code, country, and the like..

**Result analysis**

Provides analysis data for each result in relation to the input
query.

- `Distance`: If a `BiasPosition` was provided in the request,
  each result item contains a `Distance` attribute giving the distance, in meters,
  of that result from the `BiasPosition`. Requires `AdditionalFeatures` to be set to `["Core"]`.
- `Highlights` shows where words, phrases,
  and substrings from the input `QueryText` appear exactly in a result attribute,
  enabling applications to provide helpful user experiences that highlight matches for their users. Requires `AdditionalFeatures` to be set to `["Core"]`.
