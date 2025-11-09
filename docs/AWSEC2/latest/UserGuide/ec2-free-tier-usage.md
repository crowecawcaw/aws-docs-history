# Track your Free Tier usage for Amazon EC2

When you create your AWS account, you can get started with Amazon EC2 for free using the
[AWS Free Tier](https://aws.amazon.com/free "https://aws.amazon.com/free"). Your Free Tier benefits
are different depending on whether you created your account before July 15, 2025, or on
or after July 15, 2025. For more information, see [Explore AWS services with
AWS Free Tier](../../../awsaccountbilling/latest/aboutv2/free-tier.md "../../../awsaccountbilling/latest/aboutv2/free-tier.md") in the _AWS Billing User Guide_.

## Free Tier benefits before and after July

15, 2025

The following table compares your Free Tier benefits based on your AWS account
creation date:

| Free Tier benefit                                     | Account created before July 15, 2025                                                                                                                                             | Account created on or after July 15, 2025                                                                                                                                          |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instance types marked **Free tier<br>eligible**       | `t2.micro`, `t3.micro`                                                                                                                                                           | `t3.micro`, `t3.small`,<br>`t4g.micro`, `t4g.small`,<br>`c7i-flex.large`, `m7i-flex.large`                                                                                         |
| Amazon EBS volume types marked **Free tier eligible** | `standard`, `st1`, `sc1`,<br>`gp2`, and `gp3`                                                                                                                                    | `standard`, `st1`, `sc1`,<br>`gp2`, and `gp3`                                                                                                                                      |
| AMIs marked **Free tier eligible**                    | Check for AMIs marked **Free tier<br>eligible**.                                                                                                                                 | Check for AMIs marked **Free tier<br>eligible**.                                                                                                                                   |
| Usage limit                                           | Restricted to usage limits, after which you are billed<br>pay-as-you-go rates.                                                                                                   | Receive USD $100 sign-up credit and earn up to $100 in<br>additional credits.                                                                                                      |
| Free Tier duration                                    | Your Free Tier lasts for 12 months from the date you create your<br>account. During this time, if you exceed your Free Tier usage<br>limits, you are billed pay-as-you-go rates. | Your Free Tier lasts for 6 months from the date you created your<br>account, or when your credits are used up, whichever happens first.<br>You can't exceed your Free Tier limits. |

###### To list the instance types that are free tier eligible

Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command with the
`free-tier-eligible` filter.

```
aws ec2 describe-instance-types \
    --filters Name=free-tier-eligible,Values=true \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

###### To list the AMIs that are free tier eligible

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")
command with the `free-tier-eligible` filter.

```
aws ec2 describe-images \
    --filters Name=free-tier-eligible,Values=true \
    --query "Images[*].[ImageId]" \
    --output text | sort
```

## Track Free Tier usage for accounts

created before July 15, 2025

###### Note

**_This section only applies to Free Tier users who
created AWS accounts before July 15, 2025. If you created your account
on or after July 15, 2025, see [Tracking your AWS Free Tier usage](../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md "../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md") in the
AWS Billing User Guide._**

If you created your account before July 15, 2025, you can use Amazon EC2 without incurring
charges if you've been an AWS customer for less than 12 months and you stay within
the AWS Free Tier usage limits. It's important to track your Free Tier usage to
avoid billing surprises. If you exceed the Free Tier limits, you'll incur standard
pay-as-go charges. For more information, see [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

###### Note

If you've been an AWS customer for more than 12 months, you're no longer
eligible for Free Tier usage and you won't see the **EC2
Free Tier** box that is described in the following
procedure.

###### To track your Free Tier usage

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **EC2 Dashboard**.
3. Find the **EC2 Free Tier** box (at top right).

![The EC2 Free Tier box in the EC2 Dashboard.](images/ec2-free-tier-widget.png) 4. In the **EC2 Free Tier** box, check your Free Tier usage, as
follows:

    * Under **EC2 Free Tier offers in use**, take note of
     the warnings:




    	+ **End of month forecast** – This warns
    	 that you will incur charges this month if you continue with your
    	 current usage pattern.
    	+ **Exceeds Free Tier** – This warns
    	 that you've exceeded your Free Tier limits and you're already
    	 incurring charges.
    * Under **Offer usage (monthly)**, take note of your
     usage of Linux instances, Windows instances, and EBS storage. The
     percentage indicates how much of your Free Tier limits you've used this
     month. If you're at 100%, you will incur charges for further use.


    ###### Note

    This information appears only after you've created an instance.
     However, usage information is not updated in real time; it's updated
     three times a day.

5. To avoid incurring further charges, delete any resources that are either incurring charges
   now, or will incur charges if you exceed your Free Tier limit usage.
   - For the instructions to delete your instance, see [Terminate Amazon EC2 instances](terminating-instances.md "terminating-instances.md").
   - To check if you have resources in other Regions that might be incurring charges, in the
     **EC2 Free Tier** box, choose **View Global
     EC2 resources** to open the **EC2 Global
     View**. For more information, see [View resources across Regions using AWS Global
     View](global-view.md "global-view.md").

6. To view your resource usage for all AWS services under the AWS Free Tier,
   at the bottom of the **EC2 Free Tier** box, choose
   **View all AWS Free Tier offers**. For more information,
   see [Trying
   services using AWS Free Tier](../../../awsaccountbilling/latest/aboutv2/billing-free-tier.md "../../../awsaccountbilling/latest/aboutv2/billing-free-tier.md") in the _AWS
   Billing User Guide_.
