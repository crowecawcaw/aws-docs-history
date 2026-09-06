

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Choose an AWS Migration Hub home Region
<a name="select-home-region"></a>

When you first use the AWS Migration Hub console, choose a Migration Hub home Region. If you don't choose a home Region, you’ll be prompted to choose one before you can perform any write action from the console, AWS SDKs, or AWS CLI. 

The Region that you choose to set as the home Region must be one of the AWS Regions supported by AWS Migration Hub. For a list of the supported Regions, see [AWS Migration Hub Service endpoints](https://docs.aws.amazon.com/general/latest/gr/migrationhubn.html#migrationhub-region#migrationhub-region) in the *AWS General Reference*. 

You can choose the home Region from the Migration Hub console or by using the Home Region API. For information about using the API, see [Working with the AWS Migration Hub home Region APIs](home-region.md#using-migration-hub-apis). The following procedure describes how to choose the home region by using the console. 

**To choose your home Region using the console**

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the lower-section of the Migration Hub console navigation pane, choose **Settings**.

1. Under **Migration Home Region**, select your home Region.

1. Optionally, you can enable the console to automatically switch to your home Region the next time you sign in to the AWS Management Console.

1. Choose **Confirm Home Region** to set the home Region.

After you set your home Region, you can view it on the **Settings** page.

After your home Region is set, it can only be changed by contacting [AWS Support](https://aws.amazon.com/contact-us). For more information, see [Changing your AWS Migration Hub home Region](change-home-region.md).