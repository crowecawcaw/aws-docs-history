# Built-in processors for AWS vended logs

This section contains information about the built-in processors that you can use with AWS services that vend logs.

###### Contents

- [parseWAF](CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseWAF "CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseWAF")
- [parsePostgres](CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parsePostGres "CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parsePostGres")
- [parseCloudfront](CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseCloudFront "CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseCloudFront")
- [parseRoute53](CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseRoute53 "CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseRoute53")
- [parseVPC](CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseVPC "CloudWatch-Logs-Transformation-BuiltIn.md#CloudWatch-Logs-Transformation-parseVPC")
- [parseToOCSF](CloudWatch-Logs-Transformation-parseToOCSF.md "CloudWatch-Logs-Transformation-parseToOCSF.md")

## parseWAF

Use this processor to parse AWS WAF vended logs, It takes the contents of
`httpRequest.headers` and creates JSON keys from each header
name, with the corresponding value. It also does the same for
`labels`. These transformations can make querying AWS WAF logs much
easier. For more information about AWS WAF log format, see [Log examples for web ACL traffic](../../../waf/latest/developerguide/logging-examples.md "../../../waf/latest/developerguide/logging-examples.md").

This processor accepts only `@message` as the input.

###### Important

If you use this processor, it must be the first processor in your
transformer.

**Example**

Take the following example log event:

```
{
  "timestamp": 1576280412771,
  "formatVersion": 1,
  "webaclId": "arn:aws:wafv2:ap-southeast-2:111122223333:regional/webacl/STMTest/1EXAMPLE-2ARN-3ARN-4ARN-123456EXAMPLE",
  "terminatingRuleId": "STMTest_SQLi_XSS",
  "terminatingRuleType": "REGULAR",
  "action": "BLOCK",
  "terminatingRuleMatchDetails": [
    {
      "conditionType": "SQL_INJECTION",
      "sensitivityLevel": "HIGH",
      "location": "HEADER",
      "matchedData": ["10", "AND", "1"]
    }
  ],
  "httpSourceName": "-",
  "httpSourceId": "-",
  "ruleGroupList": [],
  "rateBasedRuleList": [],
  "nonTerminatingMatchingRules": [],
  "httpRequest": {
    "clientIp": "1.1.1.1",
    "country": "AU",
    "headers": [
      { "name": "Host", "value": "localhost:1989" },
      { "name": "User-Agent", "value": "curl/7.61.1" },
      { "name": "Accept", "value": "*/*" },
      { "name": "x-stm-test", "value": "10 AND 1=1" }
    ],
    "uri": "/myUri",
    "args": "",
    "httpVersion": "HTTP/1.1",
    "httpMethod": "GET",
    "requestId": "rid"
  },
  "labels": [{ "name": "value" }]
}
```

The processor configuration is this:

```
[
    {
        "parseWAF": {}
    }
]
```

The transformed log event would be the following.

```
{
  "httpRequest": {
    "headers": {
      "Host": "localhost:1989",
      "User-Agent": "curl/7.61.1",
      "Accept": "*/*",
      "x-stm-test": "10 AND 1=1"
    },
    "clientIp": "1.1.1.1",
    "country": "AU",
    "uri": "/myUri",
    "args": "",
    "httpVersion": "HTTP/1.1",
    "httpMethod": "GET",
    "requestId": "rid"
  },
  "labels": { "name": "value" },
  "timestamp": 1576280412771,
  "formatVersion": 1,
  "webaclId": "arn:aws:wafv2:ap-southeast-2:111122223333:regional/webacl/STMTest/1EXAMPLE-2ARN-3ARN-4ARN-123456EXAMPLE",
  "terminatingRuleId": "STMTest_SQLi_XSS",
  "terminatingRuleType": "REGULAR",
  "action": "BLOCK",
  "terminatingRuleMatchDetails": [
    {
      "conditionType": "SQL_INJECTION",
      "sensitivityLevel": "HIGH",
      "location": "HEADER",
      "matchedData": ["10", "AND", "1"]
    }
  ],
  "httpSourceName": "-",
  "httpSourceId": "-",
  "ruleGroupList": [],
  "rateBasedRuleList": [],
  "nonTerminatingMatchingRules": []
}
```

## parsePostgres

