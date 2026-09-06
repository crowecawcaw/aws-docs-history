

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Working with blueprint tooling and CLI
<a name="bp-cli"></a>

The [blueprint CLI](https://www.npmjs.com/package/@amazon-codecatalyst/blueprint-util.cli) provides tooling to manage and work with your custom blueprints.

**Topics**
+ [Working with blueprint tooling](#working-with-bp-cli)
+ [Image upload tool](#image-upload-tool)

## Working with blueprint tooling
<a name="working-with-bp-cli"></a>

**To work with the blueprint tools**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Resume your Dev Environment. For more information, see [Resuming a Dev Environment](devenvironment-resume.md).

   If you don't have a Dev Environment, you must first create one. For more information, see [Creating a Dev Environment](devenvironment-create.md).

1. In a working terminal, run the following the command to install the blueprint CLI:

   ```
   npm install -g @amazon-codecatalyst/blueprint-util.cli
   ```

1. In the `blueprint.ts` file, import the tools you want to use in the following format:

   ```
   import { {{<tooling-function-name>}} } from '@amazon-codecatalyst/blueprint-util.cli/lib/{{<tooling-folder-name>}}/{{<tooling-file-name>}};
   ```
**Tip**  
You can to the [`CodeCatalyst blueprints GitHub repository`](https://github.com/aws/codecatalyst-blueprints/tree/main/packages/utils/blueprint-cli) to find the name of the tooling you want to use.

   **If you want to use the image uploading tool, add the following to your script:**

   ```
   import { uploadImagePublicly } from '@amazon-codecatalyst/blueprint-util.cli/lib/image-upload-tool/upload-image-to-aws';
   ```

   **Examples**
   + **If you want to use the publishing function, add the following to your script:**

     ```
     import { publish } from '@amazon-codecatalyst/blueprint-util.cli/lib/publish/publish';
     ```
   + **If you want to use the image uploading tool, add the following to your script:**

     ```
     import { uploadImagePublicly } from '@amazon-codecatalyst/blueprint-util.cli/lib/image-upload-tool/upload-image-to-aws';
     ```

1. Call the function.

   **Examples:**
   + **If you want to use the publishing function, add the following to your script:**

     ```
     await publish(logger, config.publishEndpoint, {{{<your publishing options>}}});
     ```
   + **If you want to use the image uploading tool, add the following to your script:**

     ```
     const {imageUrl, imageName} = await uploadImagePublicly(logger, 'path/to/image'));
     ```

## Image upload tool
<a name="image-upload-tool"></a>

The image upload tool provides you with the ability to upload your own image to an S3 bucket in your AWS account and then distribute that image publicly behind CloudFront. The tool takes an image path in the local storage (and optional bucket name) as input, and returns the URL to the image that is publicly available. For more information, see [What is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) and [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

**To work with the image upload tool**

1. Clone the [open-source blueprints GitHub repository](https://github.com/aws/codecatalyst-blueprints) that provides access to the blueprints SDK and sample blueprints. In a working terminal, run the following command:

   ```
   git clone https://github.com/aws/codecatalyst-blueprints.git
   ```

1. Run the following command to navigate to the blueprints GitHub repository:

   ```
   cd codecatalyst-blueprints
   ```

1. Run the following command to install dependencies:

   ```
   yarn && yarn build
   ```

1. Run the following command to make sure the latest blueprint CLI version is installed:

   ```
   yarn upgrade @amazon-codecatalyst/blueprint-util.cli
   ```

1. Log in to the AWS account with the S3 bucket you want to upload your image to. For more information, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html), and [Sign in through the AWS Command Line Interface](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html).

1. Run the following command from the root of your CodeCatalyst repository to navigate to the directory with the blueprint CLI:

   ```
   cd packages/utils/blueprint-cli
   ```

1. Run the following command to upload your image to an S3 bucket:

   ```
   yarn blueprint upload-image-public {{<./path/to/your/image>}} 
         {{<optional:optional-bucket-name>}}
   ```

A URL to your image is generated. The URL won’t be available immediately since it requires some time for the CloudFront distribution to be deployed. Check the distribution status to get the latest deployment status. For more information, see [Working with distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html).