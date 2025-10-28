# Quotas

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Amazon S3 quotas include number of general purpose buckets, directory buckets, access points and
more. You can request an increase for some quotas, but not all quotas can be increased.
These increases are not granted immediately, so it may take a couple of days for your
increase to become effective.

For a list of Amazon S3 quotas and their default values see,
[Amazon S3 quotas](../../../general/latest/gr/s3.md#limits_s3 "../../../general/latest/gr/s3.md#limits_s3") in the
_AWS General Reference_.

## Quota increases

###### To request a quota increase

You can request a quota increase by using one of following options:

- From the AWS Management Console: Open the [Service Quotas
  console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS
  services**. Select **Amazon S3**, select a quota, and follow the directions
  to request a quota increase. For instructions, see [Requesting a
  quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
- From the AWS CLI: Use the [request-service-quota-increase](../../../cli/latest/reference/service-quotas/request-service-quota-increase.md "../../../cli/latest/reference/service-quotas/request-service-quota-increase.md") AWS CLI command. For instructions, see
  [Requesting a
  quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
