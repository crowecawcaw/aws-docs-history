On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Quotas for Amazon CodeGuru Security

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some
quotas, and other quotas cannot be increased.

To view the quotas for CodeGuru Security, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services** and
select **CodeGuru Security**.

To request a quota increase, see [Requesting a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

Your AWS account has the following quotas related to CodeGuru Security.

## Code resources

| Resource                            | Default |
| ----------------------------------- | ------- |
| Maximum input file size             | 5 GB    |
| Maximum Java source code size       | 300 MB  |
| Maximum JavaScript source code size | 300 MB  |
| Maximum Python source code size     | 50 MB   |

## CodeGuru Security quotas for

creating, deploying, and managing an API

The following fixed quotas apply to creating, deploying, and managing an API in
CodeGuru Security, using the AWS CLI, the API Gateway console, or the API Gateway REST API and its SDKs. These
quotas can't be increased.

The default quota for all except two CodeGuru Security APIs is 10 requests per second per
account. None of these quotas can be increased. For a list of all CodeGuru Security APIs, see
[Amazon CodeGuru Security Actions](../security-api/API_Operations.md "../security-api/API_Operations.md").

The two APIs with different default quotas are in the following table.

| Action                                                                                             | Default quota                       | Can be increased |
| -------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------- |
| [CreateUploadUrl](../security-api/API_CreateUploadUrl.md "../security-api/API_CreateUploadUrl.md") | 2 requests every second per account | No               |
| [CreateScan](../security-api/API_CreateScan.md "../security-api/API_CreateScan.md")                | 2 requests every second per account | No               |
