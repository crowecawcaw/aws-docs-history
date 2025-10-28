# Schedule

Represents one or more dates and times when a job is to run.

## Contents

###### Note

In the following list, the required parameters are described first.

**Name**

The name of the schedule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**AccountId**

The ID of the AWS account that owns the schedule.

Type: String

Length Constraints: Maximum length of 255.

Required: No

**CreateDate**

The date and time that the schedule was created.

Type: Timestamp

Required: No

**CreatedBy**

The Amazon Resource Name (ARN) of the user who created the schedule.

Type: String

Required: No

**CronExpression**

The dates and times when the job is to run. For more information, see [Working with cron
expressions for recipe jobs](jobs.md#jobs.cron "jobs.md#jobs.cron") in the _AWS Glue DataBrew Developer
Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Required: No

**JobNames**

A list of jobs to be run, according to the schedule.

Type: Array of strings

Array Members: Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: No

**LastModifiedBy**

The Amazon Resource Name (ARN) of the user who last modified the schedule.

Type: String

Required: No

**LastModifiedDate**

The date and time when the schedule was last modified.

Type: Timestamp

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) of the schedule.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**Tags**

Metadata tags that have been applied to the schedule.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Schedule.md "../../../goto/SdkForCpp/databrew-2017-07-25/Schedule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Schedule.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Schedule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Schedule.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Schedule.md")
