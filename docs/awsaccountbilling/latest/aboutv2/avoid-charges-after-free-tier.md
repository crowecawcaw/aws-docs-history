# Avoiding unexpected charges after Free Tier

###### Note

**_This section only applies to new AWS customers who created AWS accounts before July 15, 2025. If you created your account after July 15, 2025, see [Explore AWS services with AWS Free Tier](free-tier.md "free-tier.md")._**

Your eligibility for the 12 month free service offering AWS Free Tier expires 12 months
after you first activate your AWS account. You can’t extend your Free Tier eligibility
after this time.

###### Note

You can continue to use Always Free offers, even after your AWS Free Tier eligibility
expires. To learn more about available Always Free offers, see [AWS Free Tier](http://aws.amazon.com/free/ "http://aws.amazon.com/free/").

As the expiration date of your AWS Free Tier eligibility approaches, we recommend that
you shut down or delete any resources that you don't need. After your eligibility
expires, you’re charged at the standard AWS billing rates for usage.

For short-term trials, there are no expiration notification for these services. You
will receive free tier alerts during the trial period only. To avoid unexpected costs in
a short-term trial, you must turn off these resources before the end of the trial
period.

Even if you aren’t regularly signing in to your account, you might have active
resources running. Use the following procedure to identify your account’s active
resources.

###### Note

You can also use the `GetFreeTierUsage` API operation to get your free
tier usage. For more information about the Free Tier API, see the [AWS Billing and Cost Management API Reference](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md").

###### To identify your active resources by using

AWS Billing

1. Sign in to the AWS Management Console and open the Billing console at
   [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/").
2. On the navigation pane, choose **Bills** .
3. On the **Charges by service** tab, choose **Expand
   all**.
4. Review the list to find the services with active resources and by
   AWS Region, and the charges for each resource.

###### To identify your active resources by using

AWS Cost Explorer

1. Sign in to the AWS Management Console and open the AWS Cost Management at
   [https://console.aws.amazon.com/costmanagement/home](https://console.aws.amazon.com/costmanagement/home "https://console.aws.amazon.com/costmanagement/home").
2. On the navigation pane, choose **Cost Explorer**.
3. On the **Cost and usage graph**, note the services and
   AWS Regions with resources that you don't need. For instructions on how to
   shut down or delete those resources, see the documentation for that
   service.

For example, to terminate an Amazon EC2 Linux instance, see the [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md").

###### Tip

You might decide to close your AWS account. For more information and important
considerations, see [Close your account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md") in the _AWS Account Management Reference Guide_.
