

# Managing automated security agent for Fargate (Amazon ECS only)
<a name="managing-gdu-agent-ecs-automated"></a>

Runtime Monitoring supports managing the security agent for your Amazon ECS clusters (AWS Fargate) only through GuardDuty. There is no support for managing the security agent manually on Amazon ECS clusters.

Before proceeding with the steps in this section, make sure to follow [Prerequisites for AWS Fargate (Amazon ECS only) support](prereq-runtime-monitoring-ecs-support.md).

Based on the [Approaches to manage GuardDuty security agent in Amazon ECS-Fargate resources](how-runtime-monitoring-works-ecs-fargate.md#gdu-runtime-approaches-agent-deployment-ecs-clusters), choose a preferred method to enable GuardDuty automated agent for your resources.

**Topics**

## Configuring GuardDuty agent for multi-account environment
<a name="ecs-fargate-manage-agent-multiple-accounts"></a>

In a multiple-account environment, only the delegated GuardDuty administrator account can enable or disable automated agent configuration for the member accounts, and manage automated agent configuration for Amazon ECS clusters that belong to the member accounts in their organization. A GuardDuty member account can't modify this configuration. The delegated GuardDuty administrator account manages their member accounts using AWS Organizations. For more information about multi-account environments, see [Managing multiple accounts in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

### Enabling automated agent configuration for delegated GuardDuty administrator account
<a name="ecs-enable-automated-agent-config-delegatedadmin"></a>

------
#### [ Manage for all Amazon ECS clusters (account level) ]

If you chose **Enable for all accounts** for Runtime Monitoring, then you have the following options:
+ Choose **Enable for all accounts** in the Automated agent configuration section. GuardDuty will deploy and manage the security agent for all the Amazon ECS tasks that get launched.
+ Choose **Configure accounts manually**.

If you chose **Configure accounts manually** in the Runtime Monitoring section, then do the following:

1. Choose **Configure accounts manually** in the Automated agent configuration section.

1. Choose **Enable** in the **delegated GuardDuty administrator account (this account)** section.

Choose **Save**.

When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

For steps to update the service, see the following resources:
+ [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
+ [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
+ [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for all Amazon ECS clusters but exclude some of the clusters (cluster level) ]

1. Add a tag to this Amazon ECS cluster with the key-value pair as `GuardDutyManaged`-`false`.

1. Prevent modification of tags, except by the trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. 
**Note**  
Always add the exclusion tag to your Amazon ECS clusters before enabling Automated agent configuration for your account; otherwise the GuardDuty sidecar container will be attached to all the containers in the Amazon ECS tasks that get launched.

   Under the **Configuration** tab, choose **Enable** in the **Automated agent configuration**.

   For the Amazon ECS clusters that have not been excluded, GuardDuty will manage the deployment of the security agent in the sidecar container.

1. Choose **Save**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for selective (inclusion only) Amazon ECS clusters (cluster level) ]

1. Add a tag to an Amazon ECS cluster for which you want to include all of the tasks. The key-value pair must be `GuardDutyManaged`-`true`.

1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------
**Note**  
When using inclusion tags for your Amazon ECS clusters, you don't need to enable GuardDuty agent through automated agent congifuration explicitly.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------

### Auto-enable for all member accounts
<a name="ecs-auto-enable-all-member-accounts"></a>

------
#### [ Manage for all Amazon ECS clusters (account level) ]

The following steps assume that you chose **Enable for all accounts** in the Runtime Monitoring section.

1. Choose **Enable for all accounts** in the Automated agent configuration section. GuardDuty will deploy and manage the security agent for all the Amazon ECS tasks that get launched.

1. Choose **Save**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for all Amazon ECS clusters but exclude some of the clusters (cluster level) ]

1. Add a tag to this Amazon ECS cluster with the key-value pair as `GuardDutyManaged`-`false`.

1. Prevent modification of tags, except by the trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. 
**Note**  
Always add the exclusion tag to your Amazon ECS clusters before enabling Automated agent configuration for your account; otherwise the GuardDuty sidecar container will be attached to all the containers in the Amazon ECS tasks that get launched.

   Under the **Configuration** tab, choose **Edit**.

1. Choose **Enable for all accounts** in the **Automated agent configuration** section

   For the Amazon ECS clusters that have not been excluded, GuardDuty will manage the deployment of the security agent in the sidecar container.

1. Choose **Save**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for selective (inclusion-only) Amazon ECS clusters (cluster level) ]

