# Additional features

This section provides an overview of additional features supported by the Place APIs.
These features provide additional location information by including requested details
such as contact information, accessibility, and phonemes. You need to request additional
feature by adding `AdditionalFeatures: [ <Value1>, <Value 2>, ..]` in
your request payload.

###### Note

Review [Places pricing](places-pricing.md "places-pricing.md") for additional information about
cost.

| Valid Values        | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| ------------------- | ------- | --------------- | ------------ | --------- | ----------- | ------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core                | Default | Default         | Yes          | Default   | Default     | Default       | Yes     |
| Time Zone           | Yes     | Yes             | No           | Yes       | Yes         | Yes           | Yes     |
| Phonemes            | No      | No              | No           | Yes       | Yes         | Yes           | Yes     |
| Contacts            | No      | No              | No           | Yes       | Yes         | Yes           | No      |
| Opening Hours       | No      | No              | No           | Yes       | Yes         | Yes           | No      |
| Access Points       | No      | Yes             | No           | Yes       | Yes         | Yes           | Yes     |
| Secondary Addresses | Yes     | Yes             | No           | No        | No          | No            | No      |
| Intersections       | Yes     | Yes             | No           | No        | No          | No            | No      | To use these additional features, set the `additionalFeatures` parameter in the Place API requests. Refer to the Amazon Location Service [API documentation](../APIReference/API_geoplaces_GetPlace.md#API_geoplaces_GetPlace_RequestParameters "../APIReference/API_geoplaces_GetPlace.md#API_geoplaces_GetPlace_RequestParameters") for details. <br>• For additional information on Time Zone and Phonemes, see [Localization and internationalization](places-localization-internationalization.md "places-localization-internationalization.md"). <br>• For additional information on Contacts and Opening Hours, see [Contacts and opening hours](contacts-opening-hours.md "contacts-opening-hours.md"). ## Definitions **Time Zone** Displays the time zone of a given place. **Phonemes** Offers phonetic representations for place names, aiding pronunciation. **Contacts** Provides contact details such as phone numbers and email addresses for places. **Opening Hours** An indicator of whether a location is currently open, based on the local time. This information is helpful for users looking for businesses that are open at the time of their query. **Access Points** Includes access point information, such as entrances **Secondary addresses** Includes all secondary addresses that are under a main address. **Intersections** Includes nearby intersections. |
