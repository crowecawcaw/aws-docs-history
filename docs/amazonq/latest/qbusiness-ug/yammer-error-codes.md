# Understand error codes in the Microsoft Yammer connector

The following table provides information about error codes you may see for the
Microsoft Yammer connector and suggested resolutions.

| Error code | Error message                                                                             | Suggested resolution                                                                           |
| ---------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| YMR-5001   | Authentication error.                                                                     | Provide a valid client id, client secret, username, password.                                  |
| YMR-5002   | Error validating credentials due to invalid username or password.                         | Provide a valid username and password.                                                         |
| YMR-5003   | Error validating credentials due to invalid client id or client secret.                   | Provide valid client id and client secret.                                                     |
| YMR-5004   | Access token is empty or null .                                                           | Provide non-empty or non-null access token .                                                   |
| YMR-5100   | Null/empty client id.                                                                     | Provide client id.                                                                             |
| YMR-5101   | Null/empty client secret.                                                                 | Provide client secret.                                                                         |
| YMR-5102   | Null/empty username.                                                                      | Provide username.                                                                              |
| YMR-5103   | Null/empty password.                                                                      | Provide password .                                                                             |
| YMR-5104   | Null/empty since date.                                                                    | Provide sinceDate .                                                                            |
| YMR-5105   | invalid sinceDate format.                                                                 | since date format should be like YYYY-MM-DDTHH:mm:ss+00:00.                                    |
| YMR-5106   | Empty/null Repository configurations.                                                     | Provide Repository configurations.                                                             |
| YMR-5107   | Empty/null message entity in repository configuration.                                    | Provide message entity in repository configuration.                                            |
| YMR-5108   | Empty/null Attachment entity in repository configuration.                                 | Provide attachment entity in repository configuration.                                         |
| YMR-5109   | Empty/null message entity field mapping.                                                  | Provide message entity field mapping.                                                          |
| YMR-5110   | Empty/null attachment entity field mapping.                                               | Provide attachment entity field mapping.                                                       |
| YMR-5111   | Empty/null indexFieldName, indexFieldType or dataSourceFieldName in message<br>entity.    | Provide value for indexFieldName, indexFieldType and dataSourceFieldName in<br>message entity. |
| YMR-5112   | Empty/null indexFieldName, indexFieldType or dataSourceFieldName in attachment<br>entity. | Provide value for indexFieldName, indexFieldType and dataSourceFieldName in<br>message entity. |
| YMR-5113   | Invalid patterns in the regex.                                                            | Provide valid regex patterns.                                                                  |
| YMR-5114   | Since date should be less than current date.                                              | Provide since date less than current date.                                                     |
| YMR-5115   | Only String, Date and Long formats are supported for field mappings.                      | Provide String, Date and Long formats for field mappings.                                      |
| YMR-5116   | Null/empty Network Domain.                                                                | Provide Network Domain.                                                                        |
| YMR-5117   | Got error while building groups.                                                          | Refer to logs for more information.                                                            |
| YMR-5118   | Configuration found null during change access token.                                      | Please provide valid configurations.                                                           |
| YMR-5119   | Unable to connect to Yammer account.                                                      | Refer to logs for more details.                                                                |
| YMR-5120   | An error occurred during the test connection.                                             | Refer to logs for more details.                                                                |
| YMR-5500   | Bad zip entry.                                                                            | Provide a valid zip file.                                                                      |
| YMR-5501   | Invalid URI.                                                                              | Provide valid URI.                                                                             |
| YMR-5502   | ContinuableInternalServerError.                                                           | Try again later.                                                                               |
