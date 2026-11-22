

# Additional sample IAM policies for Session Manager

Refer to the following example policies to help you create a custom AWS Identity and Access Management (IAM) policy for any Session Manager user access scenarios you want to support.

**Topics**
+ [Example 1: Grant access to documents in the console](#grant-access-documents-console-example)
+ [Example 2: Restrict access to specific managed nodes](#restrict-access-example-instances)
+ [Example 3: Restrict access based on tags](#restrict-access-example-instance-tags)
+ [Example 4: Allow users to resume and end only sessions they started](#restrict-access-example-user-sessions)
+ [How Session Manager forms session IDs](#restrict-access-example-session-id-prefix)
+ [Example 5: Allow full (administrative) access to all sessions](#restrict-access-example-full-access)

## Example 1: Grant access to documents in the console
<a name="grant-access-documents-console-example"></a>

You can allow users to specify a custom document when they launch a session using the Session Manager console. The following example IAM policy grants permission to access documents with names that begin with **SessionDocument-** in the specified AWS Region and AWS account.

To use this policy, replace each {{example resource placeholder}} with your own information.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetDocument",
                "ssm:ListDocuments"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/SessionDocument-*"
            ]
        }
    ]
}
```

------

**Note**  
The Session Manager console only supports Session documents that have a `sessionType` of `Standard_Stream` which are used to define session preferences. For more information, see [Session document schema](session-manager-schema.md).

## Example 2: Restrict access to specific managed nodes
<a name="restrict-access-example-instances"></a>

You can create an IAM policy that defines which managed nodes that a user is allowed to connect to using Session Manager. For example, the following policy grants a user the permission to start, end, and resume their sessions on three specific nodes. The policy restricts the user from connecting to nodes other than those specified.

**Note**  
For federated users, see [Example 4: Allow users to resume and end only sessions they started](#restrict-access-example-user-sessions).

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111122223333}}:instance/i-1234567890EXAMPLE",
                "arn:aws:ec2:{{us-east-1}}:{{111122223333}}:instance/i-abcdefghijEXAMPLE",
                "arn:aws:ec2:{{us-east-1}}:{{111122223333}}:instance/i-0e9d8c7b6aEXAMPLE",
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/SSM-SessionManagerRunShell"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "arn:aws:ssm:*:*:session/*",
            "Condition": {
                "StringEquals": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": "${aws:userid}"
                }
            }
        }
    ]
}
```

------

## Example 3: Restrict access based on tags
<a name="restrict-access-example-instance-tags"></a>

You can restrict access to managed nodes based on specific tags. In the following example, the user is allowed to start and resume sessions (`Effect: Allow, Action: ssm:StartSession, ssm:ResumeSession`) on any managed node (`Resource: arn:aws:ec2:{{region}}:{{987654321098}}:instance/*`) with the condition that the node is a Finance WebServer (`ssm:resourceTag/Finance: WebServer`). If the user sends a command to a managed node that isn't tagged or that has any tag other than `Finance: WebServer`, the command result includes `AccessDenied`.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ec2:{{us-east-1}}:{{111122223333}}:instance/*"
            ],
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/Finance": [
                        "WebServers"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "arn:aws:ssm:*:*:session/*",
            "Condition": {
                "StringEquals": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": "${aws:userid}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/SSM-SessionManagerRunShell"
            ]
        }
    ]
}
```

------

You can create IAM policies that allow a user to start sessions to managed nodes that are tagged with multiple tags. The following policy allows the user to start sessions to managed nodes that have both the specified tags applied to them. If a user sends a command to a managed node that isn't tagged with both of these tags, the command result includes `AccessDenied`.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/tag-key1": [
                        "tag-value1"
                    ],
                    "ssm:resourceTag/tag-key2": [
                        "tag-value2"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "arn:aws:ssm:*:*:session/*",
            "Condition": {
                "StringEquals": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": "${aws:userid}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:document/SSM-SessionManagerRunShell"
            ]
        }
    ]
}
```

------

