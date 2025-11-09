# Error codes

The following table provides information about error codes you may see for the
Microsoft OneDrive original connector and suggested resolutions.

| Error code | Error message                                                                                               | Suggested resolution                                                                              |
| ---------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| OND-5000   | Exception occurred while sending request to OneDrive api for testing<br>connection, please try again later. | Try again.                                                                                        |
| OND-5001   | Provided client ID key is not Valid.                                                                        | Provide a valid client ID.                                                                        |
| OND-5002   | Provided client secret key is not valid.                                                                    | Provide valid client secret.                                                                      |
| OND-5003   | Provided tenant ID key is not valid.                                                                        | Provide a valid tenant ID.                                                                        |
| OND-5102   | Client ID cannot be null/empty.                                                                             | Provide a valid client ID.                                                                        |
| OND-5103   | Tenant ID cannot be null/empty.                                                                             | Provide a valid tenant Id.                                                                        |
| OND-5104   | Client Secret cannot be null/empty.                                                                         | Provide a valid client Secret.                                                                    |
| OND-5105   | Invalid client ID pattern.                                                                                  | Provide a valid client ID.                                                                        |
| OND-5106   | Client Secret Over maximum length.                                                                          | Length of client secret ID should be at least 256. Provide a valid<br>client secret.              |
| OND-5107   | User Name Filter/ User Name Path should not be null or empty<br>value.                                      | Provide User Name Filter or User Name Path.                                                       |
| OND-5108   | User Name Filter can only support up to 10 users.                                                           | Provide up to 10 users in User Name Filter or provide file of list of<br>users in User Name Path. |
| OND-5109   | Users mentioned in the list do not belong to the same domain.                                               | Provide valid list of users which belong to same domain.                                          |
| OND-5110   | Users mentioned in the list are not valid.                                                                  | Provide valid users.                                                                              |
| OND-5200   | Exception occurred while fetching files in full crawl.                                                      | Check logs for more details.                                                                      |
| OND-5203   | Exception occurred while fetching drive files.                                                              | Provide correct credentials.                                                                      |
| OND-5204   | Exception occurred while fetching OneNote files.                                                            | Check logs for more details.                                                                      |
| OND-5300   | Exception occurred while fetching files in change log.                                                      | Check logs for more details.                                                                      |
| OND-5400   | Exception occurred while building group details.                                                            | Check logs for more details.                                                                      |
| OND-5401   | Exception occurred while fetching list of groups.                                                           | Check logs for more details.                                                                      |
| OND-5500   | Exception occurred while getting file content response.                                                     | Check logs for more details.                                                                      |
| OND-5501   | Only String, String List, Date and Long formats are supported for<br>field mappings.                        | Please provide valid formats in field mappings.                                                   |
| OND-5502   | Exception occurred while fetching OneNote files.                                                            | Check logs for more details.                                                                      |
