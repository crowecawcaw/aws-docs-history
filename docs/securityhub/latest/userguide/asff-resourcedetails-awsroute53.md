# AwsRoute53 resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsRoute53` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsRoute53HostedZone

The `AwsRoute53HostedZone` object provides information about an Amazon Route 53 hosted zone, including the four
name servers assigned to the hosted zone. A hosted zone represents a collection of records that can be managed together, belonging
to a single parent domain name.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsRoute53HostedZone` object. To view descriptions of `AwsRoute53HostedZone` attributes, see
[AwsRoute53HostedZoneDetails](../../1.0/APIReference/API_AwsRoute53HostedZoneDetails.md "../../1.0/APIReference/API_AwsRoute53HostedZoneDetails.md")
in the _AWS Security Hub API Reference_.

**Example**

```
"AwsRoute53HostedZone": {
    "HostedZone": {
        "Id": "Z06419652JEMGO9TA2XKL",
        "Name": "asff.testing",
        "Config": {
            "Comment": "This is an example comment."
        }
    },
    "NameServers": [
        "ns-470.awsdns-32.net",
        "ns-1220.awsdns-12.org",
        "ns-205.awsdns-13.com",
        "ns-1960.awsdns-51.co.uk"
    ],
    "QueryLoggingConfig": {
        "CloudWatchLogsLogGroupArn": {
            "CloudWatchLogsLogGroupArn": "arn:aws:logs:us-east-1:123456789012:log-group:asfftesting:*",
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "HostedZoneId": "Z00932193AF5H180PPNZD"
        }
    },
    "Vpcs": [
        {
            "Id": "vpc-05d7c6e36bc03ea76",
            "Region": "us-east-1"
        }
    ]
}
```
