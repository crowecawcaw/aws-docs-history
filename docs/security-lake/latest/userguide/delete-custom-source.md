# Deleting a custom source from Security Lake

Delete a custom source to stop sending data from the source to Security Lake. When you remove the source, Security Lake stops collecting data from that source in the specified Regions and accounts, and subscribers can no longer consume new data from the source. However, subscribers can still consume data that Security Lake collected from the source before removal.
You can only use these instructions to remove a custom source. For information about removing a natively-supported AWS service, see [Collecting data from AWS services in Security Lake](custom-sources.md "custom-sources.md").

When deleting a custom source in Security Lake, you must disable each source outside of the Security Lake console with the source. Failure to disable an integration may result in source integrations continuing to send logs into Amazon S3.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. By using the AWS Region selector in the upper-right corner of
   the page, select the Region that you want to remove the custom
   source from.
3. In the navigation pane, choose **Custom
   sources**.
4. Select the custom source that you want to remove.
5. Choose **Deregister custom source** and then
   choose **Delete** to confirm the action.

API
To delete a custom source programmatically, use the [DeleteCustomLogSource](../APIReference/API_DeleteCustomLogSource.md "../APIReference/API_DeleteCustomLogSource.md") operation of the Security Lake API. If you're
using the AWS Command Line Interface (AWS CLI), run the [delete-custom-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-custom-log-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-custom-log-source.html") command. Use the operation in the
AWS Region where you want to delete the custom source.

In your request, use the `sourceName` parameter to specify the
name of the custom source to delete. Or specify the name of the custom
source and use the `sourceVersion` parameter to limit the scope
of the deletion to only a specific version of data from the custom
source.

The following example deletes a custom log source from Security Lake.

This example is formatted for Linux, macOS, or Unix, and it uses the
backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake delete-custom-log-source \
--source-name `EXAMPLE_CUSTOM_SOURCE``
```
