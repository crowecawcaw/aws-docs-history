

# Generating a policy based on access activity
<a name="getting-started_reduce-permissions-edit-policy"></a>

You can use the access activity recorded in AWS CloudTrail for an IAM user or IAM role to have IAM Access Analyzer generate a customer managed policy to allow access to only the services that specific users and roles need. 

When IAM Access Analyzer generates an IAM policy, information is returned to help you to further customize the policy. Two categories of information can be returned when a policy is generated:
+ **Policy with action-level information –** For some AWS services, such as Amazon EC2, IAM Access Analyzer can identify the actions found in your CloudTrail events and lists the actions used in the policy it generates. For a list of supported services, see [IAM Access Analyzer policy generation services](access-analyzer-policy-generation-action-last-accessed-support.md). For some services, IAM Access Analyzer prompts you to add actions for the services to the generated policy.
+ **Policy with service-level information –** IAM Access Analyzer uses [last accessed](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html) information to create a policy template with all of the recently used services. When using the AWS Management Console, we prompt you to review the services and add actions to complete the policy.

## To generate a policy based on access activity
<a name="getting-started_reduce-permissions-edit-policy-section-1"></a>

In the following procedure we are going to reduce the permissions given to a role to match the usage of a user. When you choose a user, choose a user whose usage exemplifies the role. Many customers set up test user accounts with **PowerUser** permissions and then have them do a specific set of tasks for a short time period to determine what access is necessary to perform those tasks,

------
#### [ Console ]

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

1. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.

1. In the navigation pane, choose **Users** and then choose the user name to go to the user details page.

1. On **Permissions** tab, under Generate policy based on CloudTrail events, choose **Generate policy**. 

1. On the **Generate policy** page, configure the following items:
   + For **Select time period**, choose **Last 7 days**.
   + For **CloudTrail trail to be analyzed**, select the Region and trail where this user's activity is recorded.
   + Choose **Create and use a new service role**.

1. Choose **Generate policy** then wait until the role is created. Don't refresh or navigate away from the console page until the **Policy generation in progress** notification message appears.

1. After the policy is generated, you must review and customize it as needed with the account IDs and ARNs for resources. In addition, the automatically generated policy might not include the action-level information needed to complete the policy. For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html).

   For example, you might edit the first statement that includes the `Allow` effect and the `NotAction` element to allow only Amazon EC2 and Amazon S3 actions. To do this, replace it with the statement with the `FullAccessToSomeServices` ID. Your new policy could look like the following example policy.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
         {
             "Sid": "FullAccessToSomeServices",
             "Effect": "Allow",
             "Action": [
                 "ec2:*",
                 "s3:*"
             ],
             "Resource": "*"
         },
         {
             "Effect": "Allow",
             "Action": [
                 "iam:CreateServiceLinkedRole",
                 "iam:DeleteServiceLinkedRole",
                 "iam:ListRoles",
                 "organizations:DescribeOrganization"
             ],
             "Resource": "*"
         }
     ]
   }
   ```

------

1. To support the best practice of [granting least privilege](best-practices.md#grant-least-privilege), review and correct any errors, warnings, or suggestions returned during [policy validation](access_policies_policy-validator.md).

1. To further reduce your policies' permissions to specific actions and resources, view your events in CloudTrail **Event history**. There you can view detailed information about the specific actions and resources that your user has accessed. For more information, see [Viewing CloudTrail Events in the CloudTrail Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html) in the *AWS CloudTrail User Guide*.

1. After reviewing and validating your policy, save it with a descriptive name. 

1. Navigate to the **Roles** page and choose the role that people will assume when they perform the tasks permitted by your new policy.

1. Select the **Permissions** tab, and then choose **Add permissions** and select **Attach policies**.

1. On the **Attach permission policies **page, in the **Other permissions policies** list, select the policy you created, then choose **Attach policies**.

1. You are returned to the **Role** details page. There are two policies attached to the role, your previous AWS managed policy, such as **PowerUserAccess**, and your new policy. Select the checkbox for the AWS managed policy and then choose **Remove**. When asked to confirm removal, choose **Remove**.

IAM users, SAML and OIDC federated principals, and workloads who assume this role now have reduced access according to the new policy you created.

------
#### [ AWS CLI ]

You can use the following commands to generate a policy using the AWS CLI. 

**To generate a policy**
+ [aws accessanalyzer start-policy-generation](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/start-policy-generation.html)

**To view a generated policy**
+ [aws accessanalyzer get-generated-policy](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/get-generated-policy.html)

**To cancel a policy generation request**
+ [aws accessanalyzer cancel-policy-generation](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/cancel-policy-generation.html)

**To view a list of policy generation requests**
+ [aws accessanalyzer list-policy-generations](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/list-policy-generations.html)

------
#### [ API ]

You can use the following operations to generate a policy using the AWS API.

**To generate a policy**
+ [StartPolicyGeneration](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StartPolicyGeneration.html)

**To view a generated policy**
+ [GetGeneratedPolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetGeneratedPolicy.html)

**To cancel a policy generation request**
+ [CancelPolicyGeneration](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CancelPolicyGeneration.html)

**To view a list of policy generation requests**
+ [ListPolicyGenerations](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListPolicyGenerations.html)

------