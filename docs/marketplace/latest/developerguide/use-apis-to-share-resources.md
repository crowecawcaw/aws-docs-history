

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Using the AWS Marketplace API to share resources
<a name="use-apis-to-share-resources"></a>

AWS Marketplace Catalog API integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. A *resource* is an entity that users can work with in AWS Marketplace, such as a product, an offer, or a resale authorization. With AWS RAM, you can share some AWS Marketplace Catalog API resources with other AWS accounts. You share resources that you own by creating a *resource share*. A resource share specifies the resources that you want to share and the consumers with whom to share them. 

**Topics**
+ [Prerequisites to share AWS Marketplace entities](#sharing-prereqs)
+ [Share an AWS Marketplace entity](#share-marketplace-entity)

## Prerequisites to share AWS Marketplace entities
<a name="sharing-prereqs"></a>

Before sharing entities in AWS Marketplace Catalog API, you must meet the following prerequisites:
+ You can only have one resource policy attached to your AWS Marketplace entity.
+ To share an AWS Marketplace entity, you must own it in your AWS account. This requirement means that the entity must be allocated or provisioned in your account. You can't share an AWS Marketplace entity that has been shared with you.

## Share an AWS Marketplace entity
<a name="share-marketplace-entity"></a>

With AWS Marketplace resource sharing, entity owners can share their entities with other AWS accounts in AWS Marketplace. Entity-owners can be ISVs and channel partners. Entities that can be shared are products, offers, and resale authorizations. 

**Note**  
At this time, you can only share entities. Entities in AWS Marketplace include `AmiProduct`, `Audience`, `BrandingSettings`, `ContainerProduct`, `Experience`, and `ProcurementPolicy`.

For more information about AWS RAM, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/). For more information about managing your shared resources, see [Using shared AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html) in the *AWS RAM User Guide*.

As a *sharing account*, you can set read-only or both read/write on the resources that you want to share. These permissions determine what operations a *consuming account * can perform on the resources that are shared with them. 
+ **Sharing account** – The resource that is shared and in which the AWS RAM administrator creates the AWS resource share by using AWS RAM.
+ **Consuming account** – The AWS account to which a resource is shared. The resource share can specify an entire account as the principal, or for some resource types, individual roles or users in the account.

To share an AWS Marketplace entity, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. When you share an entity using the AWS Marketplace console, you add it to an existing resource share. To add the AWS Marketplace entity to a new resource share, you must first create the resource share using the [AWS RAM console](https://console.aws.amazon.com/ram).

You can share an AWS Marketplace entity that you own using the AWS Marketplace console, AWS RAM console, or the AWS Command Line Interface (AWS CLI).

**To share an AWS Marketplace entity that you own using the AWS RAM console**  
See [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*.

**To share an AWS Marketplace entity that you own using the AWS CLI**  
Use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command.

**Note**  
For resource types such as entities that support resource-based policies, you can use AWS RAM to share resources to use additional AWS RAM features. For more information, see [Resource-based policy](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-terms-and-concepts.html#term-resource-based-policy) in the *AWS RAM User Guide*. AWS RAM uses the AWS Marketplace Catalog API to automatically construct the resource policy from permissions in a resource share and manages that resource policy for you.

For information about how to set, view, or delete AWS resource-based policies on your AWS Marketplace entity through AWS RAM, see [Allowing actions on all resources ](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/api-access-control.html#allowing-actions-on-all-resources) in the *AWS RAM* *User Guide*. 

### Differences between sharing an entity through AWS RAM and the AWS Marketplace Catalog API
<a name="differences-ram-capi"></a>

In addition to sharing your entity through AWS RAM, you can also set, view, or delete AWS resource-based policies on your entities through the AWS Marketplace Catalog API. However, there are a few differences between sharing your entity through AWS RAM and through the AWS Marketplace Catalog API.

When you share an entity through AWS RAM:
+ If you share your entity with accounts that are outside of AWS Organizations, the consuming account must first accept your sharing request before the entity is shared.
+ The consuming account can discover the shared entity through `ListEntities` with `OwnershipType` set to `SHARED`.
+ You must adhere to several resource quotas. For more information, see [Service quotas for AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/service-quotas.html) in the *AWS RAM User Guide*.

When you share an entity through the AWS Marketplace Catalog API:
+ Your entity will be shared as soon as the `PutResourcePolicy` request succeeds with no input from the consuming account.
+ The consuming account can't discover the shared entity through `ListEntities` with `OwnershipType` set to `SHARED`. Instead, the owner of the sharing account must inform the consuming account of the shared entity ID.

**Note**  
If your use case requires sharing resources that might exceed AWS RAM service quotas, or if you want to share resources without direct input from the consuming account, consider sharing through the AWS Marketplace Catalog API. For all other use cases, consider using AWS RAM to share AWS Marketplace resources.

The following sections detail how you can set, view, or delete AWS resource-based policies on your entities through the AWS Marketplace Catalog API.

**Topics**
+ [Differences between sharing an entity through AWS RAM and the AWS Marketplace Catalog API](#differences-ram-capi)
+ [Attach read-only policy to your resource](#read-only-policy-resource)
+ [Attach read and write resource policy to your resource](#read-and-write-resource-policy)
+ [View resource policy set on your resource](#view-resource-policy-set)
+ [Delete resource policy on your resource](#delete-resource-policy)
+ [View all resources owned by you and shared with you](#view-entities-owned)

### Attach read-only policy to your resource
<a name="read-only-policy-resource"></a>

You can create a read-only resource-based policy on your shared resource using a sharing account. With this policy, the principal can only view the details of the resource that is shared with them.

Request

```
POST /PutResourcePolicy HTTP/1.1 
Content-type: application/json

{
   "ResourceArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6",
   "Policy": { 
        "Version": "2012-10-17",		 	 	 
        "Statement": {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::222233334444:root"
            },
            "Action": [
                "aws-marketplace:DescribeEntity"
            ],
            "Resource": [
                "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6"
            ]
        }
    }
}
```

Response

```
HTTP/1.1 200
Content-type: application/json

{}
```

### Attach read and write resource policy to your resource
<a name="read-and-write-resource-policy"></a>

As a sharing account, you can create a read and write resource-based policy on your shared resource. With this policy, the principal can view the details and perform write operations on the resource that is shared with them.

Request

```
POST /PutResourcePolicy HTTP/1.1 
Content-type: application/json

{
   "ResourceArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6",
   "Policy": { 
        "Version": "2012-10-17",		 	 	 
        "Statement": {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::222233334444:root"
            },
            "Action": [
                "aws-marketplace:DescribeEntity",
                "aws-marketplace:StartChangeSet"
            ],
            "Resource": [
                "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6"
            ]
        }
    }
}
```

Response

```
HTTP/1.1 200
Content-type: application/json

{}
```

### View resource policy set on your resource
<a name="view-resource-policy-set"></a>

As a sharing account, you can view the resource policy that is set on your shared resource.

Request

```
POST /GetResourcePolicy HTTP/1.1 
Content-type: application/json

{
   "ResourceArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6"
}
```

Response

```
HTTP/1.1 200
Content-type: application/json

{
  "Policy": { 
        "Version": "2012-10-17",		 	 	 
        "Statement": {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::222233334444:root"
            },
            "Action": [
                "aws-marketplace:DescribeEntity",
                "aws-marketplace:StartChangeSet"
            ],
            "Resource": [
                "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6"
            ]
        }
    }
}
```

### Delete resource policy on your resource
<a name="delete-resource-policy"></a>

As a sharing account, you can delete the resource policy that is set on your shared resource.

Request

```
POST /DeleteResourcePolicy HTTP/1.1 
Content-type: application/json

{
   "ResourceArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6"
}
```

Response

```
HTTP/1.1 200
Content-type: application/json

{}
```

### View all resources owned by you and shared with you
<a name="view-entities-owned"></a>

As a consuming account, you can view the resources that are shared with you.

**Note**  
You can view the resources shared with you only if the resources were shared through AWS RAM.

Request

```
POST /ListEntities HTTP/1.1
Content-type: application/json
{
   "Catalog": "AWSMarketplace",
   "EntityType": "AmiProduct",
   "FilterList": [ 
      { 
         "Name": "EntityId",
         "ValueList": [ "example2-abcd-1234-5ef6" ]
      }
   ],
   "OwnershipType": "SHARED"
}
```

Response

```
HTTP/1.1 200
Content-type: application/json

{ 
  "EntitySummaryList": [ 
    { 
      "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/example2-abcd-1234-5ef6",
      "EntityId": "example2-abcd-1234-5ef6",
      "EntityType": "AmiProduct",
      "LastModifiedDate": "2018-02-27T13:45:22Z",
      "Name": "TestProduct",
      "Visibility": "public" 
    } 
  ],
  "NextToken": "" 
}
```