

# Time zone
<a name="places-timezone"></a>

Amazon Location Service Places APIs support time zone retrieval as an additional feature. When you include `TimeZone` in the `AdditionalFeatures` request parameter, the API response includes time zone information for the location, such as the IANA time zone name, UTC offset, and current offset (accounting for daylight saving time).

## Benefits
<a name="timezone-benefits"></a>

The following are key benefits of using the time zone feature.

**Accurate scheduling across regions**  
Coordinate events, deliveries, or services across multiple time zones by determining the exact local time for any location.

**Localized user experiences**  
Display local times in travel, logistics, or e-commerce applications to provide users with contextually relevant information.

**Compliance and record-keeping**  
Ensure that timestamps in billing, regulatory, and audit records reflect the correct local time for each transaction location.

**Daylight saving time awareness**  
Account for daylight saving time transitions by using the current UTC offset, which reflects seasonal adjustments.

## Supported APIs
<a name="timezone-supported-apis"></a>

The following Places APIs support the `TimeZone` additional feature.
+ **Geocode** — Determine the time zone for a city or address. For more information, see [How to geocode for the time zone of a city](how-to-geocode-timezone.md).
+ **Reverse Geocode** — Identify the time zone for a set of coordinates. For more information, see [How to reverse geocode for the time zone of a city](how-to-reverse-geocode-timezone.md).
+ **GetPlace** — Retrieve time zone details for a specific `PlaceId`. For more information, see [How to get the time zone for a PlaceId](how-to-get-timezone-by-place-id.md).
+ **SearchText** — Include time zone data in text-based place search results.
+ **SearchNearby** — Include time zone data in proximity-based search results.
+ **Suggest** — Include time zone data in search suggestion results.