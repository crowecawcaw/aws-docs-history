# View and Manage Project

Details

Project details include storage configuration, execution role assignments, member
information, and networking settings that determine how resources within the project
operate.

###### Viewing Project Details

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. In the Projects list, choose the project name you want to view.
3. The project details page displays the following information:
   1. **Project Header:**
      - Project name and status (Active, Creating, Deleting)
      - Project description
      - Action buttons: Delete, Edit, Share info

   2. **Details Section:**
      - Project URL - Link to access the project portal
      - Project ARN - Amazon Resource Name for the project
      - Storage - Amazon S3 bucket location for project files
      - Execution role ARN - IAM role that defines data access
        permissions

   3. **Members Section:**
      - Member ARN - IAM role or user that can login and access the
        project
      - Description of member access capabilities

   4. **Networking Section:**
      - VPC - Virtual Private Cloud configuration status
      - Network settings that apply to resources created in the project

4. To perform actions on the project, use the buttons in the project header:
   - Choose **Edit** to modify project settings
   - Choose **Share info** to generate welcome message for
     users
   - Choose **Delete** to remove the project

5. To return to the Projects list, choose **Projects** in the
   breadcrumb navigation.
