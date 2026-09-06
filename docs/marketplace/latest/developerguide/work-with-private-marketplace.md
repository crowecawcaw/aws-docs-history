

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with the private marketplace using the AWS Marketplace API
<a name="work-with-private-marketplace"></a>

You can use the AWS Marketplace Catalog API to manage a *private marketplace* for your AWS account or [organization](https://docs.aws.amazon.com/organizations/latest/userguide/).

All change types can be called only from the organization's management account or by a member account that is a delegated administrator for private marketplace. If you're a current private marketplace customer without the AWS Organizations integration for private marketplace, you can create and manage a private marketplace from any account in your organization that has the `AWSPrivateMarketplaceAdminFullAccess` IAM policy.

 For more information about private marketplaces, see [Private marketplaces](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-marketplace.html) in the *AWS Marketplace Buyer Guide*. 

 The following table details a set of tasks to manage private marketplaces and the change types that apply to each task. 


| Task | Action | Change types | 
| --- | --- | --- | 
| [Creating a private marketplace](#creating-a-private-marketplace) | `StartChangeSet` | `CreateExperience`<br />`CreateProcurementPolicy` | 
| [Changing the branding of a private marketplace experience](#private-marketplace-branding) | `StartChangeSet` | `CreateBrandingSettings`<br />`UpdateBrandingSettings` | 
| [Enabling or disabling a private marketplace experience](#enable-private-marketplace) | `StartChangeSet` | `UpdateExperience` | 
| [Enabling or disabling user requests](#private-marketplace-user-requests) | `StartChangeSet` | `UpdateProcurementPolicy` | 
| [Getting a list of products in a private marketplace experience](#private-marketplace-policy-details) | `DescribeEntity` | Not applicable | 
| [Adding or removing products from a private marketplace](#private-marketplace-add-products) | `StartChangeSet` | `AllowProductProcurement`<br />`DenyProductProcurement` | 
| [Finding products](#finding-product-ids) | Not applicable | Not applicable | 
| [Working with private marketplaces for AWS Organizations](#private-marketplace-organizations) | Not applicable | Not applicable | 
| [Associating principals to experiences](#private-marketplace-associate-accounts) | `StartChangeSet` | `AssociateAudience`<br />`DisassociateAudience` | 
| [Archiving and reactivating a private marketplace experience](#archiving-and-reactivating-a-private-marketplace-experience-capi) | `StartChangeSet` | `RestrictExperience`<br />`ReviveExperience` | 

## Creating a private marketplace
<a name="creating-a-private-marketplace"></a>

A private marketplace for an AWS account can be thought of as a list of products that users are allowed to procure in that account, and branding for the marketplace. In an organization with multiple accounts, you can use the grouping from AWS Organizations called [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) to associate to an experience. For example, you could have one set of products that all accounts in the organization are allowed to procure, or you could have a diﬀerent list of products for each OU in the organization. You can also have a diﬀerent list of products for individual accounts in the organization. Each list of approved products and branding is called a procurement *experience*. 

In the AWS Marketplace Catalog API, four entities represent an experience:
+ `Experience` entity – This entity is at the highest level of the experience and contains two child entities.
+ `ProcurementPolicy` entity – This entity represents the products that have been allowed and denied in your private marketplace.
+ `BrandingSettings` entity – You can also create a `BrandingSettings` entity to define how your private marketplace looks to your users. 
+ `Audience` entity – You must also associate one or more `Audience` entities, which deﬁne the set of AWS accounts, OUs, or organization that the experience applies to.

The steps to create a procurement experience are as follows:

1. Create the `Experience` entity.

1. Create a `ProcurementPolicy` entity to store the list of products that are allowed or denied for the experience.

1. (Optional) Create a `BrandingSettings` entity to customize the look of your marketplace experience.

1. Associate principals with your experience. A principal can be an AWS account, OU, or the organization.

1. Enable the experience.

**Note**  
If your account is part of an organization in AWS Organizations, see [Working with private marketplaces for AWS Organizations](#private-marketplace-organizations).

**Create the `Experience` entity**

To create the `Experience` entity, use the `StartChangeSet` action with the `CreateExperience` value for the `ChangeType` parameter to request that the experience be created by AWS Marketplace. See the following code example.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateExperience",
      "DetailsDocument":
      {
        "Name": "ExamplePrivateMarketplace"
      },
      "Entity":
      {
        "Type": "Experience@1.0"
      }
    }
  ],
  "ChangeSetName": "Create Private Marketplace Example"
}
```

In this action, `Entity` is a template for the entity that you want to create. It is assigned an `EntityId` when it is created. `ChangeSetName` identifies the change to help you find it later.

The response looks like the following.

```
{
   "ChangeSetArn": "arn:...:AWSMarketplace/ChangeSet/abcd1234example5678frjzkz",
   "ChangeSetId": "abcd1234example5678frjzkz"
}
```

The response includes a `ChangeSetId` that you can use to get the status of your change request as it is processed with `DescribeChangeSet`. You can also use `ListEntities` to find your `Experience` entity without the `ChangeSetId`. For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets).

A newly created `Experience` entity doesn't have a procurement policy by default. It is also created with default settings for branding. For more information about branding settings, including how to customize them, see [Changing the branding of a private marketplace experience](#private-marketplace-branding).

**Create a `ProcurementPolicy` entity**

You must create a `ProcurementPolicy` entity. By default, a new `Experience` entity is disabled, so you can create the procurement policy before enabling it.

**Note**  
An `Experience` entity with *no* procurement policy (null) allows all products to be procured in your private marketplace. An `Experience` entity with an *empty* procurement policy has no products available to users to procure.

To allow and deny products in your private marketplace, you must create the procurement policy. To do this, you again call `StartChangeSet`, but this time with the `ChangeType` of `CreateProcurementPolicy`. The following code example creates an empty procurement policy.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateProcurementPolicy",
      "DetailsDocument":
      {
        "Name": "ExampleProcurementPolicy"
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example@1"
      }
    }
  ]
}
```

The `Entity` you provide in this action is the `Experience` entity that you want the procurement policy created within, so you must include the identifier for the entity that you created earlier. Use `ListEntities` to find the `Experience` entity. You can also return the identifier by using `DescribeChangeSet` with the change set identifier from the `CreateExperience` action

**Note**  
This example shows the identifier with a revision of `1`. For more information about revisions for identifiers, see [Identifier](catalog-apis.md#identifier).

You can again use `DescribeChangeSet` on the `CreateProcurementPolicy` change type to follow the processing of your request.

**Note**  
The names you give the `Experience` and `ProcurementPolicy` objects do not appear in AWS Marketplace. The names are only for your ease of finding the entities in the API.

After you have created the procurement policy, your private marketplace displays in the AWS Management Console. (You can go to the [Private Marketplace page](https://aws.amazon.com/marketplace/privatemarketplace) to see it.) After you have completed these steps, your private marketplace will be disabled, have default branding, have an empty procurement policy, and will not be associated with any principals in your organization. You can update the branding and add any products that you want in it, associate the experience with one or more accounts, and then enable your private marketplace.

The following sections describing managing your private marketplace with the AWS Marketplace Catalog API.

## Changing the branding of a private marketplace experience
<a name="private-marketplace-branding"></a>

You can customize the look of your private marketplace for your users. Without customization, your private marketplace will have the default branding settings, which are described below. Aspects of branding that you can change in a private marketplace include the following:
+ `Title` – The name displayed for your private marketplace. This is the same as the **Name** field in the private marketplace **Profile settings** screen. If you set the `Title` to **Example**, then the text displayed is **Example Private Marketplace**. The default is **Private Marketplace**.
+ `Information` – The paragraph displayed under the name in your private marketplace. This is the same as the **Description** field in **Profile settings**. The default is no information, in which case a general description of private marketplaces is displayed.
+ `ThemeColor` – The color displayed in the banner of your private marketplace. This is a color in RGB hexadecimal format. This value is the same as the **Theme color** field in **Profile settings**. The default value is `#232F3E`.
+ `LogoUrl` – The URL that points to an image file to be used as the logo on your private marketplace. The URL must be publicly available (for example, a signed Amazon S3 URL). The file must be either a .png or .svg file and be under 500kb. If necessary, the image file will be resized to a maximum height of 30 pixels and a maximum width of 100 pixels. This is the same value as the **Logo** **Select** in **Profile Settings**. The default is to not show a logo.

To set these values, you must first create a `BrandingSettings` entity with the `CreateBrandingSettings` change type. You can then request an `UpdateBrandingSettings` change to set or change the branding. You only need to create a `BrandingSettings` object once. To create this object, call `StartChangeSet` with the `CreateBrandingSettings` change type, as shown in the following code example.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateBrandingSettings",
      "DetailsDocument":
      {
        "Name": "ExampleBrandingSettingsName"
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example@2"
      }
    }
  ]
}
```

This example modifies the `Experience` entity by adding the `BrandingSettings` object to it. The revision of the entity identifier has incremented to `2`. For more information about revisions for identifiers, see [Identifier](catalog-apis.md#identifier).

**Note**  
You can specify all the details of the branding settings in the call to create the branding settings entity. The details facet is the same for `CreateBrandingSettings` and `UpdateBrandingSettings`.

You modify the settings by calling `StartChangeSet` with the `UpdateBrandingSettings` change type. The settings are part of the `Configuration` of the `DetailsDocument` object.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateBrandingSettings",
      "DetailsDocument":
      {
        "Name": "ExampleBrandingSettingsName",
        "Description": "Example description",
        "Configuration":
        {
          "Title": "ExampleName",
          "Information": "Example description.",
          "ThemeColor": "#0e7f74",
          "LogoUrl": "https://example.com/path/mylogo.png"
        }
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example@3"
      }
    }
  ]
}
```

**Note**  
The URL for the logo is used to make a copy during the update change. After the change is complete, if you remove or change the URL at that path, it will not affect your private marketplace unless you again request `UpdateBrandingSettings`.

## Enabling or disabling a private marketplace experience
<a name="enable-private-marketplace"></a>

When a private marketplace is enabled (and has a procurement policy), users in associated accounts can only purchase products that you have approved. When no private marketplace experience is enabled for an account, users can purchase products across the full AWS Marketplace catalog.

To enable a private marketplace, use the `StartChangeRequest` action with the `UpdateExperience` change type.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateExperience",
      "DetailsDocument":
      {
        "Status": "Enabled"
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example@4"
      }
    }
  ]
}
```

Similarly, you can use the same action and `ChangeType`, but change the `Status` in `DetailsDocument` to `Disabled` to disable a private marketplace.

**Note**  
Disabling a private marketplace keeps your list of both allowed and denied products, as well as customizations, such as branding. When a private marketplace is disabled, users no longer see the private marketplace (although they may still be governed by the default experience for the organization). If there are no private marketplace experiences enabled for an account, then all restrictions are removed, and users are able to procure any products in the public AWS Marketplace.

## Enabling or disabling user requests
<a name="private-marketplace-user-requests"></a>

Users in your organization can view the full public AWS Marketplace, but they can only subscribe to the products that you have allowed. By default, they can request that a product that is not in the private marketplace be added to it. These requests show up in the private marketplace administrator page ([Private Marketplace](https://aws.amazon.com/marketplace/privatemarketplace/admin/)), where you can decide whether to accept or deny the request (and whether to block further requests for the same product). You cannot see or respond to the requests by using the Catalog API.

You can enable or disable the ability for users to create requests for your private marketplace experience. Use `StartChangeSet` with the `UpdateProcurementPolicy` change type. The ability to make requests is disabled in the following code example.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateProcurementPolicy",
      "DetailsDocument":
      {
        "Configuration":
        {
          "PolicyResourceRequests": "Deny"
        }
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example@5"
      }
    }
  ]
}
```

To enable the change request capability for users, use `Allow` instead of `Deny` in `PolicyResourceRequests`.

To learn how to get the current status of this setting, see the next section, [Getting a list of products in a private marketplace experience](#private-marketplace-policy-details).

## Getting a list of products in a private marketplace experience
<a name="private-marketplace-policy-details"></a>

The products allowed (and denied) in a private marketplace are part of the procurement policy in the `Experience` entity. To get the details about the procurement policies in a private marketplace, you first get the procurement policy identifier from the `Experience` entity, and then call `DescribeEntity` with that identifier.

To get the procurement policy identifier, use `DescribeEntity` on the `Experience` entity that you are interested in, as shown in the following command.

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId={{exp-example01}}
```

Following is an example response.

```
{
  "Details": "{\"Name\":\"New Private Marketplace\", \"Status\":\"Enabled\", \"ProcurementPolicies\":[\"procpolicy-123example456\"], \"BrandingSettings\":[\"brandsettings-456example123\"]}",
  "DetailsDocument":
  {
    "Name": "New Private Marketplace",
    "Status": "Enabled",
    "ProcurementPolicies":
    [
      "procpolicy-123example456"
    ],
    "BrandingSettings":
    [
      "brandsettings-456example123"
    ]
  },
  "EntityArn": "arn:<...>:AWSMarketplace/Experience/exp-example-01",
  "EntityIdentifier": "exp-example01@6",
  "EntityType": "Experience@1.0",
  "LastModifiedDate": "2021-01-13T20:31:36Z"
}
```

**Note**  
The `DetailsDocument` attribute contains the entity details as a JSON object. The legacy `Details` attribute contains the same JSON object as a string. 

You can use the returned `EntityId` for the procurement policy to get the details, as shown in the following command.

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId={{procpolicy-123example456}}
```

This returns the full details of the policy, including both allowed and denied products. Following is an example response.

```
{
  "Details": "{\"Name\":\"ExampleProcurementPolicy\", \"Statements\":[{\"Effect\":\"Allow\",\"Resources\":[{\"Type\":\"Product\",\"Ids\":[\"example1-1234-abcd-5678-90abcdef1234\"]},{\"Type\":\"Product\",\"Ids\":[\"example2-2345-bcde-6789-01bcdea2345\"]}]},{\"Effect\":\"Deny\",\"Resources\":[{\"Type\":\"Product\",\"Ids\":[\"example3-3456-cdef-7890-12defabc5678\"]}]}],\"Configuration\":{\"PolicyResourceRequests\":\"Allow\"}}",
  "DetailsDocument":
  {
    "Name": "ExampleProcurementPolicy",
    "Statements":
    [
      {
        "Effect": "Allow",
        "Resources":
        [
          {
            "Type": "Product",
            "Ids":
            [
              "example1-1234-abcd-5678-90abcdef1234"
            ]
          },
          {
            "Type": "Product",
            "Ids":
            [
              "example2-2345-bcde-6789-01bcdea2345"
            ]
          }
        ]
      },
      {
        "Effect": "Deny",
        "Resources":
        [
          {
            "Type": "Product",
            "Ids":
            [
              "example3-3456-cdef-7890-12defabc5678"
            ]
          }
        ]
      }
    ],
    "Configuration":
    {
      "PolicyResourceRequests": "Allow"
    }
  },
  "EntityArn": "arn:<...>AWSMarketplace/ProcurementPolicy/procpolicy-123example456",
  "EntityIdentifier": "procpolicy-123example456@4",
  "EntityType": "ProcurementPolicy@1.0",
  "LastModifiedDate": "2020-10-01T12:00:00Z"
}
```

In this example, the procurement policy has two allowed products and one denied product. The policy allows user resource requests.

## Adding or removing products from a private marketplace
<a name="private-marketplace-add-products"></a>

By default, a private marketplace does not have any approved products in it. Use change requests to add or remove a product. To add a product, use the `AllowProductProcurement` change type. To remove a product, use the `DenyProductProcurement` change type. 

The following code example shows the `AllowProductProcurement` change type with the `StartChangeSet` action to add a product to a private marketplace.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AllowProductProcurement",
      "DetailsDocument":
      {
        "Products":
        [
          {
            "Ids":
            [
              "example-1234-abcd-5678-90abcded1234"
            ],
            "Notes": "Useful product"
          }
        ]
      },
      "Entity":
      {
        "Identifier": "exp-1234example@6",
        "Type": "Experience@1.0"
      }
    }
  ]
}
```

You add the product to the `Experience` entity for a private marketplace by using `AllowProductProcurement`. The syntax to remove a product from a private marketplace is identical, with the exception that you use the `DenyProductProcurement` `ChangeType` instead of `AllowProductProcurement`. The products are added to the allow (or deny) list of the `ProcurementPolicy` entity that is contained by your `Experience` entity.

**Note**  
The list of products in the `DetailsDocument` of your change is an array of `Ids`, so you can add (or remove) multiple products with one call by including a list of product identifiers. The limit is 50 products in a single request.  
The `Notes` field for the list of `Ids` is not required. However, you can use it to record why a decision to allow or deny a set of products was made.

## Finding products
<a name="finding-product-ids"></a>

By getting the details of your procurement policy, you can find the product IDs for the products that are already in a private marketplace. However, the AWS Marketplace Catalog API does not provide a way to find the product IDs for other products. There are two ways to get product IDs to use with the Catalog API service:
+ **Public marketplace** – After you find a product in the public marketplace, choose **Continue to Subscribe** to see a details page about the product (it will not subscribe you to the product). The URL will include the product ID as a parameter. For example, in the URL `https://aws.amazon.com/marketplace/fulfillment?productId=ab1234cd-1234-abcd-5678-90abcdef1234&ref_=dtl_psb_continue`, {{ab1234cd-1234-abcd-5678-90abcdef1234}} is the product ID.
+ **AWS Marketplace Discovery API** – Programmatically, you can access the full list of products in the AWS Marketplace by using the Discovery API. The Discovery API is a private API. You must request access to be able to use it. For more information, see [Access control for the AWS Marketplace Discovery API](discovery-api-access-control.md). 

## Working with private marketplaces for AWS Organizations
<a name="private-marketplace-organizations"></a>

Whether you are working with a private marketplace for your account or your organization, you use the same API. However, there are differences when working within your organization:
+ Before you can use private marketplace feature in an organization, you must [enable trusted access](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html) to provide private marketplace service (`private-marketplace.marketplace.amazonaws.com`) access to your AWS Organizations data. You must also [create the private marketplace service-linked role](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html) in the management account. This role includes all the permissions that private marketplace requires to describe AWS Organizations and update private marketplace resources on your behalf. These actions can only be performed by the management account. It is recommended to perform this enablement using private marketplace administrator page. If you are a new customer, see [Private marketplaces](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-using-service-linked-roles.html) in the *AWS Marketplace Buyer Guide*. If you are an existing customer, see [Creating and managing a private marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-catalog-administration.html) in the *AWS Marketplace Buyer Guide*. 
+ Private marketplace resources in an organization are created in the management account and shared with the member account that is a delegated administrator for private marketplace.
+ When listing objects in a private marketplace from a member account that is a delegated administrator for private marketplace, you must specifically request them with the `SharedWithMe` filter. This applies to both `ListEntities` and `ListChangeSets` actions.

To list `Experience` objects in your own account, call `ListEntities` as shown in the following code example.

```
POST /ListEntities HTTP/1.1
Content-Type: application/json

{
    "Catalog":"AWSMarketplace", 
    "EntityType":"Experience"
}
```

However, to list the entities that have been shared with you, you must add a `FilterList` with a `Scope` of `SharedWithMe`, as shown in the following code example. As a result, AWS Marketplace searches outside of your own account to find entities that are shared with you.

```
POST /ListEntities HTTP/1.1
Content-Type: application/json

{"Catalog":"AWSMarketplace", 
"EntityType":"Experience",
 "FilterList": 
  [{
     "Name": "Scope",
     "ValueList":
      ["SharedWithMe"]
      }]}
```

In this case, only entities outside of your account (the ones for your organization) are returned.

Similarly, to call `ListChangeSets`, you must set the scope, as shown in the following code example.

```
POST /ListChangeSets HTTP/1.1
Content-Type: application/json

{"Catalog":"AWSMarketplace", 
 "FilterList": 
  [{
     "Name": "Scope",
     "ValueList":
      ["SharedWithMe"]
      }]}
```

This returns change sets that apply to a shared private marketplace for your organization.

## Associating principals to experiences
<a name="private-marketplace-associate-accounts"></a>

A private marketplace experience must have one or more principals associated with it in order to have any effects in your organization. For a single AWS account, you must associate the account with the experience to use the private marketplace. In an organization, you can have multiple experiences apply to different principals. 

**Note**  
The experience that is associated with the organization is the default for all other accounts in the organization. Associating a member account or OU with a diﬀerent experience directly sets a diﬀerent experience for the member account or child accounts of the OU.
If you are a current private marketplace customer without the AWS Organizations integration for private marketplace, the experience that is associated with the management account is the default for all other accounts in the organization.

To associate a principal to an experience, use the `AssociateAudience` change type with the `StartChangeSet` action, as shown in the following code example.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-example01@1"
      },
      "ChangeType": "AssociateAudience",
      "DetailsDocument":
      {
        "Name": "AudienceName",
        "Description": "Audience example.",
        "Principals":
        [
          "012345678901",
          "ou-abcd-01234567",
          "o-0123456789"
        ]
      }
    }
  ],
  "ChangeSetName": "Set Audience for experience 01"
}
```

The *audience* is the list of *principals* that are associated with the `Experience`. A principal is an AWS account, organizational unit, or organization defined by its ID. `Principals` is a list, so you can include multiple principals to be associated with the experience. After the first call, subsequent calls to the `AssociateAudience` change type will add principals to the association for the experience.

You can also remove accounts from an experience. Use the `DisassociateAudience` change type to do this, as shown in the following code example.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-example01@02"
      },
      "ChangeType": "DisassociateAudience",
      "DetailsDocument":
      {
        "Principals":
        [
          "012345678901",
          "ou-abcd-01234567",
          "o-0123456789"
        ]
      }
    }
  ],
  "ChangeSetName": "Disassociate audience example"
}
```

