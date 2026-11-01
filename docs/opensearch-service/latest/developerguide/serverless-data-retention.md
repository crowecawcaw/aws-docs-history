

# Managing data retention for NextGen time series collections
<a name="serverless-data-retention"></a>

With a NextGen time series collection, you control how long OpenSearch Serverless retains data in an index before it deletes the data. You set this retention period with the `index.data.retention` index setting. You can use this setting to control storage costs and to meet data compliance requirements.

Only NextGen time series collections support the `index.data.retention` setting. Search and vector search collections don't.

**Note**  
This setting applies only to NextGen collections. For Classic collections, use data lifecycle policies instead. For instructions on configuring data lifecycle policies, see [Using data lifecycle policies with Amazon OpenSearch Serverless](serverless-lifecycle.md).

**Topics**
+ [Key differences from data lifecycle policies](#serverless-data-retention-differences)
+ [Using the data retention index setting](#serverless-data-retention-setting)
+ [API usage patterns for data retention](#serverless-data-retention-api)
+ [Using index templates for retention](#serverless-data-retention-templates)
+ [Validation and error messages](#serverless-data-retention-validation)
+ [Java client usage](#serverless-data-retention-java)
+ [Related resources](#serverless-data-retention-related)

## Key differences from data lifecycle policies
<a name="serverless-data-retention-differences"></a>

Data retention for NextGen collections differs from data lifecycle policies in the following ways:
+ Data lifecycle policies are not applicable to NextGen collections. If you create or update a lifecycle policy that targets a NextGen collection, OpenSearch Serverless returns the error `Data lifecycle policies are not supported for OpenSearch Serverless NextGen collections. Please use the data retention index setting to manage retention.`
+ You can't use the `index.data.retention` setting on Classic collections. If you apply this setting to a Classic collection, OpenSearch Serverless returns the error `Data retention index setting is not supported for OpenSearch Serverless Classic collections. Please use data lifecycle policies to manage retention.`
+ Existing wildcard lifecycle policies (`index/*/*`) skip NextGen collections and continue to apply only to Classic collections.
+ The `BatchGetEffectiveLifecyclePolicy` API returns results for only Classic collections, not NextGen collections.

## Using the data retention index setting
<a name="serverless-data-retention-setting"></a>

For NextGen time series collections, you configure data retention directly on indexes with the `PUT <index>/_settings` API and the `index.data.retention` setting. This setting replaces the lifecycle policy mechanism that Classic collections use.

The `index.data.retention` setting has the following properties.

Setting name  
The setting name is `index.data.retention`.

Accepted values  
A string that holds an integer from `1` to `3650`, representing days. For example, `"7"`.

Storage format  
OpenSearch Serverless converts the value to a duration format. For example, OpenSearch Serverless stores `"7"` as `7d`.

Removal  
To remove the retention setting, send a `null` value.

Key normalization  
OpenSearch Serverless automatically normalizes `data.retention` to `index.data.retention`.

Supported collection types  
`TIMESERIES` only. OpenSearch Serverless rejects the setting for `SEARCH` and `VECTORSEARCH` collections.

## API usage patterns for data retention
<a name="serverless-data-retention-api"></a>

The following REST API requests show common ways to set and remove the `index.data.retention` setting. In each request, replace {{my-index}} with the name of the index that you want to configure.

**Note**  
Before you set or lower the retention setting, confirm that you no longer need any data that is older than the retention period. After the retention period for a document elapses, OpenSearch Serverless permanently deletes the document, and you can't recover it. If you lower the retention setting, the new setting applies to data that you already indexed.

The following REST API request sets retention on one or more indexes.

```
PUT {{my-index}}/_settings
{
  "index.data.retention": "7"
}
```

A successful request returns the following response.

```
{
  "acknowledged": true
}
```

The following REST API request sets retention on all indexes in a collection with a wildcard.

```
PUT */_settings
{
  "index.data.retention": "7"
}
```

The following REST API request sets retention on indexes that match a prefix.

```
PUT error*/_settings
{
  "index.data.retention": "30"
}
```

The following REST API request sets retention on multiple specific indexes.

```
PUT access-2024,error-2024/_settings
{
  "index.data.retention": "7"
}
```

The following REST API request removes retention from an index with a `null` value.

```
PUT {{my-index}}/_settings
{
  "index.data.retention": null
}
```

The following REST API request sets retention when you create an index.

```
PUT {{my-index}}
{
  "settings": {
    "index.data.retention": "7"
  }
}
```

A successful request returns the following response.

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my-index"
}
```

## Using index templates for retention
<a name="serverless-data-retention-templates"></a>

The `PUT _settings` API applies only to existing indexes. With an index template, you can automatically apply a retention setting to future indexes. When you create an index whose name matches the template pattern, the index inherits the retention setting.

The following REST API request creates an index template that applies a 30-day retention setting to new indexes whose names match the `logs-*` pattern.

```
PUT _index_template/my-template
{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "index.data.retention": "30"
    }
  }
}
```

A successful request returns the following response.

```
{
  "acknowledged": true
}
```

If an index creation request specifies `index.data.retention` and a matching template also specifies it, the request value takes precedence over the template value.

## Validation and error messages
<a name="serverless-data-retention-validation"></a>

OpenSearch Serverless validates the `index.data.retention` setting and returns an error when validation fails. The following list describes each validation scenario and the error that OpenSearch Serverless returns for it.

The value is less than 1 or greater than 3650  
OpenSearch Serverless returns `Data retention days must be between 1 and 3650`.

The value isn't an integer, such as `abc` or `7.5`  
OpenSearch Serverless returns `Data retention must be a valid integer representing days`.

You use the setting on a Classic collection  
OpenSearch Serverless returns `Data retention index setting is not supported for OpenSearch Serverless Classic collections. Please use data lifecycle policies to manage retention.`

You use the setting on a non-TIMESERIES NextGen collection  
OpenSearch Serverless returns `Data retention index setting is only supported for TIMESERIES collections`.

## Java client usage
<a name="serverless-data-retention-java"></a>

OpenSearch Serverless requires SigV4-signed requests. Use the OpenSearch Java client (`opensearch-java`) with `AwsSdk2Transport`, which signs each request. Set the signing service name to `aoss`.

The `index.data.retention` setting isn't available as a typed builder method, so set it with `IndexSettings.Builder.customSettings`. The following example creates an index named {{test-idx}} with a 5-day retention setting. Replace the endpoint and the `Region` with the values for your collection.

```
import org.opensearch.client.json.JsonData;
import org.opensearch.client.opensearch.OpenSearchClient;
import org.opensearch.client.opensearch.indices.CreateIndexRequest;
import org.opensearch.client.opensearch.indices.IndexSettings;
import org.opensearch.client.transport.aws.AwsSdk2Transport;
import org.opensearch.client.transport.aws.AwsSdk2TransportOptions;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;

SdkHttpClient httpClient = ApacheHttpClient.builder().build();

OpenSearchClient client = new OpenSearchClient(
    new AwsSdk2Transport(
        httpClient,
        "{{your-collection-endpoint}}.us-east-1.aoss.amazonaws.com", // collection endpoint, without a scheme
        "aoss",                                                      // signing service name
        Region.US_EAST_1,
        AwsSdk2TransportOptions.builder().build()));

CreateIndexRequest createIndexRequest = new CreateIndexRequest.Builder()
    .index("{{test-idx}}")
    .settings(new IndexSettings.Builder()
        .customSettings("index.data.retention", JsonData.of("5"))
        .build())
    .build();

client.indices().create(createIndexRequest);

httpClient.close();
```

## Related resources
<a name="serverless-data-retention-related"></a>

For more information about related topics, see the following resources:
+ [Using data lifecycle policies with Amazon OpenSearch Serverless](serverless-lifecycle.md)
+ [Amazon OpenSearch Serverless collections](serverless-collections.md)
+ [Index settings API](https://opensearch.org/docs/latest/api-reference/index-apis/update-settings/) on the OpenSearch website.