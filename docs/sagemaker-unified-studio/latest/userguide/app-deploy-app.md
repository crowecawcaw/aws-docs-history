# Deploy an exported Amazon Bedrock app

The following instructions show you the steps you take to deploy a chat agent app
that you [export](app-export-chat-app.md "app-export-chat-app.md") from Amazon Bedrock in SageMaker Unified Studio. Make sure
to

###### Topics

- [Prerequisites for deploying an exported app](#app-deploy-app-prerequisites "#app-deploy-app-prerequisites")
- [Deploy the exported app](#app-deploy-app-deploy "#app-deploy-app-deploy")

## Prerequisites for deploying an exported app

Before you can deploy a chat agent app that you have exported, you must first do the following:

###### To prepare for app deployment

1. Install the latest version of the AWS CLI on your local machine by following the instructions at
   [Install or
   update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Set up AWS credentials for the AWS CLI on your local machine by following
   the instructions at [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md"). The credentials that the deployment
   script uses will follow the [order of precedence](../../../cli/latest/userguide/cli-chap-configure.md#configure-precedence "../../../cli/latest/userguide/cli-chap-configure.md#configure-precedence").
3. (Optional) Using the AWS account that you set up in step 2, create an
   AWS KMS key for app export by following the instructions at [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
   The key must be tagged with key `EnableBedrock` and a value of `true`. The key
   must also have a key policy that allows it to be used for encryption of your
   chat agent app resources. You may use the suggested policy declared in the
   `kms-key-policy.json` file of your zip package.
4. Create an Amazon S3 bucket to hold the app files that you export by following
   the instructions at [Creating a
   bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). Make sure the bucket is in the same AWS Region as the app
   that you are deploying.
5. Create an IAM role that includes the policies from
   `provisioning-inline-policy.json`. For information about creating a role, see
   [IAM role
   creation](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").
6. If your app includes a Knowledge Base, copy the data source file to a
   folder named `data/` in the Amazon S3 bucket that you created in step
7. If your app uses a document as a datasource, you supply a list of
   datasource files to the deployment script. For more information, see [Deploy the exported app](#app-deploy-app-deploy "#app-deploy-app-deploy").
8. If your app calls a function that requires authorization,
   update the function environment secret in Amazon SageMaker AI to the authorization
   method that your function uses. Run the following command:

```
aws secretsmanager update-secret \
  --secret-id br-studio/`function-name`-`export-environment-id` \
  --secret-string '`secret-value`'
```

To get the `function-name` and `export-environment-id` values, open the _amazon-bedrock-ide-app-stack-`nnnn`.json_ file from
the files that you exported in [Export your Amazon Bedrock app](app-export-chat-app.md "app-export-chat-app.md"). The values
are in the `FunctionsStack0` JSON object.

Replace the following values:

    * `function-name` — to the value of the
     `functionName` field in the
     `FunctionsStack0` JSON object.
    * `export-environment-id` — to the value of the
     `exportAppInstanceId` field in the
     `FunctionsStack0` JSON object.
    * `secret-value` — to the intended value to be
     used for authentication. You specified the authentication type when
     you [created the
     function component](creating-a-function-component.md "creating-a-function-component.md"). Use the authentication values that
     you specified to complete the `secret-value`.


     If the function requires API Keys, the syntax of
     `secret-value` should be:
     `{"`key-name-1`":"`key-value-1`","`key-name-2`":"`key-value-2`"}`



    If the function requires Basic authentication, the syntax of
     `secret-value` should be:
     `{"___AuthType___":"BASIC",
     "username":"`username-value`",
     "password":"`password-value`"}`



    If the function requires Bearer token authentication, the syntax
     of `secret-value` should be:
     `{"___AuthType___":"BEARER",
     "tokenValue":"`token-value`"}`

8. Next step: [Deploy the exported app](#app-deploy-app-deploy "#app-deploy-app-deploy").

## Deploy the exported app

Before deploying your chat agent app, be sure to do the [prerequisite steps](#app-deploy-app-prerequisites "#app-deploy-app-prerequisites").

Deploying a chat agent app deploys the AWS infrastructure files that you need to run
the app in AWS.

###### To deploy an exported app

1.  At the command prompt, do the following:
    1. Navigate to the zip file that you exported from Amazon Bedrock in SageMaker Unified Studio.
    2. Assume the role of the AWS that you created in step 3 of [Prerequisites for deploying an exported app](#app-deploy-app-prerequisites "#app-deploy-app-prerequisites").
    3. Use the following command to make sure the deployment script (`deployApp.sh`) is executable:

    ```
    chmod +x deployApp.sh
    ```

    4. Run the deployment script with the following command:

    ```
    ./deployApp.sh \
        [--awsRegion=`value`] \
        [--s3BucketName=`value`] \
        [--assetsS3Path=`value`] \
        [--kmsKeyArn=`value`] \
        [--dataFiles=`value`]

    ```

    Replace the following values:

        * `awsRegion` — with the AWS Region that
         you want to deploy the app to. Amazon Bedrock must be available in
         the Region you use. For more information, see [Supported AWS Regions](../../../bedrock/latest/userguide/bedrock-regions.md "../../../bedrock/latest/userguide/bedrock-regions.md").
        * `s3BucketName` — With the Amazon S3 bucket
         that you created in step 5 of [Prerequisites for deploying an exported app](#app-deploy-app-prerequisites "#app-deploy-app-prerequisites"). The
         deployment store the CFN templates and application data
         files in this bucket.
        * `assetsS3Path` — (Optional) With the
         path in `s3BucketName` that you want deployment
         to store application files to.
        * `kmsKeyArn` — (Optional) with the ARN of
         the KMS Key that you created in step 3 of [Prerequisites for deploying an exported app](#app-deploy-app-prerequisites "#app-deploy-app-prerequisites").
        * `dataFiles` — With a comma-separated
         list of data source file paths. Required for apps that use a
         document data source.

    For example, if you have a chat agent app with a single document
    as a data source, and you want to deploy the app with encryption,
    you can use the following command.

    ```
    ./deployApp.sh \
        --awsRegion=us-east-1 \
        --s3BucketName=my-s3-bucket-name-for-exported-chat-apps \
        --assetsS3Path=my-prod-folder/my-chat-app \
        --kmsKeyArn=arn:aws:kms:us-east-1:111122223333:key/11111111-2222-3333-4444-555555555555 \
        --dataFiles=my-data-source.pdf
    ```

2.  (Optional) Monitor the deployment in the AWS CloudFormation console.
3.  Note the output from the script. You need it to run the chat agent app.
    It should be similar to: `node amazon-bedrock-ide-app.mjs
--question="`prompt`"
--region="`AWS Region`"`.

When you run the app, specify the following parameters:

    * `question` – The prompt that you want to start
     the app with.
    * `region` – The AWS Region that you deployed the
     app to. Use the value of `awsRegion` that you specified
     in step 1c.

For example, `node amazon-bedrock-ide-app.mjs --question="Tell me about my documents" --region="us-east-1"` 4. Next step: [Run a deployed Amazon Bedrock app](app-run-app.md "app-run-app.md").
