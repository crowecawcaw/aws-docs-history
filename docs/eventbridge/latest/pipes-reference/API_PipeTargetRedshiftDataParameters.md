# PipeTargetRedshiftDataParameters

These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the
Amazon Redshift Data API BatchExecuteStatement.

## Contents

**Database**

The name of the database. Required when authenticating using temporary
credentials.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: Yes

**Sqls**

The SQL statement text to run.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 40 items.

Length Constraints: Minimum length of 1. Maximum length of 100000.

Required: Yes

**DbUser**

The database user name. Required when authenticating using temporary credentials.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: No

**SecretManagerArn**

The name or ARN of the secret that enables access to the database. Required when
authenticating using Secrets Manager.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

**StatementName**

The name of the SQL statement. You can name the SQL statement when you create it to
identify the query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 500.

Required: No

**WithEvent**

Indicates whether to send an event back to EventBridge after the SQL statement
runs.

Type: Boolean

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetRedshiftDataParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetRedshiftDataParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetRedshiftDataParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetRedshiftDataParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetRedshiftDataParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetRedshiftDataParameters.md")
