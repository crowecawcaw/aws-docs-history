

# Permissions
<a name="detect-metrics-export-permissions"></a>

This section contains information about how to set up the IAM roles and policies required to manage AWS IoT Device Defender Detect metrics export. For more information, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

## Give AWS IoT Device Defender detect permission to publish messages to an MQTT topic
<a name="detect-metrics-export-permissions-publish"></a>

If you enable metrics export in [CreateSecurityProfile](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateSecurityProfile.html), you must specify an IAM role with two policies: a permissions policy and a trust policy. The permissions policy grants permission to AWS IoT Device Defender to publish messages that include metrics to an MQTT topic. The trust policy grants AWS IoT Device Defender permission to assume the required role.

### Permission policy
<a name="detect-metrics-export-permissions-policy"></a>

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
                "iot:Publish"
            ],
            "Resource": [
                "arn:aws:iot:us-east-1:123456789012:topic/your-topic-name"
            ]
        }
    ]
}
```

------

### Trust policy
<a name="detect-metrics-export-trust-policy"></a>

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
        "Service": "iot.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

### Pass role policy
<a name="detect-metrics-export-passrole-policy"></a>

You also need an IAM permissions policy attached to the IAM user that allows the user to pass roles. See [Granting a User Permissions to Pass a Role to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).

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
            "Action": [
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::123456789012:role/Role_To_Pass"
        }
    ]
}
```

------