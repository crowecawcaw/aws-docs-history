# Switching your licenses

You can switch your existing operating system (OS) licenses to AWS Marketplace third-party
subscriptions without redeploying your Amazon EC2 instances. This reduces downtime and
eliminates the need to retest applications.

License switching allows you to convert your Amazon EC2 License Included (LI) operating
systems to third-party subscriptions available in AWS Marketplace. For more information about
license type conversions, see [License type
conversions in AWS License Manager](../../../license-manager/latest/userguide/license-conversion.md "../../../license-manager/latest/userguide/license-conversion.md"). After switching, you're billed separately for:

- Amazon EC2 infrastructure costs (through Amazon Elastic Compute Cloud)
- OS software costs (through AWS Marketplace)
  This feature currently supports Red Hat Enterprise Linux (RHEL) and RHEL for SAP
  with High Availability and Update Services products.

## Benefits

- Continue using your existing instances without redeployment
- Minimize downtime during license changes
- Access private offers for OS subscriptions through AWS Marketplace
- Separate infrastructure and software billing for better cost tracking

## Prerequisites

Before switching your licenses, ensure you have:

- An active subscription to the target AWS Marketplace product
- Permissions to use AWS License Manager
- The ability to stop your Amazon EC2 instances temporarily

## Switching your license

###### To switch your license:

1. Sign in to the AWS Management Console and open the AWS License Manager console at:
   [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/")
2. In the navigation pane, choose **License type conversions**.
3. Choose **Create license type conversion**.
4. Stop the instances you plan to switch to a new license.
5. Select the source license type.
6. Select the destination license type from AWS Marketplace.
7. If you don't have an existing subscription to the selected AWS Marketplace product,
   follow the prompts to create one.
8. Review your selections and choose **Create**.
9. After the license switch completes, restart your instances.

For detailed steps on converting Linux license types, see [Convert a
license type for Linux in AWS License Manager](../../../license-manager/latest/userguide/conversion-procedures-linux.md "../../../license-manager/latest/userguide/conversion-procedures-linux.md").

## Billing changes

After switching your license:

- Your Amazon EC2 instance charges no longer include the operating system cost.
- You're billed separately for the AWS Marketplace subscription.
- You can view your AWS Marketplace charges in your AWS bill under the
  **AWS Marketplace** section.

## Considerations and limitations

- You must stop your instances during the license switching process.
- License switching is only available for supported RHEL products.
- You must have an active subscription to the target AWS Marketplace product.

## Troubleshooting

If you encounter issues when switching licenses:

- Verify that your instance is in a stopped state.
- Confirm that you have an active subscription to the target AWS Marketplace product.
- Check that your IAM permissions include access to both AWS License Manager and the
  Amazon EC2 instances.

For additional troubleshooting guidance, see [Troubleshooting
license type conversion in AWS License Manager](../../../license-manager/latest/userguide/conversion-troubleshooting.md "../../../license-manager/latest/userguide/conversion-troubleshooting.md"). For additional assistance, contact
AWS Support.
