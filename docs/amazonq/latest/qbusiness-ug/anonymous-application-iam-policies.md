# Example IAM

policies for Amazon Q Business application environment supporting anonymous
access

We strongly recommend that you use a restricted policies for the role that will be
used to call the chat APIs for anonymous access application environments.

You need permission policies to use Amazon Q Business application environments that
support anonymous access. The following are examples of such restricted
policies.

###### Topics

- [Policy for calling
  relevant APIs](#anonymous-application-iam-policies-api "#anonymous-application-iam-policies-api")
- [Policies for
  using the web experience](#anonymous-application-iam-policies-web-experience "#anonymous-application-iam-policies-web-experience")

## Policy for calling

relevant APIs

###### Example policy to allow the Amazon Q Business APIs for anonymous

access

```
{
    "Version": "2012-10-17",		 	 	 ,
    "Statement": [{
            "Sid": "QBusinessAnonymousConversationAPIPermissions",
            "Effect": "Allow",
            "Action": [
                "qbusiness:Chat",
                "qbusiness:ChatSync",
                "qbusiness:PutFeedback"
            ],
            "Resource": "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}"
        }]
}
```

###### Applying your restricted policies to an IAM role for using APIs for

Amazon Q application environments supporting anonymous access

1. Create a directory named _policies_.
2. In that directory, create and save a file named
   _permspolicyforAPIanonymous.json_ with the JSON
   for allowing Amazon Q Business API calls for anonymous
   access.
3. Finally, create and attach the policy using the following commands in
   the AWS CLI.

**Create and attach policy**

```
aws iam \
create-role \
--policy-document file://policies/permspolicyforAPIanonymous.json
```

## Policies for

using the web experience

###### Example policy to allow the Amazon Q Business web experience for anonymous

access

```
{
    "Version": "2012-10-17",		 	 	 ,
    "Statement": [{
            "Sid": "QBusinessAnonymousWebExperienceConversationPermissions",
            "Effect": "Allow",
            "Action": [
                "qbusiness:Chat",
                "qbusiness:ChatSync",
                "qbusiness:PutFeedback",
                "qbusiness:GetChatControlsConfiguration",
                "qbusiness:GetApplication",
            ],
            "Resource": "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}"
        }]
}
```

###### Example trust policy to allow the Amazon Q Business web experience for

anonymous access

```
{
    "Version": "2012-10-17",		 	 	 ,
    "Statement": [
        {
            "Sid": "QBusinessTrustPolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "application.qbusiness.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{account_id}}"
                },
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}"
                }
            }
        }
    ]
}

```

###### Applying your restricted policies for using the web experience to an

IAM role

1. Create a directory named _policies_.
2. Then, in the same directory, create and save a file named
   _permspolicyforwebexperienceanonymous_ with the
   JSON for allowing the Amazon Q Business web experience for
   anonymous access.
3. Then, in the same directory, create and save a file named
   _trustpolicyforanonymous.json_ with the JSON for
   the trust policy to allow the Amazon Q Business web experience for
   anonymous access
4. Finally, create and attach the policies using the following commands
   in the AWS CLI.

**Create and attach policy**

```
aws iam \
create-role \
--role-name --assume-role-policy-document file://policies/trustpolicyforanonymous.json \
--policy-document file://policies/permspolicyforwebexperienceanonymous.json
```

###### Note

For the web experience to work properly with AWS CLI commands both
policies are needed

**Amazon Q also supports using a service-linked role
(`AWSServiceRoleForQBusiness`) for an Amazon Q application environment.
The following is the service-linked role policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessPutMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/QBusiness"
 }
 }
 },
 {
 "Sid": "QBusinessCreateLogGroupPermission",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*"
 ]
 },
 {
 "Sid": "QBusinessDescribeLogGroupsPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QBusinessLogStreamPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*:log-stream:*"
 ]
 }
 ]
}`

```

For more information on using service-linked roles for an Amazon Q application environment,
see [Using service-linked roles](../business-use-dg/using-service-linked-roles.md "../business-use-dg/using-service-linked-roles.md").
