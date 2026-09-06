

# View and manage project details
<a name="view-manage-project-details-idc"></a>

Project details include storage configuration, execution role assignments, and member information that determine how resources within the project operate.

To view project details, complete the following procedure:

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. In the Projects list, choose the project name you want to view.

1. The project details page displays the following information:

   1. **Project Header:**
      + Project name and status (Active, Creating, Deleting)
      + Project description
      + Action buttons: Delete, Edit

   1. **Details Section:**
      + Project URL - Link to access the project portal
      + Project ID
      + AWS Region - Region where the project resources exist
      + Account - The AWS account where the project resources exist

   1. **Parameters Section:**
      + Execution role ARN - IAM role that defines data access permissions
      + Storage - Amazon S3 bucket location for project files

   1. **Members tab:**
      + Member - IAM role, IAM user, SSO user, or SSO group that can login and access the project
      + Description of member access capabilities

1. To perform actions on the project, use the buttons in the project header:
   + Choose **Edit** to modify project settings
   + Choose **Delete** to remove the project

1. To return to the Projects list, choose **Projects** in the breadcrumb navigation.