For more information about creating IAM policies, see [Managed Policies and Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*. For more information about tagging managed nodes, see [Tagging your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide* (content applies to Windows and Linux managed nodes). For more information about increasing your security posture against unauthorized root-level commands on your managed nodes, see [Restricting access to root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md)

## Example 4: Allow users to resume and end only sessions they started
<a name="restrict-access-example-user-sessions"></a>

Session Manager provides two methods to control which sessions a user in your AWS account can resume and end. You can use either method for IAM users and IAM roles, including roles that are used through IAM Identity Center, SAML or web identity federation, and instance profiles.
+ **Method 1 (recommended)** uses the session resource tag that Session Manager supplies for every session. A condition in the policy allows a user to resume and end only the sessions that they started.
+ **Method 2** scopes permissions by the session ARN prefix. Use this method when you want to grant permissions based on the session ID instead of a condition key.

### Method 1: Grant permissions by using tags supplied by AWS
<a name="restrict-access-example-user-sessions-tags"></a>

You can control which sessions a user can resume and end by including conditional tag key variables in an IAM policy. The condition specifies that the user can resume and end only the sessions that are tagged with one or both of these specific tag keys and a specified value.

When a user in your AWS account starts a session, Session Manager applies two resource tags to the session. The first resource tag is `aws:ssmmessages:target-id`, with which you specify the ID of the managed node that the user is allowed to end. The other resource tag is `aws:ssmmessages:session-id`, whose value is the user ID of the caller that started the session. This value matches the `aws:userid` policy variable. For an IAM user, the value is the user's unique ID (for example, `AIDACKCEVSQ6C2EXAMPLE`). For a role session, the value is in the format `{{role-id}}:{{role-session-name}}` (for example, `AROA123456789EXAMPLE:MySession`).

Because the `${aws:userid}` variable resolves to this value for both IAM users and role sessions, you can use it in your policy instead of hardcoding IDs. To look up the value for a caller, use the `aws sts get-caller-identity` command and refer to the `UserId` field in the output.

**Note**  
Session Manager doesn't support custom tags for this IAM access control policy. You must use the resource tags supplied by AWS, described in the following list.

 ** `aws:ssmmessages:target-id` **   
With this tag key, you include the managed node ID as the value in the policy. In the following policy, the condition allows a user to resume and end only sessions to the node i-02573cafcfEXAMPLE.    
****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/aws:ssmmessages:target-id": [
                        "{{i-02573cafcfEXAMPLE}}"
                    ]
                }
            }
        }
    ]
}
```
If a user tries to resume or end a session for which they haven't been granted permission, they receive an `AccessDeniedException` error.

 ** `aws:ssmmessages:session-id` **   
With this tag key, you allow a user to resume and end only the sessions that they started. The value of this tag is the user ID of the caller, which matches the `${aws:userid}` policy variable. Because `${aws:userid}` resolves to the correct value for both IAM users and role sessions, the following policy applies to both caller types, and you don't need to hardcode a user ID.    
****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": "${aws:userid}"
                }
            }
        }
    ]
}
```
To grant permissions for a specific user instead, you can supply that user's ID as the value. In the following example, `AIDAJQABLZS4A3QDU576Q` represents the unique ID of a user in your AWS account. To retrieve the ID for a user, use the `aws sts get-caller-identity` command and refer to the `UserId` field, or use the IAM `get-user` command. For more information, see [get-user](https://docs.aws.amazon.com/IAM/latest/UserGuide/get-user.html) in the AWS Identity and Access Management section of the *IAM User Guide*.    
****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": "AIDAJQABLZS4A3QDU576Q"
                }
            }
        }
    ]
}
```
For the system tags to be applied, the ID you supply can contain the following characters only: Unicode letters, 0-9, space, `_`, `.`, `:`, `/`, `=`, `+`, `-`, `@`, and `\`.
If a user tries to resume or end a session for which they haven't been granted permission, they receive an `AccessDeniedException` error.

**`aws:ssmmessages:target-id`** and **`aws:ssmmessages:session-id`**  
You can also create IAM policies that allow a user to resume and end sessions that are tagged with both system tags, as shown in the following example.    
****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/aws:ssmmessages:target-id": [
                        "{{i-02573cafcfEXAMPLE}}"
                    ]
                },
                "StringEquals": {
                    "ssm:resourceTag/aws:ssmmessages:session-id": "${aws:userid}"
                }
            }
        }
    ]
}
```

