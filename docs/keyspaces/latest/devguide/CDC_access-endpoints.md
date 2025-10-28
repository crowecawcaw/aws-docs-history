# How to access CDC stream endpoints in

Amazon Keyspaces

Amazon Keyspaces maintains separate [endpoints](programmatic.md#global_endpoints "programmatic.md#global_endpoints") for
keyspaces/tables and for CDC streams in each AWS Region where Amazon Keyspaces is available. To
access a CDC stream, select the Region of the table and replace the
`cassandra` prefix with `cassandra-streams` in the endpoint name as shown in the
following example:

| Region name               | Region         | Endpoint for keyspaces and tables        | Endpoint for streams                  |
| ------------------------- | -------------- | ---------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | us-east-1      | `cassandra`.us-east-1.api.aws            | `cassandra-streams`.us-east-1.api.aws | The following table contains a complete list of available public endpoints for Amazon Keyspaces change data capture streams. Amazon Keyspaces CDC streams supports both IPv4 and IPv6. All public endpoints, for example `cassandra-streams.us-east-1.api.aws`, are dual stack endpoints that can be configured for IPv4 and IPv6. |
| Region Name               | Region         | Endpoint                                 | Protocol                              |
| ---                       | ---            | ---                                      | ---                                   |
| US East (Ohio)            | us-east-2      | cassandra-streams.us-east-2.api.aws      | HTTPS                                 |
| US East (N. Virginia)     | us-east-1      | cassandra-streams.us-east-1.api.aws      | HTTPS                                 |
| US West (N. California)   | us-west-1      | cassandra-streams.us-west-1.api.aws      | HTTPS                                 |
| US West (Oregon)          | us-west-2      | cassandra-streams.us-west-2.api.aws      | HTTPS                                 |
| Africa (Cape Town)        | af-south-1     | cassandra-streams.af-south-1.api.aws     | HTTPS                                 |
| Asia Pacific (Hong Kong)  | ap-east-1      | cassandra-streams.ap-east-1.api.aws      | HTTPS                                 |
| Asia Pacific (Mumbai)     | ap-south-1     | cassandra-streams.ap-south-1.api.aws     | HTTPS                                 |
| Asia Pacific (Seoul)      | ap-northeast-2 | cassandra-streams.ap-northeast-2.api.aws | HTTPS                                 |
| Asia Pacific (Singapore)  | ap-southeast-1 | cassandra-streams.ap-southeast-1.api.aws | HTTPS                                 |
| Asia Pacific (Sydney)     | ap-southeast-2 | cassandra-streams.ap-southeast-2.api.aws | HTTPS                                 |
| Asia Pacific (Tokyo)      | ap-northeast-1 | cassandra-streams.ap-northeast-1.api.aws | HTTPS                                 |
| Canada (Central)          | ca-central-1   | cassandra-streams.ca-central-1.api.aws   | HTTPS                                 |
| Europe (Frankfurt)        | eu-central-1   | cassandra-streams.eu-central-1.api.aws   | HTTPS                                 |
| Europe (Ireland)          | eu-west-1      | cassandra-streams.eu-west-1.api.aws      | HTTPS                                 |
| Europe (London)           | eu-west-2      | cassandra-streams.eu-west-2.api.aws      | HTTPS                                 |
| Europe (Paris)            | eu-west-3      | cassandra-streams.eu-west-3.api.aws      | HTTPS                                 |
| Europe (Stockholm)        | eu-north-1     | cassandra-streams.eu-north-1.api.aws     | HTTPS                                 |
| Middle East (Bahrain)     | me-south-1     | cassandra-streams.me-south-1.api.aws     | HTTPS                                 |
| South America (São Paulo) | sa-east-1      | cassandra-streams.sa-east-1.api.aws      | HTTPS                                 |
| AWS GovCloud (US-East)    | us-gov-east-1  | cassandra-streams.us-gov-east-1.api.aws  | HTTPS                                 |
| AWS GovCloud (US-West)    | us-gov-west-1  | cassandra-streams.us-gov-west-1.api.aws  | HTTPS                                 |
