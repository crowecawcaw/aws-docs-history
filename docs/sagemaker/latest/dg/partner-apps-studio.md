# Partner AI Apps in Studio

After the admin has added the required permissions and authorized users, users can view the
Amazon SageMaker Partner AI App in Amazon SageMaker Studio. From Studio, users can launch apps that have been approved
for use by their administrator.

## Browsing and selecting

To browse the available Partner AI Apps, users must navigate to Studio. For information about
launching Studio, see [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").

After users have launched Studio, they can view all of the available Partner AI Apps by
selecting the **Partner AI Apps** section in the left navigation. The
**Partner AI Apps** page lists all of the Partner AI Apps, and gives information
about whether the Partner AI Apps have been deployed by the admin. If the desired Partner AI Apps haven't been
deployed, users can reach out to the admin to request that they deploy the Partner AI Apps for use in
the SageMaker AI domain.

If the application has been deployed, users can open the Partner AI App UI to start using it or view
details of the Partner AI App.

When users view the details of the application, they see the value of the following.

- ARN – This is the resource ARN of the Partner AI App.
- SDK URL – This is the URL of the Partner AI App that the Partner AI App SDK uses to support
  app-specific tasks such as logging model experiment tracking data from a JupyterLab
  notebook in Studio.

Users can use these values to write code that uses the Partner AI App SDK for app-specific tasks.

Each Partner AI App’s details page includes a sample notebook. To get started, users can launch the
sample notebook in a JupyterLab space in the Studio environment.
