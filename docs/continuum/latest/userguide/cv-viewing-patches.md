

# Viewing generated patches
<a name="cv-viewing-patches"></a>

Review generated patches to understand the proposed code changes before you apply them. You can download available patches in the AWS Continuum console and check their delivery to your code sources.

## Viewing and downloading a patch
<a name="cv-viewing-patches-console"></a>

Before you begin, your environment must have an issue with a generated patch. You can review the changes and download a patch file for a code source.

**To view and download a patch**

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**.

1. Choose the name of the environment that contains the issue.

1. Choose the **Issues** tab.

1. Choose the title of the issue that you want to review.

1. Choose **View patch** for your source to open its generated patch in **Patch details**.

1. To download the patch file, choose the source's **Download patch** icon, labeled **Download patch for {{source name}}**.

Your browser saves the downloaded patch as a `.patch` file.

## Checking patch delivery
<a name="cv-viewing-patches-delivery"></a>

When you select **Automatically deliver remediation patches** for an environment, AWS Continuum attempts to deliver generated patches to your code sources. For GitHub, AWS Continuum creates pull requests. For Amazon S3, AWS Continuum uploads patch files under `continuum-patches/` in your bucket.

On the issue details page, you can check the delivery destination and status. For a GitHub source, choose **View pull request** when the console displays that link.

In **Patch details**, choose the source's information icon, labeled **Patch information for {{source name}}**. The popover shows **Destination** when available. For Amazon S3, this value identifies the bucket and patch object.

To check delivery status and failure details, choose the issue's **Patch delivery** status. You can download an available patch from the console even if delivery to your code source fails.

For instructions on configuring the Amazon S3 integration role's patch permissions, see [Granting access to the bucket](cv-getting-started.md#cv-getting-started-s3-role). For information about console permissions, see [Using the AWS Continuum console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console).