# Making and signing OpenSearch Service

requests

Even if you configure a completely open resource-based access policy, _all_ requests to the OpenSearch Service configuration API must be signed.
If your policies specify IAM roles or users, requests to the OpenSearch APIs also
must be signed using AWS Signature Version 4. The signing method differs by
API:

- To make calls to the OpenSearch Service configuration API, we recommend that you use one of
  the [AWS SDKs](../../../sdkref/latest/guide/overview.md "../../../sdkref/latest/guide/overview.md"). The SDKs
  greatly simplify the process and can save you a significant amount of time
  compared to creating and signing your own requests. The configuration API
  endpoints use the following format:

```
es.`region`.amazonaws.com/2021-01-01/
```

For example, the following request makes a configuration change to the
`movies` domain, but you have to sign it yourself (not
recommended):

```
POST https://es.`us-east-1`.amazonaws.com/2021-01-01/opensearch/domain/`movies`/config
{
  "ClusterConfig": {
    "InstanceType": "c5.xlarge.search"
  }
}
```

If you use one of the SDKs, such as [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.update_domain_config "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.update_domain_config"), the SDK automatically handles the request signing:

```
import boto3

client = boto3.client(es)
response = client.update_domain_config(
  DomainName='`movies`',
  ClusterConfig={
    'InstanceType': 'c5.xlarge.search'
  }
)
```

For a Java code sample, see [Using the AWS SDKs to interact with
Amazon OpenSearch Service](configuration-samples.md "configuration-samples.md").

- To make calls to the OpenSearch APIs, you must sign your own requests. The
  OpenSearch APIs use the following format:

```
`domain-id`.`region`.es.amazonaws.com
```

For example, the following request searches the `movies` index for
_thor_:

```
GET https://`my-domain`.`us-east-1`.es.amazonaws.com/movies/_search?q=thor
```

###### Note

The service ignores parameters passed in URLs for HTTP POST requests that are
signed with Signature Version 4.
