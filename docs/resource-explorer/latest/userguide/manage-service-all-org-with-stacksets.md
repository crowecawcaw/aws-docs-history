AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Deploying Resource Explorer to the accounts in

an organization

By using AWS CloudFormation StackSets, you can define and deploy to all of the accounts managed in
an organization by AWS Organizations. When you define a stack set, you specify AWS resources that
you want created across your AWS Regions and across all of the target accounts that you
specify. When all of the accounts are part of the same organization, you can take advantage
of AWS CloudFormation integration with Organizations and let those services handle the cross-account role
creation. You can enable automatic deployment in an organization, which automatically
deploys stack instances to new accounts that you might add to the target organization or an
organizational unit (OU) in the future. If you remove an account from the organization, then
AWS CloudFormation automatically deletes any resources that were deployed as part of an organization
stack instance. For more information about StackSets, see [Working with
AWS CloudFormation StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md") in the _AWS CloudFormation User Guide_.

You can use AWS CloudFormation StackSets to turn on and configure AWS Resource Explorer in all of the accounts in
your organization, creating indexes in each enabled Region, and creating views where you
need them.

###### Important

If you try to setup an aggregator index in a Region, you must make sure the account
doesn't have an existing aggregator index in any other Regions. After you demote
an aggregator index to a local index, you must wait 24 hours before you can promote
another index to be the new aggregator index for the account.

## Prerequisites

To use AWS CloudFormation StackSets to deploy Resource Explorer to the accounts in your organization, you, or
the administrator of your organization, must first perform the following steps to enable
stacks with service-managed permissions:

1. The organization must have [all features enabled](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"). If the organization has only consolidated
   billing features enabled, you can't create a stack set with service-managed
   permissions.
2. [Turn on trusted access between AWS CloudFormation and Organizations](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md"). This grants AWS CloudFormation
   permission to create the roles needed in the organization's management account
   and the member accounts AWS CloudFormation will deploy Resource Explorer indexes and views.

Now you can create stack sets with service-managed permissions.

###### Important

You must create the stack sets in the organization's management account. AWS CloudFormation is
a Regional service, so you can view and manage the stack sets you create from only
the Region you originally created them in.

## Creating the stack sets for Resource Explorer

The fully deploy Resource Explorer, you must deploy two stack sets.

- The first stack set creates the aggregator index and default view that lets
  users search for resources across all of the Regions in the account.

Deploy this stack set to **_only_** the single Region in which you want to
create the aggregator index.

- The second stack sets creates a local index and default view. The local index
  replicates its content to the aggregator index.

Deploy this stack set to every enabled Region in the account **_except_** the Region
that contains the aggregator index. Don't choose any Regions that aren't enabled
in the accounts to which you deploy the stack. If you do, the deployment
fails.

Sample templates for each of these are in the following section. For step-by-step
instructions on how to create a stack set using these templates, see [Create a stack set with service-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#stacksets-orgs-associate-stackset-with-org "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#stacksets-orgs-associate-stackset-with-org") in the
_AWS CloudFormation User Guide_.

After you deploy these stack sets to your organization, every account within the scope
you selected, organization or organizational unit, has an aggregator index in the
specified Region, and local indexes in every other Region.

## Sample AWS CloudFormation templates

The following sample template creates the account's aggregator index and a default
view that can search for resources across all Regions in the account where you deploy an
index.

YAML

```
Description: >-
  CFN Stack setting up ResourceExplorer with an Aggregator index, and a new default view.
Resources:
  Index:
    Type: 'AWS::ResourceExplorer2::Index'
    Properties:
      Type: AGGREGATOR
      Tags:
        Purpose: ResourceExplorer CFN Stack
  View:
    Type: 'AWS::ResourceExplorer2::View'
    Properties:
      ViewName: DefaultView
      IncludedProperties:
        - Name: tags
      Tags:
        Purpose: ResourceExplorer CFN Stack
    DependsOn: Index
  DefaultViewAssociation:
    Type: 'AWS::ResourceExplorer2::DefaultViewAssociation'
    Properties:
      ViewArn: !Ref View
```

JSON

```
{
    "Description": "CFN Stack setting up Resource Explorer with an Aggregator index, and a new default view.",
    "Resources": {
        "Index": {
            "Type": "AWS::ResourceExplorer2::Index",
            "Properties": {
                "Type": "AGGREGATOR",
                "Tags": {
                    "Purpose": "ResourceExplorer CFN Stack"
                }
            }
        },
        "View": {
            "Type": "AWS::ResourceExplorer2::View",
            "Properties": {
                "ViewName": "DefaultView",
                "IncludedProperties": [{
                    "Name": "tags"
                }],
                "Tags": {
                    "Purpose": "ResourceExplorer CFN Stack"
                }
            },
            "DependsOn": "Index"
        },
        "DefaultViewAssociation": {
            "Type": "AWS::ResourceExplorer2::DefaultViewAssociation",
            "Properties": {
                "ViewArn": {
                    "Ref": "View"
                }
            }
        }
    }
}
```

The following sample template creates a local index in each enabled Region in all
accounts other than the one with the aggregator index. It also creates a default view
that users can search for resources in only that Region. Users must search with a view
in the aggregator Region to search for resource across all Regions.

YAML

```
Description: >-
  CFN Stack setting up ResourceExplorer with a local index and a new default view.
Resources:
  Index:
    Type: 'AWS::ResourceExplorer2::Index'
    Properties:
      Type: LOCAL
      Tags:
        Purpose: ResourceExplorer CFN Stack
  View:
    Type: 'AWS::ResourceExplorer2::View'
    Properties:
      ViewName: DefaultView
      IncludedProperties:
        - Name: tags
      Tags:
        Purpose: ResourceExplorer CFN Stack
    DependsOn: Index
  DefaultViewAssociation:
    Type: 'AWS::ResourceExplorer2::DefaultViewAssociation'
    Properties:
      ViewArn: !Ref View
```

JSON

```
{
    "Description": "CFN Stack setting up ResourceExplorer with a local index and a new default view.",
    "Resources": {
        "Index": {
            "Type": "AWS::ResourceExplorer2::Index",
            "Properties": {
                "Type": "LOCAL",
                "Tags": {
                    "Purpose": "ResourceExplorer CFN Stack"
                }
            }
        },
        "View": {
            "Type": "AWS::ResourceExplorer2::View",
            "Properties": {
                "ViewName": "DefaultView",
                "IncludedProperties": [{
                    "Name": "tags"
                }],
                "Tags": {
                    "Purpose": "ResourceExplorer CFN Stack"
                }
            },
            "DependsOn": "Index"
        },
        "DefaultViewAssociation": {
            "Type": "AWS::ResourceExplorer2::DefaultViewAssociation",
            "Properties": {
                "ViewArn": {
                    "Ref": "View"
                }
            }
        }
    }
}
```
