# Use `GetSendQuota` with an AWS SDK or CLI

The following code examples show how to use `GetSendQuota`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SES#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SES#code-examples").

```

    /// <summary>
    /// Get information on the current account's send quota.
    /// </summary>
    /// <returns>The send quota response data.</returns>
    public async Task<GetSendQuotaResponse> GetSendQuotaAsync()
    {
        var result = new GetSendQuotaResponse();
        try
        {
            var response = await _amazonSimpleEmailService.GetSendQuotaAsync(
                new GetSendQuotaRequest());
            result = response;
        }
        catch (Exception ex)
        {
            Console.WriteLine("GetSendQuotaAsync failed with exception: " + ex.Message);
        }

        return result;
    }



```

- For API details, see
  [GetSendQuota](../../../goto/DotNetSDKV3/email-2010-12-01/GetSendQuota.md "../../../goto/DotNetSDKV3/email-2010-12-01/GetSendQuota.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To get your Amazon SES sending limits**

The following example uses the `get-send-quota` command to return your Amazon SES sending limits:

```
`aws ses get-send-quota`

```

Output:

```
{
   "Max24HourSend": 200.0,
   "SentLast24Hours": 1.0,
   "MaxSendRate": 1.0
}
```

Max24HourSend is your sending quota, which is the maximum number of emails that you can send in a 24-hour period.
The sending quota reflects a rolling time period. Every time you try to send an email, Amazon SES checks how many
emails you sent in the previous 24 hours. As long as the total number of emails that you have sent is less than
your quota, your send request will be accepted and your email will be sent.

SentLast24Hours is the number of emails that you have sent in the previous 24 hours.

MaxSendRate is the maximum number of emails that you can send per second.

Note that sending limits are based on recipients rather than on messages. For example, an email that has 10 recipients
counts as 10 against your sending quota.

For more information, see Managing Your Amazon SES Sending Limits in the _Amazon Simple Email Service Developer Guide_.

- For API details, see
  [GetSendQuota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-send-quota.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-send-quota.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command returns the user's current sending limits.**

```
Get-SESSendQuota

```

- For API details, see
  [GetSendQuota](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command returns the user's current sending limits.**

```
Get-SESSendQuota

```

- For API details, see
  [GetSendQuota](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SES with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
