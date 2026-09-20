

# How to decommission a landing zone
<a name="how-to-decommission"></a>

To decommission your AWS Control Tower landing zone from the console, follow the procedure given here.

**Note**  
We recommend that you unmanage your enrolled accounts prior to decommissioning.

1. If the AWS Backup baseline is enabled on any registered OU, disable it on every OU where it is enabled before you decommission your landing zone. Otherwise, decommissioning fails. For instructions, see [First step: Turn off backups on OUs](stop-backups.md#turn-off-ou-backup).

   If decommissioning has already failed for this reason, you can disable the AWS Backup baseline and run decommissioning again.

1. Navigate to the **Landing Zone Settings** page in the AWS Control Tower console.

1. Choose **Decommission your landing zone** within the **Decommission your landing zone** section.

1.  A dialog appears, explaining the action you are about to perform, with a required confirmation process. To confirm your intent to decommission, you must select every box and type the confirmation as requested.
**Important**  
*The decommissioning process cannot be undone.*

1. If you confirm your intent to decommission your landing zone, you are redirected to the AWS Control Tower home page while decommissioning is in progress. The process may require up to two hours.

   Do not close any member accounts in your organization while decommissioning is in progress. Decommissioning might fail.

1. When decommissioning has succeeded, you must delete remaining resources manually before setting up a new landing zone from the AWS Control Tower console. These remaining resources include some specific Amazon S3 buckets, organizations, and CloudWatch Logs log groups.
**Note**  
*These actions may have significant consequences for your billing and compliance activities. For example, failure to delete these resources can result in unexpected charges.*

    For more information about how to delete resources manually, see [About removing AWS Control Tower resources](walkthrough-delete.md#manual-decommissioning).

1. If you intend to set up a new landing zone in a new AWS Region, follow this additional step. Enter the following command through the CLI: 

   ```
   aws organizations disable-aws-service-access --service-principal controltower.amazonaws.com
   ```