Use this processor to parse Amazon RDS for PostgreSQL vended logs, extract
fields, and convert them to JSON format. For more information about
RDS for PostgreSQL log format, see [RDS for PostgreSQL database log files](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.md#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.md#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix").

This processor accepts only `@message` as the input.

###### Important

If you use this processor, it must be the first processor in your
transformer.

**Example**

Take the following example log event:

```
2019-03-10 03:54:59 UTC:10.0.0.123(52834):postgres@logtestdb:[20175]:ERROR: column "wrong_column_name" does not exist at character 8
```

The processor configuration is this:

```
[
    {
        "parsePostgres": {}
    }
]
```

The transformed log event would be the following.

```
{
  "logTime": "2019-03-10 03:54:59 UTC",
  "srcIp": "10.0.0.123(52834)",
  "userName": "postgres",
  "dbName": "logtestdb",
  "processId": "20175",
  "logLevel": "ERROR"
}
```

## parseCloudfront

Use this processor to parse Amazon CloudFront vended logs, extract
fields, and convert them into JSON format. Encoded field values are decoded.
Values that are integers and doubles are treated as such. For more information
about Amazon CloudFront log format, see [Configure and
use standard logs (access logs)](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md").

This processor accepts only `@message` as the input.

###### Important

If you use this processor, it must be the first processor in your
transformer.

**Example**

Take the following example log event:

```
2019-12-04  21:02:31   LAX1   392    192.0.2.24    GET    d111111abcdef8.cloudfront.net  /index.html    200    -  Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/78.0.3904.108%20Safari/537.36  -  -  Hit    SOX4xwn4XV6Q4rgb7XiVGOHms_BGlTAC4KyHmureZmBNrjGdRLiNIQ==   d111111abcdef8.cloudfront.net  https  23 0.001  -  TLSv1.2    ECDHE-RSA-AES128-GCM-SHA256    Hit    HTTP/2.0   -  -  11040  0.001  Hit    text/html  78 -  -
```

The processor configuration is this:

```
[
    {
        "parseCloudfront": {}
    }
]
```

The transformed log event would be the following.

```
{
  "date": "2019-12-04",
  "time": "21:02:31",
  "x-edge-location": "LAX1",
  "sc-bytes": 392,
  "c-ip": "192.0.2.24",
  "cs-method": "GET",
  "cs(Host)": "d111111abcdef8.cloudfront.net",
  "cs-uri-stem": "/index.html",
  "sc-status": 200,
  "cs(Referer)": "-",
  "cs(User-Agent)": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "cs-uri-query": "-",
  "cs(Cookie)": "-",
  "x-edge-result-type": "Hit",
  "x-edge-request-id": "SOX4xwn4XV6Q4rgb7XiVGOHms_BGlTAC4KyHmureZmBNrjGdRLiNIQ==",
  "x-host-header": "d111111abcdef8.cloudfront.net",
  "cs-protocol": "https",
  "cs-bytes": 23,
  "time-taken": 0.001,
  "x-forwarded-for": "-",
  "ssl-protocol": "TLSv1.2",
  "ssl-cipher": "ECDHE-RSA-AES128-GCM-SHA256",
  "x-edge-response-result-type": "Hit",
  "cs-protocol-version": "HTTP/2.0",
  "fle-status": "-",
  "fle-encrypted-fields": "-",
  "c-port": 11040,
  "time-to-first-byte": 0.001,
  "x-edge-detailed-result-type": "Hit",
  "sc-content-type": "text/html",
  "sc-content-len": 78,
  "sc-range-start": "-",
  "sc-range-end": "-"
}
```

## parseRoute53

Use this processor to parse Amazon Route 53 Public Data Plane vended logs, extract
fields, and convert them into JSON format. Encoded field values are decoded.
This processor does not support Amazon Route 53 Resolver logs.

This processor accepts only `@message` as the input.

###### Important

If you use this processor, it must be the first processor in your
transformer.

**Example**

Take the following example log event:

```
1.0 2017-12-13T08:15:50.235Z Z123412341234 example.com AAAA NOERROR TCP IAD12 192.0.2.0 198.51.100.0/24
```

The processor configuration is this:

```
[
    {
        "parseRoute53": {}
    }
]
```

The transformed log event would be the following.

```
{
  "version": 1.0,
  "queryTimestamp": "2017-12-13T08:15:50.235Z",
  "hostZoneId": "Z123412341234",
  "queryName": "example.com",
  "queryType": "AAAA",
  "responseCode": "NOERROR",
  "protocol": "TCP",
  "edgeLocation": "IAD12",
  "resolverIp": "192.0.2.0",
  "ednsClientSubnet": "198.51.100.0/24"
}
```

## parseVPC

Use this processor to parse Amazon VPC vended logs, extract fields, and convert
them into JSON format. Encoded field values are decoded.

This processor accepts only `@message` as the input.

###### Important

If you use this processor, it must be the first processor in your
transformer.

**Example**

Take the following example log event:

```
2 123456789010 eni-abc123de 192.0.2.0 192.0.2.24 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK
```

The processor configuration is this:

```
[
    {
        "parseVPC": {}
    }
]
```

The transformed log event would be the following.

```
{
  "version": 2,
  "accountId": "123456789010",
  "interfaceId": "eni-abc123de",
  "srcAddr": "192.0.2.0",
  "dstAddr": "192.0.2.24",
  "srcPort": 20641,
  "dstPort": 22,
  "protocol": 6,
  "packets": 20,
  "bytes": 4249,
  "start": 1418530010,
  "end": 1418530070,
  "action": "ACCEPT",
  "logStatus": "OK"
}
```
