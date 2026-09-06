

# Troubleshooting session credentials
<a name="session-credentials-troubleshooting"></a>

**"Cannot assume role" error on StartStreamSession**  
The role's trust policy does not allow `gameliftstreams.amazonaws.com` to assume it. Verify that:  
+ The trust policy includes the service principal and `sts:AssumeRole` action.
+ The `aws:SourceAccount` condition matches your account ID.
+ The role name starts with `GameLiftStreams-`.

**"Service-linked role cannot be used" error**  
You specified a [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (identified by an ARN containing `/aws-service-role/`). Create an IAM role with a name starting with `GameLiftStreams-` instead.

**"Cross-account role is not supported" error**  
The role belongs to a different AWS account than the caller. The role must be in the same account as the stream group.

**Application cannot find credentials at runtime**  
Verify that you passed `RoleArn` when calling `StartStreamSession`. If the session started without a role, credentials are not available. To confirm credentials from within your session, run:  

```
aws sts get-caller-identity
```
Also check that your application is not overriding the credential provider chain by setting `AWS_ACCESS_KEY_ID` or configuring a specific credentials source in your SDK client.

**Credentials stop working mid-session**  
This might happen if you delete or modify the IAM role's trust policy while the session is active. The credential refresh cannot obtain new credentials if the role is no longer assumable. Avoid modifying roles that are in use by active sessions.

**"Access denied" on iam:PassRole**  
The IAM principal calling `StartStreamSession` does not have `iam:PassRole` permission for the specified role. Add the following statement to the caller's IAM policy:  

```
{
  "Effect": "Allow",
  "Action": "iam:PassRole",
  "Resource": "arn:aws:iam::{{123456789012}}:role/GameLiftStreams-{{MyAppRole}}",
  "Condition": {
    "StringEquals": {
      "iam:PassedToService": "gameliftstreams.amazonaws.com"
    }
  }
}
```
Replace the role ARN with the ARN of the role you want to pass. You can use a wildcard (`arn:aws:iam::{{123456789012}}:role/GameLiftStreams-*`) if you have multiple roles with the required prefix. For more information about passing IAM roles to AWS services, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *IAM User Guide*.

**"Stream group does not support IAM role credentials" error**  
The stream group was created before July 16, 2026. Create a new stream group to use this feature.