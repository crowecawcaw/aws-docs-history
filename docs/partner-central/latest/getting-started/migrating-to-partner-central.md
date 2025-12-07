# Migrating to Partner Central in the AWS Console

Existing APN Partners will be provided with a self-service migration tool from within their legacy Partner Central account. Upon completing migration pre-requisites, partners can use the tool to schedule and complete their migration.

## Migration process

The migration process consists of four steps:

1. **Review all pre-migration readiness steps in the checklist below.**
2. **Link an AWS account to you APN account (if not yet completed).** The linked AWS account will be charged for the APN Membership Fee and will become the primary account for managing all AWS-related activities. For more information, see [Linking AWS Partner Central and AWS accounts](linking-apc-aws-marketplace.md "linking-apc-aws-marketplace.md"). Upon migrating, accessing Partner Central will be through the linked AWS account, where partner users will need the appropriate IAM roles and permissions to gain access. This means users will authenticate through the linked AWS account using their assigned IAM credentials to access Partner Central features and capabilities. See Accessing Partner Central for more details.
3. **Set up user access through AWS IAM, including assigning new managed policies to control access to Partner Central features.** See instructions below for user onboarding during migration.
4. **Schedule or initiate migration.** Users assigned as the alliance lead or cloud admin roles in the legacy Partner Central environment can access the self-service migration tool to select the preferred migration date and time. Once scheduled, alliance leads should alert all active Partner Central users of the scheduled date and time. Once the migration is initiated, all users will be blocked from accessing Partner Central. As a result, we recommend scheduling the migration during non-business hours. The migration typically takes between 2 to 6 hours, depending on the amount of data required to transfer. Upon successful migration, alliance leads will be notified via email and all users will be able to log into the new Partner Central experience with their new IAM credentials.

## User onboarding during the migration process

### Step 1: Determine permissions for users

1. From the AWS Partner Central homepage, select **View Instructions** in the migration widget.
2. Follow the step-by-step instructions outlined in the tool.
3. Choose **Download Partner Central users**.
4. Open downloaded file of existing users. Based on their current Partner Central role assignment, and attributes such as Last Login Date, determine which users are required to be onboarded in the new Partner Central experience.
5. Map users to specific IAM managed policies based on their current role assignment. Refer to [AWS managed policies for AWS Partner Central users](managed-policies.md "managed-policies.md") for mapping and managed policy documentation.

###### Note

Users who only require access to Skill Builder for AWS training and certification content will no longer need access to AWS Partner Central. For more information, see Associating domains to your AWS Partner Central account.

### Step 2: Work with your IAM Administrator to determine the appropriate onboarding option for users with managed policies

The IAM Administrator should assign the appropriate managed policies to each user according to the mapping above. The process of onboarding users to IAM depends on a partner's AWS account access setup. Refer to Controlling access for AWS Partner Central users for more information.
