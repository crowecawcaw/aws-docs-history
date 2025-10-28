# SolutionVersionSummary

Provides a summary of the properties of a solution version. For a complete listing, call the
[DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that this version of a solution was created.

Type: Timestamp

Required: No

**failureReason**

If a solution version fails, the reason behind the failure.

Type: String

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the solution version was last updated.

Type: Timestamp

Required: No

**solutionVersionArn**

The Amazon Resource Name (ARN) of the solution version.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**status**

The status of the solution version.

A solution version can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

**trainingMode**

The scope of training to be performed when creating the solution version. A
`FULL` training considers all of the data in your dataset group.
An `UPDATE` processes only the data that
has changed since the latest training. Only solution versions created with the User-Personalization
recipe can use `UPDATE`.

Type: String

Valid Values: `FULL | UPDATE | AUTOTRAIN`

Required: No

**trainingType**

Whether the solution version was created automatically or manually.

Type: String

Valid Values: `AUTOMATIC | MANUAL`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/SolutionVersionSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/SolutionVersionSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionVersionSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionVersionSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionVersionSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionVersionSummary.md")
