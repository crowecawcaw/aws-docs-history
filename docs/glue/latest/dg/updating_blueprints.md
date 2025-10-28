# Updating a blueprint in AWS Glue

You can update a blueprint if you have a revised layout script, a revised set of
blueprint parameters, or revised supporting files. Updating a blueprint creates a new
version.

Updating a blueprint doesn't affect existing workflows created from the
blueprint.

You can update a blueprint by using the AWS Glue console, AWS Glue API, or AWS Command Line Interface
(AWS CLI).

The following procedure assumes that the AWS Glue developer has created and uploaded an updated
blueprint ZIP archive to Amazon S3.

###### To update a blueprint (console)

1. Ensure that you have read permissions (`s3:GetObject`) on the blueprint ZIP
   archive in Amazon S3.
2. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").

Sign in as a user that has permissions to update a blueprint. Switch to the same AWS
Region as the Amazon S3 bucket that contains the blueprint ZIP archive. 3. In the navigation pane, choose **blueprints**. 4. On the **blueprints** page, select a blueprint, and on the
**Actions** menu, choose **Edit**. 5. On the **Edit a blueprint** page, update the blueprint
**Description** or **ZIP archive location (S3)**. Be
sure to include the archive file name in the path. 6. Choose **Save**.

The **blueprints** page returns and shows that the blueprint status is
`UPDATING`. Choose the refresh button until the status changes to
`ACTIVE` or `FAILED`. 7. If the status is `FAILED`, select the blueprint, and on the
**Actions** menu, choose **View**.

The detail page shows the reason for the failure. If the error message is
**`"Unable to access object at location..."`** or **`"Access
 denied on object at location..."`**, review the following requirements:

    * The user that you are signed in as must have read permission on the blueprint ZIP
     archive in Amazon S3.
    * The Amazon S3 bucket that contains the ZIP archive must have a bucket policy that grants read
     permission on the object to your AWS account ID. For more information, see [Publishing a blueprint](developing-blueprints-publishing.md "developing-blueprints-publishing.md").
    * The Amazon S3 bucket that you're using must be in the same Region as the Region that you're
     signed into on the console.

###### Note

If the update fails, the next blueprint run uses the latest version of the blueprint
that was successfully registered or updated.

###### To update a blueprint (AWS CLI)

1. Enter the following command.

```
aws glue update-blueprint --name `<blueprint-name>` [--description `<description>`] --blueprint-location s3://`<s3-path>`/`<archive-filename>`
```

2. Enter the following command to check the blueprint status. Repeat the command until
   the status goes to `ACTIVE` or `FAILED`.

```
aws glue get-blueprint --name `<blueprint-name>`
```

If the status is `FAILED` and the error message is **`"Unable to
 access object at location..."`** or **`"Access denied on object at
 location..."`**, review the following requirements:

    * The user that you are signed in as must have read permission on the blueprint ZIP
     archive in Amazon S3.
    * The Amazon S3 bucket containing the ZIP archive must have a bucket policy that grants
     read permission on the object to your AWS account ID. For more information, see [Publishing a blueprint](developing-blueprints-publishing.md "developing-blueprints-publishing.md").
    * The Amazon S3 bucket that you're using must be in the same Region as the Region that
     you're signed into on the console.

###### See also

- [Overview of blueprints in AWS Glue](blueprints-overview.md "blueprints-overview.md")
