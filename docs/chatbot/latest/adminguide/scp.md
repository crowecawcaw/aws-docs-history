

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Service control policies (SCPs) for Amazon Q Developer in chat applications
<a name="scp"></a>

Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for the IAM users and IAM roles in your organization. For more information, [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.

SCPs for Amazon Q Developer in chat applications function similarly to channel guardrail policies, but are implemented on the organization level. You can use SCPs to secure your organizations by restricting what APIs can be used to configure Amazon Q Developer in chat applications and which services and operations can be run using Amazon Q Developer. This doesn’t impact resources that are already created or the ability to respond to commands in chat channels.

The global condition key, `aws:ChatbotSourceArn`, is attached to all sessions created through Amazon Q Developer in chat applications. You can use this condition key to restrict which Amazon Q Developer in chat applications API operations can be run using Amazon Q Developer in chat applications as opposed to other platforms such as the CLI or console. 

**Note**  
SCPs for Amazon Q Developer in chat applications are limited to Amazon Q Developer access in chat applications and don't apply to Amazon Q Business access from chat applications.

**Topics**
+ [Example Service control policies](#scp-example)

## Example Service control policies
<a name="scp-example"></a>

### Example 1: Deny all IAM operations
<a name="scp-1"></a>

The following SCP denies all IAM operations invoked through all Amazon Q Developer in chat applications configurations.

```
{
    "Effect": "Deny",
    "Action": "iam:*",
    "Resource": "*",
    "Condition": {
        "ArnLike": {
            "aws:ChatbotSourceArn": "arn:aws:chatbot::*"
        }
    }
}
```

### Example 2: Deny S3 bucket put requests from a specified Slack channel
<a name="scp-2"></a>

The following SCP denies S3 put requests on the specified bucket for all requests originating from a Slack channel.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ExampleS3Deny",
            "Effect": "Deny",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
            "Condition": {
                "ArnLike": {
                      "aws:ChatbotSourceArn": "arn:aws:chatbot::*:chat-configuration/slack-channel/*"
                }
            }
        }
    ]
}
```

------