# HTTP

The HTTPS (`http`) action sends data from an MQTT message to a web
application or service.

## Requirements

This rule action has the following requirements:

- You must confirm and enable HTTPS endpoints before the rules engine
  can use them. For more information, see [Working with HTTP topic rule
  destinations](rule-destination.md "rule-destination.md").

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`url`

The HTTPS endpoint where the message is sent using the HTTP POST
method. If you use an IP address in place of a hostname, it must be
an IPv4 address. IPv6 addresses are not supported.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`confirmationUrl`

(Optional) If specified, AWS IoT uses the confirmation URL to create
a matching topic rule destination. You must enable the topic rule
destination before using it in an HTTP action. For more information,
see [Working with HTTP topic rule
destinations](rule-destination.md "rule-destination.md"). If you use substitution
templates, you must manually create topic rule destinations before
the `http` action can be used.
`confirmationUrl` must be a prefix of
`url`.

The relationship between `url` and
`confirmationUrl` is described by the
following:

- If `url` is hardcoded and
  `confirmationUrl` is not provided, we
  implicitly treat the `url` field as the
  `confirmationUrl`. AWS IoT creates a topic rule
  destination for `url`.
- If `url` and `confirmationUrl` are
  hardcoded, `url` must begin with
  `confirmationUrl`. AWS IoT creates a topic rule
  destination for `confirmationUrl`.
- If `url` contains a substitution template, you
  must specify `confirmationUrl` and
  `url` must begin with
  `confirmationUrl`. If
  `confirmationUrl` contains substitution
  templates, you must manually create topic rule destinations
  before the `http` action can be used. If
  `confirmationUrl` does not contain
  substitution templates, AWS IoT creates a topic rule
  destination for `confirmationUrl`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`headers`

(Optional) The list of headers to include in HTTP requests to the
endpoint. Each header must contain the following information:

`key`

The key of the header.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`value`

The value of the header.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

###### Note

The default content type is application/json when the payload
is in JSON format. Otherwise, it is application/octet-stream.
You can overwrite it by specifying the exact content type in the
header with the key content-type (case insensitive).

`auth`

(Optional) The authentication used by the rules engine to connect
to the endpoint URL specified in the `url` argument.
Currently, Signature Version 4 is the only supported authentication
type. For more information, see [HTTP
Authorization](../apireference/API_HttpAuthorization.md "../apireference/API_HttpAuthorization.md").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines an AWS IoT rule with an HTTP action.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "http": {
                    "url": "https://www.example.com/subpath",
                    "confirmationUrl": "https://www.example.com",
                    "headers": [
                        {
                            "key": "static_header_key",
                            "value": "static_header_value"
                        },
                        {
                            "key": "substitutable_header_key",
                            "value": "${value_from_payload}"
                        }
                    ]
                }
            }
        ]
    }
}
```

## HTTP action retry logic

The AWS IoT rules engine retries the HTTP action according to these
rules:

- The rules engine tries to send a message at least once.
- The rules engine retries at most twice. The maximum number of tries is
  three.
- The rules engine does not attempt a retry if:
  - The previous try provided a response larger than 16,384
    bytes.
  - The downstream web service or application closes the TCP
    connection after the try.
  - The total time to complete a request with retries exceeded the
    request timeout limit.
  - The request returns an HTTP status code other than 429,
    500-599.

###### Note

[Standard data transfer
costs](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/") apply to retries.

## See also

- [Working with HTTP topic rule
  destinations](rule-destination.md "rule-destination.md")
- [Route data directly from AWS IoT Core to your web services](https://aws.amazon.com/blogs/iot/route-data-directly-from-iot-core-to-your-web-services/ "https://aws.amazon.com/blogs/iot/route-data-directly-from-iot-core-to-your-web-services/") in
  the _Internet of Things on AWS_ blog
