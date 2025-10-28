# Prerequisites for configuring Amazon Q Business built-in plugins

###### Important

Built-in plugins require Amazon Q Business Pro subscription. Users with Lite subscriptions cannot access built-in plugin functionality and must upgrade to Pro to use plugins.

###### Note

If you use the console and are creating a new web experience, Amazon Q Business
creates an IAM role with the necessary permissions for you. If you're using the
console and choose to use an existing web experience created before December 3, 2024, or
you use the API, make sure to add the permissions below.

Before you can configure built-in plugins, make sure you've added the following
permissions in you Amazon Q Business web experience’s IAM permissions policy:

- In `Action` field for `"Sid":
"QBusinessConversationPermissions`, add the following permissions to allow
  Amazon Q Business to list plugin actions:

```
{
    "Sid": "QBusinessConversationPermissions",
    "Effect": "Allow",
    "Action": [
        "qbusiness:ListPluginActions",
    ],
    "Resource": "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}"
}
```

Add the following permissions to allow Amazon Q Business to allow your end
users to discover plugins in their web experience:

```
{
    "Sid": "QBusinessPluginDiscoveryPermissions",
    "Effect": "Allow",
    "Action": [
        "qbusiness:ListPluginTypeMetadata",
        "qbusiness:ListPluginTypeActions"
    ],
    "Resource": "arn:aws:qbusiness:{{`region`}}:{{`account_id`}}:application/{{`application_id`}}"
}
```

For the complete set of permissions needed for an IAM role, see [IAM role for an Amazon Q Business web
experience](deploy-experience-iam-role.md "deploy-experience-iam-role.md").

- If you use the console or the API to create a plugin, make sure to add the
  following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:`secret-id`"
 ],
 "Effect": "Allow",
 "Sid": "SecretsManagerPermissions"
 }
 ]
}`

```

To allow Amazon Q to assume a role, use the following trust
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessApplicationTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "qbusiness.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```
