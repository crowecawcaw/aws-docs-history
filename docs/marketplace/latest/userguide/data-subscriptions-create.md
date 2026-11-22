

# Creating a data subscription

This procedure creates a data subscription that delivers a seller dataset from AWS Marketplace to an Amazon S3 bucket that you own. Use the following steps to create data subscriptions that deliver the datasets that you select to a bucket that you configure. Your bucket policy and key policy must allow AWS Marketplace to write encrypted files before you complete setup. If either policy is missing, the subscription isn't created and the console tells you which policy to fix.

**To create a data subscription**

1. Sign in to AWS Partner Central with the AWS account that holds your seller registration.

1. Open the AWS Partner Central [Data sharing](https://console.aws.amazon.com/partnercentral/data-sharing) page. You can also open the page from **Settings**.

1. Choose **Create data subscription**.

1. Configure the destination for the subscriptions.

   1. For **Configure destination**, enter the bucket name, the AWS Region, and the AWS KMS key ARN. The bucket must be in the same Region as the key.

   1. Under **Grant access**, copy the bucket policy and the key policy that the console shows. They are the policies in [Bucket policy](data-subscriptions-prerequisites.md#data-subscriptions-bucket-policy) and [Key policy](data-subscriptions-prerequisites.md#data-subscriptions-key-policy), filled in with your values.

   1. Apply the bucket policy to your bucket and the key policy to your key.

1. For **Choose datasets**, select one or more datasets. AWS Marketplace creates one subscription for each dataset that you choose. All of them deliver to the destination that you configured.

1. For **Review and create**, review the destination and the datasets, and then choose **Create data subscription**. If you chose more than one dataset, the button is **Create data subscriptions**.

1. Check the result for each dataset. If a dataset shows an access failure, fix the policy that the message names, choose **Previous**, and then try again. For more information about the policies, see [Prerequisites](data-subscriptions-prerequisites.md).

After setup completes, delivery starts automatically. Expect the first file within 24 hours. The first delivery fills in the dataset's available history, and the **Data delivery status** column shows how many days are done.