

# Creating a data subscription

A data subscription delivers a dataset to a bucket that you configure, so you can access the dataset in your own account. Use the following procedure to create data subscriptions.

Your bucket policy and key policy must allow AWS Partner Central to write encrypted files. Complete this before you finish setup. If either policy is missing, you can't create the subscription; check the console for which policy to fix. The bucket must be in the same AWS Region as the key.

**Important**  
Standard Amazon S3 storage and request charges apply to the files that AWS Partner Central delivers to your bucket. Because each file is encrypted with your AWS KMS key, AWS KMS charges apply when you read the files. For more information about Amazon S3 and AWS KMS pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) and [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

**To create a data subscription**

1. Sign in to AWS Partner Central.

1. Open the [AWS Partner Central Data sharing page](https://console.aws.amazon.com/partnercentral/data-sharing).

1. Choose **Create data subscription**.

1. For **Configure destination**, enter the bucket name, the AWS Region, and the AWS AWS KMS key Amazon Resource Name (ARN).

1. Under **Grant access**, copy the bucket policy and the key policy that the console shows, then apply them. They are the policies in [Bucket policy](data-subscriptions-prerequisites.md#data-subscriptions-bucket-policy) and [Key policy](data-subscriptions-prerequisites.md#data-subscriptions-key-policy), filled in with your values.

1. For **Choose datasets**, select one or more datasets.

1. For **Review and create**, review the destination and the datasets, and then choose **Create data subscription**. If you chose more than one dataset, the button is **Create data subscriptions**.

Check the result for each dataset. If a dataset shows an access failure, fix the policy that the message names, choose **Previous**, and then try again. For more information about the policies, see [Prerequisites](data-subscriptions-prerequisites.md).

After setup completes, delivery starts automatically. Expect the first file within 24 hours. The first delivery fills in the dataset's available history, and the **Data delivery status** column shows how many days are done.