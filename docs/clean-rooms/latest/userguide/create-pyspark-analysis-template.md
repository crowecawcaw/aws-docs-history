# Creating a PySpark analysis

template

**Prerequisites**

Before you create a PySpark analysis template, you must have:

- A membership in an active AWS Clean Rooms collaboration
- Access to at least one configured table in the active collaboration
- Permissions to create analysis templates
- A Python user script and a virtual environment created and stored in S3
  - S3 bucket has versioning enabled. For more information, see [Using
    versioning in S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md")
  - S3 bucket can calculate SHA-256 checksums for uploaded artifacts. For more
    information, see [Using checksums](../../../AmazonS3/latest/userguide/checking-object-integrity.md "../../../AmazonS3/latest/userguide/checking-object-integrity.md")

- Permissions to read code from an S3 bucket

For information about creating the required service role, see [Create a service role to
read code from an S3 bucket (PySpark analysis template role)](setting-up-roles.md#create-role-pyspark-analysis-template "setting-up-roles.md#create-role-pyspark-analysis-template").
The following procedure describes the process of creating a PySpark analysis template
using the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home"). It assumes that
you have already created a user script and virtual environment files and stored your user
script and virtual environment files in an Amazon S3 bucket.

###### Note

The member who creates the PySpark analysis template must also be the member who
receives results.

For information about how to create a PySpark analysis template using the AWS SDKs,
see the [AWS Clean Rooms API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

###### To create a PySpark analysis template

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with the AWS account that will function as the
   collaboration creator.
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Templates** tab, go to the **Analysis templates
   created by you** section.
5. Choose **Create analysis template**.
6. On the **Create analysis template** page, for
   **Details**,
   1. Enter a **Name** for the analysis template.
   2. (Optional) Enter a **Description**.
   3. For **Format**, choose the **PySpark**
      option.

7. For **Definition**,
   1. Review the **Prerequisites** and ensure each prerequisite is
      met before continuing.
   2. For **Entry point file**, enter the S3 bucket or choose
      **Browse S3**.
   3. (Optional) For **Libraries file**, enter the S3 bucket or
      choose **Browse S3**.

8. For **Tables referenced in the definition**,
   - If all tables referenced in the definition have been associated to the
     collaboration:
     - Leave the **All tables referenced in the definition have been
       associated to the collaboration** checkbox selected.
     - Under **Tables associated to the collaboration**, choose
       all associated tables that are referenced in the definition.

   - If all tables referenced in the definition haven't been associated to the
     collaboration:
     - Clear the **All tables referenced in the definition have been
       associated to the collaboration** checkbox.
     - Under **Tables associated to the collaboration**, choose
       all associated tables that are referenced in the definition.
     - Under **Tables that will be associated later**, enter a
       table name.
     - Choose **List another table** to list another table.

9. For **Error message configuration**, choose one of the
   following:
   - **Basic error messages** – returns basic error messages
     without exposing underlying data. Recommended for production workloads.
   - **Detailed error messages** – returns detailed error
     messages for faster troubleshooting. Recommended in development and testing
     environments. May expose sensitive data, including personally identifiable
     information (PII).

###### Note

When using **Detailed error messages**, all data provider members
must approve this setting for the template. 10. Specify the **Service access** permissions by selecting an
**Existing service role name** from the dropdown list.

    1. The list of roles are displayed if you have permissions to list roles.


    If you don't have permissions to list roles, you can enter the Amazon Resource
     Name (ARN) of the role that you want to use.
    2. View the service role by choosing the **View in IAM**
     external link.


    If there are no existing service roles, the option to **Use an existing
     service role** is unavailable.


    By default, AWS Clean Rooms doesn't attempt to update the existing role policy to add
     necessary permissions.

###### Note

    * AWS Clean Rooms requires permissions to query according to the analysis rules. For
     more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
    * If the role doesn’t have sufficient permissions for AWS Clean Rooms, you receive an
     error message stating that the role doesn't have sufficient permissions for
     AWS Clean Rooms. The role policy must be added before proceeding.
    * If you can’t modify the role policy, you receive an error message stating that
     AWS Clean Rooms couldn't find the policy for the service role.

11. If you want to enable **Tags** for the configured table resource,
    choose **Add new tag** and then enter the **Key** and
    **Value** pair.
12. Choose **Create**.
13. You are now ready to inform your collaboration member that they can [Review an analysis template](review-analysis-template.md "review-analysis-template.md"). (Optional if
    you want to query your own data.)

###### Important

Don't modify or remove artifacts (user scripts or virtual environments) after creating
an analysis template.

Doing so will:

- Cause all future analysis jobs using this template to fail.
- Require creation of a new analysis template with new artifacts.
- Not affect previously completed analysis jobs.
