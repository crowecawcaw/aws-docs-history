# List the caller's access grants

S3 data owners can use S3 Access Grants to create access grants for AWS Identity and Access Management (IAM) identities or for AWS IAM Identity Center corporate directory identities. IAM identies and IAM Identity Center directory identities can in turn use the `ListCallerAccessGrants` API to list all of the Amazon S3 buckets, prefixes, and objects they can access, as defined by their S3 Access Grants. Use this API to discover all of the S3 data an IAM or directory identity can access through S3 Access Grants.

You can use this feature to build applications that show the data that is accessible to specific end-users. For example, the AWS Storage Browser for S3, an open source UI component that customers use to access S3 buckets, uses this feature to present end-users with the data that they have access to in Amazon S3, based on their S3 Access Grants. Another example is when building an application for browsing, uploading, or downloading data in Amazon S3, you can use this feature to build a tree structure in your application that an end-user could then browse.

###### Note

For corporate directory identities, when listing the caller's access grants, S3 Access Grants returns the grants of the IAM identity that is used for the identity-aware session. For more information on identity-aware sessions, see [Granting permissions to use identity-aware console sessions](../../../IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.md") in the _AWS Identity and Access Management User Guide_.

The grantee whether an IAM identity, or a corporate directory identity can get a list of their access grants by using the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the
AWS SDKs.

To install the AWS CLI, see [Installing the
AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example command, replace the `user input
 placeholders` with your own information.

###### Example List a caller's access grants

Request:

```
aws s3control list-caller-access-grants \
--account-id `111122223333` \
--region `us-east-2`
--max-results 5


```

Response:

```
{
	"NextToken": "`6J9S...`",
	"CallerAccessGrantsList": [
		{
			"Permission": "READWRITE",
			"GrantScope": "s3://`amzn-s3-demo-bucket`/`prefix1/``sub-prefix1/`*",
			"ApplicationArn": "NA"
		},
		{
			"Permission": "READWRITE",
			"GrantScope": "s3://`amzn-s3-demo-bucket`/`prefix1/``sub-prefix2/`*",
			"ApplicationArn": "ALL"
		},
		{
			"Permission": "READWRITE",
			"GrantScope": "s3://`amzn-s3-demo-bucket`/`prefix1/``sub-prefix3/`*",
			"ApplicationArn": "arn:aws:sso::`111122223333`:application/ssoins-ssoins-`1234567890abcdef/apl-abcd1234a1b2c3d`"
		}
	]
}

```

###### Example List a caller's access grants for a bucket

You can narrow the scope of the results using the `grantscope` parameter.

Request:

```
aws s3control list-caller-access-grants \
--account-id `111122223333` \
--region `us-east-2`
--grant-scope "`s3://`amzn-s3-demo-bucket``""
--max-results 1000


```

Response:

```
{
	"NextToken": "`6J9S...`",
	"CallerAccessGrantsList": [
		{
			"Permission": "READ",
			"GrantScope": "s3://`amzn-s3-demo-bucket`*",
			"ApplicationArn": "ALL"
		},
		{
			"Permission": "READ",
			"GrantScope": "s3://`amzn-s3-demo-bucket`/`prefix1/`*",
			"ApplicationArn": "arn:aws:sso::`111122223333`:application/ssoins-ssoins-`1234567890abcdef/apl-abcd1234a1b2c3d`"
		}
	]
}

```

For information about the Amazon S3 REST API support for getting a list of the API caller's access grants, see [ListCallerAccessGrants](../API/API_control_ListCallerAccessGrants.md "../API/API_control_ListCallerAccessGrants.md") in the
_Amazon Simple Storage Service API Reference_.

This section provides an example of how grantees request temporary credentials from S3 Access Grants
by using the AWS SDKs.

Java
The following code example returns the API caller's access grants to the S3 data of a particular AWS account. To use this code example, replace the
`user input placeholders`
with your own information.

###### Example List a caller's access grants

Request:

```
Public void ListCallerAccessGrants() {
	ListCallerAccessGrantsRequest listRequest = ListCallerAccessGrantsRequest.builder()
				.withMaxResults(1000)
				.withGrantScope("`s3://`")
				.accountId("`111122223333`");
	ListCallerAccessGrantsResponse listResponse = s3control.listCallerAccessGrants(listRequest);
	LOGGER.info("ListCallerAccessGrantsResponse: " + listResponse);
	}
```

Response:

```
ListCallerAccessGrantsResponse(
CallerAccessGrantsList=[
	ListCallerAccessGrantsEntry(
		S3Prefix=s3://`amzn-s3-demo-bucket`/`prefix1/`,
		Permission=READ,
		ApplicationArn=ALL
	)
])
```
