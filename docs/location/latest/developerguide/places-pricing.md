# Places pricing

The price for the Place APIs is based on the number of API requests. The unit price
for each API request depends on the response fields you request in your API request and
the intended use for the result. For pricing information for the API and pricing
buckets, see [Amazon Location Service pricing
page](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/").

There are four pricing buckets for Place APIs: **Label**,
**Core**, **Advanced**,
and **Stored**.

## Label

The Label pricing bucket provides a cost-effective option to get address text and
PlaceID only. When you call the Autocomplete and Suggest APIs with
`additionalFeature = []` or non-existent, the API returns PlaceID
(can be used to in a GetPlace request to retrieve additional information),
PlaceType, Title, and Address Label fields for both APIs, and QueryRefinements,
QueryType, and QueryId for Suggest API. In this case, you will be charged at the
Label price. Results cannot be stored permanently for this pricing bucket. See
Stored pricing bucket for long-term use cases.

## Core

The Core pricing bucket supports the most common use cases for Place APIs. When
you call the following, you will still be charged at the Core price:

- `SearchText`, `Geocode`,
  `ReverseGeocode`, `SearchNearby`,
  `GetPlace` API with `additionalFeature` =
  `[]` or nonexistent
- `Autocomplete` and `Suggest` APIs with
  `additionalFeature` = `Core`
- `Geocode` with `additionalFeature` =
  `SecondaryAddresses` or `Intersections`
- `ReverseGeocode` with `additionalFeature` =
  `Intersections`
- `GetPlace` with `additionalFeature` =
  `SecondaryAddresses`

The API returns full address components, categories, and other place details (when
applicable). Refer to [API reference](../APIReference/Welcome.md "../APIReference/Welcome.md") for a
full list of response fields. Results can't be stored permanently for this pricing
bucket, see the [Stored](#stored-pricing "#stored-pricing") bucket for long-term use
cases.

## Advanced

The Advanced pricing bucket provides additional place or points-of-interest
details, such as business hours, contact information, and access points. When you
call SearchText, SearchNearby, GetPlace, Geocode, ReverseGeocode, and Suggest API
and include one of the following values in the `additionalFeature`
request field: Contact, Access, TimeZone, or Phonemes, the API returns corresponding
values for the additional information you have requested (for example,
`opening_hours` and `contact_details`,
`access_restriction` and `access_points`,
`Phonemes`, or `Timezone`). In this case, you will be
charged at the Advanced price. Results can be cached but not stored for long-term
use for this pricing bucket. Results cannot be stored permanently for this pricing
bucket. See Stored pricing bucket for long-term use cases.

## Stored

You can store the Places results indefinitely for long-term use cases, such as
reusing the results to reduce on-demand API calls or for analytical purpose. To do
so, set `intendedUse = Stored` in your API request. In this case, you
will be charged at the Stored price. The Stored pricing bucket supports all the
features listed above, therefore, the maximum price you will be charged for a single
Places API call is capped at the Stored price.
