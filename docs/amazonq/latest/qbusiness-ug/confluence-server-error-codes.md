# Understand error codes in the Amazon Q BusinessConfluence (Server/Data Center) connector

The following table provides information about error codes you may see for the
Confluence (Server/Data Center) connector and suggested resolutions.

| Error code | Error message                                                           | Suggested resolution                                           |
| ---------- | ----------------------------------------------------------------------- | -------------------------------------------------------------- |
| CNF-5500   | Null/empty username.                                                    | Provide username.                                              |
| CNF-5501   | Error validating credentials due to Invalid username or password.       | Provide valid username/password                                |
| CNF-5502   | Null/empty confluence AppKey.                                           | Provide confluence AppKey.                                     |
| CNF-5503   | Null/empty confluence Secret.                                           | Provide confluence Secret.                                     |
| CNF-5504   | Null/empty Client Access Token.                                         | Provide Client Access Token.                                   |
| CNF-5505   | Null/empty Client Refresh Token                                         | Provide Client Refresh Token                                   |
| CNF-5506   | Incorrect auth type.                                                    | Auth type should be Basic or OAuth2 or Personal-token.         |
| CNF-5507   | Null/empty auth type.                                                   | Auth Type should not be null or empty value.                   |
| CNF-5508   | Empty/null host URL.                                                    | Host Url should not be null or empty value.                    |
| CNF-5509   | Null/empty crawl type.                                                  | Crawl Type should not be null or empty value.                  |
| CNF-5510   | Null/empty Repository Configurations.                                   | Repository Configurations should not be null or empty value.   |
| CNF-5511   | Incorrect type.                                                         | type should be SAAS or ON_PREM.                                |
| CNF-5512   | Invalid inclusion file type patterns.                                   | Provide the correct inclusion patterns.                        |
| CNF-5513   | Invalid exclusion file type patterns.                                   | Provide the correct exclusion patterns.                        |
| CNF-5514   | Invalid regex patterns.                                                 | Provide the correct regex patterns.                            |
| CNF-5515   | Error validating credentials due to invalid username or password.       | Provide valid username and password.                           |
| CNF-5516   | Error validating credentials due to invalid client id or client secret. | Provide valid client id and client secret.                     |
| CNF-5517   | Error validating crawl type.                                            | Provide valid crawl type.                                      |
| CNF-5518   | Invalid URI.                                                            | Provide valid URI.                                             |
| CNF-5519   | Null/empty DataSourceFieldName in Space Entity.                         | Provide value for DataSourceFieldName in Space Entity.         |
| CNF-5520   | Null/empty IndexFieldName in Blog Entity.                               | Provide value for IndexFieldName in Blog Entity.               |
| CNF-5521   | Null/empty IndexFieldType in Space Entity.                              | Provide value for IndexFieldType in Space Entity.              |
| CNF-5522   | Null/empty password.                                                    | Provide password.                                              |
| CNF-5523   | Incorrect auth type.                                                    | Auth type should be Basic or OAuth2.                           |
| CNF-5524   | Null/empty DataSourceFieldName in Page Entity.                          | Provide value for DataSourceFieldName in Page Entity.          |
| CNF-5525   | Null/empty DataSourceFieldName in Blog Entity                           | Please provide value for DataSourceFieldName in Blog Entity    |
| CNF-5526   | Null/empty DataSourceFieldName in Comment Entity.                       | Provide value for DataSourceFieldName in Comment Entity.       |
| CNF-5527   | Null/empty DataSourceFieldName in Attachment Entity.                    | Provide value for DataSourceFieldName in Attachment Entity.    |
| CNF-5528   | Null/empty IndexFieldName.                                              | IndexFieldName field can't be null or empty value.             |
| CNF-5529   | Null/empty IndexFieldName in Space Entity.                              | Provide value for IndexFieldName in Space Entity.              |
| CNF-5530   | Null/empty IndexFieldName in Page Entity                                | Please provide value for IndexFieldName in Page Entity         |
| CNF-5531   | Invalid isCrawlPersonalSpace value.                                     | isCrawlPersonalSpace should be a boolean value true or false.  |
| CNF-5532   | Invalid isCrawlArchivedSpace value.                                     | isCrawlArchivedSpace should be a boolean value true or false.  |
| CNF-5533   | Invalid isCrawlArchivedPage value.                                      | isCrawlArchivedPage should be a boolean value true or false.   |
| CNF-5534   | Invalid isCrawlPage value.                                              | isCrawlPage should be a boolean value true or false.           |
| CNF-5535   | Invalid isCrawlBlogComment value.                                       | isCrawlBlogComment should be a boolean value true or false.    |
| CNF-5536   | Invalid isCrawlBlogComment value.                                       | isCrawlBlogComment should be a boolean value true or false.    |
| CNF-5537   | Invalid isCrawlBlogAttachment value.                                    | isCrawlBlogAttachment should be a boolean value true or false. |
| CNF-5538   | Error validating on protocol.                                           | Provide valid protocol.                                        |
| CNF-5539   | Null/empty IndexFieldName in Comment Entity.                            | Provide value for IndexFieldName in Comment Entity.            |
| CNF-5540   | Null/empty Personal Access Token.                                       | Provide Personal Access Token.                                 |
| CNF-5541   | Invalid OAuth value.                                                    | Give a valid OAuth URL.                                        |
| CNF-5542   | Invalid Space value.                                                    | Give a valid Space URL.                                        |
| CNF-5543   | Archived Space Exception.                                               | Check Archived Space.                                          |
| CNF-5544   | JSON Exception for Space.                                               | Check Space.                                                   |
| CNF-5545   | JSON Exception for Comment.                                             | Check Comment.                                                 |
| CNF-5546   | JSON Exception for Comment.                                             | Check Comment.                                                 |
| CNF-5547   | JSON Exception for Comment.                                             | Check Comment.                                                 |
| CNF-5548   | JSON Exception for Attachment.                                          | Check Attachment.                                              |
| CNF-5549   | JSON Exception for Blog.                                                | Check Blog.                                                    |
| CNF-5550   | JSON Exception for Page.                                                | Check Page.                                                    |
| CNF-5551   | JSON Exception for Label.                                               | Check Label.                                                   |
| CNF-5552   | JSON Exception for ACL.                                                 | Check ACL.                                                     |
| CNF-5553   | JSON Exception for Groups.                                              | Check Groups.                                                  |
| CNF-5554   | JSON Exception for Group Members.                                       | Check Group Members.                                           |
| CNF-5555   | JSON Exception for Space Group.                                         | Check Space Group.                                             |
| CNF-5556   | Exception in CommentItem.                                               | Check the CommentItem class.                                   |
| CNF-5557   | Invalid isCrawlPageComment value.                                       | isCrawlPageComment should be a boolean value true or false.    |
| CNF-5558   | Invalid isCrawlPageAttachment value.                                    | isCrawlPageAttachment should be a boolean value true or false. |
| CNF-5559   | Null/empty Repository Configurations.                                   | Repository Configurations should not be null or empty value.   |
| CNF-5560   | Null/empty IndexFieldName in Attachment.                                | Please provide value for IndexFieldName in Attachment Entity.  |
| CNF-5561   | Invalid proxy url.                                                      | Proxy url should not contain http: or https.                   |
| CNF-5562   | Null/Empty proxy port.                                                  | Provide a valid proxy port.                                    |
| CNF-5563   | Invalid Host URL.                                                       | Provide valid Host URL.                                        |
| CNF-5564   | Invalid proxy port value.                                               | Provide a valid proxy port.                                    |
| CNF-5565   | Confluence server not reachable.                                        | Provide a valid proxy and server details.                      |
| CNF-5566   | Null/empty IndexFieldType in Page Entity.                               | Provide value for IndexFieldType in Page Entity.               |
| CNF-5567   | Null/empty IndexFieldType in Blog Entity.                               | Provide value for IndexFieldType in Blog Entity.               |
| CNF-5568   | Null/empty IndexFieldType in Comment Entity.                            | Provide value for IndexFieldType in Comment Entity.            |
| CNF-5569   | Null/empty IndexFieldType in Attachment.                                | Provide value for IndexFieldType in Attachment. Entity         |
| CNF-5570   | JSON Exception for Content Ancestors.                                   | Check your Ancestors.                                          |
| CNF-5571   | Invalid Host URL Pattern.                                               | Provide valid Host URL Pattern.                                |
| CNF-5572   | Error validating credentials due to Invalid access or refresh token.    | Invalid AccessToken/RefreshToken.                              |
