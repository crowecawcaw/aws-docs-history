

# View and Manage Project Details
<a name="view-manage-project-details-iam-based"></a>

Project details include storage configuration, execution role assignments, member information, and networking settings that determine how resources within the project operate.

**Viewing Project Details**

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. In the Projects list, choose the project name you want to view.

1. The project details page displays the following information:

   1. **Project Header:**
      + Project name and status (Active, Creating, Deleting)
      + Project description
      + Action buttons: Delete, Edit, Share info

   1. **Details Section:**
      + Project URL - Link to access the project portal
      + Project ARN - Amazon Resource Name for the project
      + Storage - Amazon S3 bucket location for project files
      + Execution role ARN - IAM role that defines data access permissions

   1. **Members Section:**
      + Member ARN - IAM role or user that can login and access the project
      + Description of member access capabilities

   1. **Networking Section:**
      + VPC - Virtual Private Cloud configuration status
      + Network settings that apply to resources created in the project

1. To perform actions on the project, use the buttons in the project header:
   + Choose **Edit** to modify project settings
   + Choose **Share info** to generate welcome message for users
   + Choose **Delete** to remove the project

1. To return to the Projects list, choose **Projects** in the breadcrumb navigation.