

# AMI allowed instance types
<a name="ami-allowed-instance-types"></a>

As an AMI owner, you can specify which instance types your AMI supports or does not support. This prevents launches on incompatible instance types. Amazon EC2 enforces the allowed instance types at launch time.

For example, if your AMI requires GPU hardware, you can restrict it to GPU instance types only. If your AMI is incompatible with a specific instance family, you can exclude that family from the allowed instance types.

**Topics**
+ [How allowed instance types work](#ami-allowed-instance-types-how-it-works)
+ [Set allowed instance types for an AMI](#ami-allowed-instance-types-set)
+ [View allowed instance types for an AMI](#ami-allowed-instance-types-view)
+ [Launch behavior with allowed instance types](#ami-allowed-instance-types-launch-behavior)
+ [Considerations](#ami-allowed-instance-types-considerations)

## How allowed instance types work
<a name="ami-allowed-instance-types-how-it-works"></a>

You control allowed instance types through the `InstanceTypeSpecification` attribute on an AMI. This attribute contains two lists:
+ `SupportedInstanceTypes` – The instance types that the AMI supports. Only these instance types can launch with the AMI.
+ `UnsupportedInstanceTypes` – The instance types that the AMI does not support. All other instance types can launch with the AMI.

Amazon EC2 evaluates the specification using the following logic:
+ If `InstanceTypeSpecification` is not set, Amazon EC2 allows all instance types. This is the default behavior.
+ If only `SupportedInstanceTypes` is set, only the specified instance types are allowed. Amazon EC2 blocks all other instance types.
+ If only `UnsupportedInstanceTypes` is set, Amazon EC2 allows all instance types except those specified.
+ If both lists are set, the instance type must be in `SupportedInstanceTypes` and must not be in `UnsupportedInstanceTypes`.

### Wildcard support
<a name="ami-allowed-instance-types-wildcards"></a>

Both lists support wildcard patterns using the `*` character. You can use wildcards to match multiple instance types without listing each one individually.

The following table shows examples of wildcard patterns.


| Pattern | Matches | 
| --- | --- | 
| t3.\* | All sizes within the t3 instance family (for example, t3.micro, t3.small, and t3.large) | 
| p4d.\* | All sizes within the p4d instance family | 
| g5.\* | All sizes within the g5 instance family | 
| \*xlarge | Any instance type that is xlarge or larger across all instance families | 
| \*.12xlarge | Any 12xlarge instance type across all instance families | 

## Set allowed instance types for an AMI
<a name="ami-allowed-instance-types-set"></a>

You can set or change the allowed instance types for an AMI by using the Amazon EC2 console or the AWS Command Line Interface (AWS CLI). You must be the AMI owner to perform this procedure.

------
#### [ Console ]

**To set allowed instance types for an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI, and then choose **Actions**, **Manage instance type specification**.

1. Under **Supported instance types** or **Unsupported instance types**, choose **Add**.

1. Select the instance type.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To set supported instance types for an AMI**  
Use the [replace-image-instance-type-specification](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-image-instance-type-specification.html) command. The following example allows all `t3` and `a2` instance types except `t3.micro`.

```
aws ec2 replace-image-instance-type-specification \
    --image-id {{ami-1234567890abcdef0}} \
    --instance-type-specification '{"SupportedInstanceTypes": ["t3.*", "a2.*"], "UnsupportedInstanceTypes": ["t3.micro"]}'
```

**To set only unsupported instance types for an AMI**  
Use the following command to block specific instance types while allowing all others.

```
aws ec2 replace-image-instance-type-specification \
    --image-id {{ami-1234567890abcdef0}} \
    --instance-type-specification '{"UnsupportedInstanceTypes": ["t3.micro", "t3.nano"]}'
```

**To remove the instance type specification from an AMI**  
Use the following command without specifying `--instance-type-specification` to remove the restriction and allow all instance types.

```
aws ec2 replace-image-instance-type-specification \
    --image-id {{ami-1234567890abcdef0}}
```

------

## View allowed instance types for an AMI
<a name="ami-allowed-instance-types-view"></a>

You can view the instance type specification for an AMI by using the Amazon EC2 console or the AWS CLI.

------
#### [ Console ]

**To view the allowed instance types for an AMI**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. On the **Details** tab, view the supported and unsupported instance types.

------
#### [ AWS CLI ]

**To view the instance type specification for an AMI**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command. If the AMI has an instance type specification, the response includes the `InstanceTypeSpecification` field.

```
aws ec2 describe-images \
    --image-ids {{ami-1234567890abcdef0}}
```

The following is example output for an AMI with an instance type specification.

```
{
    "Images": [
        {
            "ImageId": "ami-1234567890abcdef0",
            ...
            "InstanceTypeSpecification": {
                "SupportedInstanceTypes": [
                    {
                        "InstanceType": "t3.*"
                    },
                    {
                        "InstanceType": "a2.*"
                    }
                ],
                "UnsupportedInstanceTypes": [
                    {
                        "InstanceType": "t3.micro"
                    }
                ]
            }
        }
    ]
}
```

------

## Launch behavior with allowed instance types
<a name="ami-allowed-instance-types-launch-behavior"></a>

When you launch an instance, Amazon EC2 checks whether the specified instance type is compatible with the AMI's instance type specification. If the instance type is not allowed, Amazon EC2 blocks the launch and returns an error.

**Example: Blocked launch**  
The following command attempts to launch a `t3.micro` instance using an AMI that does not support `t3.micro`.

```
aws ec2 run-instances \
    --image-id {{ami-1234567890abcdef0}} \
    --instance-type t3.micro
```

Amazon EC2 returns the following error:

```
An error occurred (InvalidParameterCombination) when calling the RunInstances operation: This AMI does not support the specified instance type. Check DescribeImages for InstanceTypeSpecification, and try again.
```

To resolve this error, choose an instance type that the AMI supports. Use the `describe-images` command to view the AMI's instance type specification.

## Considerations
<a name="ami-allowed-instance-types-considerations"></a>

Keep the following information in mind when you use allowed instance types.
+ By default, an AMI has no instance type specification. Amazon EC2 allows all instance types until you explicitly set a specification.
+ Only the AMI owner can set or change the instance type specification.
+ When you copy an AMI using `CopyImage`, Amazon EC2 preserves the instance type specification in the new AMI.
+ Amazon EC2 enforces the instance type specification as a hard block. If the instance type is not allowed, the launch fails with an `InvalidParameterCombination` error.
+ The specification does not affect existing instances. It applies only to new launches.
+ Launch templates and Auto Scaling groups that reference an AMI with an instance type specification can fail if the configured instance type is not allowed. We recommend verifying compatibility before setting a specification on shared AMIs.
+ The `ReplaceImageInstanceTypeSpecification` action replaces the entire specification. To add or remove individual instance types, you must include the complete updated specification in the request.