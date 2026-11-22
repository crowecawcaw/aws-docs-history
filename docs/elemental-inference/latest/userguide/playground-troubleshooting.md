

# Troubleshooting

MediaConvert queue limit reached  
If your account has reached its MediaConvert queue limit, the console can't create the playground queue. Delete an unused MediaConvert queue, or request a queue limit increase, and then try again.

A job stays in Queued  
The playground queue lets its jobs use only one Elemental Inference feed at a time, so a new Smart Cropping job waits in **Queued** until the Smart Cropping jobs ahead of it finish.

Another preview is running  
Your account runs one preview at a time. If another preview is using it, for example one left running in a tab that has since closed, choose **Stop the other preview**, and then choose **Stop it**. This deletes the other preview's feed. If that preview is still running in another tab or browser, it stops there and its results aren't saved.

A preview fails because of the frame rate  
If the source video's frame rate is above 60 fps, the preview fails, and **Error details** says that the video frame rate should be at most 60 fps. Use a video at 60 fps or less, or convert the video to a lower frame rate, and then start a new preview.

A preview fails because of the active feed quota  
If your account has reached its Active feeds per account quota in the Region, the preview can't start its feed. The preview page shows **Preview failed**. **Error details** says that you've reached the quota of active feeds. To free a feed, archive a feed that you no longer need, or request a quota increase. Then choose **Run again**. For more information, see [Quotas for AWS Elemental Inference](quotas.md).

A job fails with access denied on an encrypted output bucket  
If the output bucket uses SSE-KMS with a customer managed key, the job or preview fails with an access denied error when MediaConvert writes the output. Add the AWS KMS permissions described in [Service role](playground-service-role.md) and [User permissions](playground-user-permissions.md). Then submit a new job, or choose **Run again** for a preview.

A preview failed  
If a preview fails, the preview page shows **Preview failed**. Choose **Error details** to see the cause. If MediaConvert couldn't open the input, check that the file exists, is an MP4 file, and that the service role can read it, and then start a new preview. For other failures, choose **Run again**.