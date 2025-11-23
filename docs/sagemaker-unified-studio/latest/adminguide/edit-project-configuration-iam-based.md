# Edit Project Configuration

You can edit the project description to reflect changes in business context or project
scope and update the member role to change project access permissions.

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. Choose the project name you want to edit from the Projects list.
3. On the project details page, choose **Edit**.
4. In the Edit Project dialog, modify the available settings:
   1. **Details Section:**
      - Description - Update the project description (optional, up to 2048
        characters)

   2. **Member Section:**
      - IAM role - Update the IAM role or user that can login and access the
        project

5. Review the information note about required permissions
   (SageMakerStudioUserIAMConsolePolicy must be attached or have the same permissions
   added via another policy)
6. Choose **Save** to apply your changes.
7. The project details page refreshes with the updated information.
   Your changes are applied immediately. If you updated the member role, the new IAM
   role or user will have access to the project, and the previous role will no longer have
   access.
