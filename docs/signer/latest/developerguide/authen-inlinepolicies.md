

# Inline policies for Signer
<a name="authen-inlinepolicies"></a>

Inline policies are standalone identity-based policies that an administrator creates and embeds directly into a single principal (user, group, or role). Administrators can create and manage policies using the [AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html), the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-cli.html), or the [IAM API](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-api.html). 

**To manage policies in the AWS Management Console**

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

**Topics**
+ [Limit Access for Signing to All Signing Profiles Within an Account](#all_profiles)
+ [Limit Access for Signing to a Specific Signing Profile](#particular_profile)
+ [Limit Access for Signing to a Specific Signing Profile Version](#particular_version)
+ [Allow Full Access](#policy-full-access)

## Limit Access for Signing to All Signing Profiles Within an Account
<a name="all_profiles"></a>

The following policies allow a principal to discover every `SigningProfile` within an account and to use any of them to submit, describe, and list signing jobs.

**Policy for Lambda**

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "signer:GetSigningProfile",
            "signer:ListSigningProfiles",
            "signer:StartSigningJob",
            "signer:DescribeSigningJob",
            "signer:ListSigningJobs"
         ],
         "Resource":"*"
      }
   ]
}
```

------

**Policy for containers**

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "signer:GetSigningProfile",
            "signer:ListSigningProfiles",
            "signer:SignPayload",
            "signer:GetRevocationStatus",
            "signer:DescribeSigningJob",
            "signer:ListSigningJobs"
         ],
         "Resource":"*"
      }
   ]
}
```

------

## Limit Access for Signing to a Specific Signing Profile
<a name="particular_profile"></a>

The following policies allow a principal to call `GetSigningProfile` and `StartSigningJob` only on profile `MySigningProfile`.

**Policy for Lambda**

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
                "signer:GetSigningProfile",
                "signer:StartSigningJob"
            ],
            "Resource": "arn:aws:signer:{{us-east-1}}:444455556666:/signing-profiles/{{MySigningProfile}}"
        },
        {
            "Effect": "Allow",
            "Action": [
                "signer:ListSigningJobs",
                "signer:ListSigningProfiles",
                "signer:DescribeSigningJob"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**Policy for containers**

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
                "signer:GetSigningProfile",
                "signer:SignPayload"
            ],
            "Resource": "arn:aws:signer:{{us-east-1}}:444455556666:/signing-profiles/{{MySigningProfile}}"
        },
        {
            "Effect": "Allow",
            "Action": [
                "signer:ListSigningJobs",
                "signer:ListSigningProfiles",
                "signer:DescribeSigningJob"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Limit Access for Signing to a Specific Signing Profile Version
<a name="particular_version"></a>

The following policy allows a principal to call `GetSigningProfile` and `StartSigningJob` only on version `abcde12345` of profile `MySigningProfile`.

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
                "signer:GetSigningProfile",
                "signer:SignPayload"
            ],
            "Resource": "arn:aws:signer:{{us-east-1}}:444455556666:/signing-profiles/{{MySigningProfile}}",
            "Condition": {
                "StringEquals": {
                    "signer:ProfileVersion": "{{version}}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "signer:ListSigningJobs",
                "signer:ListSigningProfiles",
                "signer:DescribeSigningJob"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Allow Full Access
<a name="policy-full-access"></a>

 The following policy allows a principal to perform any AWS Signer action. 

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":"signer:*",
         "Resource":"*"
      }
   ]
}
```

------