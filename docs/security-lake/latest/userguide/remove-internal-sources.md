# Removing an AWS service as a source from

Security Lake

Choose your access method, and follow these steps to remove a natively-supported
AWS service as a Security Lake source. You can remove a source for one or more Regions. When
you remove the source, Security Lake stops collecting data from that source in the specified
Regions and accounts, and subscribers can no longer consume new data from the source.
However, subscribers can still consume data that Security Lake collected from the source before
removal. You can only use these instructions to remove a natively-supported
AWS service as a source. For information about removing a custom source, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. Choose **Sources** from the navigation
   pane.
3. Select a source, and choose **Disable**.
4. Select a Region or Regions in which you want to stop collecting
   data from this source. Security Lake will stop collecting data from the
   source from _all_ accounts in the selected
   Regions.

API
To remove an AWS service as a source programmatically, use the [DeleteAwsLogSource](../APIReference/API_DeleteAwsLogSource.md "../APIReference/API_DeleteAwsLogSource.md") operation of the Security Lake API. If you're using
the AWS Command Line Interface (AWS CLI), run the [delete-aws-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-aws-log-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-aws-log-source.html") command. The
`sourceName` and `regions` parameters
are required. Optionally, you can limit the scope of the removal to specific
`accounts` or a specific
`sourceVersion`.

###### Important

When you don't provide a parameter in your command, Security Lake assumes that
the missing parameter refers to the entire set. For example, if you
don't provide the `accounts` parameter , the command
applies to the entire set of accounts in your organization.

The following example removes VPC Flow Logs as a source in the designated
accounts and Regions.

```
`$` `aws securitylake delete-aws-log-source \
--sources sourceName=`VPC_FLOW`,accounts=`'["123456789012", "111122223333"]'`,regions=`'["us-east-1", "us-east-2"]'`,sourceVersion=`"2.0"``
```

The following example removes Route 53 as a source in the designated
account and Regions.

```
`$` `aws securitylake delete-aws-log-source \
--sources sourceName=`ROUTE53`,accounts=`'["123456789012"]'`,regions=`'["us-east-1", "us-east-2"]'`,sourceVersion=`"2.0"``
```

The preceding examples are formatted for Linux, macOS, or Unix, and they
use the backslash (\) line-continuation character to improve
readability.
