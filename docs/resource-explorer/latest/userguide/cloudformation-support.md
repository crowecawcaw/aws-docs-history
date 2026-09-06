

# Creating Resource Explorer resources with CloudFormation
<a name="cloudformation-support"></a>

AWS Resource Explorer is integrated with AWS CloudFormation, a service that helps you model and set up your AWS resources. This integration helps you spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you. Examples of resources include indexes, views, or the assignment of a default view for an AWS Region.

When you use CloudFormation, you can reuse your template to set up your Resource Explorer resources consistently and repeatedly. Just describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions. 

**Using CloudFormation to deploy Resource Explorer to AWS Organizations**  
You can use CloudFormation StackSets to deploy Resource Explorer to all of the accounts in your organization. When you add or create member accounts in your organization, StackSets can automatically configure indexes in each AWS Region, including an aggregator index where you specify, to each new member account. For instructions, see [Deploying Resource Explorer to the accounts in an organization](manage-service-all-org-with-stacksets.md).

## Resource Explorer and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Resource Explorer and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

Resource Explorer supports creating the following resource types in CloudFormation:
+ **[Index](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html)** – Creates an index in a Region and turns on Resource Explorer in that Region. You can specify that the index be either local or the aggregator index for the AWS account. For more information, see [Creating user-owned indexes for enhanced Resource Explorer functionality](manage-service-turn-on-region.md) and [Enabling cross-Region search by creating an aggregator index](manage-aggregator-region.md). 
+ **[View](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html)** – Creates a view that determines what results can appear when a user performs a search. Every search operation must specify a view. You must grant users permission to use the views that you want them to access. For more information, see [Configuring a Resource Explorer view to provide access to resource searches](customer-views.md#configure-views).
**Note**  
You must create a user-owned index in a Region before you can create a view in that same Region. If you create a user-owned index and view as part of the same stack, use the `DependsOn` attribute on the view, as shown in the following example template, to ensure that the index is created first.
+ **[DefaultViewAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html)** – Assigns the specified view to be the default in its Region. When a user doesn't explicitly specify the view to use for a search operation, Resource Explorer attempts to use the default view associated with the Region in which the user performs the search. For more information, see [Setting a default view in an AWS Region](configure-views-set-default.md)

The following example illustrates how you might create one index and a view in the same Region, and set the view to be the default for the Region.

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

For more information, including examples of JSON and YAML templates for Resource Explorer indexes and views, see the [ResourceExplorer2 resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResourceExplorer2.html) in the *AWS CloudFormation User Guide*.

## Troubleshooting CloudFormation setup
<a name="troubleshooting-cloudformation-setup"></a>

If you have existing Resource Explorer resources in your account, you may experience failures running CloudFormation templates to create AWS Resource Explorer indexes and views. Only one index can be created for a given Region. If the CloudFormation templates attempt to create resources in the same Region(s), they will fail (expected behavior) if the templates do not account for the prior existence of these resources. Customers may notice this following the [Immediate Resource Discovery launch](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-immediate-resource-discovery-experience.html). After this release, customers searching in the Unified Search bar or Resource Explorer console will trigger automatic index/view creation in the Region where they searched when they have appropriate permissions. Customers can do the following to work around this behavior:

### Option A: Import existing resources into the CloudFormation stack (recommended)
<a name="troubleshooting-cfn-option-a"></a>

This approach uses CloudFormation's [manual resource import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html) to adopt the auto-created resources into the customer's stack. No resources are deleted, so there is no interruption to resource discovery.

**Caveats**  

+ [Import operations don't allow new resource creations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html). You cannot mix imports and creates in the same operation.
  + If the template contains other new resources beyond index/view, they must be created separately. See [Important constraint for mixed-resource templates](#troubleshooting-cfn-mixed-resource-constraint) for more info.

### Option B: Delete the auto-created resources, then create the stack
<a name="troubleshooting-cfn-option-b"></a>

This approach removes the auto-created resources so the CloudFormation template can create them fresh. No template changes are required, and it works with any template regardless of what other resources it contains.

**Caveats**  

+ There is a temporary gap in resource discovery for the Region while the index is deleted and recreated.
+ Deleting the index also deletes all views in that Region. See [DeleteIndex API reference](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DeleteIndex.html).
+ If the deleted index was an aggregator index, the customer must wait 24 hours before another index can be promoted to aggregator.

### Comparison
<a name="troubleshooting-cfn-comparison"></a>


|  | Option A (Import) | Option B (Delete and Recreate) | 
| --- | --- | --- | 
| Downtime | None | Brief gap in resource discovery | 
| Template change | Add DeletionPolicy: Retain | None | 
| Deployment change | Use import change set instead of create-stack | Run deletion steps before create-stack | 
| Mixed-resource templates | Requires two-step process (see constraint above) | Works in a single create-stack | 
| Rollback safety | Safe: index unaffected by stack deletion | Unsafe: New index will be deleted upon stack deletion/rollback | 
| Best for | Existing production environments, aggregator indexes | New or dev/test environments, simple setups | 

### Full implementation steps
<a name="troubleshooting-cfn-full-implementation-steps"></a>

#### Option A: Import
<a name="troubleshooting-cfn-option-a-steps"></a>

##### Option A Steps (CLI)
<a name="troubleshooting-cfn-option-a-cli"></a>

**1. Retrieve the ARNs of the existing resources**

```
aws resource-explorer-2 get-index --region REGION --query 'Arn' --output text
aws resource-explorer-2 list-views --region REGION --query 'Views' --output text
```

**2. Add DeletionPolicy: Retain to the AREX resources in the template**

This is required by CloudFormation for any resource being imported. It ensures the resource is not deleted if the stack is later removed. The customer can change this after the import if desired.

```
Resources:
  MyIndex:
    Type: AWS::ResourceExplorer2::Index
    DeletionPolicy: Retain
    Properties:
      Type: LOCAL

  MyView:
    Type: AWS::ResourceExplorer2::View
    DeletionPolicy: Retain
    Properties:
      ViewName: my-view
      IncludedProperties:
        - Name: tags
    DependsOn: MyIndex
```

**3. Create the import change set**

Replace `INDEX_ARN`, `VIEW_ARN`, `MyIndex`, and `MyView` with the actual values. The logical resource IDs must match those used in the template.

```
aws cloudformation create-change-set \
  --stack-name STACK_NAME \
  --change-set-name ImportArex \
  --change-set-type IMPORT \
  --template-body file://template.yaml \
  --resources-to-import '[
    {
      "ResourceType": "AWS::ResourceExplorer2::Index",
      "LogicalResourceId": "MyIndex",
      "ResourceIdentifier": {"Arn": "INDEX_ARN"}
    },
    {
      "ResourceType": "AWS::ResourceExplorer2::View",
      "LogicalResourceId": "MyView",
      "ResourceIdentifier": {"ViewArn": "VIEW_ARN"}
    }
  ]' \
  --region REGION
```

**4. Review the change set**

```
aws cloudformation describe-change-set \
  --change-set-name ImportArex \
  --stack-name STACK_NAME \
  --region REGION
```

Verify both resources show `Action: "Import"` before executing.

**5. Execute the change set**

```
aws cloudformation execute-change-set \
  --change-set-name ImportArex \
  --stack-name STACK_NAME \
  --region REGION
```

After the import completes, subsequent stack operations (updates, deletes) work normally.

##### Option A Steps (Console)
<a name="troubleshooting-cfn-option-a-console"></a>

**1. Retrieve the ARNs**

Navigate to **Resource Explorer** → **Settings** in the target Region. Note the index ARN. Then navigate to **Views** and note the view ARN.

**2. Update the template** as described above (add `DeletionPolicy: Retain`).

**3. Import the resources**
+ For a **new stack**: Go to **CloudFormation** → **Create stack** → **With existing resources (import resources)**. Upload the template, then provide the identifier values when prompted (Index ARN and View ARN). See [Creating a stack from existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-new-stack.html).
+ For an **existing stack**: Go to **CloudFormation** → select the stack → **Stack actions** → **Import resources into stack**. Upload the updated template, then provide the identifier values. See [Importing existing resources into a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html).

**4. Review and execute** the import.

##### Important constraint for mixed-resource templates
<a name="troubleshooting-cfn-mixed-resource-constraint"></a>

[Import operations don't allow new resource creations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html). When using `--change-set-type IMPORT` to create a new stack, every resource in the template must be listed in `--resources-to-import`. You cannot mix imports and creates in the same operation.

If the template contains other resources beyond index/view (e.g., S3 buckets, Lambda functions), the customer has two paths:

**Path 1**: Import AREX resources first using a template containing only those resources, then run `update-stack` with the full template to add the remaining resources.

**Path 2**: Create the stack first with the non-AREX resources only (removing index/view from the template), then [import the AREX resources into the existing stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-existing-stack.html). When importing into an existing stack, only the resources being imported need to be in `--resources-to-import`.

If the template contains only AREX resources, no extra steps are needed — a single import operation is sufficient.

#### Option B: Delete and Recreate
<a name="troubleshooting-cfn-option-b-steps"></a>

##### Option B Steps (CLI)
<a name="troubleshooting-cfn-option-b-cli"></a>

**1. Get the index ARN and delete the index (this also deletes all views)**

```
aws resource-explorer-2 get-index --region REGION --query 'Arn' --output text
aws resource-explorer-2 delete-index --arn INDEX_ARN --region REGION
```

**2. Wait for deletion to complete**

```
aws resource-explorer-2 get-index --region REGION --query 'State' --output text
```

Repeat until the state is `DELETED` or the command returns an error (indicating the index no longer exists).

**3. Run create-stack as normal**

```
aws cloudformation create-stack \
  --stack-name STACK_NAME \
  --template-body file://template.yaml \
  --region REGION
```

##### Option B Steps (Console)
<a name="troubleshooting-cfn-option-b-console"></a>

**1.** Navigate to **Resource Explorer** → **Settings** in the target Region.

**2.** Delete the index from the settings page.

**3.** Wait for the index to be fully deleted.

**4.** Create the CloudFormation stack as normal.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)