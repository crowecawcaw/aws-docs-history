# Understand error codes in the

Zendesk connector

The following table provides information about error codes you may see for the
Zendesk connector and suggested resolutions.

| Error code | Error message                                                                                     | Suggested resolution                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ZND-5001   | Error validating credentials due to invalid username or password.                                 | Provide a valid username/password.                                                                         |
| ZND-5002   | Error validating credentials due to invalid client Id or client<br>Secret.                        | Provide a valid Zendesk client Id or client Secret.                                                        |
| ZND-5100   | The host URL is null or empty.                                                                    | Provide a valid host Url.                                                                                  |
| ZND-5101   | The username is null or empty.                                                                    | Provide a valid username.                                                                                  |
| ZND-5102   | The password is null or empty.                                                                    | Provide a valid password.                                                                                  |
| ZND-5103   | The Zendesk client Id is null or empty.                                                           | Provide a valid client Id.                                                                                 |
| ZND-5104   | The Zendesk client Secret is null or empty.                                                       | Provide a valid client Secret.                                                                             |
| ZND-5105   | Invalid date format for field 'sinceDate'.                                                        | Date format should be yyyy-MM-dd HH:mm:ss.                                                                 |
| ZND-5106   | Invalid value for field 'sinceDate'.                                                              | Since date should not be greater than the current date.                                                    |
| ZND-5107   | The datatype for the index field is invalid.                                                      | Only String, Date and Long formats are supported for field<br>mappings.                                    |
| ZND-5108   | The isCrawTicket value is invalid.                                                                | isCrawTicket should be a boolean value true or false.                                                      |
| ZND-5109   | The isCrawTicketComment value is invalid.                                                         | isCrawTicketComment should be a boolean value true or false.                                               |
| ZND-5110   | The isCrawTicketCommentAttachment value is invalid.                                               | isCrawTicketCommentAttachment should be a boolean value true or<br>false.                                  |
| ZND-5111   | The isCrawlArticle value is invalid.                                                              | isCrawlArticle should be a boolean value true or false.                                                    |
| ZND-5112   | The isCrawlArticleComment value is invalid.                                                       | isCrawlArticleComment should be a boolean value true or false.                                             |
| ZND-5113   | The isCrawlArticleAttachment value is invalid.                                                    | isCrawlArticleAttachment should be a boolean value true or false.                                          |
| ZND-5114   | The isCrawlCommunityTopic value is invalid.                                                       | isCrawlCommunityTopic should be a boolean value true or false.                                             |
| ZND-5115   | The isCrawlCommunityPost value is invalid.                                                        | isCrawlCommunityPost should be a boolean value true or false.                                              |
| ZND-5116   | The isCrawlCommunityPostComment value is invalid.                                                 | isCrawlCommunityPostComment should be a boolean value true or<br>false.                                    |
| ZND-5117   | Repository Configurations is null or empty.                                                       | Repository Configurations should not be null or empty value.                                               |
| ZND-5118   | The Host Url pattern is not valid.                                                                | Provide a valid host url. Ex: 'https://{sub-domain}.zendesk.com/' or<br>'https://{sub-domain}.zendesk.com' |
| ZND-5119   | The URI is invalid.                                                                               | Provide a valid URI.                                                                                       |
| ZND-5120   | The personal access token is null or empty.                                                       | Provide a valid patToken.                                                                                  |
| ZND-5121   | The auth type is incorrect.                                                                       | The auth type should be OAuth2 or Oauth2-ImplicitGrantFlow.                                                |
| ZND-5122   | The accessToken provided is expired, revoked, malformed or<br>invalid.                            | Provide valid accessToken.                                                                                 |
| ZND-5123   | The access token doesn't have sufficient permission.                                              | Check the user has sufficient permission to crawl.                                                         |
| ZND-5500   | Unable to fetch data from Zendesk.                                                                | Check your Zendesk account plan/subscription: it may have<br>expired.                                      |
| ZND-5501   | Unable to generate access token.                                                                  | Check your Zendesk configuration and try again.                                                            |
| ZND-5502   | There was an error parsing the field value. The size has exceeded the<br>maximum allowable limit. | The maximum size permitted is 1000 characters for the fields.                                              |
| ZND-5503   | The url is invalid.                                                                               | Provide valid URL.                                                                                         |
