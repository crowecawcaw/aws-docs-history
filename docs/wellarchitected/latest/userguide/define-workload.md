# Defining a workload in AWS WA Tool

A workload is a set of components that deliver business value. For example, workloads
can be marketing websites, ecommerce websites, the backend for a mobile app, and
analytic platforms. Accurately defining a workload helps ensure a comprehensive review
against the AWS Well-Architected Framework pillars.

###### To define a workload

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. If this is your first time using AWS WA Tool, you see a page that introduces you
   to the features of the service. In the **Define a workload**
   section, choose **Define workload**.

Alternately, in the left navigation pane, choose
**Workloads** and choose **Define
workload**.

For details on how AWS uses your workload data, choose **Why does AWS
need this data, and how will it be used?** 3. In the **Name** box, enter a name for your workload.

###### Note

The name must be between 3 and 100 characters. At least three characters
must not be spaces. Workload names must be unique. Spaces and capitalization
are ignored when checking for uniqueness. 4. In the **Description** box, enter a description of the
workload. The description must be between 3 and 250 characters. 5. In the **Review owner** box, enter the name, email address,
or identifier for the primary group or individual that owns the workload review
process. 6. In the **Environment** box, choose the environment for your
workload:

    * **Production** – Workload runs in a production
     environment.
    * **Pre-production** – Workload runs in a
     pre-production environment.

7. In the **Regions** section, choose the Regions for your
   workload:
   - **AWS Regions** – Choose the AWS Regions where
     your workload runs, one at a time.
   - **Non-AWS regions** – Enter the names of the
     Regions outside of AWS where your workload runs. You can specify up to
     five unique Regions, separated by commas.Use both options if appropriate for your workload.

8. (Optional) In the **Account IDs** box, enter the IDs of the
   AWS accounts associated with your workload. You can specify up to 100 unique
   account IDs, separated by commas.

If Trusted Advisor is activated, any account IDs specified are used to get data from
Trusted Advisor. See [Activating AWS Trusted Advisor for a workload](activate-ta-for-workload.md "activate-ta-for-workload.md") to grant AWS WA Tool permissions
to get Trusted Advisor data on your behalf within IAM. 9. (Optional) In the **Application** box, enter the application
ARN of an application from the [AWS Service Catalog AppRegistry](../../../servicecatalog/latest/arguide/intro-app-registry.md "../../../servicecatalog/latest/arguide/intro-app-registry.md") that you want to associate with this workload. Only one
ARN can be specified per workload, and the application and workload must be in
the same Region. 10. (Optional) In the **Architectural design** box, enter the URL
for your architectural design. 11. (Optional) In the **Industry type** box, choose the type of
industry associated with your workload. 12. (Optional) In the **Industry** box, choose the industry that
best matches your workload. 13. (Optional) In the **Trusted Advisor** section, to turn on Trusted Advisor
checks for your workload, select **Activate Trusted Advisor**.
Additional setup might be needed for accounts associated with your workload. See
[Activating AWS Trusted Advisor for a
workload](activate-ta-for-workload.md "activate-ta-for-workload.md") to grant AWS WA Tool permissions to get
Trusted Advisor data on your behalf. Select from **Workload
Metadata**, **AppRegistry**, or **All**
under **Resource definition** to define what resources AWS WA Tool
uses to run Trusted Advisor checks. 14. (Optional) In the **Jira** section, to turn on workload-level Jira sync settings for the workload, select **Override account level settings**. Additional setup might be needed for accounts associated with your workload. See [AWS Well-Architected Tool Connector for Jira](jira.md "jira.md") to get started with setting up and configuring the connector. Select from **Do not sync workload**, **Sync workload - Manual**, and **Sync workload - Automatic**, and optionally enter a **Jira project key** to sync to.

###### Note

If you do not override account-level settings, workloads will default to the account-level Jira sync setting. 15. (Optional) In the **Tags** section, add any tags you want to
associate with the workload.

For more information on tags, see [Tagging your AWS WA Tool resources](tagging.md "tagging.md"). 16. Choose **Next**.

If a required box is blank or if a specified value is not valid, you must
correct the issue before you can continue. 17. (Optional) In the **Apply Profile** step, associate a
profile with the workload by selecting an existing profile, searching
for the profile name, or choosing **Create profile** to [create a profile](creating-a-profile.md "creating-a-profile.md"). Choose
**Next**. 18. Choose the lenses that apply to this workload. Up to 20 lenses can be added to
a workload. For descriptions of official AWS lenses, see [Lenses](lenses.md "lenses.md").

Lenses can be selected from **[Custom lenses](lenses-custom.md "lenses-custom.md")** (lenses that you created or that were shared with your AWS account), **[Lens Catalog](lens-catalog.md "lens-catalog.md")** (AWS official lenses available to all users), or both.

###### Note

The **Custom lenses** section is empty if you have not created a custom lens or had a custom lens shared with you.

###### Disclaimer

By accessing and/or applying custom lenses created by another AWS user
or account, you acknowledge that custom lenses created by other users and
shared with you are Third Party Content as defined in the AWS Customer
Agreement. 19. Choose **Define workload**.

If a required box is blank or if a specified value is not valid, you must
correct the issue before your workload is defined.
