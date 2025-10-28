# AssessmentConfiguration

Contains configuration parameters required to perform a directory assessment.

## Contents

**CustomerDnsIps**

A list of IP addresses for the DNS servers or domain controllers in your self-managed
AD that are tested during the assessment.

Type: Array of strings

Array Members: Fixed number of 2 items.

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: Yes

**DnsName**

The fully qualified domain name (FQDN) of the self-managed AD domain to assess.

Type: String

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

Required: Yes

**InstanceIds**

The identifiers of the self-managed instances with SSM that are used to perform
connectivity and validation tests.

Type: Array of strings

Array Members: Fixed number of 2 items.

Pattern: `^(i-[0-9a-f]{8}|i-[0-9a-f]{17}|mi-[0-9a-f]{8}|mi-[0-9a-f]{17})$`

Required: Yes

**VpcSettings**

Contains VPC information for the [CreateDirectory](API_CreateDirectory.md "API_CreateDirectory.md"), [CreateMicrosoftAD](API_CreateMicrosoftAD.md "API_CreateMicrosoftAD.md"), or [CreateHybridAD](API_CreateHybridAD.md "API_CreateHybridAD.md") operation.

Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md "API_DirectoryVpcSettings.md") object

Required: Yes

**SecurityGroupIds**

By default, the service attaches a security group to allow network access to the
self-managed nodes in your Amazon VPC. You can optionally supply your own security group that
allows network traffic to and from your self-managed domain controllers outside of your
Amazon VPC.

Type: Array of strings

Array Members: Fixed number of 1 item.

Pattern: `^(sg-[0-9a-f]{8}|sg-[0-9a-f]{17})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/AssessmentConfiguration.md "../../../goto/SdkForCpp/ds-2015-04-16/AssessmentConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/AssessmentConfiguration.md "../../../goto/SdkForJavaV2/ds-2015-04-16/AssessmentConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/AssessmentConfiguration.md "../../../goto/SdkForRubyV3/ds-2015-04-16/AssessmentConfiguration.md")
