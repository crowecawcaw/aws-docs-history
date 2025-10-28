# Update a project

You and your admin can make changes to project settings and parameters by updating a
project. There are three different kinds of project updates:

- Service-initiated updates. Projects are made up of blueprints that set up resources
  using different AWS services, and sometimes these services require updates to their
  parameters due to feature changes or security initiatives.
- Admin-initiated updates. The Amazon SageMaker Unified Studio domain admin can edit or update blueprint
  parameters for a project in the Amazon SageMaker Unified Studio management console after that project has been
  created. When this happens, project owners in Amazon SageMaker Unified Studio must update the project for the
  changes to take effect.
- Owner-initiated updates. Amazon SageMaker Unified Studio project owners can update certain parameters. Some
  parameters are not modifiable, and other parameters are modifiable if the domain admins
  configure them to be editable in the Amazon SageMaker Unified Studio management console. The project owners can
  then make updates to modifiable parameters in Amazon SageMaker Unified Studio.
  When a service-initiated update or admin-initiated update occurs and a project is eligible
  for updating, a blue banner appears to notify project owners of the change. Project owners can
  then update the project to implement the changes.

###### Note

If a service or admin has initiated an update by updating relevant blueprints, the
project owner must update the project so that project members can use all project
capabilities. The project capabilities might be limited until the project owner completes
the update.

Project owners can initiate updates to some project parameters if their domain admin has
made those parameters editable.

To update a project, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. From the top center menu, choose **Browse all projects**.
3. Select the name of the project to navigate to that project.
4. On the **Project overview** page, choose **Actions > Update
   project**.
5. (Optional) Review the information in the **Domain updates** section,
   if applicable.
6. Review the information in the **Project profile updates**
   section.
7. Review the information in **Environment updates**.
   1. Choose **Show update parameters** in each section to review and
      update the modifiable parameters as desired. If there are other parameters that you
      want to update that are listed as non-modifiable, contact your admin.

8. Choose **Update project**. Updating a project might take a few
   minutes as resources are deployed.
   When the update is complete, you can use your project with the updated parameters.
