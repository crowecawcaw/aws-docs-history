# Manage Projects from Domain

Administration

The Projects section in domain administration provides centralized management of all
projects within your Amazon SageMaker Unified Studio domain. Domain administrators can view project details,
monitor project status, create new projects, and manage project configurations.

Projects in Amazon SageMaker Unified Studio enable users to collaborate on various business use cases. Within
projects, users can manage data assets, perform data analysis, organize workflows, and
develop machine learning models.

From the domain administration perspective, you can oversee all projects in the domain
and ensure proper configuration.

Prerequisites:

- Domain administrator permissions for Amazon SageMaker Unified Studio
- IAM role or user with the `SageMakerStudioAdminIAMDefaultExecutionPolicy`
  policy attached
  Perform the following procedure:

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. The Projects page displays:
   - Domain details section showing account information, region, domain ID, admin
     roles, and creation date
   - Projects section listing all projects in the domain with details
     including:
     - Project name
     - Creation date (UTC-08:00)
     - Status (Active, Creating, Deleting)
     - Project URL
     - Actions menu

3. To view project details, choose the project name from the list.
4. To create a new project, choose **Create project** in the upper
   right corner of the Projects section.
5. Use the search functionality by entering terms in the **Find**
   search box to locate specific projects.
6. To perform actions on a project, choose the **Actions** menu (three
   dots) next to the project name for available options.
7. Monitor project status in the Status column to track project lifecycle
   states.
