

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Setting up CloudFormation StackSets
<a name="setting-up-stacksets"></a>

After you set up your organization, you need to configure CloudFormation StackSets to create the required role per management account: AWSApplicationMigrationSharingRole\_<MANAGEMENT\_ACCOUNT\_ID>.

AWS CloudFormation StackSets extends the capability of stacks by enabling you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation. 

[Learn more about CloudFormation StackSets.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

**Important**  
StackSet automatically creates the roles in all accounts. You can choose to create the roles manually in each member account of the organization, however, this must be done for each account individually. 

To set up your StackSet:

1. Go to the CloudFormation console.

1. Select **StackSets.**

1. Choose the **Activate trusted access** button.

1. Create StackSet.

1. On the **Choose a template** page, under **Prerequisites – prepare template**, choose **Use a sample template**.

1. Under **Select a sample template**, select **Create roles to access multiple accounts via AWS Transform MGN**, and choose **Next**.

1. Provide the name and description or use the existing values.

1. Under **Parameters**, add the account ID of each admin or delegated admin and choose **Next**.

1. Select or provide the required parameters .
**Important**  
Under **Deployment targets**, select **Deploy to organization**. 
Select only one specific AWS Region – we recommend that you select your StackSet Region.
To provide enhanced stability, we recommend that you set the **Failure tolerance optional** to a high value - at least as high as the number of accounts within the organization. 

1. Check the box next to **I acknowledge that AWS CloudFormation might create IAM resources with custom names** and choose **Submit**.

Once all the steps are completed, you should be able to see your new StackSet in **StackSet details > Stack instances**. 