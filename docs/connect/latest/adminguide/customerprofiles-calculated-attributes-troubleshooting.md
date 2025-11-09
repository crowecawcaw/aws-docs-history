# Error

messages and resolutions for Amazon Connect Customer Profiles calculated attributes

The following table shows calculated attributes error messages, cause, and
resolution for each error.

| Error message                                                           | Cause                                                                                                                                      | Resolution                                                                                                       |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Retrieval of a calculated attribute for a profile shows a null<br>value | This is likely due to the calculated attribute not having data.<br>After creation of a calculated attribute, new data must be<br>ingested. | Ingest new data or re-ingest old data via integrations or the<br>`CreateProfile` and `PutProfileObject`<br>APIs. |
