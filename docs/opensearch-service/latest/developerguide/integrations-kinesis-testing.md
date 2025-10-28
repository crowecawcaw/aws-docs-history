# Test the Lambda Function

After you create the function, you can test it by adding a new record to the data
stream using the AWS CLI:

```
aws kinesis put-record --stream-name test --data "My test data." --partition-key partitionKey1 --region `us-west-1`
```

Then use the OpenSearch Service console or OpenSearch Dashboards to verify that
`lambda-kine-index` contains a document. You can also use the
following request:

```
GET https://`domain-name`/lambda-kine-index/_search
{
  "hits" : [
    {
      "_index": "lambda-kine-index",
      "_type": "_doc",
      "_id": "shardId-000000000000:49583511615762699495012960821421456686529436680496087042",
      "_score": 1,
      "_source": {
        "timestamp": 1523648740.051,
        "message": "My test data.",
        "id": "shardId-000000000000:49583511615762699495012960821421456686529436680496087042"
      }
    }
  ]
}
```
