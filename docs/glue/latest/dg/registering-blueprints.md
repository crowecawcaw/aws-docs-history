# Registering a blueprint in AWS Glue

After the AWS Glue developer has coded the blueprint and uploaded a ZIP archive to Amazon Simple Storage Service
(Amazon S3), an AWS Glue administrator must register the blueprint. Registering the blueprint makes
it available for use.

When you register a blueprint, AWS Glue copies the blueprint archive to a reserved Amazon S3
location. You can then delete the archive from the upload location.

To register a blueprint, you need read permissions on the Amazon S3 location that contains the
uploaded archive. You also need the AWS Identity and Access Management (IAM) permission
`glue:CreateBlueprint`. For the suggested permissions for an AWS Glue administrator
who must register, view, and maintain blueprints, see [AWS Glue administrator permissions for
blueprints](blueprints-personas-permissions.md#bp-persona-admin "blueprints-personas-permissions.md#bp-persona-admin").

You can register a blueprint by using the AWS Glue console, AWS Glue API, or AWS Command Line Interface
(AWS CLI).

###### To register a blueprint (console)

1. Ensure that you have read permissions (`s3:GetObject`) on the blueprint ZIP
   archive in Amazon S3.
2. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").

Sign in as a user that has permissions to register a blueprint. Switch to the same AWS
Region as the Amazon S3 bucket that contains the blueprint ZIP archive. 3. In the navigation pane, choose **blueprints**. Then on the
**blueprints** page, choose **Add blueprint**. 4. Enter a blueprint name and optional description. 5. For **ZIP archive location (S3)**, enter the Amazon S3 path of the uploaded
blueprint ZIP archive. Include the archive file name in the path and begin the path with
`s3://`. 6. (Optional) Add tag one or more tags. 7. Choose **Add blueprint**.

The **blueprints** page returns and shows that the blueprint status is
`CREATING`. Choose the refresh button until the status changes to
`ACTIVE` or `FAILED`. 8. If the status is `FAILED`, select the blueprint, and on the
**Actions** menu, choose **View**.

The detail page shows the reason for the failure. If the error message is
**`"Unable to access object at location..."`** or **`"Access
 denied on object at location..."`**, review the following requirements:

    * The user that you are signed in as must have read permission on the blueprint ZIP
     archive in Amazon S3.
    * The Amazon S3 bucket that contains the ZIP archive must have a bucket policy that grants read
     permission on the object to your AWS account ID. For more information, see [Developing blueprints in AWS Glue](developing-blueprints.md "developing-blueprints.md").
    * The Amazon S3 bucket that you're using must be in the same Region as the Region that you're
     signed into on the console.

9. Ensure that data analysts have permissions on the blueprint.

The suggested IAM policy for data analysts is shown in [Data analyst permissions for
blueprints](blueprints-personas-permissions.md#bp-persona-analyst "blueprints-personas-permissions.md#bp-persona-analyst"). This policy grants `glue:GetBlueprint` on any
resource. If your policy is more fine-grained at the resource level, then grant data
analysts permissions on this newly created resource.

###### To register a blueprint (AWS CLI)

1. Enter the following command.

```
aws glue create-blueprint --name `<blueprint-name>` [--description `<description>`] --blueprint-location s3://`<s3-path>`/`<archive-filename>`
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

###### See also:

- [Overview of blueprints in AWS Glue](blueprints-overview.md "blueprints-overview.md")
