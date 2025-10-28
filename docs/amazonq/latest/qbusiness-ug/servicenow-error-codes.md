# Understand error codes in the Amazon Q Business ServiceNow Online connector

The following table provides information about error codes you may see for the
ServiceNow Online connector and suggested resolutions.

| Error code | Error message                                                                                   | Suggested resolution                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| SRN-5001   | Error validating credentials due to invalid client id or client secret or username or password. | Provide a valid client id/client secret/username/password.                                         |
| SRN-5002   | Error validating credentials due to invalid username or password.                               | Provide a valid username/password.                                                                 |
| SRN-5003   | Access token is empty or null.                                                                  | Provide a non empty or non null access token.                                                      |
| SRN-5004   | Client ID exceeded the allowed length.                                                          | Provide a valid Client ID.                                                                         |
| SRN-5005   | Client Secret exceeded the allowed length.                                                      | Provide a valid Client Secret.                                                                     |
| SRN-5006   | Password exceeded the allowed length.                                                           | Provide a valid Password.                                                                          |
| SRN-5007   | clientSecret contains non-printable Ascii characters.                                           | Provide a valid clientSecret.                                                                      |
| SRN-5008   | clientId contains non-printable Ascii characters.                                               | Provide a valid clientId.                                                                          |
| SRN-5010   | Error validating credentials due to invalid username or password.                               | Provide a valid username/password.                                                                 |
| SRN-5011   | Amazon Q can't connect to the ServiceNow server with the specified credentials.                 | Provide admin credentials and try your request again.                                              |
| SRN-5014   | ServiceNow instance is not available.                                                           | Check your ServiceNow instance before crawling.                                                    |
| SRN-5100   | Client id should not be empty.                                                                  | Provide a valid client id.                                                                         |
| SRN-5101   | Client secret should not be empty.                                                              | Provide a valid client secret.                                                                     |
| SRN-5102   | User name should not be empty.                                                                  | Provide a valid username.                                                                          |
| SRN-5103   | Password should not be empty.                                                                   | Provide a valid password.                                                                          |
| SRN-5104   | Auth type should not be empty.                                                                  | Provide an auth Type.                                                                              |
| SRN-5105   | Incorrect auth type.                                                                            | Auth type should be basicAuth or OAuth2.                                                           |
| SRN-5106   | Host url should not be empty.                                                                   | Provide a valid host url.                                                                          |
| SRN-5120   | crawlType should not be empty.                                                                  | crawlType should be FORCED_FULL_CRAWL or FULL_CRAWL or CHANGE_LOG.                                 |
| SRN-5122   | isCrawlKnowledgeArticle should not be empty.                                                    | Provide valid isCrawlKnowledgeArticle.                                                             |
| SRN-5123   | Invalid isCrawlKnowledgeArticle value.                                                          | isCrawlKnowledgeArticle should be true or false.                                                   |
| SRN-5124   | isCrawlKnowledgeArticleAttachment should not be empty.                                          | Provide valid isCrawlKnowledgeArticleAttachment.                                                   |
| SRN-5125   | Invalid isCrawlKnowledgeArticleAttachment value.                                                | isCrawlKnowledgeArticleAttachment should be true or false.                                         |
| SRN-5126   | isCrawlServiceCatalog should not be empty.                                                      | Provide valid isCrawlServiceCatalog.                                                               |
| SRN-5127   | invalid isCrawlServiceCatalog value.                                                            | isCrawlServiceCatalog should be true or false.                                                     |
| SRN-5128   | isCrawlServiceCatalogAttachment should not be empty.                                            | Provide valid isCrawlServiceCatalogAttachment.                                                     |
| SRN-5129   | Invalid isCrawlServiceCatalogAttachment value.                                                  | isCrawlServiceCatalogAttachment should be true or false.                                           |
| SRN-5130   | isCrawlIncident should not be empty.                                                            | Provide valid isCrawlIncident.                                                                     |
| SRN-5131   | invalid isCrawlIncident value.                                                                  | isCrawlIncident should be true or false.                                                           |
| SRN-5132   | isCrawlIncidentAttachment should not be empty.                                                  | Provide valid isCrawlIncidentAttachment.                                                           |
| SRN-5133   | Invalid isCrawlIncidentAttachment value.                                                        | isCrawlIncidentAttachment should be true or false.                                                 |
| SRN-5134   | Invalid incidentStateType.                                                                      | Invalid incidentStateType. Incident State Type should be All, Open, Open - Unassigned or Resolved. |
| SRN-5135   | applyACLForKnowledgeArticle should not be empty.                                                | Provide valid applyACLForKnowledgeArticle.                                                         |
| SRN-5136   | applyACLForServiceCatalog should not be empty.                                                  | Provide valid applyACLForServiceCatalog.                                                           |
| SRN-5137   | applyACLForIncident should not be empty.                                                        | Provide valid applyACLForIncident.                                                                 |
| SRN-5138   | Invalid applyACLForKnowledgeArticle value.                                                      | applyACLForKnowledgeArticle should be true or false.                                               |
| SRN-5139   | Invalid applyACLForServiceCatalog value.                                                        | applyACLForServiceCatalog should be true or false.                                                 |
| SRN-5140   | Invalid applyACLForIncident value.                                                              | applyACLForIncident should be true or false.                                                       |
| SRN-5141   | invalid pattern :”file type pattern”                                                            | Provide valid patterns.                                                                            |
| SRN-5142   | includePublicArticlesOnly should not be empty.                                                  | Provide valid includePublicArticlesOnly.                                                           |
| SRN-5143   | Invalid includePublicArticlesOnly value.                                                        | includePublicArticlesOnly should be true or false.                                                 |
| SRN-5144   | Invalid URI.                                                                                    | Provide valid URI.                                                                                 |
| SRN-5145   | isCrawlActiveServiceCatalog should not be empty.                                                | Provide valid isCrawlActiveServiceCatalog.                                                         |
| SRN-5146   | isCrawlInActiveServiceCatalog should not be empty.                                              | Provide valid isCrawlInactiveServiceCatalog.                                                       |
| SRN-5147   | isCrawlActiveIncident should not be empty.                                                      | Provide valid isCrawlActiveIncident.                                                               |
| SRN-5148   | isCrawlInActiveIncident should not be empty.                                                    | Provide valid isCrawlInactiveIncident.                                                             |
| SRN-5149   | Invalid isCrawlActiveServiceCatalog value.                                                      | isCrawlActiveServiceCatalog should be true or false.                                               |
| SRN-5150   | Invalid isCrawlInactiveServiceCatalog value.                                                    | isCrawlInactiveServiceCatalog should be true or false.                                             |
| SRN-5151   | Invalid isCrawlActiveIncident value.                                                            | isCrawlActiveIncident should be true or false.                                                     |
| SRN-5152   | Invalid isCrawlInactiveIncident value.                                                          | isCrawlInactiveIncident should be true or false.                                                   |
| SRN-5153   | servicenowInstanceVersion should not be empty.                                                  | Provide a valid servicenowInstanceVersion.                                                         |
| SRN-5154   | The ServiceNow host name is invalid.                                                            | The ServiceNow host name should follow the format: example.service-now.com                         |
| SRN-5501   | continuableInternalServerError.                                                                 | Try again later.                                                                                   |
