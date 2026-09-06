

# Uninstall the product
<a name="uninstall-the-product"></a>

You can uninstall the Research and Engineering Studio on AWS product from the AWS Management Console or by using the AWS Command Line Interface. You must manually delete the Amazon Simple Storage Service (Amazon S3) buckets created by this product. This product does not automatically delete <EnvironmentName>-shared-storage-security-group in case you have stored data to retain. 

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. On the **Stacks** page, select this product’s installation stack. 

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [ What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available and configured to the administrator account in the Region where the product was deployed, run the following command. 

```
$ aws cloudformation delete-stack --stack-name {{<RES-stack-name>}}
```

## Deleting the shared-storage-security-group
<a name="deleting-security-group"></a>

**Warning**  
The product retains this file system by default to protect against unintentional data loss. If you choose to delete the security group and associated file systems, any data retained within those systems will be permanently deleted. We recommend backing up data or reassigning the data to a new security group.

1. Sign in to the AWS Management Console and open the Amazon EFS console at [ https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. Delete all file systems associated with `{{<RES-stack-name>}}-shared-storage-security-group`. Alternatively, you may reassign these file systems to another security group to maintain the data.

1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Delete the `{{<RES-stack-name>}}-shared-storage-security-group`. 

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This product is configured to retain the product-created Amazon S3 bucket (for deploying in an opt-in Region) if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the product, you can manually delete this S3 bucket if you do not need to retain the data. Follow these steps to delete the Amazon S3 bucket.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Buckets** from the navigation pane.

1. Locate the `stack-name` S3 buckets.

1. Select each Amazon S3 bucket, then choose **Empty**. You must empty each bucket.

1. Select the S3 bucket and choose **Delete**.

To delete S3 buckets using AWS CLI, run the following command: 

```
$ aws s3 rb s3://<bucket-name> --force
```

**Note**  
The `--force` command empties the bucket of its contents. 