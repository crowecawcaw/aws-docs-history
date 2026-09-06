

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with AMI-based products
<a name="work-with-single-ami-products"></a>

You can use the AWS Marketplace Catalog API to automate tasks for working with Amazon Machine Image (AMI)-based products. 

For information about creating a AMI-based product using the Catalog API, see [Create a product](work-with-seller-products.md#create-product).

The following topics describe how to use the Catalog API to perform actions on your AMI-based products:

**Topics**
+ [Add a new version](#ami-add-version)
+ [Update version information](#ami-update-version)
+ [Restrict a version](#ami-restrict-version)
+ [Update future AWS Region support](#update-future-region-support)
+ [Add a supported AWS Region](#add-regions)
+ [Restrict an AWS Region](#restrict-regions)
+ [Add a new instance type](#add-instance-types)
+ [Restrict an instance type](#restrict-instance-types)

## Add a new version
<a name="ami-add-version"></a>

You can use the Catalog API to add a new version to an existing AMI-based product in AWS Marketplace. For more information about adding new AMI versions to your product using the AWS Marketplace Management Portal, see [ Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-version) in the *AWS Marketplace Seller Guide*.

 When you create a request that includes adding a new AMI to AWS Marketplace, the AMI must be copied into the AWS Marketplace system and then scanned for security issues. You must give AWS Marketplace access to the AMI by creating an AWS Identity and Access Management (IAM) role with permissions to perform actions on your AMI. For more information on the required permissions, see [Giving AWS Marktplace access to your AMI](https://docs.aws.amazon.com/marketplace/latest/userguide/single-ami-marketplace-ami-access.html) in the *AWS Marketplace Seller Guide*.

To add a new version, call the `StartChangeSet` API operation with the `AddDeliveryOptions` change type for AMI-based products, as shown in the following example. To test your API call without actually creating a new version, set the `Intent` parameter to `VALIDATE`. For more information, see [Intent](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_RequestBody).

**Note**  
For AMI products, a version is made up of one or more delivery options. All delivery options in the same version must have the same `AmiSource` object with the same details. All delivery options must be added to a version when the version is created. It is not possible to add delivery options to an existing version.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddDeliveryOptions",
      "Entity":
      {
        "Type": "AmiProduct@1.0",
        "Identifier": "prod-example12345"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "VersionTitle": "My new title",
          "ReleaseNotes": "My new Release notes"
        },
        "DeliveryOptions":
        [
          {
            "Details":
            {
              "AmiDeliveryOptionDetails":
              {
                "AmiSource":
                {
                  "AmiId": "ami-1234567890abcdef",
                  "AccessRoleArn": "arn:aws:iam::12345678901:role/AwsMarketplaceAmiIngestion",
                  "UserName": "ec2-user",
                  "OperatingSystemName": "AMAZONLINUX",
                  "OperatingSystemVersion": "Amazon Linux 2 AMI 2.0.20210126.0 x86_64 HVM gp2",
                  "AfiIds": ["afi-1234567890abcdefg", "afi-abcdefg1234567890"] //Optional (Required only for FPGA products)
                },
                "UsageInstructions": "Easy to use AMI",
                "RecommendedInstanceType": "m4.xlarge",
                "SecurityGroups":
                [
                  {
                    "IpProtocol": "tcp",
                    "FromPort": 443,
                    "ToPort": 443,
                    "IpRanges":
                    [
                      "0.0.0.0/0"
                    ]
                  }
                ]
              }
            }
          },
          {
            "DeliveryOptionTitle": "My new AMI with CFTdelivery option",
            "Details":
            {
              "DeploymentTemplateDeliveryOptionDetails":
              {
                "ShortDescription": "My new short description",
                "LongDescription": "My new long description",
                "UsageInstructions": "My new usage instructions",
                "RecommendedInstanceType": "m4.xlarge",
                "ArchitectureDiagram": "https://my-bucket.s3.amazonaws.com/my-folder/diagram.png",
                "Template": "https://my-bucket.s3.amazonaws.com/my-folder/cft.template",
                "TemplateSources":
                [
                  {
                    "ParameterName": "MyAmiParam",
                    "AmiSource":
                    {
                      "AmiId": "ami-1234567890abcdef",
                      "AccessRoleArn": "arn:aws:iam::12345678901:role/AwsMarketplaceAmiIngestion",
                      "UserName": "ec2-user",
                      "OperatingSystemName": "AMAZONLINUX",
                      "OperatingSystemVersion": "Amazon Linux 2 AMI 2.0.20210126.0 x86_64 HVM gp2"
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  ],
  "Intent": "APPLY"
}
```

The following list provides information about the input fields you use with the `AddDeliveryOptions` change type. All fields are required unless otherwise noted. For more information about these fields, see [Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-version) in the AWS Marketplace Seller Guide.
+ **DeliveryOptions** (array of objects) – A list of delivery option objects, including the details of each. You must include at least one.
  + For *AMI (standalone)* delivery option, specify an object with the following details. You can only have one delivery option with this type.
    + **Details** (object) – Holds the details of this delivery option. Note that this nested details object does not need to be double-escaped.
      + **AmiDeliveryOptionDetails** (object) – Use to provide the details of each AMI delivery option.
        + **AmiSource** (object) – Details about the AMI to be used for the added version.
          + **AmiId** (string) – ID for the source AMI, located in the AWS Region where the API is being called. This must always be US East (N. Virginia) because that is the only region where the Catalog API is available. Must belong to the caller account.
          + **AccessRoleArn **(string) – IAM role Amazon Resource Name (ARN) used by AWS Marketplaceto access the provided AMI. For details about creating and using this ARN, see [Giving AWS Marketplace access to your AMI](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-marketplace-ami-access) in the *AWS Marketplace Seller Guide*.
          + **UserName** (string) – Login user name to access the operating system (OS) in the AMI. Typically ec2-user for Linux AMIs or Administrator for Windows.
          + **ScanningPort** (integer) – SSH or RDP port used to access the OS. Used for scanning the provided AMI for security vulnerabilities. Defaults to 22.
          + **OperatingSystemName** (string) – Name of the operating system displayed to buyers.
          + **OperatingSystemVersion** (string) – Operating system version string displayed to buyers.
          + **AfiIds** (array of strings) (optional) – Amazon FPGA Image (AFI) IDs to enable FPGA support for this version. When provided, this enables your product to run on FPGA-enabled F2 instance types. You can provide up to 15 AFI IDs per version. All AFI IDs you provide must originate from the US East (N. Virginia) region, reside within your AWS Marketplace seller account, and the provided IAM access role should have permissions to share this AFI with AWS Marketplace. For more details about the required permissions, see [Giving AWS Marketplace access to your FPGA images](https://docs.aws.amazon.com/marketplace/latest/userguide/single-ami-marketplace-ami-access.html#single-ami-marketplace-afi-access) in the *AWS Marketplace Seller Guide*.
        + **UsageInstructions** (string) – Instructions for using the AMI, or a link to more information about the AMI.
        + **AccessEndpointUrl** (object) (optional) – Used to create a path to access the AMI after it is used.
          + **Port** (string) – The port number used to access the service running on the AMI.
          + **Protocol** (string) – The protocol (http or https) used to access the service running on the AMI.
          + **RelativePath** (string) – The path from the web root to access the service running on the AMI (for example /index.html).
        + **RecommendedInstanceType** (string) – The instance type that is recommended to run the service with the AMI and is the default for 1-click installs of your service. For a list of instance types, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.
        + **SecurityGroups** (array of objects) – A list of objects representing ingress rules for the automatically created groups for the version.
          + **IpProtocol** (string) – The protocol to use (tcp or udp).
          + **FromPort** (integer) – The source port.
          + **ToPort** (integer) – The destination port.
          + **IpRanges** (array of strings) – IP ranges to allow, in CIDR format (in the form xxx.xxx.xxx.xxx/nn, for example, {{192.0.2.0/24}}).
  + For *AMI with CloudFormation* delivery option, specify an object with the following details. You can have up to three delivery options of this type.
    + **DeliveryOptionTitle** (string) – Title for delivery option.
    + **Details** (object) – Holds the details of an AMI delivery option. Note that this nested details object does not need to be double-escaped.
      + **DeploymentTemplateDeliveryOptionDetails** (object) – Use to provide the details of each CFT delivery option.
        + **ShortDescription** (string) – Brief description of your CloudFormation template delivery option.
        + **LongDescription** (string) – Detailed description of your CloudFormation template delivery option.
        + **UsageInstructions** (string) – Instructions for using the AMI, or a link to more information about the AMI.
        + **RecommendedInstanceType** (string) – The instance type that is recommended to run the service with the AMI and is the default for 1-click installs of your service. For a list of instance types, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.
        + **ArchitectureDiagram** (string) – URL to the location of your architectural diagram in Amazon S3. 
        + **Template** (string) – URL to the location of your CloudFormation Template in Amazon S3. 
        + **TemplateSources** (array of objects)
          + **ParameterName** (string) – Name of the parameter in the CloudFormation Template that the AMI in this version should be passed in to. For more information, see [Requirements for AMI details](https://docs.aws.amazon.com/marketplace/latest/userguide/cloudformation.html#ami-requirements-sse).
          + **AmiSource** (object)
            + **AmiId** (string) – ID for the source AMI, located in the AWS Region where the API is being called (currently must always be US East (N. Virginia) because that is the only region where the Catalog API is available). Must belong to the caller account.
            + **AccessRoleArn** (string) – IAM role Amazon Resource Name (ARN) used by AWS Region to access the provided AMI. For details about creating and using this ARN, see [Giving AWS Marketplace access to your AMI](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-marketplace-ami-access) in the *AWS Marketplace Seller Guide*.
            + **UserName** (string) – Login user name to access the operating system (OS) in the AMI. Typically `ec2-user` for Linux AMIs or `Administrator` for Windows.
            + **OperatingSystemName** (string) – Name of the operating system displayed to buyers.
            + **OperatingSystemVersion** (string) – Operating system version string displayed to buyers.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
   "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors).

When the request is complete, the version is added, and any existing subscribers will receive an email message telling them about the new version. For more information about the process of adding a new version, see [ Adding a new version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-version) in the *AWS Marketplace Seller Guide*.

**Asynchronous Errors**

The following errors are specific to `AddDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_AMI\_NAME | The prefix (x) in the AMI name is invalid. Provide a new name using your company or brand name as a prefix. | 
| INVALID\_PRODUCT | Use an existing limited or public product. | 
| DUPLICATE\_VERSION\_TITLE | The version title must be different from any other version titles of this product. | 
| INVALID\_VERSION\_TITLE | Remove spaces before the trademark symbol. | 
| INVALID\_VERSION\_TITLE | Remove unsupported characters: [x, y, z] | 
| INVALID\_VERSION\_TITLE | Remove spaces from the beginning of the version title. | 
| INVALID\_VERSION\_TITLE | Provide version title with fewer than [x] characters. | 
| INVALID\_RELEASE\_NOTES | Remove spaces before the trademark symbol. | 
| INVALID\_RELEASE\_NOTES | Remove unsupported characters: [x, y, z] | 
| INVALID\_RELEASE\_NOTES | Remove spaces from the beginning of release notes. | 
| INVALID\_RELEASE\_NOTES | Provide release notes with fewer than (x) characters. | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove spaces before the trademark symbol. | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove unsupported characters: [x, y, z] | 
| INVALID\_USAGE\_INSTRUCTIONS | Remove spaces from the beginning of release notes. | 
| INVALID\_USAGE\_INSTRUCTIONS | Provide usage instructions with fewer than (x) characters. | 
| RECOMMENDED\_INSTANCE\_TYPE\_NOT\_AVAILABLE | Provide an existing, available instance type. | 
| INVALID\_RECOMMENDED\_INSTANCE\_TYPE | Provide a valid instance type. | 
| INVALID\_SECURITY\_GROUP | Security group ports must be between 1 and [max]. | 
| INVALID\_SECURITY\_GROUP | Provide a value for CIDR IP ranges. | 
| INVALID\_SECURITY\_GROUP | Provide security group start port that is not greater than end port. | 
| INVALID\_SECURITY\_GROUP\_PROTOCOL | Security group protocol must either be 'tcp' or 'udp'. | 
| INVALID\_CIDR\_IP | Provide standard CIDR IP range in form '0.0.0.0/0'. | 
| INVALID\_ACCESS\_ENDPOINT\_PORT | Provide endpoint port less than [x]. | 
| INVALID\_ACCESS\_ENDPOINT\_PORT | Provide endpoint port between 1 and [max]. | 
| INVALID\_ACCESS\_ENDPOINT\_PORT | Provide endpoint port. | 
| INVALID\_ACCESS\_ENDPOINT\_RELATIVE\_PATH | Remove spaces in the relative path. | 
| INVALID\_ACCESS\_ENDPOINT\_RELATIVE\_PATH | Remove preceding '/' from relative path. | 
| INCOMPATIBLE\_OPERATING\_SYSTEM | Provide operating system name and version that is compatible with instance types: [x] | 
| INCOMPATIBLE\_OPERATING\_SYSTEM\_NAME | Provide name with fewer than (x) characters. | 
| INCOMPATIBLE\_OPERATING\_SYSTEM\_NAME | Provide operating system name that is supported. | 
| INCOMPATIBLE\_OPERATING\_SYSTEM\_VERSION | Provide version with fewer than (x) characters. | 
| INVALID\_SCANNING\_PORT | Provide scanning port between 1 and [max]. | 
| INVALID\_AMI\_ID | Provide valid AMI ID. | 
| EXISTING\_AMI\_PRODUCT\_CODE | Remove product code attached to image X. | 
| INVALID\_AMI\_ARCHITECTURE | Provide new AMI with architecture [x]. | 
| INVALID\_AMI\_VIRTUALIZATION\_TYPE | Provide new AMI with virtualization type [x]. | 
| INVALID\_AMI\_VIRTUALIZATION\_TYPE | Provide expected [z] volume on image [x]. | 
| INCOMPATIBLE\_AMI | Provide new AMI as architecture [x] on [y] is not supported by following instance types: [z] | 
| INCOMPATIBLE\_AMI | Provide new AMI as virtualization type [x] on [y] is not supported by following instance types: [z] | 
| INCOMPATIBLE\_AMI | Enable ENA support for image x because following instance types require ENA support: [y] | 
| ASSET\_NOT\_FOUND | Check if [ami-id] exists in us-east-1 Region of [account-id] AWS account and the AccessARN provided [ARN] has permissions to share this AMI with AWS Marketplace. | 
| ASSET\_ACCESS\_EXCEPTION | Unable to copy AMI [x] into AWS Marketplace account. | 
| SCAN\_ERROR | Fix security vulnerability [y] on Image [x]. | 
| ASSET\_NOT\_FOUND | Check if [afi-id] exists in us-east-1 Region of [account-id] AWS account and the AccessARN provided [ARN] has permissions to share this AFI with AWS Marketplace. | 
| ASSET\_ACCESS\_EXCEPTION | Unable to access AFI. Check if AccessARN provided [ARN] has permissions to share this AFI with AWS Marketplace and access role Account is AFI owner. | 
| MISSING\_FPGA\_INSTANCE\_TYPE | No FPGA based instance type found. Use AddInstanceTypes change type to add FPGA based instance type. | 

You can also create a AMI-based product using the AWS Marketplace Management Portal. For more information, see [ AMI products](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html) in the *AWS Marketplace Seller Guide*.

For a walk-through showing how to automate updating your AMI-based product, you can also refer to the video, [ Automating updates to your product listings in AWS Marketplace with Catalog API](https://www.youtube.com/watch?v=7KpUJ6Wcqrg) (5:08).

## Update version information
<a name="ami-update-version"></a>

You can use the Catalog API to update the details of an existing version of your AMI-based product in AWS Marketplace. 

**Note**  
For more information about updating version information using the AWS Marketplace Management Portal, see [ Updating version information](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-updating-version) in the *AWS Marketplace Seller Guide*. 

You cannot update the AMI for the version. If you need to update the AMI, create a new version instead.

To add a new version, call the `StartChangeSet` API operation with the `UpdateDeliveryOptions` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateDeliveryOptions",
      "Entity":
      {
        "Identifier": "example1-abcd-1234-5ef6-7890abcdef12@1",
        "Type": "AmiProduct@1.0"
      },
      "DetailsDocument":
      {
        "Version":
        {
          "ReleaseNotes": "*My new Release notes*"
        },
        "DeliveryOptions":
        [
          {
            "Id": "example1-2222-cccc-2222-cccccccccccc",
            "Details":
            {
              "AmiDeliveryOptionDetails":
              {
                "UsageInstructions": "Easy to use AMI"
              }
            }
          },
          {
            "Id": "example1-2222-dddd-2222-dddddddddddd",
            "Details":
            {
              "DeploymentTemplateDeliveryOptionDetails":
              {work with ami
                "DeliveryOptionTitle": "My updated delivery option title",
                "UsageInstructions": "Updated usage instructions here."
              }
            }
          }
        ]
      }
    }
  ]
}
```

The following is information about the input fields you provide for adding the `UpdateDeliveryOptions` change type. For more information about these fields, see [ Updating version information](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-updating-version) in the AWS Marketplace Seller Guide.
+ **Entity** (object) (required) – Your AMI-based product. 
  + **Identifier** (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + **Type** (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+ **DetailsDocument** (object) (required) – Details of the request. It includes any information about the version of your AMI-based product that you would like to update. The included fields are all optional, but you must include at least one field to update.
  + **Version** (object) – Details about the software version.
    + **ReleaseNotes** (string) – Notes for buyers to tell them about changes from one version to the next. 
  + **DeliveryOptions** (array of objects) – List of delivery option objects. Include only the delivery options you want to update.
    + For *AMI (standalone)* delivery option, specify an object with the following details. Include only the fields you want to update. All fields are optional unless otherwise noted.
      + **Id** (string) (required) – Unique identifier for the delivery option (you can get the unique identifier for the delivery option by calling the `DescribeEntity` action on the product you are updating).
      + **Details** (object) – Holds the details of an AMI delivery option. Note that this nested details object does *not* need to be double-escaped.
        + **AmiDeliveryOptionDetails** (object) – The details of one AMI delivery option.
          + **UsageInstructions** (string) – Instructions for using the AMI, or a link to more information about the AMI.
          + **AccessEndpointUrl** (object) – Used to create a path to access the AMI after it is used.
            + **Port** (string) – The port number used to access the service running on the AMI.
            + **Protocol** (string) – The protocol (`http` or `https`) used to access the service running on the AMI.
            + **RelativePath** (string) – The path from the web root to access the service running on the AMI (for example {{/index.html}}).
          + **RecommendedInstanceType** (string) – The instance type that is recommended to run the service with the AMI and is the default for 1-click installs of your service.
          + **SecurityGroups** (array of objects) – A list of objects representing ingress rules for the automatically created groups for the version:
            + **FromPort** (integer) – The source port.
            + **IpProtocol** (string) – The protocol to use (`tcp` or `idp`).
            + **IpRanges** (array of strings) – IP ranges to allow, in CIDR format (in the form *xxx.xxx.xxx.xxx/nn*, for example, {{192.0.2.0/24}}).
            + **ToPort** (integer) – The destination port.
    + For *AMI with CloudFormation* delivery option, specify an object with the following details. Include only the fields you want to update. All fields are optional unless otherwise noted.
      + **Id** (string) (required) – Unique identifier for the delivery option (you can get the unique identifier for the delivery option by calling the `DescribeEntity` action on the product you are updating).
      + **Details** (object) – Holds the details of an AMI delivery option. Note that this nested details object does *not* need to be double-escaped.
        + **DeploymentTemplateDeliveryOptionDetails** (object) – Use to provide the details of each CFT delivery option.
          + **DeliveryOptionTitle** (string) – Title for delivery option.
          + **ShortDescription** (string) – Brief description of your CloudFormation template delivery option.
          + **LongDescription** (string) – Detailed description of your CloudFormation template delivery option.
          + **UsageInstructions** (string) – Instructions for using the AMI, or a link to more information about the AMI.
          + **RecommendedInstanceType** (string) – The instance type that is recommended to run the service with the AMI and is the default for 1-click installs of your service. For a list of instance types, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.
          + **ArchitectureDiagram** (string) – URL to the location of your architectural diagram in Amazon S3. 
          + **Template** (string) – URL to the location of your CloudFormation Template in Amazon S3. 
          + **TemplateSources** (array of objects)
            + **ParameterName** (string) – Name of the parameter in the CloudFormation Template that the AMI in this version should be passed in to. For more information, see [Requirements for AMI details](https://docs.aws.amazon.com/marketplace/latest/userguide/cloudformation.html#ami-requirements-sse).
            + **AmiSource** (object)
              + **AmiId** (string) – ID for the source AMI, located in the AWS Region where the API is being called (currently must always be US East (N. Virginia) because that is the only region where the Catalog API is available). Must belong to the caller account.
              + **AccessRoleArn** (string) – IAM role Amazon Resource Name (ARN) used by AWS Region to access the provided AMI. For details about creating and using this ARN, see [Giving AWS Marketplace access to your AMI](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-marketplace-ami-access) in the *AWS Marketplace Seller Guide*.
              + **UserName** (string) – Login user name to access the operating system (OS) in the AMI. Typically `ec2-user` for Linux AMIs or `Administrator` for Windows.
              + **OperatingSystemName** (string) – Name of the operating system displayed to buyers.
              + **OperatingSystemVersion** (string) – Operating system version string displayed to buyers.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
   "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

For more information about change sets, see [Working with change sets](catalog-apis.md#working-with-change-sets). For more information about errors in seller product change sets, see [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors).

**Asynchronous Errors**

The following errors are specific to `UpdateDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).

You can retrieve `UpdatePricingTerms` actions by using the `DescribeChangeSet` operation after the change set begins processing. For more information about error details and troubleshooting, refer to [Change set status and errors](work-with-seller-products.md#seller-product-change-set-errors), earlier in this guide.


| Error code | Error message | 
| --- | --- | 
| INVALID\_PRODUCT | Use an existing limited or public product. | 
| MISSING\_DELIVERY\_OPTION\_IDS | Provide at least one delivery option ID. | 
| INVALID\_DELIVERY\_OPTION\_IDS | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| INVALID\_DELIVERY\_OPTIONS | Provide delivery option IDs that belong to the same version. | 

## Restrict a version
<a name="ami-restrict-version"></a>

You can use the Catalog API to restrict a version of your AMI-based product. This prevents new buyers from using that version, but keeps it available to existing buyers. Restricting all delivery options from a version restricts the version. Restricting one or more, but not all, delivery options from a version restricts just the delivery options in that version. You must always have at least one unrestricted version of a product available, so you cannot restrict the last publicly available version of a product.

**Note**  
For more information about restricting AMI versions in AWS Marketplace via the AWS Marketplace Management Portal, see [Restricting a version](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-restricting-version) in the *AWS Marketplace Seller Guide*.

To restrict a version, call the `StartChangeSet` API operation with the `RestrictDeliveryOptions` change type, as shown in the following example.

**Note**  
All subscribers can use the current version regardless of the restriction status. AWS Marketplace guidelines require that you continue to offer support to existing buyers for 90 days after restricting the version. Your AMI will be marked as deprecated after the version is restricted. For more information, see [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ami-deprecate.html) in the *Amazon Elastic Compute Cloud User Guide for Windows Instances*.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RestrictDeliveryOptions",
      "Entity":
      {
        "Identifier": "{{example1-abcd-1234-5ef6-7890abcdef12@1}}",
        "Type": "AmiProduct@1.0"
      },
      "DetailsDocument":
      {
        "DeliveryOptionIds":
        [
          "{{example1-2222-cccc-2222-cccccccccccc}}"
        ]
      }
    }
  ]
}
```

The following is information about the input fields you provide for adding the `RestrictDeliveryOptions` change type:
+ **Entity** (object) (required) – Your AMI-based product. 
  + **Identifier** (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + **Type** (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+ **DetailsDocument** (object) (required) – Details of the request. It includes IDs for the versions of your AMI-based product that you would like to restrict. 
  + **DeliveryOptionIds** (array of objects) – List of `DeliveryOption` IDs for the versions that you want to restrict. You can get the unique identifier for the `DeliveryOption` by calling the `DescribeEntity` action on the version you are restricting.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
   "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Asynchronous Errors**

The following errors are specific to `RestrictDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_PRODUCT | Use an existing public product. | 
| MISSING\_DELIVERY\_OPTION\_IDS | Provide at least one delivery option ID. | 
| INVALID\_DELIVERY\_OPTION\_IDS | Provide delivery option IDs that can be found in the product. IDs not found: [x] | 
| INVALID\_DELIVERY\_OPTION | Provide delivery option IDs that are in a public state. IDs not in public state: [x] | 
| ALL\_DELIVERY\_OPTIONS\_RESTRICTED | Provide fewer delivery options to restrict as at least one must remain in public state. | 

## Update future AWS Region support
<a name="update-future-region-support"></a>

You can use the Catalog API to change future AWS Region support preferences for your AMI-based product in AWS Marketplace. 

**Note**  
For more information about changing future Region support using the AWS Marketplace Management Portal, see [ Update support for future AWS Regions](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-updating-future-region-support) in the *AWS Marketplace Seller Guide*. 

**Note**  
The `UpdateFutureRegionSupport` change type is only available on `AmiProduct@1.0`.

To change future AWS Region support preferences, call the `StartChangeSet` API operation with the `UpdateFutureRegionSupport` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateFutureRegionSupport",
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "AmiProduct@1.0"
      },
      "DetailsDocument":
      {
        "FutureRegionSupport":
        {
          "SupportedRegions":
          [
            "All"
          ]
        }
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateFutureRegionSupport` change type:
+ `Entity` (object) (required) – Your AMI-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+ `DetailsDocument` (object) (required) – The details required to execute the ChangeSet.
  + `FutureRegionSupport` – Object
    + `SupportedRegions` – Single-element array of strings

      Element supported values: one of [`"All"`, `"US"`, `"None"`]

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
  "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Asynchronous Errors**

The following errors are specific to `UpdateFutureRegionSupport` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| TOO\_MANY\_REGIONS | Currently, only 1 value is supported for FutureRegionSupport: All, US, or None | 
| INVALID\_REGIONS | Requested Regions [a, b, c] are invalid or unavailable. Only supported values are [x, y, z]. | 
| INVALID\_INPUT | SupportedRegions can't be empty. | 

## Add a supported AWS Region
<a name="add-regions"></a>

You can use the Catalog API to add new supported AWS Regions for your AMI-based product in AWS Marketplace. 

**Note**  
For more information about adding new supported Regions using the AWS Marketplace Management Portal, see [ Add an AWS Region](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-regions) in the *AWS Marketplace Seller Guide*. 

**Note**  
The `AddRegions` change type is only available on `AmiProduct@1.0`.

To add new supported Regions, call the `StartChangeSet` API operation with the `AddRegions` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "AddRegions",
      "DetailsDocument": {
        "Regions": [
          "{{us-east-1}}",
          "{{ap-northeast-2}}"
        ]
      },
      "Entity": {
        "Identifier": "{{prod-123456@1}}",
        "Type": "AmiProduct@1.0"
      }
    }
  ]
}
```

Provide information for the fields to add the `AddRegions` change type. 
+ `Entity` (object) (required) – Your AMI-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+   
**Example**  
  + `Regions`: Array of strings

    Element supported values: Valid AWS Region code strings. 

    For example, [`"us-east- 1"`].

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.
+ If the change set execution status is `SUCCEEDED`: A new Entity `Identifier` (or `EntityId`) is generated. You can use the [`DescribeEntity`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html) API operation on the product entity to check the result. 
+ If the change set execution status is `CLIENT_ERROR`: The `DescribeChangeSet` response gives the details of the error, as well as corresponding actions to take to fix the error.

**Asynchronous Errors**

The following errors are specific to `AddRegions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INVALID\_REGIONS | Requested regions [a, b, c] are invalid or unavailable. Only supported values are [x, y, z]. | 
| INVALID\_INPUT | Regions can't be empty. | 

## Restrict an AWS Region
<a name="restrict-regions"></a>

You can use the Catalog API to restrict previously supported AWS Regions for your AMI-based product in AWS Marketplace. 

**Note**  
For more information about restricting previously supported Regions using the AWS Marketplace Management Portal, see [ Restrict an AWS Region](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-restricting-regions) in the *AWS Marketplace Seller Guide*. 

**Note**  
The `RestrictRegions` change type is only available on `AmiProduct@1.0`.

To restrict previously supported Regions, call the `StartChangeSet` API operation with the `RestrictRegions` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "RestrictRegions",
      "DetailsDocument": {
        "Regions": [
          "{{us-east-1}}",
          "{{ap-northeast-2}}"
        ]
      },
      "Entity": {
        "Identifier": "{{prod-123456@1}}",
        "Type": "AmiProduct@1.0"
      }
    }
  ]
}
```

Provide information for the fields to add the `AddRegions` change type. 
+ `Entity` (object) (required) – Your AMI-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+ **DetailsDocument** (object) (required) – The details required to execute the ChangeSet.
  + `Regions` – Array of strings

    Element supported values: Valid AWS Region code strings, such as `"us-east-1"`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.
+ If the change set execution status is `SUCCEEDED` – A new Entity `Identifier` (or `EntityId`) is generated. You can use `DescribeEntity` on the product entity to check the result. For more information, see [`DescribeEntity`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html).
+ If the change set execution status is `CLIENT_ERROR`: The `DescribeChangeSet` response gives the details of the error, as well as corresponding actions to take to fix the error.

**Asynchronous Errors**

The following errors are specific to `AddRegions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INVALID\_REGIONS | Requested regions [a, b, c] are invalid or unavailable. Only supported values are [x, y, z]. | 
| INVALID\_INPUT | Regions can't be empty. | 

## Add a new instance type
<a name="add-instance-types"></a>

You can use the Catalog API to add new instance types for your AMI-based product in AWS Marketplace. 

**Note**  
For more information about adding instance types using the AWS Marketplace Management Portal, see [ Add an instance](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-adding-instance-types) in the *AWS Marketplace Seller Guide*. 

`AddInstanceTypes` will add new instance types to existing products and newly created products when creating a product. The change type will update all versions in product document with a new instance type.

**Note**  
The `AddInstanceTypes` change type is only available on `AmiProduct@1.0`.

When adding a restricted instance type, the instance type can be removed from the restricted list and added to the available instance type list. This gives sellers more control to change their product restriction. The instance type list is interchangeable and not a permanent restricted status for a product.

For internally metered products, sellers need to call separate change types `AddDimensions` and `UpdatePricingTerms` to update pricing for the instance type.

To add new instance types, call the `StartChangeSet` API operation with the `RestrictRegions` change type, as shown in the following example.

**Request Syntax**

Only `AddInstanceTypes` change type is shown below. Although internally metered AMI sellers are required to call `AddInstanceTypes` and `UpdatePricingTerms` change types for their AMI.

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "AddInstanceTypes",
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "AmiProduct@1.0"
      },
      "DetailsDocument":
      {
        "InstanceTypes":
        [
          "m1.medium"
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `AddInstanceTypes` change type:
+ `Entity` (object) (required) – Your AMI-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+ **DetailsDocument** (object) (required) – The details required to execute the `ChangeSet`, in this case `InstanceTypes`.
  + `InstanceTypes` (array of strings) (required) – List of `InstanceTypes` to add to the product. These instances will be added to the existing `InstanceTypes`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `AddInstanceTypes` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP | 
| --- | --- | --- | 
| InstanceTypes | Required | 422 | 
| InstanceTypes | Must not be empty | 422 | 
| InstanceTypes | Entries must be between 1 to 24 characters long. Must match ^[A-Za-z0-9\_.-]\+$ | 422 | 
| InstanceTypes | Entries must be unique | 422 | 
| InstanceTypes | Must not be more than 1500 entries | 422 | 
| An unknown property | No additional properties are allowed | 422 | 

**Asynchronous Errors**

The following errors are specific to `AddInstanceTypes` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_INSTANCE\_TYPES | The following instance types are not valid: [x] | 
| INVALID\_INSTANCE\_VIRTUALIZATION | Virtualization of the product is [x]. It is not supported by the following instance types: [x] | 
| INVALID\_AMI\_ARCHITECTURE | CPU architecture of the product is '%s'." \+ "It is not supported by the following instance types: [x] | 
|  INCOMPATIBLE\_OPERATING\_SYSTEM  | The instance types are incompatible with the OS defined in the product. Provide instance types that are compatible with the OS defined in the product. | 
| INVALID\_PRODUCT\_TYPE | Use an existing single AMI product. | 
| INVALID\_ENA\_SETTING | The product does not support ENA. ENA support is required by the following instance types: [x] | 
| INVALID\_DIMENSIONS | No internally metered dimensions found for instance types: [x] | 
| MISSING\_DIMENSIONS | No dimensions found for the product. AddDimensions is required before AddInstanceTypes. | 
| UPDATE\_PRICING\_REQUIRED | UpdatePricingTerms change type is required when internally metered dimensions are available on the product. | 

## Restrict an instance type
<a name="restrict-instance-types"></a>

You can use the Catalog API to limit or restrict the instance types available for your AMI-based product in AWS Marketplace. 

**Note**  
For more information about limiting or restrict the instance types available using the AWS Marketplace Management Portal, see [ Restrict an instance](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-single-ami-products.html#single-ami-restricting-instance-types) in the *AWS Marketplace Seller Guide*. 

Existing subscribers won't be impacted by this change and they are able to use the restricted instance types. However, no new buyers will be able to use restricted instance types. To stop current instance types subscriptions (once instance types are restricted), you must contact the AWS Marketplace Seller Operations Team.

`RestrictInstanctTypes` restricts instance types to all the versions in the product document. In the `AddInstanceTypes` change type, you are updating all versions of the product. You won't be able to restrict the recommended instance types. The recommended instance type is at the version level, so it's possible that the seller won't be able to restrict multiple instance types.

For an internally metered product, you need to call separate change types when calling `RestrictDimensions`. This prevents new offers being created for the restricted instance types.

**Note**  
The `RestrictInstanceTypes` change type is only available on `AmiProduct@1.0`.

To limit or restrict the instance types available for your AMI-based product, call the `StartChangeSet` API operation with the `RestrictInstanceTypes` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "RestrictInstanceTypes",
      "Entity":
      {
        "Identifier": "{{prod-example12345}}",
        "Type": "AmiProduct@1.0"
      },
      "DetailsDocument":
      {
        "InstanceTypes":
        [
          "m1.medium"
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `RestrictInstanceTypes` change type. 
+ `Entity` (object) (required) – Your AMI-based product. 
  + `Identifier` (string) (required) – Your product ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – The `Type` is based on the delivery method (product type) that your product will be using: `AmiProduct@1.0`. 
+ **DetailsDocument** (object) (required) – The details required to execute the `ChangeSet`, in this case `InstanceTypes`.
  + `InstanceTypes` (array of strings) (required) – List of `InstanceTypes` to restrict to the product. These instances are added to the current (or if there are no existing instance types, it will add) to restricted `InstanceTypes`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "{{example123456789012abcdef}}",
   "ChangeSetArn": "arn:aws:aws-marketplace:{{us-east-1}}:{{123456789012}}:AWSMarketplace/ChangeSet/{{example123456789012abcdef}}"
}
```

The change request is added to a queue and processed. This included validating information to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `RestrictInstanceTypes` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP | 
| --- | --- | --- | 
| InstanceTypes | Required | 422 | 
| InstanceTypes | Must not be empty | 422 | 
| InstanceTypes | Entries must be between 1 to 24 characters long. Must match ^[A-Za-z0-9\_.-]\+$ | 422 | 
| InstanceTypes | Entries must be unique | 422 | 
| InstanceTypes | Must not be more than 1500 entries | 422 | 
| An unknown property | No additional properties are allowed | 422 | 

**Asynchronous Errors**

The following errors are specific to `RestrictInstanceTypes` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_ INSTANCE\_TYPES | The following instance types are not valid: [x] | 
| INVALID\_ PRODUCT\_TYPE | Use an existing single AMI product. | 
| DUPLICATE\_INSTANCE\_TYPE | Provide instance types with no duplicates. | 
| UNAVAILABLE\_INSTANCE\_TYPE | Provide an available instance type. | 
|  RECOMMENDED\_INSTANCE\_TYPE\_RESTRICTED  | The following instance types cannot be restricted. Recommended instance type must be changed to a different one before being restricted. Delivery Options Id [X] Instance Type[X] | 
|  DIMENSIONS\_NOT\_RESTICTED  | Restrict dimensions before restricting internally metered instance types: [x] | 
|  REGION\_NO\_INSTANCES  | Your restricted instance types would cause product launch failure in region: X. Consider restricting fewer instances. | 
| INCOMPATIBLE\_RESTRICTION | Your restricted instance types would cause product with no FPGA based instance types for AFIs. Product needs to support at least one FPGA based instance type. | 