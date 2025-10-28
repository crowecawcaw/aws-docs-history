# Sharing a job

You can share a job by using the MediaConvert console, AWS CLI, or API/SDK.

MediaConvert Console
To share a job by using the MediaConvert console:

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in the
   MediaConvert console.
2. Choose the **Job ID** for the job you want to
   share to view its **Job summary** page.
3. In the **Job details** section, choose
   **Share with Support**.
4. In the **Share job resources** dialog box,
   enter your active support case ID in the format
   `case-1234`.
5. Choose **Share** to submit the
   request.
6. The console displays a confirmation message when the request
   is successfully queued for processing.

AWS Command Line Interface (CLI)
The following example creates a resource share for a specific job and
support case.

###### To share a job by using the AWS CLI

1. Identify the job ID and support case ID you want to
   use:
   - _Job ID_: The MediaConvert job identifier
     (for example, `1740995632451-jkmq89`)
   - _Support case ID_: Your active
     support case identifier in the format
     `case-1234`

2. Create the resource share with the AWS CLI:

```
aws mediaconvert create-resource-share \
    --job-id "1740995632451-jkmq89" \
    --support-case-id "case-1234" \
    --region us-west-2
```

3. The API returns an HTTP 202 Accepted response when the request
   is successfully queued for processing.

For more information about the Share API, see the [MediaConvert API Reference](../apireference/resourceshares.md "../apireference/resourceshares.md").

After you create a share request, monitor its status by checking the job details with the `GetJob` API. The job response includes share status information.
