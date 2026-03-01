# Making authenticated Amazon Q Business API calls for application environment supporting anonymous access

Amazon Q Business can securely handle data with integrated authentication and
authorization. In order to achieve this, a subset of the Amazon Q Business APIs
([Chat](../api-reference/API_Chat.md "../api-reference/API_Chat.md"), [ChatSync](../api-reference/API_ChatSync.md "../api-reference/API_ChatSync.md"), and [PutFeedback](../api-reference/API_PutFeedback.md "../api-reference/API_PutFeedback.md")) require identity-unaware [AWS Sig V4
credentials](../../../IAM/latest/UserGuide/signing-elements.md "../../../IAM/latest/UserGuide/signing-elements.md") for the API call that is being made.

###### Topics

- [Prerequisites](#sigv4-auth-api-calls-prereqs-anonymous-applications "#sigv4-auth-api-calls-prereqs-anonymous-applications")
- [One-time setup](#setup-anonymous-applications "#setup-anonymous-applications")
- [Workflow for each API call session](#data-plane-workflow "#data-plane-workflow")

## Prerequisites

Before you begin setting up for making Sig V4 authenticated API calls for
anonymous application environments, make sure you've done the following:

- [Created an Amazon Q Business anonymous
  application environment](create-anonymous-application.md "create-anonymous-application.md").
- Configured access to the AWS CLI.

## One-time setup

The following section outlines the steps to set up the Amazon Q Business
access for application environment that support anonymous access. You only need to perform
these steps once.

1. Create a directory named _policies_.
2. Then, in the same directory, create and save a file named
   _permspolicyforAPIanonymous.json_ with the following
   JSON.

**API permissions policy**

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

3. Finally, create and attach the policy using the following commands in the
   AWS CLI.

**Create and attach policy**

```
aws iam \
create-role \
--role-name
--policy-document file://policies/permspolicyforAPIanonymous.json
```

## Workflow for each API call session

1. First, call the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") API to get AWS credentials. To
   do so, use the following command:

```
aws sts
assume-role
--role-arn role arn
--role-session-name session-name

```

2. Then, set the following environment variables in your command line
   environment using the credentials you received as a response from the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API call.

```
AWS_ACCESS_KEY_ID="`sigv4-access-key`"
AWS_SECRET_ACCESS_KEY="`sigv4-secret-key`"
AWS_SESSION_TOKEN="`sigv4-session-token`"
```

Then, make Amazon Q Business API calls using the following
command:

```
aws qbusiness \
chat-sync \
--application-id application-id
--user-message sample-chat-request
```
