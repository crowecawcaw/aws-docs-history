The SiteWise Monitor feature is not available to new customers. Existing customers can continue to
use the service as normal. For more information, see [SiteWise Monitor availability
change](iotsitewise-monitor-availability-change.md "iotsitewise-monitor-availability-change.md")

# Share data with AWS IoT SiteWise Monitor projects

In AWS IoT SiteWise Monitor, you share data by inviting viewers to a project. Viewers can view all
assets, asset properties, alarms, and dashboards in the project. You can create multiple
projects to give groups of viewers access to different sets of assets and dashboards. Only
portal administrators can create and update projects and associate assets with projects. Project
owners create and update dashboards and invite viewers to projects.

Your AWS administrator chooses the portal administrators. Your portal administrators
assign assets to projects and assign owners to those projects. The project owner invites viewers
to a project. At each step, these users decide who has access to your data and what type of
access they have.

You can perform the following data sharing tasks:

| Task                                                                                             | Roles that can perform the task                                                                                                                               |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Create projects in an AWS IoT SiteWise Monitor portal](create-projects.md "create-projects.md") | Only portal administrators can create projects.                                                                                                               |
| [View project details](view-project-details.md "view-project-details.md")                        | Portal administrators can view details for all projects. Project owners and project<br>viewers can view details for projects to which they have been invited. |
| [Add assets to projects](add-assets-to-projects-sd.md "add-assets-to-projects-sd.md")            | Only a portal administrator can add assets to a project.                                                                                                      |
| [Assign project owners](assign-project-owners.md "assign-project-owners.md")                     | Only a portal administrator can assign project owners to a project.                                                                                           |
| [Assign project viewers](assign-project-viewers.md "assign-project-viewers.md")                  | Portal administrators can invite viewers to any project in the portal. Project<br>owners can invite viewers to projects that they administer.                 |
| [Change project details](edit-project-details.md "edit-project-details.md")                      | Only portal administrators can update the name and description for a<br>project.                                                                              |
| [Delete projects in AWS IoT SiteWise Monitor](delete-projects.md "delete-projects.md")           | Only portal administrators can delete projects.                                                                                                               |
