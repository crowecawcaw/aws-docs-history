NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Setting up CloudFormation StackSets

After you set up your organization, you need to configure CloudFormation StackSets to
create the required role per management account:
AWSApplicationMigrationSharingRole\_<MANAGEMENT_ACCOUNT_ID>.

AWS CloudFormation StackSets extends the capability of stacks by enabling you to create,
update, or delete stacks across multiple accounts and AWS Regions with a single operation.

[Learn more about CloudFormation StackSets.](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md")

###### Important

StackSet automatically creates the roles in all accounts. You can choose to create the
roles manually in each member account of the organization, however, this must be done for
each account individually.

To set up your StackSet:

1. Go to the CloudFormation console.
2. Select **StackSets.**
3. Click the **Activate trusted access** button.
4. Create StackSet.
5. On the **Choose a template** page, under **Prerequisites – prepare template**, choose **Use a sample template**.
6. Under **Select a sample template**, select **Create roles to access multiple accounts via AWS Application Migration Service**, and
   choose **Next**.
7. Provide the name and description or use the existing values.
8. Under **Parameters**, add the account ID of each
   admin or delegated admin and choose **Next**.
9. Select or provide the required parameters .

###### Important

    * Under **Deployment targets**, select **Deploy to organization**.
    * Select only one specific AWS Region – we recommend that you select your
     StackSet Region.
    * To provide enhanced stability, we recommend that you set the **Failure tolerance optional** to a high value - at least as
     high as the number of accounts within the organization.

10. Check the box next to **I acknowledge that AWS CloudFormation
    might create IAM resources with custom names** and choose **Submit**.
    Once all the steps are completed, you should be able to see your new StackSet in
    **StackSet details > Stack instances**.
