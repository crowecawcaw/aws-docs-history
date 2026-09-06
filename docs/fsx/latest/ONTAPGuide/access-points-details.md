

# Viewing access point details
<a name="access-points-details"></a>

This section explains how to view the details of S3 access points using the AWS Management Console, AWS Command Line Interface, or REST API.

## To view the details of S3 access points attached to an FSx for ONTAP volume (Amazon FSx console)
<a name="access-points-details-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to the volume that is attached to the access point whose details you want to view.

1. Choose **S3** to display the list of access points attached to the volume.

1. Choose the access point whose details you want to view.

1. Under **S3 access point attachment summary**, view configuration details and properties for the selected access point.

   The **File system user identity** configuration and the **S3 access point permissions** policy are also listed for the access point attachment.

1. To view the access point's S3 configuration in the Amazon S3 console, choose the S3 access point name displayed under **S3 access point**. It takes you to the access point's detail page in the Amazon S3 console.