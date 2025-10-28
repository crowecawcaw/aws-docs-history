# Reading from LinkedIn entities

**Prerequisites**

A LinkedIn Object you would like to read from. Refer the supported entities table
below to check the available entities.

**Supported entities**

| Entity                          | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------ |
| Ad Accounts                     | Yes             | Yes            | Yes               | Yes                | No                    |
| Campaigns                       | Yes             | Yes            | Yes               | Yes                | No                    |
| Campaign Groups                 | Yes             | Yes            | Yes               | Yes                | No                    |
| Creatives                       | Yes             | Yes            | Yes               | Yes                | No                    |
| Ad Analytics                    | Yes             | No             | No                | Yes                | No                    |
| Ad Analytics All AdAcocunts     | Yes             | No             | No                | Yes                | No                    |
| Ad Analytics All Campaigns      | Yes             | No             | No                | Yes                | No                    |
| Ad Analytics All CampaignGroups | Yes             | No             | No                | Yes                | No                    |
| Ad Analytics All AdCreatives    | Yes             | No             | No                | Yes                | No                    |
| Share Statistics                | Yes             | No             | No                | Yes                | No                    |
| Page Statistics                 | Yes             | No             | No                | Yes                | No                    |
| Follower Statistics             | Yes             | No             | No                | Yes                | No                    | **Example** `netsuiteerp_read = glueContext.create_dynamic_frame.from_options( connection_type="linkedin", connection_options={ "connectionName": "connectionName", "ENTITY_NAME": "adaccounts", "API_VERSION": "202406" } )` LinkedIn entity and field details | **Field Data Type** | **Supported Filter Operators** |
| ---                             | ---             |                | String            | =                  |                       | DateTime                                                                                                                                                                                                                                                        | BETWEEN, =          |
| Numeric                         | =               |                | Boolean           | =                  |