Regardless of how you choose to enable Runtime Monitoring, the following steps will help you monitor selective Amazon ECS Fargate tasks for all of the member accounts in your organization.

1. Do not enable any configuration in the Automated agent configuration section. Keep the Runtime Monitoring configuration the same as you selected in the previous step.

1. Choose **Save**.

1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------
**Note**  
When using inclusion tags for your Amazon ECS clusters, you don't need to enable **GuardDuty agent auto-management** explicitly.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------

### Enabling automated agent configuration for existing active member accounts
<a name="ecs-enable-existing-active-member-accounts"></a>

------
#### [ Manage for all Amazon ECS clusters (account level) ]

1. On the Runtime Monitoring page, under the **Configuration** tab, you can view the current status of Automated agent configuration.

1. Within the Automated agent configuration pane, under the **Active member accounts** section, choose **Actions**.

1. From **Actions**, choose **Enable for all existing active member accounts**. 

1. Choose **Confirm**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for all Amazon ECS clusters but exclude some of the clusters (cluster level) ]

1. Add a tag to this Amazon ECS cluster with the key-value pair as `GuardDutyManaged`-`false`.

1. Prevent modification of tags, except by the trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. 
**Note**  
Always add the exclusion tag to your Amazon ECS clusters before enabling Automated agent configuration for your account; otherwise the GuardDuty sidecar container will be attached to all the containers in the Amazon ECS tasks that get launched.

   Under the **Configuration** tab, in the Automated agent configuration section, under **Active member accounts**, choose **Actions**.

1. From **Actions**, choose **Enable for all active member accounts**.

   For the Amazon ECS clusters that have not been excluded, GuardDuty will manage the deployment of the security agent in the sidecar container.

1. Choose **Confirm**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for selective (inclusion only) Amazon ECS clusters (cluster level) ]

1. Add a tag to an Amazon ECS cluster for which you want to include all of the tasks. The key-value pair must be `GuardDutyManaged`-`true`.

1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------
**Note**  
When using inclusion tags for your Amazon ECS clusters, you don't need to enable **Automated agent configuration** explicitly.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------

### Auto-enable Automated agent configuration for new members
<a name="ecs-auto-enable-new-members-only"></a>

------
#### [ Manage for all Amazon ECS clusters (account level) ]

1. On the Runtime Monitoring page, choose **Edit** to update the existing configuration.

1. In the Automated agent configuration section, select **Automatically enable for new member accounts**.

1. Choose **Save**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for all Amazon ECS clusters but exclude some of the clusters (cluster level) ]

1. Add a tag to this Amazon ECS cluster with the key-value pair as `GuardDutyManaged`-`false`.

1. Prevent modification of tags, except by the trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. 
**Note**  
Always add the exclusion tag to your Amazon ECS clusters before enabling Automated agent configuration for your account; otherwise the GuardDuty sidecar container will be attached to all the containers in the Amazon ECS tasks that get launched.

   Under the **Configuration** tab, select **Automatically enable for new member accounts** in the **Automated agent configuration** section.

   For the Amazon ECS clusters that have not been excluded, GuardDuty will manage the deployment of the security agent in the sidecar container.

1. Choose **Save**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for selective (inclusion only) Amazon ECS clusters (cluster level) ]

1. Add a tag to an Amazon ECS cluster for which you want to include all of the tasks. The key-value pair must be `GuardDutyManaged`-`true`.

1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------
**Note**  
When using inclusion tags for your Amazon ECS clusters, you don't need to enable **Automated agent configuration** explicitly.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------

### Enabling Automated agent configuration for active member accounts selectively
<a name="ecs-enable-gdu-agent-individual-active-members"></a>

------
#### [ Manage for all Amazon ECS (account level) ]

