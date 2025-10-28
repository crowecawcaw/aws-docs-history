# Step 3: Create the console bucket

You use an Amazon Rekognition Custom Labels project to create and manage your models. When you first open
the Amazon Rekognition Custom Labels console in a new AWS Region, Amazon Rekognition Custom Labels creates an Amazon S3 bucket (console
bucket) to store your projects. You should note the console bucket name somewhere where
you can refer to it later because you might need to use the bucket name in AWS SDK
operations or console tasks, such as creating a dataset.

The format of the bucket name is
`custom-labels-console`-`<region>`-`<random
 value>`. The random value ensures that there isn't a collision between
bucket names.

###### To create the console bucket

1. Ensure that the user has the correct permissions.
   For more information, see [Allowing console access](su-console-policy.md#su-console-access "su-console-policy.md#su-console-access").
2. Sign in to the AWS Management Console and open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
3. Choose **Get started**.
4. If this is the first time that you've opened the console in the current AWS Region, do the
   following in the **First Time Set Up** dialog box:
   1. Copy down the name of the Amazon S3 bucket that's shown. You'll need this information later.
   2. Choose **Create S3 bucket** to let Amazon Rekognition Custom Labels create an Amazon S3 bucket (console bucket) on your behalf.

5. Close the browser window.
