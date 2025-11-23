# Create a recurring "Patch Tuesday" maintenance window from the AMS console (recommended)

Microsoft releases patches for its operating systems on the second Tuesday of each month, also know as Patch Tuesday. It is common
to schedule patching for both Windows and Linux instances relative to Patch Tuesday. To schedule recurring patch maintenance windows on
the first or second weekends after Patch Tuesday, visit the AMS console and follow these steps:

1. Provide a name for your patch maintenance window.
2. [optional] Provide a description for the patch maintenance window.
3. Select a day relative to Patch Tuesday.
4. Enter a time for the patch maintenance window to start in hh:mm. For example, midnight is **00:00** and 11pm is **23:00**.
   Then select a timezone.
5. [optional] Change the duration to suit your needs. AMS recommends a four hour minimum duration.
6. Enter a patch tag key and value for the target. For information, see
   [What are tags?](acc-tag-intro.md#acc-tag-what-is "acc-tag-intro.md#acc-tag-what-is").
7. [optional] Expand the optional parameters to adjust concurrency, error rate, and maintenance window cut-off.
   1. Concurrency controls how many target instances are patching at the same time. For example, a 50% concurrency for 10 target
      instances will patch no more that 5 instances at a time, while 100% concurrency will patch all 10 at once.
   2. Error rate controls the tolerance for errors before patching is suspended. For example, an error rate of 100% for 10 target
      instances will patch all instances regardless of how many fail, while a 50% error rate will suspend patching once 5 instances have failed
      to patch. AMS recommends a 100% error rate.
   3. Patch maintenance window cutoff prevents breach of the patch maintenance window by suspending the start of new patching
      activities the specified hours before the end of the patch maintenance window. For example a cutoff of 1 hour (recommended), ceases new
      patch activities 1 hour before the end of the patch maintenance window.

###### Important

Verify the next execution time.

Visit the [SSM Maintenance Window console](https://console.aws.amazon.com/systems-manager/maintenance-windows "https://console.aws.amazon.com/systems-manager/maintenance-windows")
, search for your newly created patch maintenance window, and verify the next execution time.
If you have any questions or need to edit your patch maintenance window, create a service request to talk with an AMS patch expert

To schedule a CRON-based patch maintenance window using CloudFormation, see [Create a patch maintenance window using CloudFormation for AMS Accelerate](acc-p-maint-window-cfn.md "acc-p-maint-window-cfn.md").
