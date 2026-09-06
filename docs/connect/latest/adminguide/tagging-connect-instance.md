

# Tagging an Connect Customer instance
<a name="tagging-connect-instance"></a>

Instance Tagging provides the ability for you to tag Connect Customer instances and build tailored authorization through tag-based access control (TBAC). To help you manage your Connect Customer instances, you can assign your own metadata in the form of tags to the instance. If you have multiple Connect Customer instances in a single AWS account, each serving different functions or catering to specific lines of business, using tags can help you better organize and apply tag-based access control (TBAC) policies to these instances for improved management and control.

[AWS Tags](tagging.md) serve as a useful tool for organizing your AWS resources. They consist of key-value pairs that help you categorize resources based on criteria like purpose, owner, or environment. With tags, you can identify and manage your resources. With Connect Customer, you can add tags to your instances directly from the AWS console, or by using public APIs.

## Tagging Connect Customer instances at creation
<a name="tagging-connect-instance-at-creation"></a>

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. Choose **Add an instance**.  
![Add an instance that you would like to tag.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-instance-at-creation-1.png)

1. Under **Set identity**, select the type of **Identity management** that you would like to use, enter a customer **Access URL**, and choose **Next**.  
![Set identity management options and enter a customer access URL.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-instance-at-creation-2.png)

1. Under the **Add administrator** section, you can choose the **Add new tag** option if you would like to add tags to your instance.  
![You can chose to add tags on this step of instance creation.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-instance-at-creation-3.png)

1. Enter a `Key` and `Value` pair and choose **Next**.

1. After you have made your desired configurations under the **Set telephony** and **Data storage** steps, review your configurations and choose **Create instance**.  
![Create you instance after reviewing your desired configurations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-instance-at-creation-4.png)

1. After the instance has been created, navigate to the **Account overview** page of the instance and the tags that you added will appear in the **Tags** section.  
![The characters after the last /.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-instance-at-creation-5.png)

## Tagging an existing Connect Customer instance
<a name="tagging-existing-connect-instance"></a>

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. Select an existing instance that you would like to add tags too.  
![An instance that you would like to tag.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-existing-instance-1.png)

1. On the **Account overview**, choose **Add new tag**.  
![The add tag button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-existing-instance-2.png)

1. Enter a `Key` and `Value` pair and choose **Next**. You can add up to 50 tags on a single instance.  
![Add key and value pairs for your tags.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-existing-instance-3.png)

1. Choose **Save** to add your tags to your instance.  
![Save to add your tags to your instance.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tag-existing-instance-4.png)

## Tagging an Connect Customer instance using the API
<a name="tagging-connect-instance-api"></a>

To tag Connect Customer instances using the public APIs, see [TagResource](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/connect/latest/APIReference/API_UntagResource.html).

## Sample IAM policies for scenarios with and without instance tags
<a name="tagging-connect-instance-sample-iam-policies"></a>

For TBAC on instances, you can define IAM policies based on instance tags and assign them to IAM roles to control access to specific instances. The following are sample scenarios and sample IAM policies for how to use conditions on tags or conditions on resource IDs.

**Scenario 1**: Controlling access to a specific Connect Customer instance through an IAM role using tags associated with the instance. The following policy allows access only to instances which are tagged with key:`Environment` and value:`Dev`.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "connect:*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "Dev"
        }
      }
    }
  ]
}
```

------

**Scenario 2**: Controlling access to a specific instance and all resources within the instance without using tags.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "connect:*",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "connect:InstanceId": [
                        "{{AllowedInstanceID-1}}",
                        "{{AllowedInstanceID-2}}"
                    ]
                }
            }
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Deny",
            "Action": "connect:*",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                   "connect:InstanceId": "{{DeniedInstanceID-1}}"
                }
            }
        }
    ]
}
```

------

## Additional information about instance tagging
<a name="tagging-connect-instance-additional-info"></a>

**Replicating instances:** When you create a [replica of your existing Connect Customer instance](create-replica-connect-instance.md) to another Region using the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API, tags from the source instance will not be automatically tagged to the newly replicated instance. You will have to tag the replicated instance manually.

**Tag inheritance:** When you tag an Connect Customer instance, all underlying resources in Connect Customer, such as routing profiles, queues, will not inherit the instance tags. To learn how to control granular access to specific resources in Connect Customer, see how to configure more granular access by using [ tag-based access control](tag-based-access-control.md).