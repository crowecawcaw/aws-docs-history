

# Configure remediation tutorials
<a name="tr-tutorials"></a>

The following tutorials provide examples of creating common remediations in Trusted Remediator

## Remediate all resources manually
<a name="tr-tutorials-man"></a>

This example configures manual remediation for all Amazon EBS volumes with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes).

**Configure manual remediation for Amazon EBS volumes with check ID DAvU99Dc4C**

1. Open the AWS AppConfig console at [https://console.aws.amazon.com/systems-manager/appconfig](https://console.aws.amazon.com/systems-manager/appconfig).

   Make sure that you sign in as the **Delegated Administrator** account.

1. Select **Trusted Remediator** from the list of applications.

1. Choose the **Cost Optimization** configuration profile.

1. Select the **Underutilized Amazon EBS Volumes** flag.

1. For **execution-mode**, select **Manual**.

1. Make sure that the **automated-for-tagged-only** and **manual-for-tagged-only** attributes are blank. These attributes are used to override the default execution-mode for resources with matching tags.

   The following is an example of the **Attributes** section with blank values for **automated-for-tagged-only** and **manual-for-tagged-only** and **Manual** for **execution-mode**:  
![An example of the Attributes section.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/tr-tutorial1.png)

1. Choose **Save** to update the value, and then choose **Save new version** to apply the changes. You must choose **Save new version** for Trusted Remediator to recognize the change.

1. Make sure that your Amazon EBS volumes don't have a tag with the key`TR-DAvU99Dc4C-Execution-Mode`. This tag key overrides the default execution-mode for that EBS Volume.

## Remediate all resources automatically, except for selected resources
<a name="tr-tutorials-auto"></a>

This example configures automatic remediation for all Amazon EBS volumes with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes), with the exception of specified volumes that won't be remediated (designated **Inactive**.

**Configure automatic remediation for Amazon EBS volumes with check ID DAvU99Dc4C, with the exception of selected inactive resources**

1. Open the AWS AppConfig console at [https://console.aws.amazon.com/systems-manager/appconfig](https://console.aws.amazon.com/systems-manager/appconfig).

   Make sure that you sign in as the **Delegated Administrator** account.

1. Select **Trusted Remediator** from the list of applications.

1. Choose the **Cost Optimization** configuration profile.

1. Select the **Underutilized Amazon EBS Volumes** flag.

1. For **execution-mode**, select **Automated**.

1. Make sure that the **automated-for-tagged-only** and **manual-for-tagged-only** attributes are blank. These attributes are used to override the default execution-mode for resources with matching tags.

   The following is an example of the **Attributes** section with blank values for **automated-for-tagged-only** and **manual-for-tagged-only** and **Automated** for **execution-mode**:  
![An example of the Attributes section.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/tr-tutorial2.png)

1. Choose **Save** to update the value, and then choose **Save new version** to apply the changes. You must choose **Save new version** for Trusted Remediator to recognize the change.

   At this point, all Amazon EBS volumes are set for automatic remediation.

1. Override automatic remediation for selected Amazon EBS volumes:

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. Choose **Elastic Block Store**, **Volumes**.

   1. Choose **Tags**.

   1. Choose **Manage tags**.

   1. Add the following tag:
      + **Key:** TR-DAvU99Dc4C-Execution-Mode
      + **Value:** Inactive

      The following is an example of the **Tags** section showing the **Key** and **Value** fields:  
![An example of the Attributes section.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/tr-tutorial-inactive.png)

   1. Repeat steps 2 through 5 for all Amazon EBS volumes that you want to exclude from remediation.

## Remediate tagged resources automatically
<a name="tr-tutorials-auto-tags"></a>

This example configures automatic remediation for all Amazon EBS volumes with the tag `Stage=NonProd` with the Trusted Advisor check ID DAvU99Dc4C (Underutilized Amazon EBS Volumes). All other resources without this tag aren't remediated.

**Configure automatic remediation for Amazon EBS volumes with the tag `Stage=NonProd` for check ID DAvU99Dc4C**

1. Open the AWS AppConfig console at [https://console.aws.amazon.com/systems-manager/appconfig](https://console.aws.amazon.com/systems-manager/appconfig).

   Make sure that you sign in as the **Delegated Administrator** account.

1. Select **Trusted Remediator** from the list of applications.

1. Choose the **Cost Optimization** configuration profile.

1. Select the **Underutilized Amazon EBS Volumes** flag.

1. For **execution-mode**, select **Conditional**.

1. Set the **automated-for-tagged-only** to `Stage=NonProd`. This attribute overrides the default `execution-mode` for resources with matching tags. Make sure that the **manual-for-tagged-only** attributes is blank.

   The following is an example of the **Attributes** section with **automated-for-tagged-only** set to **Stage=NonProd** and **Conditional** for **execution-mode**:  
![An example of the Attributes section.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/tr-tutorial-conditional.png)

1. Optionally, set the preconfigured-parameters to one of the following:
   + `CreateSnapshot=false` to not to create snapshot of the Amazon EBS volume before it's deleted
   + `MinimumUnattachedDays=10` to set minimum unattached days of the Amazon EBS volume to delete to be 10 days
   + `CreateSnapshot=false`, `MinimumUnattachedDays=10` for both of the above

1. Choose **Save** to update the value, and then choose **Save new version** to apply the changes. You must choose **Save new version** for Trusted Remediator to recognize the change.

1. Make sure that your Amazon EBS volumes don't have a tag with the key`TR-DAvU99Dc4C-Execution-Mode`. This tag key overrides the default execution-mode for that EBS Volume.