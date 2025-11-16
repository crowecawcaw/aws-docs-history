# Creating and using AWS Glue DataBrew projects

In AWS Glue DataBrew, a _project_ is the centerpiece of your data analysis and
transformation efforts.

When you create a project, you bring together two fundamental components:

- A dataset, to provide read-only access to your source data. For more information,
  see [Connecting to data with AWS Glue DataBrew](datasets.md "datasets.md").
- A recipe, to apply DataBrew data transformations to the dataset. For more
  information, see [Creating and using AWS Glue DataBrew recipes](recipes.md "recipes.md").
  The DataBrew console presents your project in a highly interactive, intuitive user interface.
  It encourages you to experiment with hundreds of data transformations, so you can learn how
  they work and what effect they have on your data.

The data that you see in project view is a sample of
your dataset. Because datasets can be very large, with thousands or even millions of rows,
using a sample helps ensure that the DataBrew console remains responsive while you transform
the sample data in various ways. By default, the sample consists of the first 500 rows of
data from the dataset. You can choose different settings for the sample size, and which rows
are chosen.

As you transform the sample data, DataBrew helps you build and refine the project recipe—a
step-by-step series of the transformations that you applied thus far. Your work-in-progress
recipe is saved automatically, so you can leave the project view at any time, return later,
and pick up where you left off.

When your recipe is ready for use you can publish it. Publishing a recipe makes it
available to the DataBrew job subsystem, where you can apply the recipe to your entire dataset,
or create an extensive data profile that lets you understand the structure, content, and
statistical characteristics of your data.

###### Topics

- [Creating a project](#projects.creating "#projects.creating")
- [Overview of a DataBrew project session](projects.md "projects.md")
- [Deleting a project](projects.md "projects.md")

## Creating a project

Use the following procedure to create a project.

###### To create a project

1. Sign in to the AWS Management Console and open the DataBrew console
   .
2. On the navigation pane, choose **PROJECTS**. Then choose **Create project**.
3. Enter a name for your project. Then choose a recipe to attach to your project:
   - Choose **Create new recipe** if you are starting from the
     beginning. Doing this creates a new, empty recipe and attaches it to
     your project.
   - Choose **Edit existing recipe** if you have a previously published recipe that you
     want to use for this project. If the recipe is currently attached to
     another project, or has any jobs defined for it, then you can't
     use it in your new project. Choose **Browse recipes** to see what
     recipes are available.
   - Choose **Import steps from recipe** if you have an existing
     recipe that's been published previously and want to import its steps,
     and then do the following:
     1. Choose **Browse recipes** to see what recipes are
        available.
     2. Choose the published version of the recipe that you
        want to use. A recipe can have multiple versions, depending on how
        often you published it while working in project view.
     3. Choose **View recipe steps** to examine the data
        transformations in the recipe.

4. After you have a recipe, choose the dataset that you want to work with
   on the **Select a dataset** pane:
   - **My datasets** – Choose a dataset that you created
     previously. For more information, see Creating a project.)
   - **Sample files** – Create a new dataset based on
     sample data maintained by AWS. This sample data is a great way to
     explore what DataBrew can do, without having to provide your own data. Make
     sure to enter a name for your dataset.
   - **New dataset** – Create a new dataset. For more
     information, see Creating a project.

5. For **Access permissions**, choose an AWS Identity and Access Management (IAM) role that
   allows DataBrew to read from your Amazon S3 input location. For an S3 location owned by
   your AWS account, you can choose the `AwsGlueDataBrewDataAccessRole`
   service-managed role. Doing this allows DataBrew to access S3 resources that you
   own.
6. On the **Sampling** pane, you can find options for
   DataBrew to build a sample of data from your dataset.

For **Type**, choose how DataBrew should get rows from your
dataset:

    * Use **First n rows** to create a sample based on the
     first rows in the dataset.
    * Use **Random rows** to create a
     sample based on a random selection of rows in the dataset.
    * Choose the number of rows to appear in the sample: 500, 1,000, 2,500,
     or a custom sample size, up to a maximum of 5,000 rows. A smaller sample
     size allows DataBrew to perform transformations faster, saving you time as
     you develop your recipe. A larger sample size more accurately reflects
     the makeup of the underlying source data. However, project session
     initialization and interactive transformations are slower.

7. (Optional) Choose **Tags** to attach tags to your
   dataset.

_Tags_ are simple labels consisting of a
user-defined key and an optional value that can make it easier to manage, search
for, and filter DataBrew projects by purpose, owner, environment, or other
criteria. 8. When the settings are as you want them, choose **Create
job**.

DataBrew creates a new dataset if needed, creates a new recipe if needed, builds the data
sample, and creates an interactive project session. This process can take a couple of
minutes to complete. When the project is ready for use, you can begin working with the
data sample.
