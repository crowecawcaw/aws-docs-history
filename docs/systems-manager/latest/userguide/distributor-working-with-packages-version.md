• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Add a version to a

Distributor package

To add a package version, [create a package](distributor-working-with-packages-create.md "distributor-working-with-packages-create.md"), and then use Distributor to add a package version by
adding an entry to the AWS Systems Manager (SSM) document that already exists for older
versions. Distributor is a tool in AWS Systems Manager. To save time, update the manifest for an
older version of the package, change the value of the `version` entry in
the manifest (for example, from `Test_1.0` to `Test_2.0`) and
save it as the manifest for the new version. The simple **Add
version** workflow in the Distributor console updates the manifest file
for you.

A new package version can:

- Replace at least one of the installable files attached to the current
  version.
- Add new installable files to support additional platforms.
- Delete files to discontinue support for specific platforms.
  A newer version can use the same Amazon Simple Storage Service (Amazon S3) bucket, but must have a URL with
  a different file name shown at the end. You can use the Systems Manager console or the
  AWS Command Line Interface (AWS CLI) to add the new version. Uploading an installable file with the
  exact name as an existing installable file in the Amazon S3 bucket overwrites the
  existing file. No installable files are copied over from the older version to the
  new version; you must upload installable files from the older version to have them
  be part of a new version. After Distributor is finished creating your new package
  version, you can delete or repurpose the Amazon S3 bucket, because Distributor copies your
  software to an internal Systems Manager bucket as part of the versioning process.

###### Note

Each package is held to a maximum of 25 versions. You can delete versions that
are no longer required.

###### Topics

