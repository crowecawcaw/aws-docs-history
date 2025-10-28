# Error

messages and resolutions for Amazon Connect Customer Profiles calculated attributes

The following table shows calculated attributes error messages, cause, and
resolution for each error.

| Error message                                                        | Cause                                                                                                                                | Resolution                                                                                                 |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Retrieval of a calculated attribute for a profile shows a null value | This is likely due to the calculated attribute not having data. After creation of a calculated attribute, new data must be ingested. | Ingest new data or re-ingest old data via integrations or the `CreateProfile` and `PutProfileObject` APIs. |
