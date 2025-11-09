# AppClientSummary

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains information about an AppClient.

###### Topics

| Parameter              | Description                                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------ |
| **arn**                | The Amazon Resource Name (ARN) of the AppClient.<br>Type: String<br>Length Constraints: Minimum length of 1. Maximum length of<br>1011.<br>Pattern: `arn:.+`<br>Required: Yes                  |
| **verificationStatus** | The AppClient verification status.<br>Type: String<br>Valid Values: `pending_verification                                                                                                      | verified | <br>rejected`<br>Required: Yes |
| **appClientId**        | The ID of the AppClient. Meant to be used in o-auth flows for<br>the app-client.<br>Type: String<br>Pattern:<br>`[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br>Required: No |
