**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Removing AWS Shield Advanced protection from an AWS resource

You can remove AWS Shield Advanced protection from any of your AWS resources at any time.

###### Important

Deleting an AWS resource doesn't remove the resource from AWS Shield Advanced. You must also remove
the protection on the resource from AWS Shield Advanced, as described in this procedure.

###### Remove AWS Shield Advanced protection from an AWS resource

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the AWS Shield navigation pane, choose **Protected resources**.
3. In the **Protections** tab, select the resources whose protections you want to remove.
4. Choose **Delete protections**.
   1. If you have an Amazon CloudWatch alarm configured for a protection, you are
      given the option to delete the alarm along with the protection. If you
      choose not to delete the alarm at this point, you can instead delete it
      later using the CloudWatch console.###### Note

For protections that have an Amazon Route 53 health check configured, if you add the
protection again later, the protection still includes the health check.
The preceding steps remove AWS Shield Advanced protection from specific AWS resources. They
don't cancel your AWS Shield Advanced subscription. You will continue to be charged for the
service. For information about your AWS Shield Advanced subscription, contact the
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Removing a CloudWatch alarm from your Shield Advanced

protections

To remove a CloudWatch alarm from your Shield Advanced protections, do one of the following:

- Delete the protection as described in [Removing AWS Shield Advanced protection from an AWS resource](remove-protection.md "remove-protection.md"). Be sure to select the check box next to
  **Also delete related DDoSDetection alarm**.
- Delete the alarm using the CloudWatch console. The name of the alarm to delete
  starts with **DDoSDetectedAlarmForProtection**.
