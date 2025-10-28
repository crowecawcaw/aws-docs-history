# Get exported outputs from a deployed CloudFormation

stack

When you have multiple stacks in the same AWS account and Region, you might want to share
information between them. This is useful when one stack needs to use resources created by
another stack.

For example, you might have one stack that creates network resources, such as subnets and
security groups, for your web servers. Other stacks that create the actual web servers can then
use the network resources created by the first stack. You don't need to hard code resource IDs
in the stack's template or pass IDs as input parameters.

To share information between stacks, you _export_ output values from one
stack and _import_ them into another stack. Here's how it works:

1. In the first stack's template (for example, the networking stack), you define certain
   values for export by using the `Export` field in the `Outputs`
   section. For more information, see [CloudFormation template Outputs syntax](outputs-section-structure.md "outputs-section-structure.md").
2. When you create or update that stack, CloudFormation exports the output values, making them
   available to other stacks in the same AWS account and Region.
3. In the other stack's template, you use the [Fn::ImportValue](../TemplateReference/intrinsic-function-reference-importvalue.md "../TemplateReference/intrinsic-function-reference-importvalue.md") function to import the exported values from the first stack.
4. When you create or update the second stack (for example, the web server stack),
   CloudFormation automatically retrieves the exported values from the first stack and uses
   them.
   For a walkthrough and sample templates, see [Refer to resource outputs in another CloudFormation
   stack](walkthrough-crossstackref.md "walkthrough-crossstackref.md").

## Exporting stack output values versus using nested

stacks

A nested stack is a stack that you create within another stack by using the
`AWS::CloudFormation::Stack` resource. With nested stacks, you deploy and manage
all resources from a single stack. You can use outputs from one stack in the nested stack
group as inputs to another stack in the group. This differs from exporting values.

If you want to isolate information sharing to within a nested stack group, we suggest that
you use nested stacks. To share information with other stacks (not just within the group of
nested stacks), export values. For example, you can create a single stack with a subnet and
then export its ID. Other stacks can use that subnet by importing its ID. Each stack doesn't
need to create its own subnet. As long as stacks are importing the subnet ID, you can't change
or delete it.

For more information about nested stacks, see [Split a template into reusable pieces using nested
stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md").

## Considerations

The following restrictions apply to cross-stack references:

- For each AWS account, `Export` names must be unique within a Region.
- You can't create cross-stack references across Regions. You can use the intrinsic function
  `Fn::ImportValue` to import only values that have been exported within the same Region.
- For outputs, the value of the `Name` property of an `Export` can't use `Ref` or `GetAtt` functions that depend on a resource.

Similarly, the `ImportValue` function can't include `Ref` or `GetAtt` functions that depend on a resource.

- After another stack imports an output value, you can't delete the stack that is exporting the output value or modify the exported output value. All the imports
  must be removed before you can delete the exporting stack or modify the output value.

## Listing exported output values

If you need to view the exported output values from your stacks, use one of the following
methods:

###### To list exported output

values (console)

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. From the left navigation pane, choose **Exports**.

###### To list exported output values

(AWS CLI)

Use the following [list-exports](../../../cli/latest/reference/cloudformation/list-exports.md "../../../cli/latest/reference/cloudformation/list-exports.md") command. Replace
`us-east-1` with your AWS Region.

```
aws cloudformation list-exports --region `us-east-1`
```

The following is example output.

```
{
    "Exports": [
        {
            "ExportingStackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/private-vpc/99764070-b56c-xmpl-bee8-062a88d1d800",
            "Name": "private-vpc-subnet-a",
            "Value": "subnet-07b410xmplddcfa03"
        },
        {
            "ExportingStackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/private-vpc/99764070-b56c-xmpl-bee8-062a88d1d800",
            "Name": "private-vpc-subnet-b",
            "Value": "subnet-075ed3xmplebd2fb1"
        },
        {
            "ExportingStackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/private-vpc/99764070-b56c-xmpl-bee8-062a88d1d800",
            "Name": "private-vpc-vpcid",
            "Value": "vpc-011d7xmpl100e9841"
        }
    ]
}
```

CloudFormation shows the names and values of the exported outputs for the current region and
the stack they were exported from. To use an exported output value in another stack's
template, you can reference it using the export name and the `Fn::ImportValue` function.

## Listing stacks that import an exported output

value

To delete or change exported output values, you must first find out which stacks are
importing them.

To view the stacks that import an exported output value, use one of the following
methods:

###### To list stacks that import an

exported output value (console)

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the left navigation pane, choose **Exports**.
3. To see which stacks import a given export value, choose the **Export
   Name** for that export value. CloudFormation displays the export details page, which
   lists all the stacks that are importing the value.

###### To list stacks that import an exported

output value (AWS CLI)

Use the [list-imports](../../../cli/latest/reference/cloudformation/list-imports.md "../../../cli/latest/reference/cloudformation/list-imports.md") command. Replace
`us-east-1` with your AWS Region and
`private-vpc-vpcid` with the name of the exported
output value.

```
aws cloudformation list-imports --region `us-east-1` \
    --export-name `private-vpc-vpcid`
```

CloudFormation returns a list of stacks that are importing the value.

```
{
    "Imports": [
        "my-app-stack"
    ]
}
```

Once you know which stacks are importing a particular exported value, you need to modify
those stacks to remove the `Fn::ImportValue` functions that reference the output values. You must
remove all the imports that reference exported output values before you can delete or modify the
exported output values.
