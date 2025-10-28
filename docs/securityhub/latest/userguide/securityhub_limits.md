# Quotas for

Security Hub

Your AWS account has certain default quotas, formerly referred to as _limits_, for each AWS service. These quotas are the maximum
number of service resources or operations for your account. This topic links to the quotas
that apply to AWS Security Hub resources and operations for your account. Unless otherwise
noted, each quota applies to your account in each AWS Region.

Some quotas can be increased, while others cannot. To request an increase to a quota, use the
[Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). To learn how to
request an increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. If a quota isn't available
on the Service Quotas console, use the [service limit increase
form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase") on the AWS Support Center Console to request an increase to the quota.

## Maximum quotas

For a list of quotas that apply to
AWS Security Hub
resources, see [AWS Security Hub
endpoints and quotas](../../../general/latest/gr/sechub.md "../../../general/latest/gr/sechub.md") in the _AWS General Reference_.

## Rate quotas

For a list of quotas that apply to
AWS Security Hub
API operations, see the [AWS Security Hub API
Reference](../../1.0/APIReference/Welcome.md "../../1.0/APIReference/Welcome.md").

If you set up [cross-Region aggregation in Security Hub CSPM](finding-aggregation.md "finding-aggregation.md"), one
call to `BatchImportFindings` and `BatchUpdateFindings` impacts
linked Regions and the aggregation Region. The `GetFindings` operation
retrieves findings from linked Regions and the aggregation Region. However, the
`BatchEnableStandards` and `UpdateStandardsControl` operations
are Region-specific.
