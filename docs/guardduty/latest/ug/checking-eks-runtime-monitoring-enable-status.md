# Checking EKS Runtime Monitoring configuration

status

Use the following APIs or AWS CLI commands to check the existing configuration status of
EKS Runtime Monitoring.

###### To check existing EKS Runtime Monitoring configuration status in your account

- Run [GetDetector](../APIReference/API_GetDetector.md "../APIReference/API_GetDetector.md") to check the configuration status of your own account.
- Alternatively, you can run the following command by using AWS CLI:

```
aws guardduty get-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1`
```

Make sure to replace the detector ID of your AWS account and the current Region.
To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

###### To check existing EKS Runtime Monitoring configuration status for your organization (as a delegated GuardDuty administrator account

only)

- Run [DescribeOrganizationConfiguration](../APIReference/API_DescribeOrganizationConfiguration.md "../APIReference/API_DescribeOrganizationConfiguration.md") to check the configuration status of your
  organization.

Alternatively, you can run the following command using AWS CLI:

```
aws guardduty describe-organization-configuration --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1`
```

Make sure to replace the detector ID with the detector ID of your delegated GuardDuty administrator account and the Region
with your current Region. To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
