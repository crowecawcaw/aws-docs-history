

# Create a role for Amazon EC2
<a name="gsg-iam-permissions-roles-ec2"></a>

This role enables your Amazon EC2 resources to communicate with Amazon GameLift Servers FleetIQ. For example, your game servers, which are running on Amazon EC2 instances, need to be able to report health status. Include this role in an IAM instance profile with your Amazon EC2 launch template when creating a Amazon GameLift Servers FleetIQ game server group.

Use the AWS CLI to create a role for Amazon EC2, attach a custom policy with the necessary permissions, and attach the role to an instance profile. For more information, see [Creating a Role for an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console).

------
#### [ AWS CLI ]

These steps describe how to create a service role with custom Amazon GameLift Servers permissions for Amazon EC2 using the AWS CLI. 

1. Create a trust policy file (example: `FleetIQtrustpolicyEC2.json`) with the following JSON syntax.

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
           "Service": "ec2.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Create a new IAM role with [iam create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) and associate it with the trust policy JSON file that you just created.

   Windows: 

   ```
   AWS iam create-role --role-name FleetIQ-role-for-EC2 --assume-role-policy-document file://C:\policies\FleetIQtrustpolicyEC2.json
   ```

   Linux: 

   ```
   AWS iam create-role --role-name FleetIQ-role-for-EC2 --assume-role-policy-document file://policies/FleetIQtrustpolicyEC2.json
   ```

   When the request is successful, the response includes the properties of the newly created role. Take note of the ARN value. You will need this information when setting up your Amazon EC2 launch template.

1. Create a permissions policy file (example: `FleetIQpermissionsEC2.json`) with the following JSON syntax.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "gamelift:*",
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Use [iam put-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html) to attach the permissions policy JSON file, which you just created, to the new role. 

   Windows: 

   ```
   AWS iam put-role-policy --role-name FleetIQ-role-for-EC2 --policy-name FleetIQ-permissions-for-EC2 --policy-document file://C:\policies\FleetIQpermissionsEC2.json
   ```

   Linux: 

   ```
   AWS iam put-role-policy --role-name FleetIQ-role-for-EC2 --policy-name FleetIQ-permissions-for-EC2 --policy-document file://policies/FleetIQpermissionsEC2.json
   ```

   To verify that the permissions policy is attached, call [iam list-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-role-policies.html) with the new role's name.

1. Create an instance profile with [iam create-instance-profile](https://docs.aws.amazon.com/cli/latest/reference/iam/create-instance-profile.html) with the new role for use with Amazon EC2. For more information, see [ Managing Instance Profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html).

   ```
   AWS iam create-instance-profile --instance-profile-name FleetIQ-role-for-EC2
   ```

   When the request is successful, the response includes the properties of the newly created instance profile.

1. Use [iam add-role-to-instance-profile](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html) to attach the role to the instance profile.

   ```
    AWS iam add-role-to-instance-profile --role-name FleetIQ-role-for-EC2 --instance-profile-name FleetIQ-role-for-EC2
   ```

The role and profile is now ready to be used with an Amazon EC2 launch template.

------