

# Troubleshooting
<a name="playground-troubleshooting"></a>

If you have trouble using the playground, review the following issues and solutions.

MediaConvert queue limit reached  
If your account has reached its MediaConvert queue limit, the console can't create the playground queue. Delete an unused MediaConvert queue, or request a queue limit increase, and then try again.

The service role doesn't cover the selected bucket  
If the service role doesn't grant access to the input or output location you chose, choose **Update role permissions** before you submit the job. The update removes the role's access to buckets that it covered before.

A video can't be previewed  
If the output's format or codec isn't supported for browser playback, the preview can't play it. This doesn't affect the job; the file was processed successfully. Open it in MediaConvert, or download it from Amazon S3.

A job stays in Queued  
Because the playground queue runs one job at a time, a new job waits in **Queued** until capacity is available, and then begins processing.