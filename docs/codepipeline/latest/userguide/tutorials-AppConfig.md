# Tutorial: Create a pipeline that uses AWS AppConfig

as a deployment provider

In this tutorial, you configure a pipeline that continuously delivers configuration files
using AWS AppConfig as the deployment action provider in your deployment stage.

###### Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be
used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source
action.) If the S3 artifact bucket is in a different account from the account for your
pipeline, make sure that the S3 artifact bucket is owned by AWS accounts that are safe
and will be dependable.

###### Topics

- [Prerequisites](#tutorials-AppConfig-prereq "#tutorials-AppConfig-prereq")
- [Step 1: Create your AWS AppConfig
  resources](#tutorials-AppConfig-application "#tutorials-AppConfig-application")
- [Step 2: Upload files to your S3 source
  bucket](#tutorials-AppConfig-bucket "#tutorials-AppConfig-bucket")
- [Step 3: Create your pipeline](#tutorials-AppConfig-pipeline "#tutorials-AppConfig-pipeline")
- [Step 4: Make a change to any source file
  and verify deployment](#tutorials-AppConfig-verify "#tutorials-AppConfig-verify")

## Prerequisites

Before you begin, you must complete the following:

- This example uses an S3 source for your pipeline. Create or use an Amazon S3 bucket
  with versioning enabled. Follow the instructions in [Step 1: Create an S3 source bucket for your
  application](tutorials-simple-s3.md#s3-create-s3-bucket "tutorials-simple-s3.md#s3-create-s3-bucket") to
  create an S3 bucket.

## Step 1: Create your AWS AppConfig

resources

In this section, you create the following resources:

- An _application_ in AWS AppConfig is a
  logical unit of code that provides capabilities for your customers.
- An _environment_ in AWS AppConfig is a
  logical deployment group of AppConfig targets, such as applications in a beta or
  production environment.
- A _configuration profile_ is a collection of
  settings that influence the behavior of your application. The configuration
  profile enables AWS AppConfig to access your configuration in its stored
  location.
- (Optional) A _deployment strategy_ in AWS
  AppConfig defines the behavior of a configuration deployment, such as what
  percentage of clients should receive the new deployed config at any given time
  during a deployment.

###### To create an application, environment, configuration profile, and deployment

strategy

1. Sign in to the AWS Management Console.
2. Use the steps in the following topics to create your resources in AWS
   AppConfig.
   - [Create
     an application](../../../systems-manager/latest/userguide/appconfig-creating-application.md "../../../systems-manager/latest/userguide/appconfig-creating-application.md").
   - [Create
     an environment](../../../systems-manager/latest/userguide/appconfig-creating-environment.md "../../../systems-manager/latest/userguide/appconfig-creating-environment.md").
   - [Create an AWS CodePipeline configuration profile](../../../systems-manager/latest/userguide/appconfig-creating-configuration-and-profile.md "../../../systems-manager/latest/userguide/appconfig-creating-configuration-and-profile.md").
   - (Optional) [Choose a predefined deployment strategy or create your
     own](../../../systems-manager/latest/userguide/appconfig-creating-deployment-strategy.md "../../../systems-manager/latest/userguide/appconfig-creating-deployment-strategy.md").

## Step 2: Upload files to your S3 source

bucket

In this section, create your configuration file or files. Then zip and push your
source files to the bucket that the pipeline uses for your source stage.

###### To create configuration files

1. Create a `configuration.json` file for each configuration
   in each Region. Include the following contents:

```
Hello World!
```

2. Use the following steps to zip and upload your configuration files.

###### To zip and upload source files

1. Create a .zip file with your files and name the .zip file
   `configuration-files.zip`. As an example, your .zip file
   can use the following structure:

```
.
└── appconfig-configurations
    └── MyConfigurations
        ├── us-east-1
        │   └── configuration.json
        └── us-west-2
            └── configuration.json
```

2. In the Amazon S3 console for your bucket, choose **Upload**, and follow the instructions to upload your .zip
   file.

## Step 3: Create your pipeline

In this section, you create a pipeline with the following actions:

- A source stage with an Amazon S3 action where the source artifacts are the files
  for your configuration.
- A deployment stage with an AppConfig deployment action.

###### To create a pipeline with the wizard

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").
2. On the **Welcome** page, **Getting started**
   page, or the **Pipelines** page, choose **Create
   pipeline**.
3. On the **Step 1: Choose creation option** page, under
   **Creation options**, choose the **Build custom
   pipeline** option. Choose **Next**.
4. In **Step 2: Choose pipeline settings**, in
   **Pipeline name**, enter
   `MyAppConfigPipeline`.
5. CodePipeline provides V1 and V2 type pipelines, which differ in characteristics and
   price. The V2 type is the only type you can choose in the console. For more
   information, see [pipeline types](pipeline-types-planning.md "pipeline-types-planning.md"). For information about pricing for CodePipeline, see [Pricing](https://aws.amazon.com/codepipeline/pricing/ "https://aws.amazon.com/codepipeline/pricing/").
6. In **Service role**, choose **New service
   role** to allow CodePipeline to create a service role in IAM.
7. Leave the settings under **Advanced settings** at their
   defaults, and then choose **Next**.
8. In **Step 3: Add source stage**, in **Source
   provider**, choose **Amazon S3**. In
   **Bucket**, choose the name of your S3 source bucket.

In **S3 object key**, enter the name of your .zip
file: `configuration-files.zip`.

Choose **Next**. 9. In **Step 4: Add build stage**, choose **Skip build
stage**, and then accept the warning message by choosing
**Skip** again.

Choose **Next**. 10. In **Step 5: Add test stage**, choose **Skip test
stage**, and then accept the warning message by choosing
**Skip** again.

Choose **Next**. 11. In **Step 6: Add deploy stage**:

    1. In **Deploy provider**, choose **AWS
     AppConfig**.
    2. In **Application**, choose the name of the
     application you created in AWS AppConfig. The field shows the ID for
     your application.
    3. In **Environment**, choose the name of the
     environment you created in AWS AppConfig. The field shows the ID for
     your environment.
    4. In **Configuration profile**, choose the name of the
     configuration profile you created in AWS AppConfig. The field shows
     the ID for your configuration profile.
    5. In **Deployment strategy**, choose the name of your
     deployment strategy. This can be either a deployment strategy you
     created in AppConfig or one you have chosen from predefined deployment
     strategies in AppConfig. The field shows the ID for your deployment
     strategy.
    6. In **Input artifact configuration path**, enter the
     file path. Make sure that your input artifact configuration path matches
     the directory structure in your S3 bucket .zip file. For this example,
     enter the following file path:
     `appconfig-configurations/MyConfigurations/us-west-2/configuration.json`.
    7. Choose **Next**.

12. In **Step 7: Review**, review the information, and then
    choose **Create pipeline**.

## Step 4: Make a change to any source file

and verify deployment

Make a change to your source files and upload the change to your bucket. This triggers
your pipeline to run. Verify that your configuration is available by viewing the
version.
