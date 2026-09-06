

# Giving AWS Marketplace access to your AMI
<a name="single-ami-marketplace-ami-access"></a>

When you create a request that includes adding a new Amazon Machine Image (AMI) to AWS Marketplace, the AMI must be copied into the AWS Marketplace system and then scanned for security issues. You must give AWS Marketplace access to the AMI by creating an AWS Identity and Access Management (IAM) role with permissions to perform actions on your AMI and a trust policy that allows AWS Marketplace to assume the role. You only need to create the IAM role once. The following procedure shows you how to create a role for AWS Marketplace assets ingestion that gives AWS Marketplace access to your AMI.

**To create a role for AWS Marketplace AMI assets ingestion**

1. Sign in to the AWS Management Console, open the IAM console and go to the [Roles page](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles).

1. Select **Create role**.

1. On the **Create role** page, make the following selections:
   + **Select type of trusted entity** – Choose **AWS Service**.
   + **Choose a use case** – Choose **AWS Marketplace**.
   + **Select your use case** – Choose **Marketplace – AMI Assets Ingestion**. 
   + To move to the next page, select **Next: Permissions**.

1. Select the **AWSMarketplaceAmiIngestion** policy. Add a permissions boundary if required, and then select **Next: Tags** to continue.
**Note**  
You can use permissions boundaries to limit the access that you give AWS Marketplace with this role. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *AWS Identity and Access Management User Guide*.

1. To continue, select **Next: Review**.

1. Provide a name for the role, and select **Create role**.

1. You should see "The role {{rolename}} has been created" at the top of the page, and the role should appear in the list of roles.

On this page, when you select the role that you just created, you can see its ARN in the form *arn:aws:iam::123456789012:role/exampleRole*. Use the ARN for the **IAM access role ARN** when you create change requests, for example, when [adding a new version](single-ami-versions.md#single-ami-adding-version) to your product.

## Giving AWS Marketplace access to your FPGA images
<a name="single-ami-marketplace-afi-access"></a>

If your AMI includes FPGA images (AFIs), you must also grant AWS Marketplace additional permissions to access and manage these FPGA images. In addition to the **AWSMarketplaceAmiIngestion** policy, you need to create an inline policy that allows AWS Marketplace to perform actions on your FPGA images.

**To add FPGA image permissions to your AWS Marketplace AMI assets ingestion role**

1. Sign in to the AWS Management Console, open the IAM console and go to the [Roles page](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles).

1. Select the role that you created for AWS Marketplace AMI assets ingestion.

1. On the role details page, select the **Permissions** tab, and then select **Add inline policy**.

1. Select the **JSON** tab and enter the following policy:

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[
         {
            "Effect":"Allow",
            "Action":[
               "ec2:DescribeFpgaImages",
               "ec2:DescribeFpgaImageAttribute",
               "ec2:CopyFpgaImage",
               "ec2:ModifyFpgaImageAttribute"
            ],
            "Resource":"*"
         }
      ]
   }
   ```

------

1. Select **Review policy**.

1. Provide a name for the policy, such as **AWSMarketplaceAfiIngestion**, and then select **Create policy**.

After you add this inline policy, AWS Marketplace will have the necessary permissions to access and manage your FPGA images during the ingestion and scanning process.