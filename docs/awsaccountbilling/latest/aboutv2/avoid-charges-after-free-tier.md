

# Avoiding unexpected charges after Free Tier
<a name="avoid-charges-after-free-tier"></a>

Your eligibility for the AWS Free Tier expires 6 months or when your credits are fully used - whichever occurs first. You can't extend your Free Tier eligibility after this time.

**Note**  
You can continue to use Always Free offers, even after your AWS Free Tier eligibility expires. To learn more about available Always Free offers, see [AWS Free Tier](http://aws.amazon.com/free/).

As the expiration date of your AWS Free Tier eligibility approaches, shut down or delete any resources that you don't need. After your eligibility expires, you're charged at the standard AWS billing rates for usage.

Even if you aren't regularly signing in to your account, you might have active resources running. Use the following procedure to identify your account's active resources.

**Note**  
You can also use the `GetFreeTierUsage` API operation to get your free tier usage. For more information about the Free Tier API, see the [AWS Billing and Cost Management API Reference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.html).<a name="identify-active-resources-billing"></a>

**To identify your active resources by using AWS Billing**

1. Sign in to the AWS Management Console and open the Billing console at [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/).

1. On the navigation pane, choose **Bills** .

1. On the **Charges by service** tab, choose **Expand all**.

1. Review the list to find the services with active resources and by AWS Region, and the charges for each resource.<a name="identify-active-resources"></a>

**To identify your active resources by using AWS Cost Explorer**

1. Sign in to the AWS Management Console and open the AWS Cost Management at [https://console.aws.amazon.com/costmanagement/home](https://console.aws.amazon.com/costmanagement/home).

1.  On the navigation pane, choose **Cost Explorer**.

1. On the **Cost and usage graph**, note the services and AWS Regions with resources that you don't need. For instructions on how to shut down or delete those resources, see the documentation for that service.

   For example, to terminate an Amazon EC2 Linux instance, see the [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html).

**Tip**  
You might decide to close your AWS account. For more information and important considerations, see [Close your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html) in the *AWS Account Management Reference Guide*.