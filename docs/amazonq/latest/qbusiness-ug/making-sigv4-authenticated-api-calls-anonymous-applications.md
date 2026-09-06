

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Making authenticated Amazon Q Business API calls for application environment supporting anonymous access
<a name="making-sigv4-authenticated-api-calls-anonymous-applications"></a>

Amazon Q Business can securely handle data with integrated authentication and authorization. In order to achieve this, a subset of the Amazon Q Business APIs ([Chat](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Chat.html), [ChatSync](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html), and [PutFeedback](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html)) require identity-unaware [AWS Sig V4 credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/signing-elements.html) for the API call that is being made.

**Topics**
+ [Prerequisites](#sigv4-auth-api-calls-prereqs-anonymous-applications)
+ [One-time setup](#setup-anonymous-applications)
+ [Workflow for each API call session](#data-plane-workflow)

## Prerequisites
<a name="sigv4-auth-api-calls-prereqs-anonymous-applications"></a>

Before you begin setting up for making Sig V4 authenticated API calls for anonymous application environments, make sure you've done the following:
+ [Created an Amazon Q Business anonymous application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-anonymous-application.html).
+ Configured access to the AWS CLI.

## One-time setup
<a name="setup-anonymous-applications"></a>

The following section outlines the steps to set up the Amazon Q Business access for application environment that support anonymous access. You only need to perform these steps once.

1. Create a directory named *policies*.

1. Then, in the same directory, create and save a file named *permspolicyforAPIanonymous.json* with the following JSON.

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

1. Finally, create and attach the policy using the following commands in the AWS CLI.

   **Create and attach policy**

   ```
   aws iam \
   create-role \
   --role-name 
   --policy-document file://policies/permspolicyforAPIanonymous.json
   ```

## Workflow for each API call session
<a name="data-plane-workflow"></a>

1. First, call the [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) API to get AWS credentials. To do so, use the following command:

   ```
   aws sts
   assume-role
   --role-arn role arn
   --role-session-name session-name
   ```

1. Then, set the following environment variables in your command line environment using the credentials you received as a response from the [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API call. 

   ```
   AWS_ACCESS_KEY_ID="{{sigv4-access-key}}"
   AWS_SECRET_ACCESS_KEY="{{sigv4-secret-key}}"
   AWS_SESSION_TOKEN="{{sigv4-session-token}}"
   ```

   Then, make Amazon Q Business API calls using the following command:

   ```
   aws qbusiness \
   chat-sync \
   --application-id application-id
   --user-message sample-chat-request
   ```