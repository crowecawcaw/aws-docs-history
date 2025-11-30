# Constructing an ARN for Amazon RDS

Resources created in Amazon Web Services are each uniquely identified with an Amazon Resource Name (ARN).
You can construct an ARN for an Amazon RDS resource using the following syntax.

`arn:aws:rds:`<region>`:`<account number>`:`<resourcetype>`:`<name>``

| Region Name                | Region         | Endpoint                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | rds.us-east-2.amazonaws.com<br>rds-fips.us-east-2.api.aws<br>rds.us-east-2.api.aws<br>rds-fips.us-east-2.amazonaws.com             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | rds.us-east-1.amazonaws.com<br>rds-fips.us-east-1.api.aws<br>rds-fips.us-east-1.amazonaws.com<br>rds.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | rds.us-west-1.amazonaws.com<br>rds.us-west-1.api.aws<br>rds-fips.us-west-1.amazonaws.com<br>rds-fips.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | rds.us-west-2.amazonaws.com<br>rds-fips.us-west-2.amazonaws.com<br>rds.us-west-2.api.aws<br>rds-fips.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | rds.af-south-1.amazonaws.com<br>rds.af-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | rds.ap-east-1.amazonaws.com<br>rds.ap-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | rds.ap-south-2.amazonaws.com<br>rds.ap-south-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | rds.ap-southeast-3.amazonaws.com<br>rds.ap-southeast-3.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | rds.ap-southeast-5.amazonaws.com                                                                                                   | HTTPS                            |
| Asia Pacific (Melbourne)   | ap-southeast-4 | rds.ap-southeast-4.amazonaws.com<br>rds.ap-southeast-4.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | rds.ap-south-1.amazonaws.com<br>rds.ap-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | rds.ap-southeast-6.amazonaws.com                                                                                                   | HTTPS                            |
| Asia Pacific (Osaka)       | ap-northeast-3 | rds.ap-northeast-3.amazonaws.com<br>rds.ap-northeast-3.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | rds.ap-northeast-2.amazonaws.com<br>rds.ap-northeast-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | rds.ap-southeast-1.amazonaws.com<br>rds.ap-southeast-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | rds.ap-southeast-2.amazonaws.com<br>rds.ap-southeast-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | rds.ap-east-2.amazonaws.com                                                                                                        | HTTPS                            |
| Asia Pacific (Thailand)    | ap-southeast-7 | rds.ap-southeast-7.amazonaws.com                                                                                                   | HTTPS                            |
| Asia Pacific (Tokyo)       | ap-northeast-1 | rds.ap-northeast-1.amazonaws.com<br>rds.ap-northeast-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | rds.ca-central-1.amazonaws.com<br>rds.ca-central-1.api.aws<br>rds-fips.ca-central-1.api.aws<br>rds-fips.ca-central-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | rds.ca-west-1.amazonaws.com<br>rds-fips.ca-west-1.amazonaws.com                                                                    | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)         | eu-central-1   | rds.eu-central-1.amazonaws.com<br>rds.eu-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | rds.eu-west-1.amazonaws.com<br>rds.eu-west-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | rds.eu-west-2.amazonaws.com<br>rds.eu-west-2.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | rds.eu-south-1.amazonaws.com<br>rds.eu-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | rds.eu-west-3.amazonaws.com<br>rds.eu-west-3.api.aws                                                                               | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | rds.eu-south-2.amazonaws.com<br>rds.eu-south-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | rds.eu-north-1.amazonaws.com<br>rds.eu-north-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | rds.eu-central-2.amazonaws.com<br>rds.eu-central-2.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | rds.il-central-1.amazonaws.com<br>rds.il-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | rds.mx-central-1.amazonaws.com                                                                                                     | HTTPS                            |
| Middle East (Bahrain)      | me-south-1     | rds.me-south-1.amazonaws.com<br>rds.me-south-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | rds.me-central-1.amazonaws.com<br>rds.me-central-1.api.aws                                                                         | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | rds.sa-east-1.amazonaws.com<br>rds.sa-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | rds.us-gov-east-1.amazonaws.com<br>rds.us-gov-east-1.api.aws                                                                       | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | rds.us-gov-west-1.amazonaws.com<br>rds.us-gov-west-1.api.aws                                                                       | HTTPS<br>HTTPS                   |

The following table shows the format that you should use when constructing an ARN for a
particular Amazon RDS resource type.

| Resource type                 | ARN format                                                                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DB instance                   | arn:aws:rds:`<region>`:`<account>`:db:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:db:`my-mysql-instance-1`<br>``                                                    |
| DB cluster                    | arn:aws:rds:`<region>`:`<account>`:cluster:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster:`my-aurora-cluster-1`<br>``                                          |
| Event subscription            | arn:aws:rds:`<region>`:`<account>`:es:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:es:`my-subscription`<br>``                                                        |
| DB option group               | arn:aws:rds:`<region>`:`<account>`:og:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:og:`my-og`<br>``                                                                  |
| DB parameter group            | arn:aws:rds:`<region>`:`<account>`:pg:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:pg:`my-param-enable-logs`<br>``                                                   |
| DB cluster parameter group    | arn:aws:rds:`<region>`:`<account>`:cluster-pg:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster-pg:`my-cluster-param-timezone`<br>``                              |
| Reserved DB instance          | arn:aws:rds:`<region>`:`<account>`:ri:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:ri:`my-reserved-postgresql`<br>``                                                 |
| DB security group             | arn:aws:rds:`<region>`:`<account>`:secgrp:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:secgrp:`my-public`<br>``                                                      |
| Automated DB snapshot         | arn:aws:rds:`<region>`:`<account>`:snapshot:rds:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:snapshot:rds:`my-mysql-db-2019-07-22-07-23`<br>``                       |
| Automated DB cluster snapshot | arn:aws:rds:`<region>`:`<account>`:cluster-snapshot:rds:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster-snapshot:rds:`my-aurora-cluster-2019-07-22-16-16`<br>`` |
| Manual DB snapshot            | arn:aws:rds:`<region>`:`<account>`:snapshot:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:snapshot:`my-mysql-db-snap`<br>``                                           |
| Manual DB cluster snapshot    | arn:aws:rds:`<region>`:`<account>`:cluster-snapshot:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:cluster-snapshot:`my-aurora-cluster-snap`<br>``                     |
| DB subnet group               | arn:aws:rds:`<region>`:`<account>`:subgrp:`<name>`<br>For example:<br>``<br>arn:aws:rds:`us-east-2`:`123456789012`:subgrp:`my-subnet-10`<br>``                                                   |