1. On the Accounts page, select the accounts for which you want to enable Runtime Monitoring-Automated agent configuration (ECS-Fargate). You can select multiple accounts. Make sure that the accounts that you select in this step are already enabled with Runtime Monitoring.

1. From **Edit protection plans**, choose the appropriate option to enable **Runtime Monitoring-Automated agent configuration (ECS-Fargate)**.

1. Choose **Confirm**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for all Amazon ECS clusters but exclude some of the clusters (cluster level) ]

1. Add a tag to this Amazon ECS cluster with the key-value pair as `GuardDutyManaged`-`false`.

1. Prevent modification of tags, except by the trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. 
**Note**  
Always add the exclusion tag to your Amazon ECS clusters before enabling GuardDuty agent auto-management for your account; otherwise the GuardDuty sidecar container will be attached to all the containers in the Amazon ECS tasks that get launched.

   On the Accounts page, select the accounts for which you want to enable Runtime Monitoring-Automated agent configuration (ECS-Fargate). You can select multiple accounts. Make sure that the accounts that you select in this step are already enabled with Runtime Monitoring.

   For the Amazon ECS clusters that have not been excluded, GuardDuty will manage the deployment of the security agent in the sidecar container.

1. From **Edit protection plans**, choose the appropriate option to enable **Runtime Monitoring-Automated agent configuration (ECS-Fargate)**.

1. Choose **Save**.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------
#### [ Manage for selective (inclusion only) Amazon ECS clusters (cluster level) ]

1. Make sure you don't enable **Automated agent configuration** (or **Runtime Monitoring-Automated agent configuration (ECS-Fargate)**) for the selected accounts that have the Amazon ECS clusters that you want to monitor. 

1. Add a tag to an Amazon ECS cluster for which you want to include all of the tasks. The key-value pair must be `GuardDutyManaged`-`true`.

