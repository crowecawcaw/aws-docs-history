

# Using condition keys to limit access to CloudWatch namespaces
<a name="iam-cw-condition-keys-namespace"></a>

 Use IAM condition keys to limit users to publishing metrics only in the CloudWatch namespaces that you specify. This section provides examples that describe how to allow and exclude users from publishing metrics in a namespace. 

**Allowing publishing in one namespace only**

The following policy limits the user to publishing metrics only in the namespace named `MyCustomNamespace`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Resource": "*",
        "Action": "cloudwatch:PutMetricData",
        "Condition": {
            "StringEquals": {
                "cloudwatch:namespace": "MyCustomNamespace"
            }
        }
    }
}
```

------

**Excluding publishing from a namespace**

The following policy allows the user to publish metrics in any namespace except for `CustomNamespace2`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData"
        },
        {
            "Effect": "Deny",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "CustomNamespace2"
                }
            }
        }
    ]
}
```

------

**Controlling OTLP ingest**

The following policy allows the user to publish metrics using the OTLP API:

------
#### [ JSON ]

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Resource": "*",
            "Action": "cloudwatch:PutMetricData"
        }
    ]
}
```

------

For disabling dual ingest, that is, only using PutMetricData and deny any OTLP ingest, you can use the following policy. It limits the user to publishing metrics using PutMetricData in the namespace `MyCustomNamespace` and at the same time implicitly denies any OTLP ingest due to the `StringEquals` condition:

------
#### [ JSON ]

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricData",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                     "cloudwatch:namespace": "MyCustomNamespace"
                }
            }
         }
    ]
}
```

------

For enabling dual ingest, that is, to allow both PutMetricData and OTLP ingest, you can use the following policy. It limits the user to publishing metrics using PutMetricData in the namespace named `MyCustomNamespace` and at the same time allows OTLP ingest due to the `StringEqualsIfExists` condition:

------
#### [ JSON ]

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricData",
            "Resource": "*",
            "Condition": {
                "StringEqualsIfExists": {
                     "cloudwatch:namespace": "MyCustomNamespace"
                }
            }
         }
    ]
}
```

------