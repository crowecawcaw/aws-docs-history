# AwsAppSync resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsAppSync`
resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsAppSyncGraphQLApi

`AwsAppSyncGraphQLApi` provides information about an AWS AppSync GraphQL API, which is a top-level construct for your
application.

The following example shows the ASFF for the `AwsAppSyncGraphQLApi` object. To view
descriptions of `AwsAppSyncGraphQLApi` attributes, see
[AwsAppSyncGraphQLApi](../../1.0/APIReference/API_AwsAppSyncGraphQLApiDetails.md "../../1.0/APIReference/API_AwsAppSyncGraphQLApiDetails.md")
in the _AWS Security Hub API Reference_.

**Example**

```
"AwsAppSyncGraphQLApi": {
    "AdditionalAuthenticationProviders": [
    {
    	"AuthenticationType": "AWS_LAMBDA",
    	"LambdaAuthorizerConfig": {
    		"AuthorizerResultTtlInSeconds": 300,
    		"AuthorizerUri": "arn:aws:lambda:us-east-1:123456789012:function:mylambdafunc"
    	}
    },
    {
    	"AuthenticationType": "AWS_IAM"
    }
    ],
    "ApiId": "021345abcdef6789",
    "Arn": "arn:aws:appsync:eu-central-1:123456789012:apis/021345abcdef6789",
    "AuthenticationType": "API_KEY",
    "Id": "021345abcdef6789",
    "LogConfig": {
    	"CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/service-role/appsync-graphqlapi-logs-eu-central-1",
    	"ExcludeVerboseContent": true,
    	"FieldLogLevel": "ALL"
    },
    "Name": "My AppSync App",
    "XrayEnabled": true,
}
```
