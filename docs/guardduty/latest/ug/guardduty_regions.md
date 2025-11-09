# Amazon GuardDuty Regions and endpoints

To view the AWS Regions where Amazon GuardDuty is available, see [Amazon GuardDuty endpoints](../../../general/latest/gr/guardduty.md "../../../general/latest/gr/guardduty.md") in the
_Amazon Web Services General Reference_.

We recommend that you enable GuardDuty in all supported AWS Regions. This enables GuardDuty to
generate findings about unauthorized or unusual activity even in Regions that you are not
actively using. This also allows GuardDuty to monitor AWS CloudTrail events for the supported
AWS Regions, its ability to detect activity that involves global services is
reduced.

## Region-specific feature

availability

A list of regional differences to specify the availability of GuardDuty features.

**ListFindings and GetFindingsStatistics APIs**

The [GetFindingsStatistics](../APIReference/API_GetFindingsStatistics.md "../APIReference/API_GetFindingsStatistics.md") and [ListFindings](../APIReference/API_ListFindings.md "../APIReference/API_ListFindings.md") APIs have a temporary
`consoleOnly` flag. When you use any or both of these APIs,
the `consoleOnly` flag means that the API can fetch results to a
maximum limit of 1000.

**Malware Protection for EC2**

GuardDuty supports the [Malware Protection for EC2](malware-protection.md "malware-protection.md") feature in the [AWS Dedicated
Local Zones](https://aws.amazon.com/dedicatedlocalzones "https://aws.amazon.com/dedicatedlocalzones").

**RDS Protection**

RDS Protection is not supported in Asia Pacific (Taipei) (`ap-east-2`) Region.

**General API support**

The following APIs in the Amazon GuardDuty API Reference may have regional differences
because of the unavailability of some of the data sources or features in
previously specified AWS Regions:

- [CreateDetector](../APIReference/API_CreateDetector.md "../APIReference/API_CreateDetector.md")
- [UpdateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md")
- [UpdateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md")
- [UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md")
- [GetDetector](../APIReference/API_GetDetector.md "../APIReference/API_GetDetector.md")
- [GetMemberDetectors](../APIReference/API_GetMemberDetectors.md "../APIReference/API_GetMemberDetectors.md")
- [DescribeOrganizationConfiguration](../APIReference/API_DescribeOrganizationConfiguration.md "../APIReference/API_DescribeOrganizationConfiguration.md")

**Amazon EC2 finding types – [DefenseEvasion:EC2/UnusualDoHActivity](guardduty_finding-types-ec2.md#defenseevasion-ec2-unsualdohactivity "guardduty_finding-types-ec2.md#defenseevasion-ec2-unsualdohactivity") and [DefenseEvasion:EC2/UnusualDoTActivity](guardduty_finding-types-ec2.md#defenseevasion-ec2-unusualdotactivity "guardduty_finding-types-ec2.md#defenseevasion-ec2-unusualdotactivity")**

The following table shows the AWS Regions where GuardDuty is available but
these two Amazon EC2 finding types are not yet supported.

| AWS Region             | Region code    |
| ---------------------- | -------------- |
| Asia Pacific (Seoul)   | ap-northeast-2 |
| Asia Pacific (Osaka)   | ap-northeast-3 |
| Asia Pacific (Jakarta) | ap-southeast-3 |

**AWS GovCloud (US) Regions**

For latest information, see [Amazon GuardDuty](../../../govcloud-us/latest/UserGuide/govcloud-guardduty.md "../../../govcloud-us/latest/UserGuide/govcloud-guardduty.md") in the
_AWS GovCloud (US) User Guide_.

**China Regions**

For latest information, see [Feature availability and implementation differences](https://docs.amazonaws.cn/en_us/aws/latest/userguide/guardduty.html#feature-diff "https://docs.amazonaws.cn/en_us/aws/latest/userguide/guardduty.html#feature-diff").