1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "Null": {
                       "ecs:ResourceTag/GuardDutyManaged": false
                   }
               }
           },
           {
               "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
               "Effect": "Deny",
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],
               "Resource": [
                   "*"
               ],
               "Condition": {
                   "StringNotEquals": {
                       "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },
                   "ForAnyValue:StringEquals": {
                       "aws:TagKeys": [
                           "GuardDutyManaged"
                       ]   
                   }   
               }
           },
           {       
               "Sid": "DenyModifyTagsIfPrinTagNotExists",
               "Effect": "Deny", 
               "Action": [
                   "ecs:TagResource",
                   "ecs:UntagResource"
               ],      
               "Resource": [
                   "*"     
               ],      
               "Condition": {
                   "StringNotEquals": {
                       "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                   },      
                   "Null": {
                       "aws:PrincipalTag/GuardDutyManaged": true
                   }       
               }       
           }
       ]
   }
   ```

------
**Note**  
When using inclusion tags for your Amazon ECS clusters, you don't need to enable **Automated agent configuration** explicitly.

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.

------

## Configuring GuardDuty agent for a standalone account
<a name="ecs-fargate-manage-agent-standalone-account"></a>

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. Under the **Configuration** tab:

   1. 

**To manage Automated agent configuration for all Amazon ECS clusters (account level)**

      Choose **Enable** in the **Automated agent configuration** section for **AWS Fargate (ECS only)**. When a new Fargate Amazon ECS task launches, GuardDuty will manage the deployment of the security agent.

      1. Choose **Save**.

   1. 

**To manage Automated agent configuration by excluding some of the Amazon ECS clusters (cluster level)**

      1. Add a tag to the Amazon ECS cluster for which you want to exclude all of the tasks. The key-value pair must be `GuardDutyManaged`-`false`.

      1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

         ```
         {
             "Version":"2012-10-17",		 	 	 
             "Statement": [
                 {
                     "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
                     "Effect": "Deny",
                     "Action": [
                         "ecs:TagResource",
                         "ecs:UntagResource"
                     ],
                     "Resource": [
                         "*"
                     ],
                     "Condition": {
                         "StringNotEquals": {
                             "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                             "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                         },
                         "Null": {
                             "ecs:ResourceTag/GuardDutyManaged": false
                         }
                     }
                 },
                 {
                     "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
                     "Effect": "Deny",
                     "Action": [
                         "ecs:TagResource",
                         "ecs:UntagResource"
                     ],
                     "Resource": [
                         "*"
                     ],
                     "Condition": {
                         "StringNotEquals": {
                             "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                             "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                         },
                         "ForAnyValue:StringEquals": {
                             "aws:TagKeys": [
                                 "GuardDutyManaged"
                             ]   
                         }   
                     }
                 },
                 {       
                     "Sid": "DenyModifyTagsIfPrinTagNotExists",
                     "Effect": "Deny", 
                     "Action": [
                         "ecs:TagResource",
                         "ecs:UntagResource"
                     ],      
                     "Resource": [
                         "*"     
                     ],      
                     "Condition": {
                         "StringNotEquals": {
                             "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                         },      
                         "Null": {
                             "aws:PrincipalTag/GuardDutyManaged": true
                         }       
                     }       
                 }
             ]
         }
         ```

------

      1. Under the **Configuration** tab, choose **Enable** in the **Automated agent configuration** section.
**Note**  
Always add the exclusion tag to your Amazon ECS cluster before enabling GuardDuty agent auto-management for your account; otherwise, the security agent will be deployed in all the tasks that are launched within the corresponding Amazon ECS cluster.

         For the Amazon ECS clusters that have not been excluded, GuardDuty will manage the deployment of the security agent in the sidecar container.

      1. Choose **Save**.

   1. 

**To manage Automated agent configuration by including some of the Amazon ECS clusters (cluster level)**

      1. Add a tag to an Amazon ECS cluster for which you want to include all of the tasks. The key-value pair must be `GuardDutyManaged`-`true`.

      1. Prevent modification of these tags, except by trusted entities. The policy provided in [Prevent tags from being modified except by authorized principles](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin) in the *AWS Organizations User Guide* has been modified to be applicable here.

------
#### [ JSON ]

****  

         ```
         {
             "Version":"2012-10-17",		 	 	 
             "Statement": [
                 {
                     "Sid": "DenyModifyTagsIfResAuthzTagAndPrinTagDontMatch",
                     "Effect": "Deny",
                     "Action": [
                         "ecs:TagResource",
                         "ecs:UntagResource"
                     ],
                     "Resource": [
                         "*"
                     ],
                     "Condition": {
                         "StringNotEquals": {
                             "ecs:ResourceTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                             "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                         },
                         "Null": {
                             "ecs:ResourceTag/GuardDutyManaged": false
                         }
                     }
                 },
                 {
                     "Sid": "DenyModifyResAuthzTagIfPrinTagDontMatch",
                     "Effect": "Deny",
                     "Action": [
                         "ecs:TagResource",
                         "ecs:UntagResource"
                     ],
                     "Resource": [
                         "*"
                     ],
                     "Condition": {
                         "StringNotEquals": {
                             "aws:RequestTag/GuardDutyManaged": "${aws:PrincipalTag/GuardDutyManaged}",
                             "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                         },
                         "ForAnyValue:StringEquals": {
                             "aws:TagKeys": [
                                 "GuardDutyManaged"
                             ]   
                         }   
                     }
                 },
                 {       
                     "Sid": "DenyModifyTagsIfPrinTagNotExists",
                     "Effect": "Deny", 
                     "Action": [
                         "ecs:TagResource",
                         "ecs:UntagResource"
                     ],      
                     "Resource": [
                         "*"     
                     ],      
                     "Condition": {
                         "StringNotEquals": {
                             "aws:PrincipalArn": "arn:aws:iam::123456789012:role/org-admins/iam-admin"
                         },      
                         "Null": {
                             "aws:PrincipalTag/GuardDutyManaged": true
                         }       
                     }       
                 }
             ]
         }
         ```

------

1. When you want GuardDuty to monitor tasks that are part of a service, it requires a new service deployment after you enable Runtime Monitoring. If the last deployment for a specific ECS service was started before you enabled Runtime Monitoring, you can either restart the service, or update the service by using `forceNewDeployment`.

   For steps to update the service, see the following resources:
   + [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*.
   + [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
   + [update-service](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html) in the *AWS CLI Command Reference*.