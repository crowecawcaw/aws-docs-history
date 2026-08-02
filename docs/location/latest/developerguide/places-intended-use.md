# IntendedUse

###### Note

If you store results, the higher storage pricing
tier applies. Use the request parameter `IntendedUse` to specify whether the results
are for single use or storage. For more information about costs associated with stored results, see [Places pricing](places-pricing.md "places-pricing.md").

When you call a place API, specify `IntendedUse` by setting the value to be
either `SingleUse` or `Storage`, based on the intended use of the
results. If you are going to store the results (even for caching purposes), you must
choose the _storage_ option, not the _single use_ option.

| Filter Type | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| ----------- | ------- | --------------- | ------------ | --------- | ----------- | ------------- | ------- |
| SingleUse   | Yes     | Yes             | Yes          | Yes       | Yes         | Yes           | Yes     |
| Storage     | Yes     | Yes             | No           | Yes       | Yes         | Yes           | No      |
