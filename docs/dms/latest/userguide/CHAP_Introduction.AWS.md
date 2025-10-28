# Constructing an Amazon Resource Name

(ARN) for AWS DMS

If you use the AWS CLI or AWS DMS API to automate your database migration, then you
work with Amazon Resource Name (ARNs). Each resource that is created in Amazon Web Services is
identified by an ARN, which is a unique identifier. If you use the AWS CLI or AWS DMS
API to set up your database migration, you supply the ARN of the resource that you
want to work with.

An ARN for an AWS DMS resource uses the following syntax:

`arn:aws:dms:`region`:`account
number`:`resourcetype`:`resourcename``

In this syntax, the following apply:

- `region` is the ID of the AWS Region
  where the AWS DMS resource was created, such as `us-west-2`.

The following table shows AWS Region names and the values that you should
use when constructing an ARN.

| Region                           | Name                                                                     |
| -------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Asia Pacific (Tokyo) Region      | ap-northeast-1                                                           |
| Asia Pacific (Seoul) Region      | ap-northeast-2                                                           |
| Asia Pacific (Mumbai) Region     | ap-south-1                                                               |
| Asia Pacific (Singapore) Region  | ap-southeast-1                                                           |
| Asia Pacific (Sydney) Region     | ap-southeast-2                                                           |
| Canada (Central) Region          | ca-central-1                                                             |
| China (Beijing) Region           | cn-north-1                                                               |
| China (Ningxia) Region           | cn-northwest-1                                                           |
| Europe (Stockholm) Region        | eu-north-1                                                               |
| Europe (Milan) Region            | eu-south-1                                                               |
| EU (Frankfurt) Region            | eu-central-1                                                             |
| Europe (Ireland) Region          | eu-west-1                                                                |
| EU (London) Region               | eu-west-2                                                                |
| EU (Paris) Region                | eu-west-3                                                                |
| South America (São Paulo) Region | sa-east-1                                                                |
| US East (N. Virginia) Region     | us-east-1                                                                |
| US East (Ohio) Region            | us-east-2                                                                |
| US West (N. California) Region   | us-west-1                                                                |
| US West (Oregon) Region          | us-west-2                                                                | <br>• `*`account number`*` is your account number with dashes omitted. To find your account number, sign in to your AWS account at http://aws.amazon.com, choose **My Account/Console**, and then choose **My Account**. <br>• _`resourcetype`_ is the type of AWS DMS resource. The following table shows the resource types to use when constructing an ARN for a particular AWS DMS resource. |
| AWS DMS resource type            | ARN format                                                               |
| ---                              | ---                                                                      |
| Replication instance             | `arn:aws:dms:`region`: `account`:rep: `resourcename``                    |
| Endpoint                         | `arn:aws:dms:`region`:`account`:endpoint: `resourcename``                |
| Replication task                 | `arn:aws:dms:`region`:`account`:task:`resourcename``                     |
| Subnet group                     | `arn:aws:dms:`region`:`account`:subgrp:`resourcename``                   | <br>• `resourcename` is the resource name assigned to the AWS DMS resource. This is a generated arbitrary string. The following table shows examples of ARNs for AWS DMS resources. Here, we assume an AWS account of 123456789012, which were created in the US East (N. Virginia) Region, and has a resource name.                                                                             |
| Resource type                    | Sample ARN                                                               |
| ---                              | ---                                                                      |
| Replication instance             | `arn:aws:dms:us-east-1:123456789012:rep:QLXQZ64MH7CXF4QCQMGRVYVXAI`      |
| Endpoint                         | `arn:aws:dms:us-east-1:123456789012:endpoint:D3HMZ2IGUCGFF3NTAXUXGF6S5A` |
| Replication task                 | `arn:aws:dms:us-east-1:123456789012:task:2PVREMWNPGYJCVU2IBPTOYTIV4`     |
| Subnet group                     | `arn:aws:dms:us-east-1:123456789012:subgrp:test-tag-grp`                 |
