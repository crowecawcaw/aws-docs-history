

# PipeTargetRedshiftDataParameters
<a name="API_PipeTargetRedshiftDataParameters"></a>

These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.

## Contents
<a name="API_PipeTargetRedshiftDataParameters_Contents"></a>

 ** Database **   <a name="eventbridge-Type-PipeTargetRedshiftDataParameters-Database"></a>
The name of the database. Required when authenticating using temporary credentials.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** Sqls **   <a name="eventbridge-Type-PipeTargetRedshiftDataParameters-Sqls"></a>
The SQL statement text to run.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 40 items.  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: Yes

 ** DbUser **   <a name="eventbridge-Type-PipeTargetRedshiftDataParameters-DbUser"></a>
The database user name. Required when authenticating using temporary credentials.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** SecretManagerArn **   <a name="eventbridge-Type-PipeTargetRedshiftDataParameters-SecretManagerArn"></a>
The name or ARN of the secret that enables access to the database. Required when authenticating using Secrets Manager.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

 ** StatementName **   <a name="eventbridge-Type-PipeTargetRedshiftDataParameters-StatementName"></a>
The name of the SQL statement. You can name the SQL statement when you create it to identify the query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

 ** WithEvent **   <a name="eventbridge-Type-PipeTargetRedshiftDataParameters-WithEvent"></a>
Indicates whether to send an event back to EventBridge after the SQL statement runs.  
Type: Boolean  
Required: No

## See Also
<a name="API_PipeTargetRedshiftDataParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetRedshiftDataParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetRedshiftDataParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetRedshiftDataParameters) 