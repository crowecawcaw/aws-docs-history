# Updating a default event bus using

AWS CloudFormation in EventBridge

CloudFormation enables you to configure and manage your AWS
resources across accounts and regions in a centralized and repeatable manner by
treating infrastructure as code. CloudFormation does this by letting you
create _templates_, which define the resources you want to
provision and manage.

Because EventBridge provisions the default event bus into your account
automatically, you cannot create it using a CloudFormation template, as you
normally would for any resource you wanted to include in a CloudFormation
stack. To include the default event bus in a CloudFormation stack, you must
first _import_ it into a stack. Once you have imported the
default event bus into a stack, you can then update the event bus properties as
desired.

To import an existing resource into a new or existing CloudFormation
stack, you need the following information:

- A unique identifier for the resource to import.

For default event buses, the identifier is `Name` and then identifier value is `default`.

- A template that accurately describes the current properties of the existing resource.

The template snippet below contains an `AWS::Events::EventBus`
resource that describes the current properties of a default event bus. In
this example, the event bus has been configured to use a customer managed key and DLQ for encryption at rest.

Also, the `AWS::Events::EventBus` resource that describes the
default event bus you want to import should include a `DeletionPolicy` property set to `Retain`.

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Default event bus import example",
    "Resources": {
        "defaultEventBus": {
            "Type" : "AWS::Events::EventBus",
            "DeletionPolicy": "Retain",
            "Properties" : {
                "Name" : "default",
                "KmsKeyIdentifier" : "`KmsKeyArn`",
                "DeadLetterConfig" : {
                    "Arn" : "`DLQ_ARN`"
                }
            }
        }
    }
}
```

For more information, see [Bringing existing resources into CloudFormation management](../../../AWSCloudFormation/latest/UserGuide/resource-import.md "../../../AWSCloudFormation/latest/UserGuide/resource-import.md")
in the _CloudFormation User Guide_.
