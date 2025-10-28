# Amazon OpenSearch Service Serverless

###### Note

OpenSearch Service Serverless support is only available with Grafana workspaces that
are running Grafana version 9.4 and later.

You can use the OpenSearch Service data source to access Amazon OpenSearch Service Serverless data with
Amazon Managed Grafana. Access to the data is controlled by data access policies. The
following example shows a policy that allows users to query a specific
collection and index. Be sure to replace
`collection_name`,
`index_name`, and
`principal_arn` with the correct
values for your use case.

```
[
  {
    "Rules": [
      {
        "Resource": ["collection/{`collection_name`}"],
        "Permission": ["aoss:DescribeCollectionItems"],
        "ResourceType": "collection"
      },
      {
        "Resource": ["index/{`collection_name`}/{`index_name`}"],
        "Permission": ["aoss:DescribeIndex", "aoss:ReadDocument"],
        "ResourceType": "index"
      }
    ],
    "Principal": ["`principal_arn`"],
    "Description": "read-access"
  }
]
```
