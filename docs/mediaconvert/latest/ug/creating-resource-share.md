

# Sharing a job
<a name="creating-resource-share"></a>

You can share a job by using the MediaConvert console, AWS CLI, or API/SDK.

------
#### [ MediaConvert Console ]

To share a job by using the MediaConvert console:

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Choose the **Job ID** for the job you want to share to view its **Job summary** page.

1. In the **Job details** section, choose **Share with Support**.

1. In the **Share job resources** dialog box, enter your active support case ID in the format `case-1234`.

1. Choose **Share** to submit the request.

1. The console displays a confirmation message when the request is successfully queued for processing.

------
#### [ AWS Command Line Interface (CLI) ]

The following example creates a resource share for a specific job and support case.

**To share a job by using the AWS CLI**

1. Identify the job ID and support case ID you want to use:
   + *Job ID*: The MediaConvert job identifier (for example, `1740995632451-jkmq89`)
   + *Support case ID*: Your active support case identifier in the format `case-1234`

1. Create the resource share with the AWS CLI:

   ```
   aws mediaconvert create-resource-share \
       --job-id "1740995632451-jkmq89" \
       --support-case-id "case-1234" \
       --region us-west-2
   ```

1. The API returns an HTTP 202 Accepted response when the request is successfully queued for processing.

For more information about the Share API, see the [MediaConvert API Reference](https://docs.aws.amazon.com/mediaconvert/latest/apireference/resourceshares.html).

------

After you create a share request, monitor its status by checking the job details with the `GetJob` API. The job response includes share status information.