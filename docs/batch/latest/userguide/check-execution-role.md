

# Tutorial: Check the IAM execution role
<a name="check-execution-role"></a>

Use the following procedure to check that your account already has the IAM execution role and attach the managed IAM policy, if needed.<a name="procedure_check_execution_role"></a>

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**. 

1. Search the list of roles for `ecsTaskExecutionRole`. If you can't find the role, see [Tutorial: Create the IAM execution role](create-execution-role.md). If you found the role, choose the role to view the attached policies.

1. On the **Permissions** tab, verify that the **AmazonECSTaskExecutionRolePolicy** managed policy is attached to the role. If the policy is attached, your execution role is properly configured. If not, follow the substeps below to attach the policy.

   1. Choose **Add permissions**, then choose **Attach policies**.

   1. Search for **AmazonECSTaskExecutionRolePolicy**.

   1. Check the box to the left of the **AmazonECSTaskExecutionRolePolicy** policy and choose **Attach policies**.

1. Choose **Trust relationships**.

1. Verify that the trust relationship contains the following policy. If the trust relationship matches the policy below, the role is configured correctly. If the trust relationship does not match, choose **Edit trust policy**, enter the following, and choose **Update policy**.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": "ecs-tasks.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------