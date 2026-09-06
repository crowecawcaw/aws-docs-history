

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Access control for the AWS Marketplace Catalog API
<a name="catalog-api-access-control"></a>

You can use the AWS Marketplace Catalog API to manage [a seller product in AWS Marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) or an [experience in a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html). However, first make sure your user or role can access the API functionality that you want to call.

Use AWS Identity and Access Management (IAM) to create users and roles and assign policies that grant limited permissions to end users. The policies define the actions that the user or role can take on your resources through the AWS Marketplace Catalog API.

For example, you can define roles such as engineering, marketing, and pricing. Then, you can add a user in your organization to the engineering role. In that role, they might be granted permissions to initiate a change request to publish a new version of your seller product. However, the engineering role doesn't allow the user to list all change sets.

**Note**  
To sell products on AWS Marketplace, your AWS account must be set up as a seller account. For more details about becoming an AWS Marketplace seller, see [Getting started as a seller](https://docs.aws.amazon.com/marketplace/latest/userguide/user-guide-for-sellers.html) in the *AWS Marketplace Seller Guide*.

You can use AWS managed policies, or you can create your own IAM policies to have more granular control than what's available in AWS managed policies. For details about these approaches, see the following topics.

**Topics**
+ [Allowing actions with AWS managed policies](#allowing-actions-with-managed-policies)
+ [Allowing actions on all resources](#allowing-actions-on-all-resources)
+ [Allowing actions on specific resources](#allowing-actions-on-specific-resources)
+ [Allowing actions with specific ChangeType condition key](#allowing-actions-with-specific-changetype-condition-key)
+ [Allowing actions with specific aws:ResourceTag condition key](#allowing-actions-with-specific-resource-tag-condition-key)
+ [Creating a custom IAM role](#create-custom-role)
+ [Managing tags on resources](#managing-tags-on-resources)
+ [Managing tags when requesting changes to resources](#managing-tags-when-requesting-changes-to-resources)
+ [Granting permission to manage tags on resources](#grant-permission-to-mange-tags-on-resources)
+ [Granting permission to manage tags on resources only when those resources have specific tags](#grant-permission-to-manage-tags-resources-specific-tags)
+ [Granting permission to create entities and change sets only with tags](#grant-permission-create-entities-change-sets-tags)

## Allowing actions with AWS managed policies
<a name="allowing-actions-with-managed-policies"></a>

You can use policies that are managed by AWS to grant permissions to your user or role.

To work with products that you sell on AWS Marketplace, you can use the `AWSMarketplaceSellerFullAccess` IAM managed policy, which has full access to the AWS Marketplace Catalog API in addition to its other permissions. You can grant read-only access for the Catalog API with the `AWSMarketplaceSellerProductsReadOnly` policy. For more information, see [Controlling access to AWS Marketplace Management Portal](https://docs.aws.amazon.com/marketplace/latest/userguide/marketplace-management-portal-user-access.html), [Policies and permissions for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html), and [AWS managed policies for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html) in the *AWS Marketplace Seller Guide.*

To manage a private marketplace, you can use the `AWSPrivateMarketplaceAdminFullAccess` IAM managed policy, which has full access to create and edit the private marketplace for your account or AWS organization. For more information, see [Controlling access to AWS Marketplace subscriptions](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-iam-users-groups-policies.html), [Creating a private marketplace administrator](https://docs.aws.amazon.com/marketplace/latest/buyerguide/it-administrator.html), and [AWS managed policies for AWS Marketplace buyers](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.html) in the *AWS Marketplace Buyer Guide.*

Alternatively, you can create your own IAM policies to have more granular control than is available in AWS managed policies. Use the following topics to create your own IAM policies.

## Allowing actions on all resources
<a name="allowing-actions-on-all-resources"></a>

Resources are objects that the actions can act upon. Not every resource type can be specified with every action. Some resource types work with only certain actions. For more information, see [Actions, resources, and condition keys for the AWS Marketplace Catalog](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacecatalog.html) in the *Service Authorization Reference*.

There are two resource types in the Catalog API:
+ **Entity** – An entity is a [seller product in AWS Marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) or an [experience in a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).
+ **ChangeSet** – A change set is returned each time you use Catalog API to make changes to an entity. The change set describes the requested changes and its status. A change set can be canceled if the status is in the `PREPARING` state.

To allow a user or role the permission to make changes to all entities in an AWS account, you can add the following IAM policy. With this policy, the user or role can use the `StartChangeSet` action on all resources (`"*"`).

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": "*"
    }
  ]
}
```

For information about all actions available for the Catalog API, see [Actions, resources, and condition keys for AWS Marketplace Catalog](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacecatalog.html) in the *Service Authorization Reference*.

## Allowing actions on specific resources
<a name="allowing-actions-on-specific-resources"></a>

**Note**  
Resource-level permissions and condition context keys for the `StartChangeSet` action are supported only when used with Catalog API. They are not supported when used with the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management).

Instead of allowing changes to all resources, you can use resource-level permissions to allow changes to specific resources.

For example, you can allow changes to a specific seller product in the AWS account instead of to all seller products. You do this by specifying the Amazon Resource Name (ARN) of the seller product in the `Resource` of the IAM policy.

**Note**  
To specify granular, resource-level permissions with actions that create new change sets, you need to also include a `ChangeSet` ARN to the list of resources. The `ChangeSet` ARN must include the wildcard (`/*`) to match any new change set ID that's created as shown.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:{{123456789012}}:AWSMarketplace/AmiProduct/{{example1-abcd-1234-5ef6-7890abcdef12}}",
        "arn:aws:aws-marketplace:us-east-1:{{123456789012}}:AWSMarketplace/ChangeSet/*"
      ]
    }
  ]
}
```

For another example, you can allow changes to a specific experience in a private marketplace instead of to all experiences. You do this by specifying the ARN of the experience in the `Resource` of the IAM policy.

**Note**  
To specify granular, resource-level permissions with actions that create new change sets, you need to also include a `ChangeSet` ARN to the list of resources. The `ChangeSet` ARN must include the wildcard (`/*`) to match any new change set ID that's created as shown.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:{{123456789012}}:AWSMarketplace/Experience/{{exp-example12345}}",
        "arn:aws:aws-marketplace:us-east-1:{{123456789012}}:AWSMarketplace/ChangeSet/*"
      ]
    }
  ]
}
```

## Allowing actions with specific ChangeType condition key
<a name="allowing-actions-with-specific-changetype-condition-key"></a>

**Note**  
Resource-level permissions and condition context keys for the `StartChangeSet` action are supported only when used with Catalog API. They are not supported when used with the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management).

The Catalog API action `StartChangeSet` has several different change types. You can allow access to only specific change types.

For example, you might only want to allow changes to the metadata of the seller product, such as the product title, and not allow adding new product versions. In this example, the change type `UpdateInformation` allows changing the metadata of a seller product, including the title. For more information about the different change types, see [Working with seller products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) and [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html) in the *AWS Marketplace Catalog API Reference*.

To limit the action to one or multiple change types, specify the `ChangeType` in the condition keys. In the following example IAM policy, the condition operator `StringEquals` specifies that the action is only allowed if the `ChangeType` matches `UpdateInformation`. For more information about condition keys, see [Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the *AWS Identity and Access Management User Guide*.

**Note**  
To specify granular, resource-level permissions with actions that create new change sets, you need to also include a `ChangeSet` ARN to the list of resources. The `ChangeSet` ARN must include the wildcard (`/*`) to match any new change set ID that's created as shown.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example1-abcd-1234-5ef6-7890abcdef12",
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/*"
      ],
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": "UpdateInformation"
        }
      }
    }
  ]
}
```

## Allowing actions with specific aws:ResourceTag condition key
<a name="allowing-actions-with-specific-resource-tag-condition-key"></a>

**Note**  
Resource-level permissions and condition context keys for the `StartChangeSet` action are supported only when used with Catalog API. They are not supported when used with the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management).

You can allow actions on a group of entities without having to keep updating the policy and specifying a possibly growing list of entity ARNs. You can do this with resource tagging. Adding tags to resources allows you to control access to those resources based on their tags. For example, you might want to allow describing a group of seller products without specifying individual ARNs for each seller product.

For example, the following IAM policy allows the `DescribeEntity` action on any entity resource (`"*"`) that has a tag key of `product-team` and tag value of `team-xyz`.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:DescribeEntity"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```

You can also allow describing and canceling change sets that were created with specific tags.

For example, the following IAM policy allows the `DescribeChangeSet` and `CancelChangeSet` actions on any change set resource (`"*"`) that has a tag key of `product-team` and tag value of `team-xyz`.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:DescribeChangeSet",
        "aws-marketplace:CancelChangeSet"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```

Also, you can allow starting change sets on entities only when those entities have specific tags. For example, you can allow changes to seller products with specific tags.

For example, the following IAM policy allows the `StartChangeSet` action on any entity resource (`"*"`) that has a tag key of `product-team` and tag value of `team-xyz`. In addition, the `TagResource` action is required so that when the change set is created, it's tagged with the same tag key and value.

**Note**  
If your policy to allow the `StartChangeSet` action includes a condition to match against specific tags, the same policy must also include the `TagResource` action. This is because the policy condition must match both the tag on the entity and the tag on the newly created change set resulting from the change request. Thus, it requires the user or role to also have the permission to tag the newly created change set. For an example of starting a change set and tagging the change set, see [Example: Adding tags to an entity and change set during creation](#example-adding-tags-entity-creation).

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet",
        "aws-marketplace:TagResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```

## Creating a custom IAM role
<a name="create-custom-role"></a>

Customers who want to use a Resale Authorization ChangeType or a CPPO ChangeType need to create a custom AWS Identity and Access Management (IAM) role. This will support the creation of the Resale Authorization product lifecycle.

**To create a custom IAM role**

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/)).

1. Under **Access management**, choose **Policies**.

1. Choose **Create policy**.

1. For **Step 1: Specify permissions**,

   1. In the **Policy editor**, select the **JSON** button, and then add the following policy:

------
#### [ JSON ]

****  

      ```
      {
      "Version":"2012-10-17",		 	 	 
      	"Statement": [
      		{
      			"Sid": "AllowResaleAuthorizationShareActionsRAMCreate",
      			"Effect": "Allow",
      			"Action": [
      				"ram:CreateResourceShare",
      				"ram:AssociateResourceShare"
      			],
      			"Resource": [
      			    "arn:aws:ram:*:*:*"
      			],
      			"Condition": {
      			    "ArnLikeIfExists": {
      					"ram:ResourceArn": "arn:aws:aws-marketplace:*:*:AWSMarketplace/ResaleAuthorization/*"
      				},
      				"StringEqualsIfExists": {
      					"ram:RequestedResourceType": "aws-marketplace:Entity"
      				}
      			}
      		},
      		{
      			"Sid": "AllowResaleAuthorizationShareActionsRAMAccept",
      			"Effect": "Allow",
      			"Action": [
      				"ram:AcceptResourceShareInvitation",
      				"ram:GetResourceShareInvitations",
      				"ram:GetResourcePolicies",
      				"ram:GetResourceShareAssociations"
      			],
      			"Resource": [
      		    	"arn:aws:ram:*:*:*"
      			]
      		},
      		{
      			"Sid": "AllowResaleAuthorizationShareActionsMarketplace",
      			"Effect": "Allow",
      			"Action": [
      				"aws-marketplace:PutResourcePolicy",
      				"aws-marketplace:GetResourcePolicy",
      				"aws-marketplace:DescribeEntity"
      			],
      			"Resource": "arn:aws:aws-marketplace:*:*:AWSMarketplace/ResaleAuthorization/*"
      		}
      	]
      }
      ```

------

   1. Choose **Next**.

1. For **Step 2: Review and create**, 

   1. For **Policy details**, enter **FullResaleAuthorizationAccess** under **Policy name** and enter an optional **Description**.

   1. Review the **Permissions defined in this policy**.

   1. For **Add tags**, add tags (optional).

   1. Choose **Create policy**.

      You have created the FullResaleAuthorizationAccess policy.

1. Under **Access management**, choose **Roles**.

1. Choose **Create role**.

1. For **Step 1: Select trusted entity**, 

   1. For **Trusted entity type**, choose **Custom trust policy**.

   1. Copy and paste the following custom trust policy into the JSON editor.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Service": "resale-authorization.marketplace.amazonaws.com"
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
       }
      ```

------

   1. Choose **Next**.

1. For **Step 2: Add permissions**, 

   1. Enter **FullResaleAuthorizationAccess** in the search bar.

   1. Select the **FullResaleAuthorizationAccess** permission policy and then choose **Next**.

1. For **Step 3: Name, review, and create**,

1. For **Role details**, enter **FullResaleAuthorizationAccess** as the **Role name** and enter an optional **Description**.

1. Under **Step 1: Select trusted entities**, ensure that the policy name you choose is attached to the role.

1. Under **Step 2: Add permissions**, review the **Policy name**.

1. Under **Step 3: Add tags**, add tags (optional).

1. Choose **Create role**.

   You have created the FullResaleAuthorizationAccess role.

## Managing tags on resources
<a name="managing-tags-on-resources"></a>

You can add, list, and remove tags from existing entities or change sets.

### Add tags to resources
<a name="add-tags-to-resources"></a>

To add tags to an entity or change set, use the `TagResource` API action.

**Request**

```
POST /TagResource HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ResourceArn": "string",
  "Tags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ]
}
```

Request parameters include:
+ Catalog (String) – (Required) Must be `AWSMarketplace`.
+ ResourceArn (String) – (Required) ARN of the change set or entity. A change set describes changes you make with Catalog API. An entity can be a [seller product in AWS Marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) or an [experience in a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).
+ Tags (Array of objects) – (Required) A list of objects specifying each tag key and value. Number of objects allowed: 1–50.
  + Key (String) – (Required) Name of the tag.
    + Regex pattern – `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
    + Character length – 1–128
  + Value (String) – (Required) Value of the tag.
    + Regex pattern – `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
    + Character length – 0–256

**Response**

```
{}
```

### Remove tags from resources
<a name="remove-tags-from-resources"></a>

To remove a tag or list of tags from an entity or change set, use the `UntagResource` API action.

**Request**

```
POST /UntagResource HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ResourceArn": "string",
  "TagKeys": [
    "string"
    ...
  ]
}
```

Request parameters include:
+ Catalog (String) – (Required) Must be `AWSMarketplace`.
+ ResourceArn (String) – (Required) ARN of the change set or entity. A change set describes changes you make with Catalog API. An entity can be a [seller product in AWS Marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) or an [experience in a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).
+ Tags (Array of objects) – (Required) A list of key names of tags to be removed. Number of strings allowed: 0–256.

**Response**

```
{}
```

### List all tags on a resource
<a name="list-all-tags-on-resource"></a>

To list all tags that have been added to and not yet removed from a change set or entity, use the `ListTagsForResource` API action.

**Request**

```
POST /ListTagsForResource HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ResourceArn": "string"
}
```

Request parameters include:
+ Catalog (String) – (Required) Must be `AWSMarketplace`.
+ ResourceArn (String) - (Required) ARN of the change set or entity. A change set describes changes you make with Catalog API. An entity can be a [seller product in AWS Marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) or an [experience in a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html).

**Response**

```
{
  "ResourceArn": "string",
  "Tags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ]
}
```

## Managing tags when requesting changes to resources
<a name="managing-tags-when-requesting-changes-to-resources"></a>

You can add tags when entities or change sets are created.

### Example: Adding tags to a change set when creating a change set
<a name="example-adding-tags-creating-change-set"></a>

The following is an example of a `StartChangeSet` request that updates the product metadata for a seller product. This request adds a tag to the change set that's created with this request by including the tag in the `ChangeSetTags` property.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [ 
    { 
      "ChangeType":"UpdateInformation",
      "Entity": {
        "Identifier":"example1-abcd-1234-5ef6-7890abcdef12",
        "Type":"AmiProduct@1.0"
      },
      "Details": "{\"ProductTitle\":\"My updated title\"}"
    }
  ],
  "ChangeSetTags": [
    {
      "Key": "product-team",
      "Value": "team-xyz"
    }
  ]
}
```

For more information about managing seller products, see [Working with seller products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html) in the *AWS Marketplace Catalog API Reference*.

### Example: Adding tags to an entity and change set during creation
<a name="example-adding-tags-entity-creation"></a>

The following is an example of a `StartChangeSet` request that creates a private marketplace experience entity. The request adds tags to both the entity resource and change set resource created with this request by including the tags in the `EntityTags` and `ChangeSetTags` properties. With these tags, the permission policy of a user or role can be specified to only allow describing or canceling the change set this request creates or only allow creating further change sets on the entity this request creates. For more information, see [Granting permission to create entities and change sets only with tags](#grant-permission-create-entities-change-sets-tags).

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [ 
    { 
      "ChangeType": "CreateExperience",
      "Entity": { 
        "Type": "Experience@1.0"
      },
      "Details": "{\"Name\": \"ExamplePrivateMarketplace\"}",
      "EntityTags": [
        {
          "Key": "product-team",
          "Value": "team-xyz"
        }
      ]
    }
  ],
  "ChangeSetTags": [
    {
      "Key": "product-team",
      "Value": "team-xyz"
    }
  ]
}
```

For more information about managing a private marketplace, see [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html) in the *AWS Marketplace Catalog API Reference*.

## Granting permission to manage tags on resources
<a name="grant-permission-to-mange-tags-on-resources"></a>

To allow a user or role to add, remove, and list tags on all entities or change sets, they need the following IAM policy.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:TagResource",
        "aws-marketplace:UntagResource",
        "aws-marketplace:ListTagsForResource"
      ],
      "Resource": "*"
    }
  ]
}
```

## Granting permission to manage tags on resources only when those resources have specific tags
<a name="grant-permission-to-manage-tags-resources-specific-tags"></a>

You can allow a user or role to add, remove, and list tags on entities or change sets that have specific tags. The following IAM policy allows those actions on any entity resource (`"*"`) that has a tag key of `product-team` and tag value of `team-xyz`.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:TagResource",
        "aws-marketplace:UntagResource",
        "aws-marketplace:ListTagsForResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```

## Granting permission to create entities and change sets only with tags
<a name="grant-permission-create-entities-change-sets-tags"></a>

**Note**  
Resource-level permissions and condition context keys for the `StartChangeSet` action are supported only when used with Catalog API. They are not supported when used with the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management).

You can enforce tagging when entities or change sets are created. Add the following policy to allow the `StartChangeSet` and the `TagResource` actions, with a condition specifying the tag key matches `product-team` and the tag value matches `team-xyz`. This policy condition must match both the tag on the newly created entity and the tag on the newly created change set resulting from the creation request. For an example of tagging an entity on creation, see [Example: Adding tags to an entity and change set during creation](#example-adding-tags-entity-creation).

For existing entities, this policy also enforces tagging change sets when requesting changes to those entities. This also requires that the existing entity has this existing tag. This is because the policy condition must match both the tag on the existing entity and the newly created change set resulting from the change request. For an example of adding tags to change requests, see [Example: Adding tags to a change set when creating a change set](#example-adding-tags-creating-change-set).

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet",
        "aws-marketplace:TagResource"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/product-team": "team-xyz"
        }
      }
    }
  ]
}
```