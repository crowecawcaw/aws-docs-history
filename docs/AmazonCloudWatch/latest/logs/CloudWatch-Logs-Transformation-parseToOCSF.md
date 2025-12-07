# parseToOCSF

The `parseToOCSF` processor converts logs into Open Cybersecurity
Schema Framework (OCSF) events. OCSF is an open standard that provides a common
schema for security data, enabling better interoperability and analysis across
different security tools and platforms.

This processor is particularly useful for security analytics workflows where
you need to standardize log formats from various AWS services into a
consistent schema for downstream analysis.

**Parameters**

`eventSource` (required)

Specifies the AWS service or process that produces the log
events to be converted. Valid values are:

- `CloudTrail` - CloudTrail logs
- `Route53Resolver` - Route 53 Resolver
  logs
- `VPCFlow` - Amazon VPC Flow Logs
- `EKSAudit` - Amazon EKS audit logs
- `AWSWAF` - AWS WAF logs

`ocsfVersion` (required)

Specifies which version of the OCSF schema to use for the
transformed log events. Currently supported versions: `V1.1,
 V1.5`

`mappingVersion` (optional)

Specifies the OCSF transformation mapping version. Controls which
transformation logic is applied when converting logs to OCSF format.
If not specified, uses the latest available version at policy
creation time. Existing policies do not automatically upgrade when
new mapping versions are released. Current latest version:
`v1.5.0`.

**Note:** Not supported when
`ocsfVersion` is `V1.1`.

`source` (optional)

The path to the field in the log event that you want to parse. If
omitted, the entire log message is parsed.

**Example**

The following example shows how to use `parseToOCSF` to convert VPC
Flow Logs to OCSF format:

```
{
  "parseToOCSF": {
    "eventSource": "VPCFlow",
    "ocsfVersion": "V1.1"
  }
}
```

The following example shows how to specify a particular mapping version for
consistent transformation behavior:

```
{
  "parseToOCSF": {
    "eventSource": "CloudTrail",
    "ocsfVersion": "V1.5",
    "mappingVersion": "v1.5.0"
  }
}
```
