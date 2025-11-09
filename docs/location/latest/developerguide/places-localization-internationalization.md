# Localization and

internationalization

Localization (L10n) and Internationalization (I18n) are key processes in adapting
software, content, or applications for different languages, regions, and views. Here's
an overview in the context of specific factors:

| Filter Type    | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| -------------- | ------- | --------------- | ------------ | --------- | ----------- | ------------- | ------- |
| Language       | Yes     | Yes             | Yes          | N/A       | Yes         | Yes           | Yes     |
| Political View | Yes     | Yes             | Yes          | N/A       | Yes         | Yes           | Yes     |
| Time Zone      | Yes     | Yes             | No           | N/A       | Yes         | Yes           | Yes     |
| Phonemes       | No      | No              | No           | N/A       | Yes         | Yes           | Yes     |

**Language**

The feature allows you to select a preferred response language from
BCP47-compliant codes. It detects the query language based on name variants
and uses the preferred language for unmatched tokens and ambiguous cases. If
no requested language, Places API provides results in the official country
language, but it prioritizes the regional language in regions where it
differs.

As a fallback strategy, Places APIs return addresses in the default
language if some address elements are unavailable in the requested
language.

**Political view**

Places APIs allow you to adapt results to reflect local political
sensitivities or guidelines of the local government. By default, Places APIs
show an international perspective on disputed political boundaries.

- **AR:** Argentina's view on the
  Southern Patagonian Ice Field and Tierra Del Fuego, including the
  Falkland Islands, South Georgia, and South Sandwich Islands.
- **EG:** Egypt's view on Bir Tawil.
- **IN:** India's view on
  Gilgit-Baltistan.
- **KE:** Kenya's view on the Ilemi
  Triangle.
- **MA:** Morocco's view on Western
  Sahara.
- **RU:** Russia's view on
  Crimea.
- **SD:** Sudan's view on the Halaib
  Triangle.
- **RS:** Serbia's view on Kosovo,
  Vukovar, and Sarengrad Islands.
- **SR:** Suriname's view on the
  Courantyne Headwaters and Lawa Headwaters.
- **SY:** Syria's view on the Golan
  Heights.
- **TR:** Turkey's view on Cyprus and
  Northern Cyprus.
- **TZ:** Tanzania's view on Lake
  Malawi.
- **UY:** Uruguay's view on Rincon de
  Artigas.
- **VN:** Vietnam's view on the Paracel
  Islands and Spratly Islands.

**Time zone**

The feature provides additional time zone information. This includes time
zone names and UTC offsets.

**Phonemes**

The feature provides additional phoneme information on how to pronounce
the various components of the address or place.
