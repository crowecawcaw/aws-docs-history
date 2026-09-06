

# Running operations on EC2 instances automatically in response to events in AWS Health
<a name="automating-instance-actions"></a>

You can automate actions that respond to scheduled events for your Amazon EC2 instances. When AWS Health sends an event to your AWS account, your EventBridge rule can then invoke targets, such as AWS Systems Manager Automation documents, to automate actions on your behalf.

For example, when an Amazon EC2 instance retirement event is scheduled for an Amazon Elastic Block Store (Amazon EBS)-backed EC2 instance, AWS Health will send the `AWS_EC2_PERSISTENT_INSTANCE_RETIREMENT_SCHEDULED` event type to your AWS Health Dashboard. When your rule detects this event type, you can automate the stop and start of the instance. This way, you don't have to perform these actions manually.

**Note**  
To automate actions for your Amazon EC2 instances, the instances must be managed by Systems Manager.

For more information, see [Automating Amazon EC2 with EventBridge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automating_with_cloudwatch_events.html) in the *Amazon EC2 User Guide*.

## Prerequisites
<a name="prerequisites-automation-ec2-instances"></a>

You must create an AWS Identity and Access Management (IAM) policy, create an IAM role, and update the role's trust policy before you can create a rule.

### Create an IAM policy
<a name="create-iam-role-for-ssm-automation"></a>

Follow this procedure to create a customer managed policy for your role. This policy gives the role permission to perform actions on your behalf. This procedure uses the JSON policy editor in the IAM console.

**To create an IAM policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. 

1. Choose **Create policy**.

1. Choose the **JSON** tab.

1. Copy the following JSON and then replace the default JSON in the editor.

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
           "ec2:StartInstances",
           "ec2:StopInstances",
           "ec2:DescribeInstanceStatus"
         ],
         "Resource": [
           "*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "ssm:*"
         ],
         "Resource": [
           "*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "sns:Publish"
         ],
         "Resource": [
           "arn:aws:sns:*:*:Automation*"
         ]
       },
       {
         "Effect": "Allow",
         "Action": [
           "iam:PassRole"
         ],
         "Resource": "arn:aws:iam::{{123456789012}}:role/{{AutomationEVRole}}"
       }
     ]
   }
   ```

------

   1. In the `Resource` parameter, for the Amazon Resource Name (ARN), enter your AWS account ID.

   1. You can also replace the role name or use the default. This example uses {{AutomationEVRole}}.

1. Choose **Next: Tags**.

1. (Optional) You can use tags as key–value pairs to add metadata to the policy.

1. Choose **Next: Review**.

1. On the **Review policy** page, enter a **Name**, such as {{AutomationEVRolePolicy}} and an optional **Description**.

1. Review the **Summary** page to see the permissions that the policy allows. If you're satisfied with your policy, choose **Create policy**.

This policy defines the actions that the role can take. For more information, see [Creating IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*. 

### Create an IAM role
<a name="creating-an-iam-role-for-ssm-automation"></a>

After you create the policy, you must create an IAM role, and then attach the policy to that role.

**To create a role for an AWS service**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose **Create role**.

1. For **Select type of trusted entity**, choose **AWS service**. 

1. Choose **EC2** for the service that you want to allow to assume this role.

1. Choose **Next: Permissions**.

1. Enter the policy name that you created, such as {{AutomationEVRolePolicy}}, and then select the check box next to the policy.

1. Choose **Next: Tags**.

1. (Optional) You can use tags as key–value pairs to add metadata to the role.

1. Choose **Next: Review**. 

1. For **Role name**, enter {{AutomationEVRole}}. This name must be the same name that appears in the ARN of the IAM policy that you created.

1. (Optional) For **Role description**, enter a description for the role.

1. Review the role and then choose **Create role**.

For more information, see [Creating a role for an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the *IAM User Guide*.

### Update the trust policy
<a name="modify-trust-policy"></a>

Finally, you can update the trust policy for the role that you created. You must complete this procedure so that you can choose this role in the EventBridge console.

**To update the trust policy for the role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. In the list of roles in your AWS account, choose the name of the role that you created, such as {{AutomationEVRole}}.

1. Choose the **Trust relationships** tab, and then choose **Edit trust relationship**.

1. For **Policy Document**, copy the following JSON, remove the default policy, and paste the copied JSON in its place.

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
                   "Service": [
                       "ssm.amazonaws.com",
                       "events.amazonaws.com"
                   ]
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. Choose **Update Trust Policy**.

For more information, see [Modifying a role trust policy (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy) in the *IAM User Guide*. 

## Create a rule for EventBridge
<a name="create-rule-for-ssm-automation"></a>

Follow this procedure to create a rule in the EventBridge console so that you can automate the stop and start of EC2 instances that are scheduled for retirement.

**To create a rule for EventBridge for Systems Manager automated actions**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, under **Events**, choose **Rules**.

1. On the **Create rule** page, enter a **Name** and **Description** for your rule.

1. Under **Define pattern**, choose **Event pattern**, and then choose **Pre-defined pattern by service**.

1. For **Service provider**, choose **AWS**.

1. For **Service name**, choose **Health**.

1. For **Event type**, choose **Specific Health events**.

1. Choose **Specific service(s)** and then choose **EC2**.

1. Choose **Specific event type category(s)** and then choose **scheduledChange**. 

1. Choose **Specific event types code(s)** and then choose the event type code. 

   For example, for Amazon EC2 EBS-backed instances, choose **`AWS_EC2_PERSISTENT_INSTANCE_RETIREMENT_SCHEDULED`**. For Amazon EC2 instance store-backed instances, choose **`AWS_EC2_INSTANCE_RETIREMENT_SCHEDULED`**.

1. Choose **Any resource**.

   Your **Event pattern** will look similar to the following example.  
**Example**  

   ```
   {
     "source": [
       "aws.health"
     ],
     "detail-type": [
       "AWS Health Event"
     ],
     "detail": {
       "service": [
         "EC2"
       ],
       "eventTypeCategory": [
         "scheduledChange"
       ],
       "eventTypeCode": [
         "AWS_EC2_PERSISTENT_INSTANCE_RETIREMENT_SCHEDULED"
       ]
     }
   }
   ```

1. Add the Systems Manager Automation document target. Under **Select targets**, for **Target**, choose **SSM Automation**.

1. For **Document**, choose `AWS-RestartEC2Instance`.

1. Expand the **Configure automation parameters(s)** and then choose **Input Transformer**.

1. For the **Input Path** field, enter **`{"Instances":"$.resources"}`**.

1. For the second field, enter **`{"InstanceId": <Instances>}`**.

1. Choose **Use existing role**, and then choose the IAM role that you created, such as {{AutomationEVRole}}.

   Your target should look like the following example.  
![Screenshot of the "SSM Automation" example in the EventBridge console.](http://docs.aws.amazon.com/health/latest/ug/images/event-bridge-event-pattern-ssm-automation.png)
**Note**  
If you don't have an existing IAM role with the required EC2 and Systems Manager permissions and trusted relationship, your role won't appear in the list. For more information, see [Prerequisites](#prerequisites-automation-ec2-instances).

1. Choose **Create**. 

   If an event occurs in your account that matches your rule, EventBridge will send the event to your specified target.