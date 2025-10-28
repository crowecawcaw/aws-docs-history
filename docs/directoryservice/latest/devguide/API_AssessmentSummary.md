# AssessmentSummary

Contains summary information about a directory assessment, providing a high-level
overview without detailed validation results.

## Contents

**AssessmentId**

The unique identifier of the directory assessment.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

Required: No

**CustomerDnsIps**

The IP addresses of the DNS servers or domain controllers in your self-managed AD
environment.

Type: Array of strings

Array Members: Fixed number of 2 items.

Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

Required: No

**DirectoryId**

The identifier of the directory associated with this assessment.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**DnsName**

The fully qualified domain name (FQDN) of the Active Directory domain being
assessed.

Type: String

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

Required: No

**LastUpdateDateTime**

The date and time when the assessment status was last updated.

Type: Timestamp

Required: No

**ReportType**

The type of assessment report generated. Valid values include `CUSTOMER`
and `SYSTEM`.

Type: String

Required: No

**StartTime**

The date and time when the assessment was initiated.

Type: Timestamp

Required: No

**Status**

The current status of the assessment. Valid values include `SUCCESS`,
`FAILED`, `PENDING`, and `IN_PROGRESS`.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/AssessmentSummary.md "../../../goto/SdkForCpp/ds-2015-04-16/AssessmentSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/AssessmentSummary.md "../../../goto/SdkForJavaV2/ds-2015-04-16/AssessmentSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/AssessmentSummary.md "../../../goto/SdkForRubyV3/ds-2015-04-16/AssessmentSummary.md")
