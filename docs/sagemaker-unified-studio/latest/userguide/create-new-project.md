# Create a new project

In Amazon SageMaker Unified Studio, projects enable a group of users to collaborate on various business use
cases. Within projects, you can manage data assets in the Amazon SageMaker Unified Studio catalog, perform data
analysis, organize workflows, develop machine learning models, build generative AI apps, and
more.

In order to create a project in Amazon SageMaker Unified Studio, you must gain access to Amazon SageMaker Unified Studio. A domain
unit owner must also grant you access to create projects through an authorization policy. For
more information, see [Domain units and authorization policies in Amazon SageMaker Unified Studio](../adminguide/domain-units.md "../adminguide/domain-units.md").

When you create a project, you choose a name and description, customize parameters for
project resources, and then review selections.

## Step 1: Project name and description

To begin creating a project, navigate to the Amazon SageMaker Unified Studio landing page and choose
**Create project**.

The Project name and description includes the following fields:

- Project name - The name of your Amazon SageMaker Unified Studio project. Enter a name here. The name of
  the project can not be edited after the project is created.
- Description - An optional description of your project. You can edit this
  later.
- Domain unit - The business-level entity that lets your team organize and manage
  policies for business needs in the project. If nobody in the domain has created domain
  units, you create a project in the root domain unit by default and no action is needed
  here. If domain units have been created, select the name of the domain unit you want
  your project to be in. For more information, see [Domain units and authorization policies in Amazon SageMaker Unified Studio](../adminguide/domain-units.md "../adminguide/domain-units.md").
- Project profile - Project profiles define which resources and tools should be
  provisioned in the project. These include tools and compute resources for SQL, data
  science, data engineering, and machine learning development. Project profiles can
  include resources and tools from Amazon Redshift, Amazon SageMaker AI, and
  other AWS services. Select the project profile that contains the resources and tools
  you will need to use in your project. The project profiles available for you to choose
  from are defined by your administrator in the Amazon SageMaker Unified Studio management console. For more
  information, see the Amazon SageMaker Unified Studio Administrator Guide.

After you fill in the fields for project creation, choose **Continue**
to customize parameters.

## Step 2: Customize parameters

On the next page of project creation, select a project file storage — Amazon S3 storage
or Git repository for your project code artifacts. You can view and edit the names and
values for different resources that are created when the project is created.

For S3 storage, you will be provided with a link to a shared folder. For more
information on Amazon S3 storage for Amazon SageMaker Unified Studio, refer to [Unified storage](storage.md "storage.md") in Amazon SageMaker Unified Studio storage.

###### Note

Some of the parameter values might be determined by your admin or by the default value
from the environment blueprint, according to the configurations that your admin has set in
the Amazon SageMaker Unified Studio management console. If you are not able to view or change a parameter value
that you want to specify, contact your admin to edit the configurations. For more
information, see the section Edit a project profile in the Amazon SageMaker Unified Studio Administrator
Guide.

### Connect to a Git repository

As part of this process, if your admin has configured the parameters to be editable,
you can choose a Git repository to connect to your project. You can choose to connect your
project to an existing third-party Git repository or create a new Git repository to
connect to.

#### To connect to an existing 3P Git

repository

1. In the Git connection dropdown, select a connection from
   AWS CodeConnections that is enabled for Amazon SageMaker Unified Studio. Available Git
   connections are provided by your administrator in the Amazon SageMaker Unified Studio management
   console.
2. Select either the Existing repository and existing branch or Existing repository
   and new branch radio button. Then in the Repository name dropdown, you will see a
   list of repositories accessible with the connection.
3. Select the name of the repository you want to connect your project to.
4. In the branch name dropdown, either select an existing branch, or enter a branch
   name to create a new one.

#### To create a new Git repository

1. In the Git connection dropdown, select a connection from
   AWS CodeConnections that is enabled for Amazon SageMaker Unified Studio. Available Git
   connections are provided by your administrator in the Amazon SageMaker Unified Studio management
   console.
2. Select the New repository and new branch radio button.
3. Provide a name for the repository.
4. Enter a name for the branch you want to create within the new repository. The
   new repository and branch will then be created when the project is created.

Depending on which project profile you are using to create a project and what
parameters your admin has configured to be editable, you might have other fields to choose
parameters for.

When you have chosen the parameters you want, choose **Continue** to
review the selections.

## Step 3: Review

Use the last page of project creation to review the configurations you have selected.
When everything is configured as desired on the project creation review page, choose
**Create project**.

You are then redirected to the project home page. It might take a few minutes before the
project is created and you can access tools.

## Next steps

After you create a project, you can add members and resources to the project and begin
using tools. There are many ways to get started building your project, including the
following options:

- Add members to your project to collaborate together. For more information, see [Add project members](add-project-members.md "add-project-members.md").
- Add data to your project. For more information, see [Data](data.md "data.md").
- Add compute resources to your project. For more information, see [Compute](compute.md "compute.md").
- Find, train, and deploy machine learning models. For more information, see [Machine learning](sagemaker.md "sagemaker.md").
- Use Amazon Bedrock in SageMaker Unified Studio to create generative AI apps. For more information, see [Amazon Bedrock in SageMaker Unified Studio](bedrock.md "bedrock.md").
