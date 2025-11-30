# Granting

fine-grained access for Performance Insights

Fine-grained access control offers additional ways of controlling access to Performance Insights. This
access control can allow or deny access to individual dimensions for
`GetResourceMetrics`, `DescribeDimensionKeys`, and
`GetDimensionKeyDetails` Performance Insights actions. To use fine-grained access,
specify dimensions in the IAM policy by using condition keys. The evaluation of the access follows the IAM
policy evaluation logic. For more information, see [Policy
evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_. If the IAM
policy statement doesn't specify any dimension, then the statement controls access to
all the dimensions for the specified action. For the list of available dimensions, see [DimensionGroup](../../../performance-insights/latest/APIReference/API_DimensionGroup.md "../../../performance-insights/latest/APIReference/API_DimensionGroup.md").

To find out the dimensions that your credentials are authorized to access, use the `AuthorizedActions`
parameter in `ListAvailableResourceDimensions` and specify the action. The allowed
values for `AuthorizedActions` are as follows:

- `GetResourceMetrics`
- `DescribeDimensionKeys`
- `GetDimensionKeyDetails`
  For example, if you specify `GetResourceMetrics` to the `AuthorizedActions` parameter,
  `ListAvailableResourceDimensions` returns the list of dimensions that the `GetResourceMetrics`
  action is authorized to access. If you specify multiple actions in the `AuthorizedActions` parameter, then
  `ListAvailableResourceDimensions` returns an intersection of dimensions that those actions are
  authorized to access.

The following example provides access to the specified dimensions for
`GetResourceMetrics` and `DescribeDimensionKeys`
actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowToDiscoverDimensions",
 "Effect": "Allow",
 "Action": [
 "pi:ListAvailableResourceDimensions"
 ],
 "Resource": [
 "arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
 ]
 },
 {
 "Sid": "SingleAllow",
 "Effect": "Allow",
 "Action": [
 "pi:GetResourceMetrics",
 "pi:DescribeDimensionKeys"
 ],
 "Resource": [
 "arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
 ],
 "Condition": {
 "ForAllValues:StringEquals": {
 "pi:Dimensions": [
 "db.sql_tokenized.id",
 "db.sql_tokenized.statement"
 ]
 }
 }
 }


 ]
}`

```

The following is the response for the requested dimension:

```

	// ListAvailableResourceDimensions API
// Request
{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Metrics": [ "db.load" ],
    "AuthorizedActions": ["DescribeDimensionKeys"]
}

// Response
{
    "MetricDimensions": [ {
        "Metric": "db.load",
        "Groups": [
            {
                "Group": "db.sql_tokenized",
                "Dimensions": [
                    { "Identifier": "db.sql_tokenized.id" },
                  //  { "Identifier": "db.sql_tokenized.db_id" }, // not included because not allows in the IAM Policy
                    { "Identifier": "db.sql_tokenized.statement" }
                ]
            }

        ] }
    ]
}

```

The following example specifies one allow and two deny access for the dimensions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowToDiscoverDimensions",
 "Effect": "Allow",
 "Action": [
 "pi:ListAvailableResourceDimensions"
 ],
 "Resource": [
 "arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
 ]
 },

 {
 "Sid": "O01AllowAllWithoutSpecifyingDimensions",
 "Effect": "Allow",
 "Action": [
 "pi:GetResourceMetrics",
 "pi:DescribeDimensionKeys"
 ],
 "Resource": [
 "arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
 ]
 },

 {
 "Sid": "O01DenyAppDimensionForAll",
 "Effect": "Deny",
 "Action": [
 "pi:GetResourceMetrics",
 "pi:DescribeDimensionKeys"
 ],
 "Resource": [
 "arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "pi:Dimensions": [
 "db.application.name"
 ]
 }
 }
 },

 {
 "Sid": "O01DenySQLForGetResourceMetrics",
 "Effect": "Deny",
 "Action": [
 "pi:GetResourceMetrics"
 ],
 "Resource": [
 "arn:aws:pi:us-east-1:123456789012:metrics/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "pi:Dimensions": [
 "db.sql_tokenized.statement"
 ]
 }
 }
 }
 ]
}`

```

The following are the responses for the requested dimensions:

```

			// ListAvailableResourceDimensions API
// Request
{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Metrics": [ "db.load" ],
    "AuthorizedActions": ["GetResourceMetrics"]
}

// Response
{
    "MetricDimensions": [ {
        "Metric": "db.load",
        "Groups": [
            {
                "Group": "db.application",
                "Dimensions": [

                  // removed from response because denied by the IAM Policy
                  //  { "Identifier": "db.application.name" }
                ]
            },
            {
                "Group": "db.sql_tokenized",
                "Dimensions": [
                    { "Identifier": "db.sql_tokenized.id" },
                    { "Identifier": "db.sql_tokenized.db_id" },

                  // removed from response because denied by the IAM Policy
                  //  { "Identifier": "db.sql_tokenized.statement" }
                ]
            },
            ...
        ] }
    ]
}

```

```

// ListAvailableResourceDimensions API
// Request
{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Metrics": [ "db.load" ],
    "AuthorizedActions": ["DescribeDimensionKeys"]
}

// Response
{
    "MetricDimensions": [ {
        "Metric": "db.load",
        "Groups": [
            {
                "Group": "db.application",
                "Dimensions": [
                  // removed from response because denied by the IAM Policy
                  //  { "Identifier": "db.application.name" }
                ]
            },
            {
                "Group": "db.sql_tokenized",
                "Dimensions": [
                    { "Identifier": "db.sql_tokenized.id" },
                    { "Identifier": "db.sql_tokenized.db_id" },

                  // allowed for DescribeDimensionKeys because our IAM Policy
                  // denies it only for GetResourceMetrics
                    { "Identifier": "db.sql_tokenized.statement" }
                ]
            },
            ...
        ] }
    ]
}

```
