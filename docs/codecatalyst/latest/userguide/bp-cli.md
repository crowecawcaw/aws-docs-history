Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Working with blueprint tooling and CLI

The [blueprint CLI](https://www.npmjs.com/package/@amazon-codecatalyst/blueprint-util.cli "https://www.npmjs.com/package/@amazon-codecatalyst/blueprint-util.cli")
provides tooling to manage and work with your custom blueprints.

###### Topics

- [Working with blueprint tooling](#working-with-bp-cli "#working-with-bp-cli")
- [Image upload tool](#image-upload-tool "#image-upload-tool")

## Working with blueprint tooling

**To work with the blueprint tools**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Resume your Dev Environment. For more information, see [Resuming a Dev Environment](devenvironment-resume.md "devenvironment-resume.md").

If you don't have a Dev Environment, you must first create one. For more information, see
[Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md"). 3. In a working terminal, run the following the command to install the blueprint CLI:

```
npm install -g @amazon-codecatalyst/blueprint-util.cli
```

4. In the `blueprint.ts` file, import the tools you want to use in the following format:

```
import { `<tooling-function-name>` } from '@amazon-codecatalyst/blueprint-util.cli/lib/`<tooling-folder-name>`/`<tooling-file-name>`;
```

###### Tip

You can to the [`CodeCatalyst 
 blueprints GitHub repository`](https://github.com/aws/codecatalyst-blueprints/tree/main/packages/utils/blueprint-cli "https://github.com/aws/codecatalyst-blueprints/tree/main/packages/utils/blueprint-cli") to find the name of the tooling you want to use.

**If you want to use the image uploading tool, add the following to your script:**

```
import { uploadImagePublicly } from '@amazon-codecatalyst/blueprint-util.cli/lib/image-upload-tool/upload-image-to-aws';
```

**Examples**

    * **If you want to use the publishing function, add the following to your script:**



    ```
    import { publish } from '@amazon-codecatalyst/blueprint-util.cli/lib/publish/publish';
    ```
    * **If you want to use the image uploading tool, add the following to your script:**



    ```
    import { uploadImagePublicly } from '@amazon-codecatalyst/blueprint-util.cli/lib/image-upload-tool/upload-image-to-aws';
    ```

5. Call the function.

**Examples:**

    * **If you want to use the publishing function, add the following to your script:**



    ```
    await publish(logger, config.publishEndpoint, {`<your publishing options>`});
    ```
    * **If you want to use the image uploading tool, add the following to your script:**



    ```
    const {imageUrl, imageName} = await uploadImagePublicly(logger, 'path/to/image'));
    ```

## Image upload tool

The image upload tool provides you with the ability to upload your own image to an S3 bucket in your AWS account
and then distribute that image publicly behind CloudFront. The tool takes an image path in the local storage (and
optional bucket name) as input, and returns the URL to the image that is publicly available. For more information, see
[What is Amazon
CloudFront?](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md") and [What is Amazon
S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")

**To work with the image upload tool**

1. Clone the [open-source
   blueprints GitHub repository](https://github.com/aws/codecatalyst-blueprints "https://github.com/aws/codecatalyst-blueprints") that provides access to the blueprints SDK and sample blueprints. In a working
   terminal, run the following command:

```
git clone https://github.com/aws/codecatalyst-blueprints.git
```

2. Run the following command to navigate to the blueprints GitHub repository:

```
cd codecatalyst-blueprints
```

3. Run the following command to install dependencies:

```
yarn && yarn build
```

4. Run the following command to make sure the latest blueprint CLI version is installed:

```
yarn upgrade @amazon-codecatalyst/blueprint-util.cli
```

5. Log in to the AWS account with the S3 bucket you want to upload your image to. For more information, see
   [Configure the AWS
   CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md"), and [Sign in
   through the AWS Command Line Interface](../../../signin/latest/userguide/command-line-sign-in.md "../../../signin/latest/userguide/command-line-sign-in.md").
6. Run the following command from the root of your CodeCatalyst repository to navigate to the directory with the blueprint
   CLI:

```
cd packages/utils/blueprint-cli
```

7. Run the following command to upload your image to an S3 bucket:

```
yarn blueprint upload-image-public `<./path/to/your/image>`
      `<optional:optional-bucket-name>`
```

A URL to your image is generated. The URL won’t be available immediately since it requires some time for the CloudFront
distribution to be deployed. Check the distribution status to get the latest deployment status. For more information, see
[Working with
distributions](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.md").
