

# Amazon ECS Managed Instances instance profile
<a name="managed-instances-instance-profile"></a>

An instance profile is an IAM container that holds exactly one IAM role and allows Amazon ECS Managed Instances to assume that role securely. The instance profile contains an instance role that the ECS agent assumes to register instances with clusters and communicate with the ECS service.

**Important**  
If you use Amazon ECS Managed Instances with the `AmazonECSInfrastructureRolePolicyForManagedInstances` managed policy, the instance role name must start with `ecsInstanceRole`. The policy scopes `iam:PassRole` to `arn:aws:iam::*:role/ecsInstanceRole*`, so a mismatched name causes an authorization error at task launch. This is common with CloudFormation when you omit `RoleName`, because CloudFormation auto-generates names like `MyStack-InstanceRole-ABC123`.  
If you use a custom infrastructure role policy instead, the instance role can have any name as long as your policy includes an `iam:PassRole` grant targeting the instance role ARN.

## Create the role with the trust policy
<a name="create-instance-role"></a>

Replace all {{user input}} with your own information.

1. Create a file named `ecsInstanceRole-trust-policy.json` that contains the trust policy to use for the IAM role. The file should contain the following:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "Service": "ec2.amazonaws.com"},
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. Use the following AWS CLI command to create a role named `ecsInstanceRole` by using the trust policy that you created in the previous step.

   ```
   aws iam create-role \
         --role-name ecsInstanceRole \
         --assume-role-policy-document file://{{ecsInstanceRole-trust-policy.json}}
   ```

1. Attach the AWS managed `AmazonECSInstanceRolePolicyForManagedInstances` policy to the `ecsInstanceRole` role.

   ```
   aws iam attach-role-policy \
         --role-name ecsInstanceRole \
         --policy-arn arn:aws:iam::aws:policy/AmazonECSInstanceRolePolicyForManagedInstances
   ```
**Note**  
If you choose to apply least-privilege permissions and specify your own permissions instead, you can add the following permissions to help with troubleshooting task-related issues with Amazon ECS Managed Instances:   
`ecs:StartTelemetrySession`
`ecs:PutSystemLogEvents`

You can also use the IAM console's **Custom trust policy** workflow to create the role. For more information, see [Creating a role using custom trust policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html) in the *IAM User Guide*.

After you create the file, you must grant your user permission to pass the role to Amazon ECS.

## Create the instance profile using the AWS CLI
<a name="create-instance-profile"></a>

After creating the role, create the instance profile using the AWS CLI:

```
aws iam create-instance-profile --instance-profile-name ecsInstanceRole 
```

Add the role to the instance profile:

```
aws iam add-role-to-instance-profile \
   --instance-profile-name ecsInstanceRole \
   --role-name ecsInstanceRole
```

Verify the profile was created successfully:

```
aws iam get-instance-profile --instance-profile-name ecsInstanceRole 
```

## Create the instance profile using CloudFormation
<a name="create-instance-profile-cfn"></a>

You can use AWS CloudFormation to create the instance role and instance profile. Choose one of the following options based on whether you use the AWS-managed infrastructure policy or a custom policy.

### Option 1: Use the ecsInstanceRole naming convention (recommended)
<a name="create-instance-profile-cfn-managed"></a>

When you use the AWS-managed infrastructure policy, you must explicitly set `RoleName` to a value that starts with `ecsInstanceRole`. If you omit `RoleName`, CloudFormation auto-generates a name that does not match the managed policy's `iam:PassRole` condition, and tasks fail to launch.

```
Resources:
  EcsInstanceRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: ecsInstanceRole
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonECSInstanceRolePolicyForManagedInstances

  EcsInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: ecsInstanceRole
      Roles:
        - !Ref EcsInstanceRole
```

### Option 2: Use a custom role name
<a name="create-instance-profile-cfn-custom"></a>

If you prefer to let CloudFormation generate the role name, or you use a custom name that does not start with `ecsInstanceRole`, you must add an inline policy on your infrastructure role that grants `iam:PassRole` for the instance role.

```
Resources:
  EcsInstanceRole:
    Type: AWS::IAM::Role
    Properties:
      # No RoleName — CFN auto-generates
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonECSInstanceRolePolicyForManagedInstances

  EcsInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Roles:
        - !Ref EcsInstanceRole

  EcsInfrastructureRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: ecs.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonECSInfrastructureRolePolicyForManagedInstances
      Policies:
        - PolicyName: PassInstanceRoleToEC2
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action: iam:PassRole
                Resource: !GetAtt EcsInstanceRole.Arn
                Condition:
                  StringLike:
                    iam:PassedToService: "ec2.*"
```

## Troubleshooting
<a name="managed-instances-instance-profile-troubleshooting"></a>

### Tasks fail with iam:PassRole authorization error
<a name="managed-instances-instance-profile-ts-passrole"></a>

If your tasks fail with a `ResourceInitializationError` that mentions `iam:PassRole`, verify that your instance role name starts with `ecsInstanceRole`. You can check the auto-generated name in the CloudFormation console under your stack's **Resources** tab. If the name does not match, either:
+ Add `RoleName: ecsInstanceRole` to your `AWS::IAM::Role` resource.
+ Add an explicit `iam:PassRole` inline policy to your infrastructure role. For more information, see [Option 2: Use a custom role name](#create-instance-profile-cfn-custom).