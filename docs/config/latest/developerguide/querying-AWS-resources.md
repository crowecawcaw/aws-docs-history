# Querying the Current Configuration State of AWS

Resources with AWS Config

|                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Introducing a preview feature for advanced queries that allows you to use<br>generative artificial intelligence (generative AI) capabilities to enter<br>prompts in plain English and convert them into a ready-to-use query format.<br>For more information, see [Natural language query processor for advanced queries](query-assistant.md "query-assistant.md"). |

You can use AWS Config to query the current configuration state of AWS resources based on
configuration properties for a single account and Region or across multiple accounts and
Regions. You can perform property-based queries against current AWS resource state
metadata across a list of resources that AWS Config supports. For more information on the list
of supported resource types, see [Supported Resource Types for Advanced Queries](https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types "https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types").

_Advanced queries_ provides a single query endpoint and a query
language to get current resource state metadata without performing service-specific describe
API calls. You can use configuration aggregators to run the same queries from a central
account across multiple accounts and AWS Regions.

###### Topics

- [Features](#query-features "#query-features")
- [Query Components](query-components.md "query-components.md")
- [Query Editor (Console)](query-using-sql-editor-console.md "query-using-sql-editor-console.md")
- [Query Editor (AWS CLI)](query-using-sql-editor-cli.md "query-using-sql-editor-cli.md")
- [Natural language query processor](query-assistant.md "query-assistant.md")
- [Examples Queries](example-query.md "example-query.md")
- [Example Relationship Queries](examplerelationshipqueries.md "examplerelationshipqueries.md")
- [Limitations](#query-limitations "#query-limitations")
- [CIDR notation/IP range](#query-cidr-notation "#query-cidr-notation")
- [Multiple properties within an array](#array-property-query-behavior "#array-property-query-behavior")
- [Region Support](#query-regionsupport "#query-regionsupport")

## Features

AWS Config uses a subset of structured query language (SQL) `SELECT` syntax to
perform property-based queries and aggregations on the current configuration item (CI)
data. The queries range in complexity from matches against tag and/or resource
identifiers, to more complex queries, such as viewing all Amazon S3 buckets that have
versioning disabled. This allows you to query exactly the current resource state you
need without performing AWS service-specific API calls.

It supports aggregation functions such as `AVG`, `COUNT`,
`MAX`, `MIN`, and `SUM`.

You can use advanced query for:

- Inventory management; for example, to retrieve a list of Amazon EC2 instances of a
  particular size.
- Security and operational intelligence; for example, to retrieve a list of
  resources that have a specific configuration property enabled or
  disabled.
- Cost optimization; for example, to identify a list of Amazon EBS volumes that are
  not attached to any EC2 instance.
- Compliance data; for example, to retrieve a list of all your conformance packs
  and their compliance status.

For information about how to use the AWS SQL Query Language, see [What Is SQL (Structured Query
Language)?](https://aws.amazon.com/what-is/sql/ "https://aws.amazon.com/what-is/sql/").

## Limitations

###### Note

Advanced query does not support querying resources which have not been configured
to be recorded by the configuration recorder. AWS Config creates Configuration Items (CIs)
with `ResourceNotRecorded` in the `configurationItemStatus`
when a resource has been discovered but is not configured to be recorded by the
configuration recorder. While an aggregator will aggregate these CIs, advanced query
does not support querying CIs with `ResourceNotRecorded`. Update your
recorder settings to enable recording of the resource types that you want to
query.

As a subset of SQL `SELECT`, the query syntax has following
limitations:

- No support for `ALL`, `AS`, `DISTINCT`,
  `FROM`, `HAVING`, `JOIN`, and
  `UNION` keywords in a query. `NULL` value queries are
  not supported.
- No support for complex `CASE` statements for creating a priority
  field directly in the query.
- No support for querying on third-party resources. Third-party resources
  retrieved using advanced queries will have the configuration field set as
  `NULL`.
- No support for nested structures (such as tags) to be unpacked with SQL
  queries.
- No support for querying deleted resources. To discover deleted resources, see [Looking Up Resources That Are Discovered by AWS Config](looking-up-discovered-resources.md "looking-up-discovered-resources.md").
- The `SELECT` all columns shorthand (that is `SELECT *`)
  selects only the top-level, scalar properties of a CI. The scalar properties
  returned are `accountId`, `awsRegion`, `arn`,
  `availabilityZone`, `configurationItemCaptureTime`,
  `resourceCreationTime`, `resourceId`,
  `resourceName`, `resourceType`, and
  `version`.
- Wildcard limitations:
  - Wildcards are supported only for property values and not for property
    keys (for example, `...WHERE someKey LIKE 'someValue%'` is
    supported but `...WHERE 'someKey%' LIKE 'someValue%'` is not
    supported).
  - Support for only suffix wildcards (for example, `...LIKE
'AWS::EC2::%'` and `...LIKE 'AWS::EC2::_'` is
    supported but `...LIKE '%::EC2::Instance'` and `...LIKE
'_::EC2::Instance'`is not supported).
  - Wildcard matches must be at least three characters long (for example,
    `...LIKE 'ab%'` and `...LIKE 'ab_'` is not
    allowed but `...LIKE 'abc%'` and `...LIKE 'abc_'`
    is allowed).

###### Note

The "`_`" (single underscore) is also treated as a
wildcard.

- Aggregation limitations:
  - Aggregate functions can accept only a single argument or
    property.
  - Aggregate functions cannot take other functions as arguments.
  - `GROUP BY` with an `ORDER BY` clause referencing
    aggregate functions may contain only a single property.
  - For all other aggregations `GROUP BY` clauses may contain
    up to three properties.
  - Pagination is supported for all aggregate queries except when
    `ORDER BY` clause has an aggregate function. For example,
    `GROUP BY X, ORDER BY Y` does not work if `Y`
    is an aggregate function.
  - No support for `HAVING` clauses in aggregations.

- Mismatched identifier limitations:

Mismatched identifiers are properties that have the same spelling but
different cases (upper and lower case). Advanced query does not support
processing queries that contain mismatched identifiers. For example:

    + Two properties that have the exact same spelling but with different
     casing (`configuration.dbclusterIdentifier` and
     `configuration.dBClusterIdentifier`).
    + Two properties where one property is a subset of the other, and they
     have different casing (`configuration.ipAddress` and
     `configuration.ipaddressPermissions`).

## CIDR notation/IP range behavior for advanced queries

CIDR notation is converted to IP ranges for search.

This means that
`"="` and `"BETWEEN"` search for any range that
includes the provided IP, instead of for an exact one.

To search for an exact IP
range, you need to add in additional conditions to exclude IPs outside of the
range.

###### Example Searching for exact CIDR block 10.0.0.0/24

```
SELECT * WHERE resourceType = 'AWS::EC2::SecurityGroup'
  AND configuration.ipPermissions.ipRanges BETWEEN '10.0.0.0'
  AND '10.0.0.255'
  AND NOT configuration.ipPermissions.ipRanges < '10.0.0.0'
  AND NOT configuration.ipPermissions.ipRanges > '10.0.0.255'

```

###### Example Searching for exact IP address 192.168.0.2/32

```
SELECT * WHERE resourceType = 'AWS::EC2::SecurityGroup'
  AND configuration.ipPermissions.ipRanges = '192.168.0.2'
  AND NOT configuration.ipPermissions.ipRanges > '192.168.0.2'
  AND NOT configuration.ipPermissions.ipRanges < '192.168.0.2'

```

## Multiple properties within an array behavior for advanced queries

When querying against multiple properties within an array of objects, matches
are computed against _all the array elements_.

For example, for a resource R with
rules A and B, the resource is compliant to rule A but noncompliant to rule B.
The resource R is stored as:

```
{
    configRuleList: [
        {
            configRuleName: 'A', complianceType: 'compliant'
        },
        {
            configRuleName: 'B', complianceType: 'non_compliant'
        }
    ]
}
```

R will be returned by this query:

```
SELECT configuration WHERE configuration.configRuleList.complianceType = 'non_compliant'
AND configuration.configRuleList.configRuleName = 'A'
```

The first condition `configuration.configRuleList.complianceType =
 'non_compliant'` is applied to ALL elements in R.configRuleList,
because R has a rule (rule B) with complianceType = 'non_compliant', the
condition is evaluated as true.

The second condition
`configuration.configRuleList.configRuleName` is applied to ALL
elements in R.configRuleList, because R has a rule (rule A) with configRuleName
= 'A', the condition is evaluated as true. As both conditions are true, R will
be returned.

## Region Support

Advanced queries is supported in the following Regions:

| Region Name                | Region         | Endpoint                            | Protocol |
| -------------------------- | -------------- | ----------------------------------- | -------- |
| US East (Ohio)             | us-east-2      | config.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)      | us-east-1      | config.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)    | us-west-1      | config.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)           | us-west-2      | config.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)         | af-south-1     | config.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)   | ap-east-1      | config.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)   | ap-south-2     | config.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)     | ap-southeast-3 | config.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Malaysia)    | ap-southeast-5 | config.ap-southeast-5.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)   | ap-southeast-4 | config.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)      | ap-south-1     | config.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (New Zealand) | ap-southeast-6 | config.ap-southeast-6.amazonaws.com | HTTPS    |
| Asia Pacific (Osaka)       | ap-northeast-3 | config.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)       | ap-northeast-2 | config.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)   | ap-southeast-1 | config.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)      | ap-southeast-2 | config.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Taipei)      | ap-east-2      | config.ap-east-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Thailand)    | ap-southeast-7 | config.ap-southeast-7.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)       | ap-northeast-1 | config.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)           | ca-central-1   | config.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)      | ca-west-1      | config.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)         | eu-central-1   | config.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)           | eu-west-1      | config.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)            | eu-west-2      | config.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)             | eu-south-1     | config.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)             | eu-west-3      | config.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)             | eu-south-2     | config.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)         | eu-north-1     | config.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)            | eu-central-2   | config.eu-central-2.amazonaws.com   | HTTPS    |
| Israel (Tel Aviv)          | il-central-1   | config.il-central-1.amazonaws.com   | HTTPS    |
| Mexico (Central)           | mx-central-1   | config.mx-central-1.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)      | me-south-1     | config.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)          | me-central-1   | config.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo)  | sa-east-1      | config.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)     | us-gov-east-1  | config.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)     | us-gov-west-1  | config.us-gov-west-1.amazonaws.com  | HTTPS    |