### Method 2: Grant permissions by using the session ARN
<a name="restrict-access-example-user-sessions-username"></a>

You can scope permissions to sessions by using the session ARN. Every session ID has the format `{{prefix}}-{{random-suffix}}`, and the session ARN has the format `arn:aws:ssm:{{region}}:{{account-id}}:session/{{session-id}}`. The credentials of the caller that starts the session determine the session ID prefix. For more information about how Session Manager forms session IDs and which prefix each type of caller receives, see [How Session Manager forms session IDs](#restrict-access-example-session-id-prefix).

The following IAM policy allows a user to view the IDs of all sessions in your account, but allows them to resume and end only the sessions whose session ID begins with a specific prefix. To use this policy, replace {{session-id-prefix}} with the session ID prefix for the user or role.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeSessions"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "arn:aws:ssm:*:*:session/{{session-id-prefix}}-*"
        }
    ]
}
```

------

If your account grants access only to IAM users who sign in with long-term credentials, you can scope sessions by using the `${aws:username}` policy variable. The following policy allows a user to resume and end only the sessions that they started.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeSessions"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "arn:aws:ssm:*:*:session/${aws:username}-*"
        }
    ]
}
```

------

**Note**  
The `aws:username` variable is available only for IAM users who sign in with long-term credentials. It isn't available for role sessions or federated users. For those caller types, use Method 1 or scope by the session ID prefix.

## How Session Manager forms session IDs
<a name="restrict-access-example-session-id-prefix"></a>

Every session ID has the format `{{prefix}}-{{random-suffix}}`, and the session ARN has the format `arn:aws:ssm:{{region}}:{{account-id}}:session/{{session-id}}`. The prefix depends on the credentials of the caller that starts the session. The following table shows the prefix for each type of caller.


| Credential type | Example caller ARN | Session ID prefix | 
| --- | --- | --- | 
| AWS account root user | arn:aws:iam::111122223333:root | root | 
| IAM user | arn:aws:iam::111122223333:user/MaryMajor (or, with a path, arn:aws:iam::111122223333:user/eng/MaryMajor) | MaryMajor (the path isn't included) | 
| IAM role session (AssumeRole, AssumeRoleWithSAML, AssumeRoleWithWebIdentity, IAM Identity Center, Amazon EC2 instance profiles, AWS Lambda, Amazon ECS, and Amazon EKS task roles) | arn:aws:sts::111122223333:assumed-role/AppRole/mary-major-session | mary-major-session (the role session name) | 
| IAM Identity Center example | arn:aws:sts::111122223333:assumed-role/AWSReservedSSO\_Admin\_1a2b/marymajor@example.com | marymajor@example.com | 
| Amazon EC2 instance profile example | arn:aws:sts::111122223333:assumed-role/Ec2Role/i-0abc123def4567890 | i-0abc123def4567890 | 
| AWS Lambda example | arn:aws:sts::111122223333:assumed-role/my-function-role/my-function | my-function | 
| Federated user (GetFederationToken) | arn:aws:sts::111122223333:federated-user/RichardRoe | RichardRoe | 
| Temporary credentials from GetSessionToken | Same ARN as the IAM user or root user | Same as the IAM user or root user | 

**Important**  
Consider the following before you scope sessions by the session ID prefix:  
For roles, the caller chooses the role session name when they call `AssumeRole`. Prefix scoping restricts a user only if something other than the caller sets the session name. For example, the role trust policy can require a specific name with the `sts:RoleSessionName` condition key, or an identity provider or IAM Identity Center can set the name.
A prefix pattern such as `session/MaryMajor-*` also matches sessions that are started by a principal whose prefix begins with `MaryMajor-` (for example, `MaryMajor-Admin`). If either consideration is a concern, use Method 1.

## Example 5: Allow full (administrative) access to all sessions
<a name="restrict-access-example-full-access"></a>

The following IAM policy allows a user to fully interact with all managed nodes and all sessions created by all users for all nodes. It should be granted only to an Administrator who needs full control over your organization's Session Manager activities.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "ssm:StartSession",
                "ssm:TerminateSession",
                "ssm:ResumeSession",
                "ssm:DescribeSessions",
                "ssm:GetConnectionStatus"
            ],
            "Effect": "Allow",
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*"
        }
    ]
}
```

------