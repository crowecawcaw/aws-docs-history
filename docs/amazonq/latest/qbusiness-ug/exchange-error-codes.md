# Understand error codes in the Microsoft Exchange connector

The following table provides information about error codes you may see for the
Microsoft Exchange connector and suggested resolutions.

| Error code | Error message                                                                     | Suggested resolution                                                                                                          |
| ---------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| MSE-5101   | Exception occurred while validating the configurations.                           | Error occurred while validating the configurations. Verify the<br>configurations and try again.                               |
| MSE-5102   | Invalid clientId pattern.                                                         | Error occurred while validating the configurations. Verify the<br>configurations and try again.                               |
| MSE-5103   | ClientSecret Over maximum length.                                                 | Error occurred while validating the configurations. Verify the<br>configurations and try again.                               |
| MSE-5104   | Enter valid credentials. Client ID should not be null or<br>empty.                | Error occurred while validating the configurations. Client ID should<br>not be null.                                          |
| MSE-5105   | Enter valid credentials. Client Secret should not be null or<br>empty.            | Error occurred while validating the configurations. Client Secret<br>should not be null.                                      |
| MSE-5106   | Enter valid credentials. Tenant ID should not be null or<br>empty                 | Error occurred while validating the configurations. Tenant ID should<br>not be null.                                          |
| MSE-5107   | The provided client ID is invalid.Please verify the client ID and try<br>again.   | Provide client id is invalid while doing authentication. Connection<br>will be unsuccessful. Provide valid client id.         |
| MSE-5108   | The provided client secret is invalid. Verify the client secret and<br>try again. | Provide client secret is invalid while doing authentication.<br>Connection will be unsuccessful. Provide valid client secret. |
| MSE-5109   | The provided tenant ID is invalid. Please verify the tenant ID and<br>try again.  | Provide tenant ID is invalid while doing authentication. Connection<br>will be unsuccessful. Provide valid tenant ID.         |
| MSE-5200   | Got exception from customer while accessing the list of<br>users.                 | Error occurred while fetching the list of users from Microsoft Graph<br>API. Check logs for more details.                     |
| MSE-5201   | Got exception from customer while accessing mails.                                | Error occurred while fetching mails from Microsoft Graph API. Check<br>logs for more details.                                 |
| MSE-5202   | Got exception from customer while accessing calendar events.                      | Error occurred while fetching calendar events from Microsoft Graph<br>API. Check logs for more details.                       |
| MSE-5203   | Got exception from customer while accessing OneNotes.                             | Error occurred while fetching one notes from Microsoft Graph API.<br>Check logs for more details.                             |
| MSE-5204   | Got exception from customer while accessing attachments.                          | Error occurred while fetching attachments from Microsoft Graph API.<br>Check logs for more details.                           |
| MSE-5205   | Got exception from customer while accessing contacts.                             | Error occurred while fetching contacts from Microsoft Graph API.<br>Check logs for more details.                              |
| MSE-5206   | Error occurred while retrying API requests.                                       | Error occurred while retrying API requests to fetch data from<br>Microsoft Graph API.                                         |
| MSE-5301   | Got exception from customer while running changelog mode.                         | Error occurred while handling changelog token. Refer logs or contact<br>connector team for more information.                  |
