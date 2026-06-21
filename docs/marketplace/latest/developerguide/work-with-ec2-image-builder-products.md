The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Work with EC2 Image Builder component products

As an AWS Marketplace seller, you can list AMI-based products delivered to AWS
Marketplace buyers using EC2 Image Builder components. To create your component and publish an
AWS Marketplace listing, proceed sequentially through the following sections.

###### Topics

- [Building and testing your Image Builder component](#build-and-test-ib-component "#build-and-test-ib-component")
- [Copying the component ARN](#ib-copy-component-arn "#ib-copy-component-arn")
- [Creating AWS Marketplace IAM policies](#ib-create-iam-policies "#ib-create-iam-policies")
- [Creating the AWS Marketplace IAM role](#ib-create-iam-role "#ib-create-iam-role")
- [Prepare your Image Builder component listing](#prepare-ec2-ib-listing "#prepare-ec2-ib-listing")
- [Publishing your Image Builder component product listing](#publishing-ib-component-listing "#publishing-ib-component-listing")
- [Updating Image Builder component product information](#updating-ec2-image-builder-product "#updating-ec2-image-builder-product")
- [Adding a new version to an existing Image Builder component product](#adding-new-ec2-ib-version-existing-product "#adding-new-ec2-ib-version-existing-product")
- [Updating information about an existing version](#updating-ec2-ib-product-version "#updating-ec2-ib-product-version")
- [Restricting an Image Builder component product version](#restricting-ec2-ib-product-version "#restricting-ec2-ib-product-version")
- [Monitoring a change set](#monitor-changeset "#monitor-changeset")
- [Securing software downloads](#securing-software-downloads "#securing-software-downloads")

## Building and testing your Image Builder component

Build and test your component on Image Builder. For instructions, refer to [Develop
custom components for your Image Builder image](../../../imagebuilder/latest/userguide/create-custom-components.md "../../../imagebuilder/latest/userguide/create-custom-components.md") in the
_Image Builder User Guide_. When creating your component using Image Builder,
ensure that you do the following:

- The component and all of its underlying dependencies, such as an Amazon Simple Storage Service
  (Amazon S3) bucket, secrets, or parameters, must be created in the
  US East (N. Virginia) (`us-east-1`) AWS Region.
- Include supported architecture and any software dependencies in the
  component description.
- Test your component in your AWS account by creating an [image pipeline](../../../imagebuilder/latest/userguide/start-build-image-pipeline.md "../../../imagebuilder/latest/userguide/start-build-image-pipeline.md") and deploying the AMI created by the
  pipeline.
- If your component contains instructions to copy binaries, packages, or
  files from an S3 bucket, use the `S3Download` action module. In
  the `S3Download` module, for `source`, enter the
  static location of your file in the S3 bucket. The following example copies
  a binary from an S3 bucket as part of the component installation.

```
- name: DownloadMyFile
    action: S3Download
    inputs:
      - source: s3://amzn-s3-demo-source-bucket/path/to/package.zip
        destination: C:\myfolder\package.zip
```

- Components can ingest files of up to 2 GB when using the
  `S3Download` action.
- If your component uses [parameters](../../../imagebuilder/latest/userguide/toe-user-defined-variables.md#user-defined-vars-parameters "../../../imagebuilder/latest/userguide/toe-user-defined-variables.md#user-defined-vars-parameters"), ensure that all parameters have default values. For
  example, if you have a parameter named `region`, ensure that you
  have a valid default value such as `us-east-1`. These default
  values are for AWS Marketplace processing and testing. Testing may fail if you do not
  include default values.
- If your component uses AWS Secrets Manager, Parameter Store, or a capability of
  AWS Systems Manager to store parameters, do the following:
- - To retrieve values as a step in your component, embed AWS Command Line Interface
    commands in your YAML configuration file.
  - Create a corresponding entry in Secrets Manager or Parameter Store in your
    AWS account. Use the default key and provide a valid value that
    will assist in building the component during the AWS Marketplace testing
    process. For example, say you have a parameter called
    `saas_token` with a default value of
    `token` that uses Parameter Store. In this case,
    create a key-value pair in Parameter Store. Use `token`
    as the key. For the value, enter a valid SaaS token for your
    application.

  Note that values stored in your AWS Marketplace seller account will only be
  used for AWS Marketplace testing purposes. These values will not be shared
  with buyers.
  - AWS Marketplace automatically generates Amazon Machine Images (AMIs) for
    your component across all compatible operating system versions you
    choose during the component creation process. When building your
    component, choose at least one compatible operating system version.
    Validate your component's compatibility with all chosen operating
    system versions by using EC2 Image Builder pipelines to create and
    test AMIs.

## Copying the component ARN

After creating and testing the component on Image Builder, copy and save the component ARN.
You will use the ARN when you publish the product listing using the AWS Marketplace Catalog
API.

###### To copy the Image Builder component ARN

1. Sign in to the AWS Management Console and open the Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. In the left navigation bar, under **Saved resources**,
   choose **Components**.
3. On the **Components** page, for **Filter
   owner**, choose **Owned by me**.
4. Choose the component name.
5. On the component detail page, in the **Summary** section,
   copy the ARN.

## Creating AWS Marketplace IAM policies

Create the following IAM policies to grant AWS Marketplace access to your Image Builder component
and related resources like Amazon S3 buckets and secrets. Use the example policies
provided. You attach these policies to an [AWS Marketplace
IAM role](#ib-create-iam-role "#ib-create-iam-role"). For help creating policies, see [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
_IAM User Guide_.

- Image Builder get-component policy, to allow AWS Marketplace to access your component on
  Image Builder. This policy is required. Name the policy
  `mp_ib_ingest`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "imagebuilder:GetComponent",
 "Resource": "*"
 }
 ]
}`

```

- Amazon S3 read-access policy, to allow AWS Marketplace to retrieve binaries from an S3
  bucket. This policy is only required if your component uses the
  `S3Download` action module and stores associated binaries in
  an S3 bucket. Name the policy `mp_ib_s3_read_only`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListObjectsInBucket",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket_name`"
 ]
 },
 {
 "Sid": "ReadObjectsInBucket",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectAttributes"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket_name`/*"
 ]
 }
 ]
}`

```

- Secrets Manager read-access policy, to allow AWS Marketplace to retrieve secrets stored in
  Secrets Manager. This policy is only required if your component uses Secrets Manager to store
  secrets. Name the policy `mp_ib_sm_read_only`. To restrict the
  policy to just your secret, replace the `*` in the
  `Resource` section with your secret.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

- Parameter Store read-access policy, to allow AWS Marketplace to retrieve secrets
  stored in Parameter Store. This policy is only required if your component
  uses Parameter Store to store secrets. Name the policy
  `mp_ib_ssm_parameter_read_only`. To restrict the policy to
  just your secret, replace the `*` in the `Resource`
  section with your secret.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "ssm:getParameter"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Creating the AWS Marketplace IAM role

Use the following procedure to create an AWS Marketplace IAM role with policies to grant
AWS Marketplace access to your component and its dependencies.

###### To create the AWS Marketplace IAM role

1. Sign in to the AWS Management Console and open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation bar, choose **Roles**.
3. Choose **Create role**.
4. Select **Custom trust policy**.
5. Enter the following statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Principal": {
 "Service": "assets.marketplace.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. Choose **Next**.
7. Add the Image Builder get-component policy you created previously. The
   get-component policy is required. Add the relevant policies for S3, Secrets Manager,
   and Parameter Store if your component uses these AWS services.
8. Choose **Next**.
9. Enter a role name, such as `MPEC2IBIngestion`.
10. Choose **Create role**.

### Copy AWS Marketplace IAM role ARN

After creating the AWS Marketplace IAM role, copy and save the role ARN. You will use
the ARN when publishing the listing using the AWS Marketplace Catalog API.

###### To copy the AWS Marketplace IAM role ARN

1. In the IAM console, in the left navigation bar, choose
   **Roles**.
2. Choose the AWS Marketplace IAM role you created previously, such as
   `MPEC2IBIngestion`.
3. On the role detail page, in the **Summary** section,
   copy the ARN.

## Prepare your Image Builder component listing

Before publishing your AWS Marketplace listing, ensure that you have the following
information ready:

- **Product metadata –** Metadata
  includes the product logo, product title, End User License agreement,
  supported instance types, and AWS Region.
- **Pricing information –** You can
  offer your product for free, at an hourly rate, or at an hourly rate with an
  initial free trial period. Bring your own license (BYOL) is not
  supported.
- **Component details –** Details
  include the component Amazon Resource Number (ARN), usage details, and
  AWS Identity and Access Management (IAM) role that AWS Marketplace will assume to process your
  component.

## Publishing your Image Builder component product listing

This topic contains instructions to publish your EC2 Image Builder component listing on
AWS Marketplace using the AWS Marketplace Catalog API.

### Prerequisites

Ensure that you have the following before publishing your Image Builder component
product listing:

- Registration as a seller in AWS Marketplace. For more information, refer to
  [Register as an AWS Marketplace seller](https://catalog.workshops.aws/mpseller/en-US/pre-requisite-register-as-seller "https://catalog.workshops.aws/mpseller/en-US/pre-requisite-register-as-seller").
- An IAM user with `AWSMarketplaceSellerFullAccess`
  permission.
- A publicly accessible Amazon Simple Storage Service (Amazon S3) bucket to host your company
  logo and EULA, if used in your component. You will enter the URL for the
  S3 bucket in your `ChangeSet` JSON file.
- AWS Command Line Interface (AWS CLI). For more information, refer to [What is the AWS
  Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the
  _AWS Command Line Interface User Guide_.

### Creating an Image Builder component product on AWS Marketplace

To create an EC2 Image Builder component product on AWS Marketplace using the Catalog API, refer
to [Create a product](work-with-seller-products.md#create-product "work-with-seller-products.md#create-product").

## Updating Image Builder component product information

You can update information about a Image Builder component product on the AWS Marketplace Management
Portal.

###### To update Image Builder component product information

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/") and sign in to your seller account.
2. On the **Products** menu, choose
   **Server**.
3. On the **Server products** page, select the
   product.
4. On the product detail page, on the **Request changes**
   menu, choose the item that corresponds to the information you want to
   update.
5. After submitting any changes, the request will appear on the
   **Requests** tab in "Under review" status, and will
   change to "Succeeded" once completed.

## Adding a new version to an existing Image Builder component product

You can add a new version to an Image Builder component product on AWS Marketplace using the
AWS Marketplace Catalog API.

###### To add a new version

1. From the AWS Marketplace Management Portal, obtain the Product ID.

   1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/") and sign in to your seller account.
   2. On the **Products** menu, choose
      **Server**.
   3. On the **Server products** page, select the
      product.
   4. In the **Product summary**, copy the
      **Product ID**.

2. Using the following code example, create a changeset file in JSON format.
   In the example, replace `your-product-ID` with the
   product ID you obtained in step 1. Replace
   `new-version-name` with your version title.
   Replace `new-delivery-option-title` with your
   delivery option title.

```
[
    {
        "ChangeType": "AddDeliveryOptions",
        "Entity": {
            "Identifier": "`your-product-ID`",
            "Type": "AmiProduct@1.0"
        },
        "DetailsDocument": {
            "Version": {
                "VersionTitle": "`new-version-name`",
                "ReleaseNotes": "Release notes goes here."
            },
            "DeliveryOptions": [
                {
                    "DeliveryOptionTitle": "`new title`",
                    "Details": {
                        "Ec2ImageBuilderComponentDeliveryOptionDetails": {
                            "UsageInstructions": "Test usage instructions for IB",
                            "AccessRoleArn": "arn:aws:iam::123456789:role/sample",
                            "ComponentArn": "arn:aws:imagebuilder:us-east-1:123456789:component/sample/2.0.0/1"
                        }
                    }
                }
            ]
        }
    }
]
```

3. Save the changeset file with the name
   `addIBversion.json`.
4. In your terminal or AWS CloudShell, run the following command:

```
aws marketplace-catalog start-change-set --catalog AWSMarketplace --region us-east-1 --change-set file://addIBversion.json
```

The `start-change-set` command will return a `ChangeSetId`
value. To monitor a change set, see [Monitoring a change set](#monitor-changeset "#monitor-changeset").

**Asynchronous Errors**

The following errors are specific to `AddDeliveryOptions` actions in
the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

###### Note

The following error codes are specific to the Image Builder delivery method. For
existing error messages on fields such as `Usage Instructions`,
`Recommended Instance type`, and `AccessRoleArn`, see
[Add a new version](work-with-single-ami-products.md#ami-add-version "work-with-single-ami-products.md#ami-add-version").

| Error code                              | Error message                                                                                                                                                                                                                                |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ASSET_NOT_FOUND                         | **`Check if [component arn] exists in [account-id]<br>AWS account and the AccessARN provided [ARN] has<br>permissions to share this Image Builder component with<br>AWS Marketplace.`**                                                      |
| ASSET_NOT_FOUND                         | **`The specified S3 link [x] within the<br>component[x] does not exist. Provide a valid S3 link within<br>the component.`**                                                                                                                  |
| DUPLICATE_COMPONENT_NAME                | **`The component name [x] already exists within the<br>same version. Provide a different component<br>name.`**                                                                                                                               |
| DUPLICATE_COMPONENT_NAME                | **`The component name [x] you provided is already<br>in use by a different product. Provide a different component<br>name.`**                                                                                                                |
| DUPLICATE_COMPONENT_ARN                 | **`The component Arn [x] must be different from<br>Component Arn used in other delivery options of the same<br>version of this product.`**                                                                                                   |
| DUPLICATE_COMPONENT_ARN                 | **`The component ARN [x] must be different from<br>component ARN used in other versions of this<br>product.`**                                                                                                                               |
| SCAN_ERROR                              | **`Fix security vulnerability [y] on Component<br>[x].`**                                                                                                                                                                                    |
| ASSET_ACCESS_EXCEPTION                  | **`We don't have the necessary permissions to read<br>the contents from the specified S3 bucket[x]. Ensure the S3<br>bucket has the appropriate read<br>permissions.`**                                                                      |
| ASSET_ACCESS_EXCEPTION                  | **`We don't have the necessary permissions to read<br>the contents of the specified component ARN[x]. Ensure the<br>component ARN has the appropriate read<br>permissions.`**                                                                |
| ASSET_ACCESS_EXCEPTION                  | **`We don't have the necessary permissions to read<br>the contents of the specified package URI [x]. Ensure the<br>package URI has the appropriate read<br>permissions.`**                                                                   |
| ASSET_ACCESS_EXCEPTION                  | **`Failed to read from the HTTP source [x]. Verify<br>that the provided HTTP source is<br>correct.`**                                                                                                                                        |
| INVALID_IMAGE_BUILDER_COMPONENT_PACKAGE | **`Component assets exceed the size limit for<br>ingestion. Reduce the size of S3/web downloads or eliminate<br>unnecessary downloads to proceed.`**                                                                                         |
| INVALID_IMAGE_BUILDER_COMPONENT_PACKAGE | **`Component assets are taking too long to ingest.<br>Ensure that your network connection is stable and has<br>adequate bandwidth.`**                                                                                                        |
| TOO_MANY_IMAGE_BUILDER_COMPONENTS       | **`Max of 5 unique component names are supported<br>per product, restrict the additional delivery<br>option.`**                                                                                                                              |
| INCOMPLETE_SELLER_PUBLIC_PROFILE        | **`Your seller public profile is not complete.<br>Complete your public profile before adding versions to the<br>product.`**                                                                                                                  |
| INVALID_DESCRIPTION                     | **`The description is missing. Provide a<br>description with fewer than 1024 characters in component<br>[x].`**                                                                                                                              |
| INVALID_COMPONENT_NAME                  | **`Provide a component name with fewer than [x]<br>characters.`**                                                                                                                                                                            |
| INVALID_SUPPORTED_OS_VERSION            | **`The OS version is missing. Provide a valid<br>supported OS version in component<br>[x].`**                                                                                                                                                |
| INVALID_PATH_FORMAT                     | **`Step [STEP_NAME] in phase [PHASE_NAME] is not<br>allowed to use S3 or web URLs for the<br>InstallMSI/UninstallMSI actions. Ensure that the path<br>specified is a valid local path accessible from the system<br>executing the action.`** |
| INCOMPATIBLE_OS_TYPE                    | **`The specified component OS type[x] is not<br>compatible with the platform of the base image. Provide an<br>OS type that is compatible with the base<br>image.`**                                                                          |
| ASSET_ACCESS_EXCEPTION                  | **`We don't have the necessary permissions to read<br>the contents from the specified SSM parameter [x]. Ensure<br>that the IAM access role provided in the API input has the<br>required read permissions.`**                               |
| ASSET_ACCESS_EXCEPTION                  | **`We don't have the necessary permissions to read<br>the contents from the specified SecretsManager secret [x].<br>Ensure that the IAM access role provided in the API input<br>has the required read<br>permissions.`**                    |
| INVALID_IB_COMPONENT_BUILD_VERSION      | **`Component ARN [x] has a build version of [y].<br>AWS Marketplace only supports build version 1.<br>Create a new EC2 Image Builder version with Build versions 1,<br>and try again on AWS Marketplace`**                                   |
| INVALID_IB_COMPONENT_PARAMETER          | **`Unable to parse the SSM parameter in input [x]<br>for component [y].`**                                                                                                                                                                   |
| INVALID_IB_COMPONENT_PARAMETER          | **`Unable to parse the SecretsManager secret in<br>input [x] for component [y].`**                                                                                                                                                           |
| MISSING_IB_COMPONENT_PARAMETER          | **`Parameter not found in component [x] for input<br>[y]`**                                                                                                                                                                                  |
| INVALID_IB_COMPONENT_PARAMETER          | **`Provide a default value for parameter [x] in<br>component [y].`**                                                                                                                                                                         |
| FAILED_LAUNCH_TEST                      | **`The launch test for component [x] has failed.<br>Error message: [z]`**                                                                                                                                                                    |
| SSHAuthFailedForUserAndKeypair          | **`Unable to log into the instance with OS default<br>username [X].`**                                                                                                                                                                       |
| INVALID_IB_COMPONENT                    | **`A component build phase is required. Add a valid<br>build phase to component [x]`**                                                                                                                                                       |
| DUPLICATE_VERSION_TITLE                 | **`The version title must be different from any<br>other version titles of this<br>product.`**                                                                                                                                               |
| INVALID_VERSION_TITLE                   | **`Remove spaces before the trademark<br>symbol.`**                                                                                                                                                                                          |
| INVALID_VERSION_TITLE                   | **`Remove unsupported characters: [x, y,<br>z]`**                                                                                                                                                                                            |
| INVALID_VERSION_TITLE                   | **`Remove spaces from the beginning of the version<br>title.`**                                                                                                                                                                              |
| INVALID_VERSION_TITLE                   | **`Provide version title with fewer than [x]<br>characters.`**                                                                                                                                                                               |
| INVALID_RELEASE_NOTES                   | **`Remove spaces before the trademark<br>symbol.`**                                                                                                                                                                                          |
| INVALID_RELEASE_NOTES                   | **`Remove unsupported characters: [x, y,<br>z]`**                                                                                                                                                                                            |
| INVALID_RELEASE_NOTES                   | **`Remove spaces from the beginning of release<br>notes.`**                                                                                                                                                                                  |
| INVALID_RELEASE_NOTES                   | **`Provide release notes with fewer than (x)<br>characters.`**                                                                                                                                                                               |
| INVALID_USAGE_INSTRUCTIONS              | **`Remove spaces before the trademark<br>symbol.`**                                                                                                                                                                                          |
| INVALID_USAGE_INSTRUCTIONS              | **`Remove unsupported characters: [x, y,<br>z]`**                                                                                                                                                                                            |
| INVALID_USAGE_INSTRUCTIONS              | **`Provide usage instructions with fewer than (x)<br>characters.`**                                                                                                                                                                          |
| DUPLICATE_DELIVERY_OPTION_TITLES        | **`Provide unique delivery option<br>title.`**                                                                                                                                                                                               |
| INVALID_DELIVERY_OPTION_TITLES          | **`Delivery option title already exists, retry with<br>a different title.`**                                                                                                                                                                 |

## Updating information about an existing version

###### To update information about an existing version

1. From the AWS Marketplace Management Portal, obtain the Product ID.

   1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/") and sign in to your seller account.
   2. On the **Products** menu, choose
      **Server**.
   3. On the **Server products** page, select the
      product.
   4. In the **Product summary**, copy the
      **Product ID**.

2. In your terminal, run the following command. In the command, replace
   `your-product-ID` with the ID you obtained in
   step 1.

```
aws marketplace-catalog describe-entity --catalog AWSMarketplace --region us-east-1 --entity-id '`your-product-ID`'
```

3. In the output returned, go to the `DetailsDocument`,
   `Versions` section. Copy the `DeliveryOptions`,
   `Id` value for the version you want to update.
4. Using the following code example, create a changeset file in JSON format.
   In the example, replace `your-product-ID` with the
   product ID you obtained in step 1. Replace
   `your-release-notes` with your release notes.
   Replace `your-delivery-option-ID` with the ID of
   the delivery option you obtained in step 3. Replace
   `your-usage-instructions` with your usage
   instructions.

```
[
    {
        "ChangeType": "UpdateDeliveryOptions",
        "Entity": {
            "Identifier": "`your-product-ID`",
            "Type": "AmiProduct@1.0"
        },
        "DetailsDocument": {
            "Version": {
                "ReleaseNotes": "`your-release-notes`"
            },
            "DeliveryOptions": [
                {
                    "Id": "`your-delivery-option-ID`",
                    "Details": {
                        "Ec2ImageBuilderComponentDeliveryOptionDetails": {
                            "UsageInstructions": "`your-usage-instructions`"
                        }
                    }
                }
            ]
        }
    }
]
```

5. Save the changeset file with the name
   `updateVersionInfo.json`.
6. In your terminal or AWS CloudShell, run the following command:

```
aws marketplace-catalog start-change-set --catalog AWSMarketplace --region us-east-1 --change-set file://updateVersionInfo.json
```

The `start-change-set` command will return a `ChangeSetId`
value. To monitor a change set, see [Monitoring a change set](#monitor-changeset "#monitor-changeset").

## Restricting an Image Builder component product version

Restricting a version makes it unavailable to buyers. You can restrict a version
of your Image Builder component product on AWS Marketplace using the AWS Marketplace Catalog API. You must keep
at least one version of your product unrestricted on AWS Marketplace. You can't restrict
access to the only public version.

###### To update information about an existing version

1. From the AWS Marketplace Management Portal, obtain the Product ID.

   1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/") and sign in to your seller account.
   2. On the **Products** menu, choose
      **Server**.
   3. On the **Server products** page, select the
      product.
   4. In the **Product summary**, copy the
      **Product ID**.

2. In your terminal, run the following command. In the command, replace
   `your-product-ID` with the ID you obtained in
   step 1.

```
aws marketplace-catalog describe-entity --catalog AWSMarketplace --region us-east-1 --entity-id '`your-product-ID`'
```

3. In the output returned, go to the `DetailsDocument`,
   `Versions` section. Copy the `DeliveryOptions`,
   `Id` value for the version you want to update.
4. Using the following code example, create a changeset file in JSON format.
   In the example, replace `your-product-ID` with the
   product ID you obtained in step 1. Replace
   `your-delivery-option-ID` with the ID of the
   delivery option you obtained in step 3.

```
[
    {
        "ChangeType": "RestrictDeliveryOptions",
        "Entity": {
            "Identifier": "`your-product-ID`",
            "Type": "AmiProduct@1.0"
        },
        "DetailsDocument": {
            "DeliveryOptionIds": [
                "`your-delivery-option-ID`"
            ]
        }
    }
]
```

5. Save the changeset file with the name
   `restrictec2ibversion.json`.
6. In your terminal or AWS CloudShell, run the following command:

```
aws marketplace-catalog start-change-set --catalog AWSMarketplace --region us-east-1 --change-set file://restrictec2ibversion.json
```

The `start-change-set` command will return a `ChangeSetId`
value. To monitor a change set, see [Monitoring a change set](#monitor-changeset "#monitor-changeset").

## Monitoring a change set

The `start-change-set` command will return a `ChangeSetId`
value. You can monitor change set progress in the following ways:

- Run the following command in your terminal. In the command. replace
  `changeset-ID` with the
  `ChangeSetId` value returned by the
  `start-change-set` command.

```
aws marketplace-catalog describe-change-set ‐‐catalog AWSMarketplace ‐‐change-set-id `changesetID`
```

- View the request status on the **Requests** tab in the
  [AWS Marketplace
  Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/").

## Securing software downloads

To safeguard ISV software intellectual property and ensure stable, consistent
software delivery to AWS Marketplace buyers, AWS Marketplace automatically parses
`S3Download` and `WebDownload` action modules in your
component. The referenced files are then securely stored in a private Amazon S3 bucket
managed by AWS Marketplace. To opt out of this ingestion process and manage software downloads
independently, run bash scripts that use the `wget` or `curl`
download commands.
