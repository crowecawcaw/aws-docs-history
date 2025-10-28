Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Creating a space for identity

federation

You cannot directly add or remove users in your space that supports identity
federation. You must work with your Identity federation administrator to manage SSO users and
groups in IAM Identity Center. CodeCatalyst syncs on a regular basis with the IAM Identity Center identity store with the latest
directory status for your space members.

Before you start to set up your space, make sure you are signed in to the AWS Management Console
with the AWS account that will be the specified billing account for your space.

###### Before you begin

- Before you begin, you must be ready to provide an AWS account ID for an account
  where you have administrative privileges as the billing account for your space. Have your
  12-digit AWS account ID ready. For information about finding your AWS account ID, see
  [Your AWS account ID and its alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md").

You must have completed the prerequisites as follows:

    1. Create an organization in AWS Organizations (not required).
    2. Set up your billing account or your account in AWS Organizations.
    3. Enable IAM Identity Center.
    4. Set up your provider in IAM Identity Center.
    5. Create users and groups in IAM Identity Center.

###### To create a space for identity federation

1. Sign in to the Amazon CodeCatalyst page in the AWS Management Console with the AWS account that will be the specified
   billing account for your space.
2. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").
3. Choose **IAM Identity Center**. On the **IAM Identity Center** page, under
   **Application Enabled Spaces**, choose
   **Connect**.

###### Tip

Make sure you are signed in to the AWS Management Console with the AWS account that will be the
specified billing account for your space. 4. In **AWS Region** , choose the Region for your space. Make sure to
choose the same Region as that where your identity resources are created.

###### Note

For IAM Identity Center resources, choose the same Region as your CodeCatalyst space. While you can
choose a different Region, this might impact connectivity and latency. 5. Under **Step 1: Choose application name**, in **Display
name**, enter a name that will match your company name for display on login
screens and in CodeCatalyst.

###### Note

Identity Center application names must be globally unique.

###### Important

Your application name will represent your company and will be visible for selection
as an option where users from a workforce directory will access CodeCatalyst. 6. In **AWS Identity Center application name**, provide the name to use when signing
in to CodeCatalyst with SSO. This is the name that will represent your company association
between your identity provider and your CodeCatalyst space. When you create an application, it
is associated with your identity store ID in IAM Identity Center. 7. In **Identity store ID**, the ID for the associated identity store in
IAM Identity Center displays. To change this, choose **go to IAM Identity Center**. 8. Choose **Next**. 9. Under **Step 2: Choose or create a CodeCatalyst space**, do one of the
following:

    * To set up an existing CodeCatalyst to support identity federation and create an
     application for it, choose **Existing CodeCatalyst**. In the dropdown field
     for **Choose existing CodeCatalyst**, choose the existing CodeCatalyst space
     you want to set up.


    ###### Note

    If you set up an existing space by adding SSO support, only SSO users and groups
     will be supported. Existing AWS Builder ID users will no longer be supported. This
     action cannot be undone, and you can't change the space back to an AWS Builder ID space
     later.
    * To set up a new CodeCatalyst, choose **New space**.


    In **Space name**, enter a name for your CodeCatalyst
     space.


    ###### Note

    Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

10. Choose **Next**.
11. Under **Step 3: Connect groups**, in **Choose
    groups**, choose the SSO users and groups you want to add to the space.
    Choose the box next to each group you want to add. These must be already available in
    IAM Identity Center for your identity provider.
12. Choose **Next**.
13. Under **Step 4: Assign users to the CodeCatalyst
    **Space administrator** role**, choose which users you want to
    assign the **Space administrator** role. These users will have
    **Space administrator** permissions in CodeCatalyst for your space, to
    include removing members and deleting the space. For more information about the role,
    see [Working
    with roles in Amazon CodeCatalyst](../userguide/ipa-roles.md "../userguide/ipa-roles.md").
14. Choose **Next**.
15. In the wizard Step 5 page, review the summary for the space.

###### Note

Make sure you are ready to create the space with the space name you have
chosen. Once you create the space, you will not be able to reuse the space
name, even if the space is deleted. SSO application names can be reassigned to
another space, but the space name itself cannot be reused.

## Next steps: Create teams, projects,

and resources in CodeCatalyst

After you have created your space, you can perform the following tasks.

- Create projects from blueprints in CodeCatalyst. For a tutorial, see [Tutorial: Creating a project with the Modern three-tier web application
  blueprint](../userguide/getting-started-template-project.md "../userguide/getting-started-template-project.md") in the _Amazon CodeCatalyst User
  Guide_.
- Work with workflows, repositories, and other resources in CodeCatalyst. See [Build, test, and
  deploy with workflows in CodeCatalyst](../userguide/flows.md "../userguide/flows.md") in the _Amazon CodeCatalyst User
  Guide_.
- Create teams in CodeCatalyst and import your users and groups into teams. See [Managing
  teams](../userguide/managing-teams.md "../userguide/managing-teams.md") in the _Amazon CodeCatalyst User Guide_.
- Create issues and assign tasks to users and teams in CodeCatalyst. See [Issues in
  CodeCatalyst](../userguide/managing-teams.md "../userguide/managing-teams.md") in the _Amazon CodeCatalyst User Guide_.
