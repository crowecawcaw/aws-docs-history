

# Granting permissions to use identity-enhanced console sessions
<a name="id_credentials_temp_control-access_sts-setcontext"></a>

Identity-enhanced console sessions enables AWS IAM Identity Center user and session IDs to be included in users' AWS console sessions when they sign in. For example, Amazon Q Developer Pro uses identity-enhanced console sessions to personalize the service experience. For more information about identity-enhanced console sessions, see [Enabling identity-enhanced console sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-enhanced-sessions.html) in the *AWS IAM Identity Center User Guide*. For information about Amazon Q Developer setup, see [Setting up Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/setting-up.html) in the *Amazon Q Developer User Guide*.

For identity-enhanced console sessions to be available to a user, you must use an identity-based policy to grant the IAM principal the `sts:SetContext` permission for the resource that represents their own console session. 

**Important**  
By default, users do not have permission to set context for their identity-enhanced console sessions. To allow this, you must grant the IAM principal the `sts:SetContext` permission in an identity-based policy as shown in the policy example below.

The following example identity-based policy grants the `sts:SetContext` permission to an IAM principal, allowing the principal to set identity-enhanced console session context for their own AWS console sessions. The policy resource, `arn:aws:sts::{{account-id}}:self`, represents the caller’s AWS session. The `account-id` ARN segment can be replaced with a wildcard character `*` in cases where the same permission policy is deployed across multiple accounts, such as when this policy is deployed using IAM Identity Center permission sets.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:SetContext",
            "Resource": "arn:aws:sts::{{111122223333}}:self"
        }
    ]
}
```

------