

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Enabling email event logging
<a name="tracking"></a>

You enable email event logging in the Amazon WorkMail console in order to track email messages for your organization. Email event logging uses an AWS Identity and Access Management service-linked role (SLR) to grant permissions to publish the email event logs to Amazon CloudWatch. For more information about IAM service-linked roles, see [Using service-linked roles for Amazon WorkMail](using-service-linked-roles.md).

In the CloudWatch event logs, you can use CloudWatch search tools and metrics to track messages and troubleshoot email issues. For more information about the event logs that Amazon WorkMail sends to CloudWatch, see [Monitoring Amazon WorkMail email event logs](cw-events.md). For more information about CloudWatch Logs, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).

**Topics**
+ [Turning on email event logging](#enable-tracking)
+ [Creating a custom log group and IAM role for email event logging](#custom-tracking-role)
+ [Turning off email event logging](#turn-off-tracking)
+ [Cross-service confused deputy prevention](#cross-service-confused-deputy-prevention)

## Turning on email event logging
<a name="enable-tracking"></a>

The following occurs when you turn on email event logging using the default settings, Amazon WorkMail:
+ Creates an AWS Identity and Access Management service-linked role – `AmazonWorkMailEvents`.
+ Creates a CloudWatch log group – `/aws/workmail/emailevents/{{organization-alias}}`.
+ Sets CloudWatch log retention to 30 days.

**To turn on email event logging**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Logging settings**.

1. Choose the **Email flow log settings** tab. 

1. In the **Email flow log settings** section, choose **Edit**.

1. Move the **Enable mail events** slider to the **on** position.

1. Do one of the following:
   + (Recommended) Choose **Use default settings**.
   + (Optional) Clear the **Use default settings**, and select a **Destination Log Group** and **IAM Role** from the lists that appear.
**Note**  
Choose this option only if you have already created a log group and custom IAM role using the AWS CLI. For more information, see [Creating a custom log group and IAM role for email event logging](#custom-tracking-role).

1. Select **I authorize Amazon WorkMail to publish logs in my account using this configuration**.

1. Choose **Save**.

## Creating a custom log group and IAM role for email event logging
<a name="custom-tracking-role"></a>

We recommend using the default settings when enabling email event logging for Amazon WorkMail. If you require a custom monitoring configuration, you can use the AWS CLI to create a dedicated log group and custom IAM role for email event logging.

**To create a custom log group and IAM role for email event logging**

1. Use the following AWS CLI command to create a log group in the same AWS Region as your Amazon WorkMail organization. For more information, see [create-log-group](https://docs.aws.amazon.com/cli/latest/reference/logs/create-log-group.html) in the *AWS CLI Command Reference*.

   ```
   aws –-region {{us-east-1}} logs create-log-group --log-group-name {{workmail-monitoring}}
   ```

1. Create a file containing the following policy:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": "events.workmail.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Use the following AWS CLI command to create an IAM role and attach this file as the role policy document. For more information, see [create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) in the *AWS CLI Command Reference*.

   ```
   aws iam create-role --role-name {{workmail-monitoring-role}} --assume-role-policy-document file://{{trustpolicyforworkmail.json}}
   ```
**Note**  
If you're a `WorkMailFullAccess` managed policy user, you must include the term `workmail` in the role name. This managed policy only allows you to configure email event logging using roles with `workmail` in the name. For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *IAM User Guide*.

1. Create a file containing the policy for the IAM role that you created in the previous step. At minimum, the policy must grant permissions to the role to create log streams and put log events into the log group that you created in step 1.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{example-log-group}}*"
           }
       ]
   }
   ```

------

1. Use the following AWS CLI command to attach the policy file to the IAM role. For more information, see [put-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html) in the *AWS CLI Command Reference*.

   ```
   aws iam put-role-policy --role-name {{workmail-monitoring-role}} --policy-name {{workmail-permissions}} --policy-document file://{{rolepolicy.json}}
   ```

## Turning off email event logging
<a name="turn-off-tracking"></a>

Turn off email event logging from the Amazon WorkMail console. If you no longer need to use email event logging, we recommend that you delete the related CloudWatch log group and service-linked role as well. For more information, see [Deleting a service-linked role for Amazon WorkMail](using-service-linked-roles.md#delete-slr).

**To turn off email event logging**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Monitoring**.

1. In the **Log settings** section, choose **Edit**.

1. Move the **Enable mail events** slider to the off position.

1. Choose **Save**.

## Cross-service confused deputy prevention
<a name="cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). 

The calling service can be manipulated to use its permissions to act on another customer’s resources it wouldn’t otherwise have permission to access. 

 To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. 

We recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource policies to limit the permissions that CloudWatch Logs and Amazon S3 give to the services that are generating logs. If you use both global condition context keys, the values must use the same account ID when used in the same policy statement.

The values of `aws:SourceArn` must be the ARNs of the delivery sources that are generating logs.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if you're specifying multiple resources, use the `aws:SourceArn` global context condition key with wildcards (`*`) for the unknown portions of the ARN.