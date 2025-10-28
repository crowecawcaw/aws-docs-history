# Use `GetSendStatistics` with a CLI

The following code examples show how to use `GetSendStatistics`.

CLI

**AWS CLI**

**To get your Amazon SES sending statistics**

The following example uses the `get-send-statistics` command to return your Amazon SES sending statistics

```
`aws ses get-send-statistics`

```

Output:

```
{
   "SendDataPoints": [
       {
           "Complaints": 0,
           "Timestamp": "2013-06-12T19:32:00Z",
           "DeliveryAttempts": 2,
           "Bounces": 0,
           "Rejects": 0
       },
       {
           "Complaints": 0,
           "Timestamp": "2013-06-12T00:47:00Z",
           "DeliveryAttempts": 1,
           "Bounces": 0,
           "Rejects": 0
       }
   ]
}
```

The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list
contains statistics for a 15-minute interval.

In this example, there are only two data points because the only emails that the user sent in the last two weeks fell
within two 15-minute intervals.

For more information, see Monitoring Your Amazon SES Usage Statistics in the _Amazon Simple Email Service Developer Guide_.

- For API details, see
  [GetSendStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-send-statistics.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-send-statistics.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command returns the user's sending statistics. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute interval.**

```
Get-SESSendStatistic

```

- For API details, see
  [GetSendStatistics](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command returns the user's sending statistics. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute interval.**

```
Get-SESSendStatistic

```

- For API details, see
  [GetSendStatistics](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SES with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
