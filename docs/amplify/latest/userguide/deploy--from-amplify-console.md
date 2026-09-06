

# Deploying a static website from S3 using the Amplify console
<a name="deploy--from-amplify-console"></a>

Use the following instructions to deploy a new static website from an Amazon S3 general purpose bucket using the Amplify console.

**To deploy a static website from an Amazon S3 general purpose bucket using the Amplify console**

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose **Create new app**.

1. On the **Start building with Amplify** page, choose **Deploy without Git**.

1. Choose **Next**.

1. On the **Start a manual deployment** page, do the following.

   1. For **App name**, enter the name of your app.

   1. For **Branch name**, enter the name of the branch to deploy.

1. For **Method**, choose **Amazon S3**.

1. For the **S3 location of objects to host**, choose **Browse**. Select the Amazon S3 general purpose bucket to use, then select **Choose prefix**.

1. Choose **Save and deploy**.