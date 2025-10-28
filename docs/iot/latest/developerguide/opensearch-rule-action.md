# OpenSearch

The OpenSearch (`openSearch`) action writes data from MQTT messages to
an Amazon OpenSearch Service domain. You can then use tools like OpenSearch Dashboards to query and
visualize data in OpenSearch Service.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `es:ESHttpPut` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If you use a customer managed AWS KMS key to encrypt data at rest
  in OpenSearch Service, the service must have permission to use the KMS key on the
  caller's behalf. For more information, see [Encryption of data at rest
  for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/encryption-at-rest.md "../../../opensearch-service/latest/developerguide/encryption-at-rest.md") in the _Amazon OpenSearch Service Developer
  Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`endpoint`

The endpoint of your Amazon OpenSearch Service domain.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`index`

The OpenSearch index where you want to store your data.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`type`

The type of document you are storing.

###### Note

For OpenSearch versions later than 1.0, the value of the
`type` parameter must be `_doc`. For
more information, see the [OpenSearch documentation](https://opensearch.org/docs/1.0/opensearch/rest-api/document-apis/index-document/#response-body-fields "https://opensearch.org/docs/1.0/opensearch/rest-api/document-apis/index-document/#response-body-fields").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`id`

The unique identifier for each document.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`roleARN`

The IAM role that allows access to the OpenSearch Service domain. For more
information, see [Requirements](#opensearch-rule-action-requirements "#opensearch-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Limitations

The OpenSearch (`openSearch`) action cannot be used to deliver data
to VPC Elasticsearch clusters.

## Examples

The following JSON example defines an OpenSearch action in an AWS IoT rule and
how you can specify the fields for the `OpenSearch` action. For more
information, see [OpenSearchAction](../apireference/API_OpenSearchAction.md "../apireference/API_OpenSearchAction.md").

```
{
    "topicRulePayload": {
        "sql": "SELECT *, timestamp() as timestamp FROM 'iot/test'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "openSearch": {
                    "endpoint": "https://my-endpoint",
                    "index": "my-index",
                    "type": "_doc",
                    "id": "${newuuid()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_os"
                }
            }
        ]
    }
}
```

The following JSON example defines an OpenSearch action with substitution
templates in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "openSearch": {
                    "endpoint": "https://my-endpoint",
                    "index": "${topic()}",
                    "type": "${type}",
                    "id": "${newuuid()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_os"
                }
            }
        ]
    }
}
```

###### Note

The the substituted `type` field works for OpenSearch version
1.0. For any versions later than 1.0, the value of `type` must be
`_doc`.

## See also

[What is Amazon OpenSearch Service?](../../../opensearch-service/latest/developerguide.md "../../../opensearch-service/latest/developerguide.md") in the
_Amazon OpenSearch Service Developer Guide_
