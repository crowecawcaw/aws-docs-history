

# Additional features
<a name="additional-features"></a>

This section provides an overview of additional features supported by the Place APIs. These features provide additional location information by including requested details such as contact information, accessibility, and phonemes. You need to request additional feature by adding `AdditionalFeatures: [ <Value1>, <Value 2>, ..]` in your request payload.

**Note**  
Review [Places pricing](places-pricing.md) for additional information about cost.


| Valid Values | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Core | Default | Default | Yes | Default | Default | Default | Yes | 
| Time Zone | Yes | Yes | No | Yes | Yes | Yes | Yes | 
| Phonemes | No | No | No | Yes | Yes | Yes | Yes | 
| Contacts | No | No | No | Yes | Yes | Yes | No | 
| Opening Hours | No | No | No | Yes | Yes | Yes | No | 
| Access Points | No | Yes | No | Yes | Yes | Yes | Yes | 
| Secondary Addresses | Yes | No | No | Yes | No | No | No | 
| Intersections | Yes | Yes | No | No | No | No | No | 
| Cross-References | No | No | No | Yes | Yes | Yes | Yes | 

To use these additional features, set the `additionalFeatures` parameter in the Place API requests. For more information about additional features, see the Amazon Location Service [GetPlace API reference](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html#API_geoplaces_GetPlace_RequestParameters).
+ For additional information on Time Zone and Phonemes, see [Localization and internationalization](places-localization-internationalization.md).
+ For additional information on Contacts and Opening Hours, see [Contacts and opening hours](contacts-opening-hours.md).

## Definitions
<a name="additional-definitions"></a>

**Time zone**  
Displays the time zone of a given place.

**Phonemes**  
Offers phonetic representations for place names, aiding pronunciation.

**Contacts**  
Provides contact details such as phone numbers and email addresses for places.

**Opening hours**  
An indicator of whether a location is currently open, based on the local time. This information is helpful for users looking for businesses that are open at the time of their query.

**Access points**  
Includes access point information, such as entrances

**Secondary addresses**  
Includes all secondary addresses that are under a main address.

**Intersections**  
Includes nearby intersections.

**Cross-references**  
The list of supplier references available for a place, enabling correlation of places across external systems.