

# Step 1: Create a project
<a name="getting-started.01"></a>

In this step, you use the DataBrew console to quickly get started with a sample project.

**To create a project**

1. Sign in to the AWS Management Console and open the DataBrew console at [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/databrew/).

1. Make sure that your AWS Region is selected at upper-right on the DataBrew console. For a list of AWS Regions supported by DataBrew, see [DataBrew endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/databrew.html) in the *AWS General Reference.*

1. On the navigation pane, choose **Projects**, and then choose **Create project**.

1. On the **Project details** pane, do the following: 
   + For **Project name**, enter `chess-project`.
   + For **Attached recipe**, create a new recipe. A suggested name for the recipe is provided (`chess-project-recipe`).

1. On the **Select a dataset** pane, choose **Sample files**.

1. On the **Sample files** pane, choose **Famous chess game moves**. This dataset contains detailed information on more than 20,000 games of chess.

   For **Dataset name** a suggested name for the dataset is provided (`chess-games`).

1. On the **Access permissions** pane, choose `AwsGlueDataBrewDataAccessRole`. This is a service-linked role that lets DataBrew access your Amazon S3 buckets on your behalf. 

1. Choose **Create project**, and wait until DataBrew finishes preparing the project. The window looks similar to the following.

   The data that you see represents a sample from the `chess-games` dataset. By default, the sample consists of the first 500 rows from the dataset. You can change this project setting later.

   The toolbar provides access to hundreds of data transforms that you can apply to the data.

   The recipe pane at right in the DataBrew console tracks the transformations you applied so far.