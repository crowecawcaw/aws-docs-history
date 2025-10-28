# Delete an environment

In Amazon DataZone projects, environments are collections of configured resources (for
example, an Amazon S3 bucket, an AWS Glue database, or an Amazon Athena workgroup),
with a given set of IAM principals (with assigned contributor permissions) who can
operate on those resources. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

Any Amazon DataZone user with the required permissions to access the data portal can delete
an Amazon DataZone environment within a project.

To delete an existing environment, complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Browse project** from the top navigation pane and
   select the project that contains the environment that you want to delete.
3. Locate and choose the environment to open its details page, then expand
   **Actions** and choose **Delete
   environment**.
4. In the **Delete environment** pop up window, confirm deletion
   by typing `Delete` in the field and then choose **Delete
   environment**.

You can successfully delete an environment only after all entities with a
dependency to this environment have been deleted. To delete an environment, you
must first delete all its associated data sources and subscription targets.
