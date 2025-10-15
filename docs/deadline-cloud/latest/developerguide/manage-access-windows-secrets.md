# Manage access to Windows job user secrets

When you configure a queue with a Windows `jobRunAsUser`, you must specify
 an AWS Secrets Manager secret. The value of this secret is expected to be JSON-encoded 
 object of the form:


```
`{
 "password": "JOB_USER_PASSWORD"
}`
```
For Workers to run jobs as the queue’s configured `jobRunAsUser`, the fleet’s 
 IAM role must have permissions to get the value of the secret. If the secret is encrypted
 using a customer-managed KMS key, then the fleet’s IAM role must also have permissions 
 to decrypt using the KMS key.

It is highly recommended to follow the principle of least-privilege for these secrets. 
 This means that access to fetch the secret value of a queue’s `jobRunAsUser` → 
 `windows` → `passwordArn` should be:


* granted to a fleet role when a queue-fleet association is created between the 
 fleet and queue
* revoked from a fleet role when a queue-fleet association is deleted between the fleet and queue
Further, the AWS Secrets Manager secret containing the `jobRunAsUser` password 
 should be deleted when it is no longer being used.


## Grant access to a password secret


Deadline Cloud fleets require access to the `jobRunAsUser` password stored in the queue’s 
 password secret when the queue and fleet are associated. We recommend using the AWS 
 Secrets Manager resource policy to grant access to the fleet roles. If you strictly adhere
 to this guideline, it is easier to determine which fleet roles have access to the secret.


**To grant access to the secret**

1. Open the AWS Secret Manager console to the secret.
2. In the “Resource permissions“ section, add a policy statement of the form:



```

                   `{
 "Version" : "2012-10-17", 
 "Statement" : [
 {
 "Effect" : "Allow",
 "Principal" : {
 "AWS" : "`FLEET_ROLE_ARN`"
 },
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource" : "*"
 }
 ]
}`
               
```

## Revoke access to a password secret


When a fleet no longer requires access to a queue, remove access to the password secret for 
 the queue `jobRunAsUser`. We recommend using the AWS Secrets Manager resource 
 policy to grant access to the fleet roles. If you strictly adhere to this guideline, 
 it is easier to determine which fleet roles have access to the secret.


**To revoke access to the secret**

1. Open the AWS Secret Manager console to the secret.
2. In the Resource permissions section, remove the policy statement of the form:



```

                   `{
 "Version" : "2012-10-17", 
 "Statement" : [
 {
 "Effect" : "Allow",
 "Principal" : {
 "AWS" : "`FLEET_ROLE_ARN`"
 },
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource" : "*"
 }
 ]
}`
               
```
