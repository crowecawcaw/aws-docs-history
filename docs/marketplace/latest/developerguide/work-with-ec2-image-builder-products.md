

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with EC2 Image Builder component products
<a name="work-with-ec2-image-builder-products"></a>

As an AWS Marketplace seller, you can list AMI-based products delivered to AWS Marketplace buyers using EC2 Image Builder components. To create your component and publish an AWS Marketplace listing, proceed sequentially through the following sections.

**Topics**
+ [Building and testing your Image Builder component](#build-and-test-ib-component)
+ [Copying the component ARN](#ib-copy-component-arn)
+ [Creating AWS Marketplace IAM policies](#ib-create-iam-policies)
+ [Creating the AWS Marketplace IAM role](#ib-create-iam-role)
+ [Prepare your Image Builder component listing](#prepare-ec2-ib-listing)
+ [Publishing your Image Builder component product listing](#publishing-ib-component-listing)
+ [Updating Image Builder component product information](#updating-ec2-image-builder-product)
+ [Adding a new version to an existing Image Builder component product](#adding-new-ec2-ib-version-existing-product)
+ [Updating information about an existing version](#updating-ec2-ib-product-version)
+ [Restricting an Image Builder component product version](#restricting-ec2-ib-product-version)
+ [Monitoring a change set](#monitor-changeset)
+ [Securing software downloads](#securing-software-downloads)

## Building and testing your Image Builder component
<a name="build-and-test-ib-component"></a>

Build and test your component on Image Builder. For instructions, refer to [Develop custom components for your Image Builder image](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-custom-components.html) in the *Image Builder User Guide*. When creating your component using Image Builder, ensure that you do the following:
+ The component and all of its underlying dependencies, such as an Amazon Simple Storage Service (Amazon S3) bucket, secrets, or parameters, must be created in the US East (N. Virginia) (`us-east-1`) AWS Region.
+ Include supported architecture and any software dependencies in the component description.
+ Test your component in your AWS account by creating an [image pipeline](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html) and deploying the AMI created by the pipeline.
+ If your component contains instructions to copy binaries, packages, or files from an S3 bucket, use the `S3Download` action module. In the `S3Download` module, for `source`, enter the static location of your file in the S3 bucket. The following example copies a binary from an S3 bucket as part of the component installation.

  ```
  - name: DownloadMyFile
      action: S3Download
      inputs:
        - source: s3://amzn-s3-demo-source-bucket/path/to/package.zip
          destination: C:\myfolder\package.zip
  ```
+ Components can ingest files of up to 2 GB when using the `S3Download` action.
+ If your component uses [parameters](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-user-defined-variables.html#user-defined-vars-parameters), ensure that all parameters have default values. For example, if you have a parameter named `region`, ensure that you have a valid default value such as `us-east-1`. These default values are for AWS Marketplace processing and testing. Testing may fail if you do not include default values.
+ If your component uses AWS Secrets Manager, Parameter Store, or a capability of AWS Systems Manager to store parameters, do the following:
+ 
  + To retrieve values as a step in your component, embed AWS Command Line Interface commands in your YAML configuration file.
  + Create a corresponding entry in Secrets Manager or Parameter Store in your AWS account. Use the default key and provide a valid value that will assist in building the component during the AWS Marketplace testing process. For example, say you have a parameter called `saas_token` with a default value of `token` that uses Parameter Store. In this case, create a key-value pair in Parameter Store. Use `token` as the key. For the value, enter a valid SaaS token for your application.

    Note that values stored in your AWS Marketplace seller account will only be used for AWS Marketplace testing purposes. These values will not be shared with buyers.
  + AWS Marketplace automatically generates Amazon Machine Images (AMIs) for your component across all compatible operating system versions you choose during the component creation process. When building your component, choose at least one compatible operating system version. Validate your component's compatibility with all chosen operating system versions by using EC2 Image Builder pipelines to create and test AMIs.

## Copying the component ARN
<a name="ib-copy-component-arn"></a>

After creating and testing the component on Image Builder, copy and save the component ARN. You will use the ARN when you publish the product listing using the AWS Marketplace Catalog API.

**To copy the Image Builder component ARN**

1. Sign in to the AWS Management Console and open the Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. In the left navigation bar, under **Saved resources**, choose **Components**.

1. On the **Components** page, for **Filter owner**, choose **Owned by me**.

1. Choose the component name.

1. On the component detail page, in the **Summary** section, copy the ARN.

## Creating AWS Marketplace IAM policies
<a name="ib-create-iam-policies"></a>

Create the following IAM policies to grant AWS Marketplace access to your Image Builder component and related resources like Amazon S3 buckets and secrets. Use the example policies provided. You attach these policies to an [AWS Marketplace IAM role](#ib-create-iam-role). For help creating policies, see [Creating policies using the JSON editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor) in the *IAM User Guide*.
+ Image Builder get-component policy, to allow AWS Marketplace to access your component on Image Builder. This policy is required. Name the policy `mp_ib_ingest`.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "VisualEditor0",
              "Effect": "Allow",
              "Action": "imagebuilder:GetComponent",
              "Resource": "*"
          }
      ]
  }
  ```

------
+ Amazon S3 read-access policy, to allow AWS Marketplace to retrieve binaries from an S3 bucket. This policy is only required if your component uses the `S3Download` action module and stores associated binaries in an S3 bucket. Name the policy `mp_ib_s3_read_only`.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Sid": "ListObjectsInBucket",
              "Effect": "Allow",
              "Action": [
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws:s3:::{{bucket_name}}"
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
                  "arn:aws:s3:::{{bucket_name}}/*"
              ]
          }
      ]
  }
  ```

------
+ Secrets Manager read-access policy, to allow AWS Marketplace to retrieve secrets stored in Secrets Manager. This policy is only required if your component uses Secrets Manager to store secrets. Name the policy `mp_ib_sm_read_only`. To restrict the policy to just your secret, replace the `*` in the `Resource` section with your secret.

------
#### [ JSON ]

****  

  ```
  {
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
  }
  ```

------
+ Parameter Store read-access policy, to allow AWS Marketplace to retrieve secrets stored in Parameter Store. This policy is only required if your component uses Parameter Store to store secrets. Name the policy `mp_ib_ssm_parameter_read_only`. To restrict the policy to just your secret, replace the `*` in the `Resource` section with your secret.

------
#### [ JSON ]

****  

  ```
  {
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
  }
  ```

------

## Creating the AWS Marketplace IAM role
<a name="ib-create-iam-role"></a>

Use the following procedure to create an AWS Marketplace IAM role with policies to grant AWS Marketplace access to your component and its dependencies.

**To create the AWS Marketplace IAM role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation bar, choose **Roles**.

1. Choose **Create role**.

1. Select **Custom trust policy**.

1. Enter the following statement:

------
#### [ JSON ]

****  

   ```
   {
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
   }
   ```

------

1. Choose **Next**.

1. Add the Image Builder get-component policy you created previously. The get-component policy is required. Add the relevant policies for S3, Secrets Manager, and Parameter Store if your component uses these AWS services.

1. Choose **Next**.

1. Enter a role name, such as `MPEC2IBIngestion`.

1. Choose **Create role**.

### Copy AWS Marketplace IAM role ARN
<a name="copy-ib-role-arn"></a>

After creating the AWS Marketplace IAM role, copy and save the role ARN. You will use the ARN when publishing the listing using the AWS Marketplace Catalog API.

**To copy the AWS Marketplace IAM role ARN**

1. In the IAM console, in the left navigation bar, choose **Roles**.

1. Choose the AWS Marketplace IAM role you created previously, such as `MPEC2IBIngestion`.

1. On the role detail page, in the **Summary** section, copy the ARN.

## Prepare your Image Builder component listing
<a name="prepare-ec2-ib-listing"></a>

Before publishing your AWS Marketplace listing, ensure that you have the following information ready:
+ **Product metadata – **Metadata includes the product logo, product title, End User License agreement, supported instance types, and AWS Region.
+ **Pricing information – ** You can offer your product for free, at an hourly rate, or at an hourly rate with an initial free trial period. Bring your own license (BYOL) is not supported.
+ **Component details – **Details include the component Amazon Resource Number (ARN), usage details, and AWS Identity and Access Management (IAM) role that AWS Marketplace will assume to process your component.

## Publishing your Image Builder component product listing
<a name="publishing-ib-component-listing"></a>

This topic contains instructions to publish your EC2 Image Builder component listing on AWS Marketplace using the AWS Marketplace Catalog API.

### Prerequisites
<a name="publish-ib-component-listing-capi-prerequisites"></a>

Ensure that you have the following before publishing your Image Builder component product listing:
+ Registration as a seller in AWS Marketplace. For more information, refer to [Register as an AWS Marketplace seller](https://catalog.workshops.aws/mpseller/en-US/pre-requisite-register-as-seller).
+ An IAM user with `AWSMarketplaceSellerFullAccess` permission.
+ A publicly accessible Amazon Simple Storage Service (Amazon S3) bucket to host your company logo and EULA, if used in your component. You will enter the URL for the S3 bucket in your `ChangeSet` JSON file.
+ AWS Command Line Interface (AWS CLI). For more information, refer to [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS Command Line Interface User Guide*.

### Creating an Image Builder component product on AWS Marketplace
<a name="ib-create-json"></a>

To create an EC2 Image Builder component product on AWS Marketplace using the Catalog API, refer to [Create a product](work-with-seller-products.md#create-product).

## Updating Image Builder component product information
<a name="updating-ec2-image-builder-product"></a>

You can update information about a Image Builder component product on the AWS Marketplace Management Portal.

**To update Image Builder component product information**

1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/) and sign in to your seller account.

1. On the **Products** menu, choose **Server**.

1. On the **Server products** page, select the product.

1. On the product detail page, on the **Request changes** menu, choose the item that corresponds to the information you want to update.

1. After submitting any changes, the request will appear on the **Requests** tab in "Under review" status, and will change to "Succeeded" once completed. 

## Adding a new version to an existing Image Builder component product
<a name="adding-new-ec2-ib-version-existing-product"></a>

You can add a new version to an Image Builder component product on AWS Marketplace using the AWS Marketplace Catalog API.

**To add a new version**

1. From the AWS Marketplace Management Portal, obtain the Product ID.

   1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/) and sign in to your seller account.

   1. On the **Products** menu, choose **Server**.

   1. On the **Server products** page, select the product.

   1. In the **Product summary**, copy the **Product ID**.

1. Using the following code example, create a changeset file in JSON format. In the example, replace {{your-product-ID}} with the product ID you obtained in step 1. Replace {{new-version-name}} with your version title. Replace {{new-delivery-option-title}} with your delivery option title.

   ```
   [
       {
           "ChangeType": "AddDeliveryOptions",
           "Entity": {
               "Identifier": "{{your-product-ID}}",
               "Type": "AmiProduct@1.0"
           },
           "DetailsDocument": {
               "Version": {
                   "VersionTitle": "{{new-version-name}}",
                   "ReleaseNotes": "Release notes goes here."
               },
               "DeliveryOptions": [
                   {
                       "DeliveryOptionTitle": "{{new title}}",
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

1. Save the changeset file with the name `addIBversion.json`.

1. In your terminal or AWS CloudShell, run the following command:

   ```
   aws marketplace-catalog start-change-set --catalog AWSMarketplace --region us-east-1 --change-set file://addIBversion.json
   ```

The `start-change-set` command will return a `ChangeSetId` value. To monitor a change set, see [Monitoring a change set](#monitor-changeset).

**Asynchronous Errors**

The following errors are specific to `AddDeliveryOptions` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).

**Note**  
The following error codes are specific to the Image Builder delivery method. For existing error messages on fields such as `Usage Instructions`, `Recommended Instance type`, and `AccessRoleArn`, see [Add a new version](work-with-single-ami-products.md#ami-add-version).


| Error code | Error message | 
| --- | --- | 
| ASSET\_NOT\_FOUND | Check if [component arn] exists in [account-id] AWS account and the AccessARN provided [ARN] has permissions to share this Image Builder component with AWS Marketplace. | 
| ASSET\_NOT\_FOUND | The specified S3 link [x] within the component[x] does not exist. Provide a valid S3 link within the component. | 
| DUPLICATE\_COMPONENT\_NAME | The component name [x] already exists within the same version. Provide a different component name. | 
| DUPLICATE\_COMPONENT\_NAME | The component name [x] you provided is already in use by a different product. Provide a different component name. | 
| DUPLICATE\_COMPONENT\_ARN | The component Arn [x] must be different from Component Arn used in other delivery options of the same version of this product. | 
| DUPLICATE\_COMPONENT\_ARN | The component ARN [x] must be different from component ARN used in other versions of this product. | 
| SCAN\_ERROR | Fix security vulnerability [y] on Component [x]. | 
| ASSET\_ACCESS\_EXCEPTION | We don't have the necessary permissions to read the contents from the specified S3 bucket[x]. Ensure the S3 bucket has the appropriate read permissions. | 
| ASSET\_ACCESS\_EXCEPTION | We don't have the necessary permissions to read the contents of the specified component ARN[x]. Ensure the component ARN has the appropriate read permissions. | 
| ASSET\_ACCESS\_EXCEPTION | We don't have the necessary permissions to read the contents of the specified package URI [x]. Ensure the package URI has the appropriate read permissions. | 
| ASSET\_ACCESS\_EXCEPTION | Failed to read from the HTTP source [x]. Verify that the provided HTTP source is correct. | 
| INVALID\_IMAGE\_BUILDER\_COMPONENT\_PACKAGE | Component assets exceed the size limit for ingestion. Reduce the size of S3/web downloads or eliminate unnecessary downloads to proceed. | 
| INVALID\_IMAGE\_BUILDER\_COMPONENT\_PACKAGE | Component assets are taking too long to ingest. Ensure that your network connection is stable and has adequate bandwidth. | 
| TOO\_MANY\_IMAGE\_BUILDER\_COMPONENTS | Max of 5 unique component names are supported per product, restrict the additional delivery option. | 
| INCOMPLETE\_SELLER\_PUBLIC\_PROFILE | Your seller public profile is not complete. Complete your public profile before adding versions to the product. | 
| INVALID\_DESCRIPTION | The description is missing. Provide a description with fewer than 1024 characters in component [x]. | 
| INVALID\_COMPONENT\_NAME | Provide a component name with fewer than [x] characters. | 
| INVALID\_SUPPORTED\_OS\_VERSION | The OS version is missing. Provide a valid supported OS version in component [x]. | 
| INVALID\_PATH\_FORMAT | Step [STEP\_NAME] in phase [PHASE\_NAME] is not allowed to use S3 or web URLs for the InstallMSI/UninstallMSI actions. Ensure that the path specified is a valid local path accessible from the system executing the action. | 
| INCOMPATIBLE\_OS\_TYPE | The specified component OS type[x] is not compatible with the platform of the base image. Provide an OS type that is compatible with the base image. | 
| ASSET\_ACCESS\_EXCEPTION | We don't have the necessary permissions to read the contents from the specified SSM parameter [x]. Ensure that the IAM access role provided in the API input has the required read permissions. | 
| ASSET\_ACCESS\_EXCEPTION | We don't have the necessary permissions to read the contents from the specified SecretsManager secret [x]. Ensure that the IAM access role provided in the API input has the required read permissions. | 
| INVALID\_IB\_COMPONENT\_BUILD\_VERSION | Component ARN [x] has a build version of [y]. AWS Marketplace only supports build version 1. Create a new EC2 Image Builder version with Build versions 1, and try again on AWS Marketplace | 
| INVALID\_IB\_COMPONENT\_PARAMETER | Unable to parse the SSM parameter in input [x] for component [y]. | 
| INVALID\_IB\_COMPONENT\_PARAMETER | Unable to parse the SecretsManager secret in input [x] for component [y]. | 
| MISSING\_IB\_COMPONENT\_PARAMETER | Parameter not found in component [x] for input [y] | 
| INVALID\_IB\_COMPONENT\_PARAMETER | Provide a default value for parameter [x] in component [y]. | 
| FAILED\_LAUNCH\_TEST | The launch test for component [x] has failed. Error message: [z] | 
| SSHAuthFailedForUserAndKeypair | Unable to log into the instance with OS default username [X]. | 
| INVALID\_IB\_COMPONENT | A component build phase is required. Add a valid build phase to component [x] | 
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
| INVALID\_USAGE\_INSTRUCTIONS | Provide usage instructions with fewer than (x) characters. | 
| DUPLICATE\_DELIVERY\_OPTION\_TITLES | Provide unique delivery option title. | 
| INVALID\_DELIVERY\_OPTION\_TITLES | Delivery option title already exists, retry with a different title. | 

## Updating information about an existing version
<a name="updating-ec2-ib-product-version"></a>



**To update information about an existing version**

1. From the AWS Marketplace Management Portal, obtain the Product ID.

   1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/) and sign in to your seller account.

   1. On the **Products** menu, choose **Server**.

   1. On the **Server products** page, select the product.

   1. In the **Product summary**, copy the **Product ID**.

1. In your terminal, run the following command. In the command, replace {{your-product-ID}} with the ID you obtained in step 1.

   ```
   aws marketplace-catalog describe-entity --catalog AWSMarketplace --region us-east-1 --entity-id '{{your-product-ID}}'
   ```

1. In the output returned, go to the `DetailsDocument`, `Versions` section. Copy the `DeliveryOptions`, `Id` value for the version you want to update.

1. Using the following code example, create a changeset file in JSON format. In the example, replace {{your-product-ID}} with the product ID you obtained in step 1. Replace {{your-release-notes}} with your release notes. Replace {{your-delivery-option-ID}} with the ID of the delivery option you obtained in step 3. Replace {{your-usage-instructions}} with your usage instructions.

   ```
   [
       {
           "ChangeType": "UpdateDeliveryOptions",
           "Entity": {
               "Identifier": "{{your-product-ID}}",
               "Type": "AmiProduct@1.0"
           },
           "DetailsDocument": {
               "Version": {
                   "ReleaseNotes": "{{your-release-notes}}"
               },
               "DeliveryOptions": [
                   {
                       "Id": "{{your-delivery-option-ID}}",
                       "Details": {
                           "Ec2ImageBuilderComponentDeliveryOptionDetails": {
                               "UsageInstructions": "{{your-usage-instructions}}"
                           }
                       }
                   }
               ]
           }
       }
   ]
   ```

1. Save the changeset file with the name `updateVersionInfo.json`.

1. In your terminal or AWS CloudShell, run the following command:

   ```
   aws marketplace-catalog start-change-set --catalog AWSMarketplace --region us-east-1 --change-set file://updateVersionInfo.json
   ```

The `start-change-set` command will return a `ChangeSetId` value. To monitor a change set, see [Monitoring a change set](#monitor-changeset).

## Restricting an Image Builder component product version
<a name="restricting-ec2-ib-product-version"></a>

Restricting a version makes it unavailable to buyers. You can restrict a version of your Image Builder component product on AWS Marketplace using the AWS Marketplace Catalog API. You must keep at least one version of your product unrestricted on AWS Marketplace. You can't restrict access to the only public version.

**To update information about an existing version**

1. From the AWS Marketplace Management Portal, obtain the Product ID.

   1. Open the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour/) and sign in to your seller account.

   1. On the **Products** menu, choose **Server**.

   1. On the **Server products** page, select the product.

   1. In the **Product summary**, copy the **Product ID**.

1. In your terminal, run the following command. In the command, replace {{your-product-ID}} with the ID you obtained in step 1.

   ```
   aws marketplace-catalog describe-entity --catalog AWSMarketplace --region us-east-1 --entity-id '{{your-product-ID}}'
   ```

1. In the output returned, go to the `DetailsDocument`, `Versions` section. Copy the `DeliveryOptions`, `Id` value for the version you want to update.

1. Using the following code example, create a changeset file in JSON format. In the example, replace {{your-product-ID}} with the product ID you obtained in step 1. Replace {{your-delivery-option-ID}} with the ID of the delivery option you obtained in step 3.

   ```
   [
       {
           "ChangeType": "RestrictDeliveryOptions",
           "Entity": {
               "Identifier": "{{your-product-ID}}",
               "Type": "AmiProduct@1.0"
           },
           "DetailsDocument": {
               "DeliveryOptionIds": [
                   "{{your-delivery-option-ID}}"
               ]
           }
       }
   ]
   ```

1. Save the changeset file with the name `restrictec2ibversion.json`.

1. In your terminal or AWS CloudShell, run the following command:

   ```
   aws marketplace-catalog start-change-set --catalog AWSMarketplace --region us-east-1 --change-set file://restrictec2ibversion.json
   ```

The `start-change-set` command will return a `ChangeSetId` value. To monitor a change set, see [Monitoring a change set](#monitor-changeset).

## Monitoring a change set
<a name="monitor-changeset"></a>

The `start-change-set` command will return a `ChangeSetId` value. You can monitor change set progress in the following ways:
+ Run the following command in your terminal. In the command. replace {{changeset-ID}} with the `ChangeSetId` value returned by the `start-change-set` command.

  ```
  aws marketplace-catalog describe-change-set ‐‐catalog AWSMarketplace ‐‐change-set-id {{changesetID}}
  ```
+ View the request status on the **Requests** tab in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/).

## Securing software downloads
<a name="securing-software-downloads"></a>

To safeguard ISV software intellectual property and ensure stable, consistent software delivery to AWS Marketplace buyers, AWS Marketplace automatically parses `S3Download` and `WebDownload` action modules in your component. The referenced files are then securely stored in a private Amazon S3 bucket managed by AWS Marketplace. To opt out of this ingestion process and manage software downloads independently, run bash scripts that use the `wget` or `curl` download commands.