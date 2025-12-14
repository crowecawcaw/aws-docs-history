# Quotas for AWS Account Management

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is AWS Region-specific.

Each AWS account has the following quotas related to Account Management.

| Resource                                                                   | Quota                                                          |
| -------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Maximum number of `StartPrimaryEmailUpdate` requests per<br>target account | 3 per 30 seconds                                               |
| Number of alternate contacts in an AWS account                             | 3<br>• one each for `BILLING`, `SECURITY`, and<br>`OPERATIONS` |
| Number of concurrent region-opt requests per account                       | 6                                                              |
| Number of concurrent region-opt requests per organization                  | 50                                                             |
| Rate of `AcceptPrimaryEmailUpdate` requests per caller<br>account          | 1 per second, burst to 1 per second                            |
| Rate of `DeleteAlternateContact` requests per account                      | 1 per second, burst to 6 per second                            |
| Rate of `DisableRegion` requests per account                               | 1 per second, burst to 1 per second                            |
| Rate of `EnableRegion` requests per account                                | 1 per second, burst to 1 per second                            |
| Rate of `GetAccountInformation` requests per<br>caller account             | 3 per second, burst to 3 per second                            |
| Rate of `GetAlternateContact` requests per account                         | 10 per second, burst to 15 per second                          |
| Rate of `GetContactInformation` requests per account                       | 10 per second, burst to 15 per second                          |
| Rate of `GetGovCloudAccountInformation` requests per account               | 3 per second, burst to 5 per second                            |
| Rate of `GetPrimaryEmail` requests per caller account                      | 3 per second, burst to 3 per second                            |
| Rate of `GetRegionOptStatus` requests per account                          | 5 per second, burst to 5 per second                            |
| Rate of `ListRegions` requests per account                                 | 5 per second, burst to 5 per second                            |
| Rate of `PutAccountName` requests per caller account                       | 1 per second, burst to 1 per second                            |
| Rate of `PutAlternateContact` requests per account                         | 5 per second, burst to 8 per second                            |
| Rate of `PutContactInformation` requests per account                       | 5 per second, burst to 8 per second                            |
| Rate of `StartPrimaryEmailUpdate` requests per caller<br>account           | 1 per second, burst to 1 per second                            |
