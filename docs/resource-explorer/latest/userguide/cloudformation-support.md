AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Creating Resource Explorer resources with CloudFormation

AWS Resource Explorer is integrated with AWS CloudFormation, a service that helps you model and set up your
AWS resources. This integration helps you spend less time creating and managing your
resources and infrastructure. You create a template that describes all the AWS resources
that you want, and CloudFormation provisions and configures those resources for you. Examples of
resources include indexes, views, or the assignment of a default view for an
AWS Region.

When you use CloudFormation, you can reuse your template to set up your Resource Explorer resources
consistently and repeatedly. Just describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

###### Using AWS CloudFormation to deploy Resource Explorer to AWS Organizations

You can use AWS CloudFormation StackSets to deploy Resource Explorer to all of the accounts in your
organization. When you add or create member accounts in your organization, StackSets can
automatically configure indexes in each AWS Region, including an aggregator index where
you specify, to each new member account. For instructions, see [Deploying Resource Explorer to the accounts in
an organization](manage-service-all-org-with-stacksets.md "manage-service-all-org-with-stacksets.md").

## Resource Explorer and CloudFormation templates

To provision and configure resources for Resource Explorer and related services, you must
understand [AWS CloudFormation
templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md"). Templates are formatted text files in JSON or YAML. These templates
describe the resources that you want to provision in your CloudFormation stacks. If you're
unfamiliar with JSON or YAML, you can use AWS CloudFormation Designer to help you get started with
CloudFormation templates. For more information, see [What is AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the
_AWS CloudFormation User Guide_.

Resource Explorer supports creating the following resource types in CloudFormation:

- **[Index](../../../AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.md")** – Creates an index in a Region and
  turns on Resource Explorer in that Region. You can specify that the index be either local
  or the aggregator index for the AWS account. For more information, see [Completing setup for Resource Explorer](manage-service-turn-on-region.md "manage-service-turn-on-region.md") and [Enabling cross-Region search by creating an
  aggregator index](manage-aggregator-region.md "manage-aggregator-region.md").
- **[View](../../../AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.md")** – Creates a view that determines what
  results can appear when a user performs a search. Every search operation must
  specify a view. You must grant users permission to use the views that you want
  them to access. For more information, see [Configuring a Resource Explorer view to provide access to
  resource searches](customer-views.md#configure-views "customer-views.md#configure-views").

###### Note

You must create an index in a Region before you can create a view in that
same Region. If you create an index and view as part of the same stack, use
the `DependsOn` attribute on the view, as shown in the following
example template, to ensure that the index is created first.

- **[DefaultViewAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.md")** – Assigns the
  specified view to be the default in its Region. When a user doesn't explicitly
  specify the view to use for a search operation, Resource Explorer attempts to use the
  default view associated with the Region in which the user performs the search.
  For more information, see [Setting a default view in an
  AWS Region](configure-views-set-default.md "configure-views-set-default.md")

The following example illustrates how you might create one index and a view in the
same Region, and set the view to be the default for the Region.

**YAML**

```
Description: >-
  Sample CFN Stack setting up Resource Explorer with an aggregator index and a default view
Resources:
  SampleIndex:
    Type: 'AWS::ResourceExplorer2::Index'
    Properties:
      Type: AGGREGATOR
      Tags:
        Purpose: ResourceExplorer Sample CFN Stack
  SampleView:
    Type: 'AWS::ResourceExplorer2::View'
    Properties:
      ViewName: mySampleView
      IncludedProperties:
        - Name: tags
      Tags:
        Purpose: ResourceExplorer Sample CFN Stack
    DependsOn: SampleIndex
  SampleDefaultViewAssociation:
    Type: 'AWS::ResourceExplorer2::DefaultViewAssociation'
    Properties:
      ViewArn: !Ref SampleView
```

**JSON**

```
{
    "Description": "Sample CFN Stack setting up Resource Explorer with an aggregator index and a default view ",
    "Resources": {
        "SampleIndex": {
            "Type": "AWS::ResourceExplorer2::Index",
            "Properties": {
                "Type": "AGGREGATOR",
                "Tags": {
                    "Purpose": "ResourceExplorer Sample Stack"
                }
            }
        },
        "SampleView": {
            "Type": "AWS::ResourceExplorer2::View",
            "Properties": {
                "ViewName": "mySampleView",
                "IncludedProperties": [
                    {
                        "Name": "tags"
                    }
                ],
                "Tags": {
                    "Purpose": "ResourceExplorer Sample CFN Stack"
                }
            },
            "DependsOn": "SampleIndex"
        },
        "SampleDefaultViewAssociation": {
            "Type": "AWS::ResourceExplorer2::DefaultViewAssociation",
            "Properties": {
                "ViewArn": {
                    "Ref": "SampleView"
                }
            }
        }
    }
}
```

For more information, including examples of JSON and YAML templates for Resource Explorer indexes
and views, see the [ResourceExplorer2 resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_ResourceExplorer2.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ResourceExplorer2.md") in the
_AWS CloudFormation User Guide_.

## Learn more about AWS CloudFormation

To learn more about CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User
  Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation Command Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