**Note**  
A principal can only be directly associated with one experience. To move a principal from being directly associated with one experience to another experience, you must disassociate it from the initial experience, then associate it with the second.

## Archiving and reactivating a private marketplace experience
<a name="archiving-and-reactivating-a-private-marketplace-experience-capi"></a>

You can remove a private marketplace experience by archiving it. Archived experiences can't be updated or used to govern accounts in your organization. If you have audiences associated with an archived experience, you can associate them with a different experience. If you decide to use the experience at a later time, you can always reactivate it. Administrators from the management account or a member account that is a delegated administrator for private marketplace have permissions to archive and reactivate experiences. If you're a current private marketplace customer without the AWS Organizations integration for private marketplace, administrators from the account that created the experience have permissions to archive and reactivate experiences.

**Note**  
Before archiving an experience, you must disable it. For information about disabling an experience, see [Configuring your private marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-catalog-administration.html#configure-your-private-marketplace) in the *AWS Marketplace Buyer Guide.*

To archive an experience, use the `RestrictExperience` change type with the `StartChangeSet` action, as shown in the following code example.

```
POST /StartChangeSet HTTP/1.1 
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RestrictExperience",
      "DetailsDocument":
      {},
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example"
      }
    }
  ]
}
```

To reactivate an experience, use the `ReviveExperience` change type with the `StartChangeSet` action, as shown in the following code example.

```
POST /StartChangeSet HTTP/1.1 
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "ReviveExperience",
      "DetailsDocument":
      {},
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example"
      }
    }
  ]
}
```

## Errors in the private marketplace API
<a name="private-marketplace-error-codes"></a>

The following errors are specific to the private marketplace actions in the AWS Marketplace Catalog API.


<table>
<thead>
  <tr><th>Change type</th><th>Error code</th><th>Error message</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="4"><b>Errors returned directly by the StartChangeSet action</b></td></tr>
  <tr><td>All</td><td>422</td><td>Document not valid JSON format</td><td>Invalid JSON input used, check your syntax.</td></tr>
  <tr><td>AllowProductProcurement, DenyProductProcurement</td><td>422</td><td>Values in Ids array must be unique</td><td>You can't include the same product multiple times in a single change request.</td></tr>
  <tr><td>AllowProductProcurement, DenyProductProcurement</td><td>422</td><td>Cumulative number of values in Ids array must be less than or equal to 50</td><td>You can allow or deny up to 50 products in a single change request.</td></tr>
  <tr><td colspan="4"><b>Errors found by calling the DescribeChangeSet action</b></td></tr>
  <tr><td>CreateBrandingSettings, UpdateBrandingSettings</td><td>INVALID_URL</td><td>Image could not be fetched from the input URL</td><td>You must specify a valid, reachable URL for the logo field in <code>BrandingSettings</code>.</td></tr>
  <tr><td>CreateBrandingSettings, UpdateBrandingSettings</td><td>INVALID_IMAGE</td><td>Image verification for type, content, or file size failed. Only .png and .svg file types with sizes less than or equal to 500KB are supported.</td><td>Your image file must match the logo requirements for branding settings.</td></tr>
  <tr><td>AllowProductProcurement, DenyProductProcurement</td><td>ENTITY_NOT_FOUND</td><td>Procurement policy missing from Experience</td><td>You must create a <code>ProcurementPolicy</code> before allowing or denying products.</td></tr>
  <tr><td>CreateProcurementPolicy</td><td>ENTITY_ALREADY_EXISTS</td><td>Procurement policy exists for Experience</td><td>You can only have a single procurement policy for a private marketplace.</td></tr>
  <tr><td>UpdateProcurementPolicy</td><td>ENTITY_NOT_FOUND</td><td>Procurement policy missing from Experience</td><td>You must create a <code>ProcurementPolicy</code> before updating the procurement policy.</td></tr>
  <tr><td>CreateBrandingSettings</td><td>ENTITY_ALREADY_EXISTS</td><td>Branding settings exists for Experience</td><td>You can only have a single branding settings for a private marketplace.</td></tr>
  <tr><td>UpdateBrandingSettings</td><td>ENTITY_NOT_FOUND</td><td>Branding settings missing from Experience</td><td>You must create a <code>BrandingSettings</code> entity before updating the branding settings.</td></tr>
  <tr><td>AssociateAudience</td><td>CALLER_NOT_AUTHORIZED</td><td>Caller not authorized to execute the action</td><td>You must have permissions to call the action. The accounts being added must be in the same organization.</td></tr>
  <tr><td>CreateExperience</td><td>CALLER_NOT_AUTHORIZED</td><td>Caller not authorized to create experience. </td><td>You must have permissions to create an experience.</td></tr>
  <tr><td>AssociateAudience</td><td>ENTITY_ALREADY_EXISTS</td><td>An experience is already associated with the account {accountId}. Disassociate previous experience before updating</td><td>You can only associate a single experience with an account. Disassociate the current experience before associating a new one. </td></tr>
  <tr><td>AssociateAudience, DisassociateAudience</td><td>ENTITY_IN_USE</td><td>There is already a conflicting change in progress for the selected account. Try again later</td><td>You can't change the association with an account while another change request to change the association is already in progress.</td></tr>
</tbody>
</table>


## Entity types defined by private marketplace
<a name="entity-types-defined-by-private-marketplace"></a>

The following table lists the private marketplace entity types, purpose, and actions on which each can be specified. Each entity type can be used to specify a resource Amazon Resource Name (ARN) that can be used in the AWS Identity and Access Management (IAM) policy. For more details on ARN formats, see [Catalog API entities](catalog-apis.md#catalog-api-entities).


| Entity | Purpose | Actions | 
| --- | --- | --- | 
| `Experience` | Stores the top-level settings for a private marketplace | `StartChangeSet`<br />`DescribeEntity` | 
| `BrandingSettings` | Stores the branding settings for a private marketplace | `DescribeEntity` | 
| `ProcurementPolicy` | Stores the procurement settings and lists of products in a private marketplace | `DescribeEntity` | 
| `Audience` | Stores the details of principals associated with a private marketplace | `DescribeEntity` | 