# Use `ListQueryLoggingConfigs` with a CLI

The following code examples show how to use `ListQueryLoggingConfigs`.

CLI

**AWS CLI**

**To list query logging configurations**

The following `list-query-logging-configs` example lists information about the first 100 query logging configurations in your AWS account, for the hosted zone `Z1OX3WQEXAMPLE`.

```
`aws route53 list-query-logging-configs \
 --hosted-zone-id `Z1OX3WQEXAMPLE``

```

Output:

```
{
    "QueryLoggingConfigs": [
        {
            "Id": "964ff34e-ae03-4f06-80a2-9683cexample",
            "HostedZoneId": "Z1OX3WQEXAMPLE",
            "CloudWatchLogsLogGroupArn": "arn:aws:logs:us-east-1:111122223333:log-group:/aws/route53/example.com:*"
        }
    ]
}
```

For more information, see
[Logging DNS queries](query-logs.md "query-logs.md") in the _Amazon Route 53 Developer Guide_.

- For API details, see
  [ListQueryLoggingConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-query-logging-configs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-query-logging-configs.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns all the configurations for DNS query logging that are associated with the current AWS account.**

```
Get-R53QueryLoggingConfigList

```

**Output:**

```
Id                                   HostedZoneId   CloudWatchLogsLogGroupArn
--                                   ------------   -------------------------
59b0fa33-4fea-4471-a88c-926476aaa40d Z385PDS6EAAAZR arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example1.com:*
ee528e95-4e03-4fdc-9d28-9e24ddaaa063 Z94SJHBV1AAAAZ arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example2.com:*
e38dddda-ceb6-45c1-8cb7-f0ae56aaaa2b Z3MEQ8T7AAA1BF arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example3.com:*
```

- For API details, see
  [ListQueryLoggingConfigs](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns all the configurations for DNS query logging that are associated with the current AWS account.**

```
Get-R53QueryLoggingConfigList

```

**Output:**

```
Id                                   HostedZoneId   CloudWatchLogsLogGroupArn
--                                   ------------   -------------------------
59b0fa33-4fea-4471-a88c-926476aaa40d Z385PDS6EAAAZR arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example1.com:*
ee528e95-4e03-4fdc-9d28-9e24ddaaa063 Z94SJHBV1AAAAZ arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example2.com:*
e38dddda-ceb6-45c1-8cb7-f0ae56aaaa2b Z3MEQ8T7AAA1BF arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example3.com:*
```

- For API details, see
  [ListQueryLoggingConfigs](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