- [Adding a package version using the
  console](#add-pkg-version "#add-pkg-version")
- [Adding a package version using the
  AWS CLI](#add-pkg-version-cli "#add-pkg-version-cli")

## Adding a package version using the

console

Before you perform these steps, follow the instructions in [Create a package in
Distributor](distributor-working-with-packages-create.md "distributor-working-with-packages-create.md") to create a new
package for the version. Then, use the Systems Manager console to add a new package
version to Distributor.

### Adding a package version using the

Simple workflow

To add a package version by using the **Simple**
workflow, prepare updated installable files or add installable files to
support more platforms and architectures. Then, use Distributor to upload new
and updated installable files and add a package version. The simplified
**Add version** workflow in the Distributor console
updates the manifest file and associated SSM document for you.

###### To add a package version using the Simple workflow

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose
   **Distributor**.
3. On the Distributor home page, choose the package to which you want to
   add another version.
4. On the **Add version** page, choose
   **Simple**.
5. For **Version name**, enter a version name. The
   version name for the new version must be different from older
   version names. Version names can be a maximum of 512 characters, and
   can't contain special characters.
6. For **S3 bucket name**, choose an existing S3
   bucket from the list. This can be the same bucket that you used to
   store installable files for older versions, but the installable file
   names must be different to avoid overwriting existing installable
   files in the bucket.
7. For **S3 key prefix**, enter the subfolder of the
   bucket where your installable assets are stored.
8. For **Upload software**, navigate to the
   installable software files that you want to attach to the new
   version. Installable files from existing versions aren't
   automatically copied over to a new version; you must upload any
   installable files from older versions of the package if you want any
   of the same installable files to be part of the new version. You can
   upload more than one software file in a single action.
9. For **Target platform**, verify that the target
   operating system platform shown for each installable file is
   correct. If the operating system shown isn't correct, choose the
   correct operating system from the dropdown list.

In the **Simple** versioning workflow, because
you upload each installable file only once, extra steps are required
to target a single file at multiple operating systems. For example,
if you upload an installable software file named
`Logtool_v1.1.1.rpm`, you must change some
defaults in the **Simple** workflow to instruct
Distributor to target the same software at both Amazon Linux and Ubuntu Server
operating systems. You can do one of the following to work around
this limitation.

    * Use the **Advanced** versioning workflow
     instead, zip each installable file into a .zip file before
     you begin, and manually author the manifest so that one
     installable file can be targeted at multiple operating
     system platforms or versions. For more information, see
     [Adding a package version using the
     Advanced workflow](#add-pkg-version-adv "#add-pkg-version-adv").
    * Manually edit the manifest file in the
     **Simple** workflow so that your .zip
     file is targeted at multiple operating system platforms or
     versions. For more information about how to do this, see the
     end of step 4 in [Step 2: Create the JSON package
     manifest](distributor-working-with-packages-create.md#packages-manifest "distributor-working-with-packages-create.md#packages-manifest").

10. For **Platform version**, verify that the
    operating system platform version shown is either
    `_any`, a major release version followed by
    a wildcard (8.\*), or the exact operating system release version to
    which you want your software to apply. For more information about
    specifying a platform version, see step 4 in [Step 2: Create the JSON package
    manifest](distributor-working-with-packages-create.md#packages-manifest "distributor-working-with-packages-create.md#packages-manifest").
11. For **Architecture**, choose the correct
    processor architecture for each installable file from the drop-down
    list. For more information about supported architectures, see [Supported package platforms and
    architectures](distributor.md#what-is-a-package-platforms "distributor.md#what-is-a-package-platforms").
12. (Optional) Expand **Scripts**, and review the
    installation and uninstallation scripts that Distributor generates for
    your installable software.
13. To add more installable software files to the new version, choose
    **Add software**. Otherwise, go to the next
    step.
14. (Optional) Expand **Manifest**, and review the
    JSON package manifest that Distributor generates for your installable
    software. If you changed any information about your installable
    software since you began this procedure, such as platform version or
    target platform, choose **Generate manifest** to
    show the updated package manifest.

You can edit the manifest manually if you want to target a
software installable at more than one operating system, as described
in step 9. For more information about editing the manifest, see
[Step 2: Create the JSON package
manifest](distributor-working-with-packages-create.md#packages-manifest "distributor-working-with-packages-create.md#packages-manifest"). 15. When you finish adding software and reviewing the target platform,
version, and architecture data, choose **Add
version**. 16. Wait for Distributor to finish uploading your software and creating
the new package version. Distributor shows upload status for each
installable file. Depending on the number and size of packages you
are adding, this can take a few minutes. Distributor automatically
redirects you to the **Package details** page for
the package, but you can choose to open this page yourself after the
software is uploaded. The **Package details** page
doesn't show all information about your package until Distributor
finishes creating the new package version. To stop the upload and
package version creation, choose **Stop
upload**. 17. If Distributor can't upload any of the software installable files, it
displays an **Upload failed** message. To retry the
upload, choose **Retry upload**. For more
information about how to troubleshoot package version creation
failures, see [Troubleshooting
AWS Systems Manager Distributor](distributor-troubleshooting.md "distributor-troubleshooting.md"). 18. When Distributor is finished creating the new package version, on the
package's **Details** page, on the
**Versions** tab, view the new version in the
list of available package versions. Set a default version of the
package by choosing a version, and then choosing **Set
default version**.

If you don't set a default version, the newest package version is
the default version.

### Adding a package version using the

Advanced workflow

To add a package version, [create a
package](distributor-working-with-packages-create.md "distributor-working-with-packages-create.md"), and then use Distributor to add a package version by adding
an entry to the SSM document that exists for older versions. To save time,
update the manifest for an older version of the package, change the value of
the `version` entry in the manifest (for example, from
`Test_1.0` to `Test_2.0`) and save it as the
manifest for the new version. You must have an updated manifest to add a new
package version by using the **Advanced** workflow.

###### To add a package version using the Advanced workflow

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose
   **Distributor**.
3. On the Distributor home page, choose the package to which you want to
   add another version, and then choose **Add
   version**.
4. For **Version name**, enter the exact value that
   is in the `version` entry of your manifest file.
5. For **S3 bucket name**, choose an existing S3
   bucket from the list. This can be the same bucket that you used to
   store installable files for older versions, but the installable file
   names must be different to avoid overwriting existing installable
   files in the bucket.
6. For **S3 key prefix**, enter the subfolder of the
   bucket where your installable assets are stored.
7. For **Manifest**, choose **Extract from
   package** to use a manifest that you uploaded to the S3
   bucket with your .zip files.

(Optional) If you didn't upload your revised JSON manifest to the
Amazon S3 bucket where you stored your .zip files, choose **New
manifest**. You can author or paste the entire manifest
in the JSON editor field. For more information about how to create
the JSON manifest, see [Step 2: Create the JSON package
manifest](distributor-working-with-packages-create.md#packages-manifest "distributor-working-with-packages-create.md#packages-manifest"). 8. When you're finished with the manifest, choose **Add
package version**. 9. On the package's **Details** page, on the
**Versions** tab, view the new version in the
list of available package versions. Set a default version of the
package by choosing a version, and then choosing **Set
default version**.

If you don't set a default version, the newest package version is
the default version.

## Adding a package version using the

AWS CLI

You can use the AWS CLI to add a new package version to Distributor. Before you run
these commands, you must create a new package version and upload it to S3, as
described at the start of this topic.

###### To add a package version using the AWS CLI

1. Run the following command to edit the AWS Systems Manager document with an entry
   for a new package version. Replace
   `document-name` with the name of your
   document. Replace `amzn-s3-demo-bucket` with
   the URL of the JSON manifest that you copied in [Step 3: Upload the package and manifest
   to an Amazon S3 bucket](distributor-working-with-packages-create.md#packages-upload-s3 "distributor-working-with-packages-create.md#packages-upload-s3").
   `S3-bucket-URL-of-package` is the URL of
   the Amazon S3 bucket where the entire package is stored. Replace
   `version-name-from-updated-manifest` with
   the value of `version` in the manifest. Set the
   `--document-version` parameter to `$LATEST` to
   make the document associated with this package version the latest
   version of the document.

```
aws ssm update-document \
    --name "`document-name`" \
    --content "`S3-bucket-URL-to-manifest-file`" \
    --attachments Key="SourceUrl",Values="`amzn-s3-demo-bucket`" \
    --version-name `version-name-from-updated-manifest` \
    --document-version $LATEST
```

The following is an example.

```
aws ssm update-document \
    --name ExamplePackage \
    --content "https://s3.amazonaws.com/amzn-s3-demo-bucket/ExamplePackage/manifest.json" \
    --attachments Key="SourceUrl",Values="https://s3.amazonaws.com/amzn-s3-demo-bucket/ExamplePackage" \
    --version-name 1.1.1 \
    --document-version $LATEST
```

2. Run the following command to verify that your package was updated and
   show the package manifest. Replace
   `package-name` with the name of your
   package, and optionally, `document-version`
   with the version number of the document (not the same as the package
   version) that you updated. If this package version is associated with
   the latest version of the document, you can specify `$LATEST`
   for the value of the optional `--document-version`
   parameter.

```
aws ssm get-document \
    --name "`package-name`" \
    --document-version "`document-version`"
```

For information about other options you can use with the
**update-document** command, see [**update-document**](../../../cli/latest/reference/ssm/update-document.md "../../../cli/latest/reference/ssm/update-document.md") in the AWS Systems Manager section of
the _AWS CLI Command Reference_.
