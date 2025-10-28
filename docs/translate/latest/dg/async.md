# Asynchronous batch processing with Amazon Translate

To translate large collections of documents (up to 5 GB in size), use the Amazon Translate
asynchronous batch processing operation, [StartTextTranslationJob](../APIReference/API_StartTextTranslationJob.md "../APIReference/API_StartTextTranslationJob.md"). This is best for
collections of short documents, such as social media postings or user reviews, or any situation in which
instantaneous translation is not required.

To perform an asynchronous batch translation, you typically perform the following
steps:

1. Store a set of documents in an input folder inside of an Amazon S3 bucket.
2. Start a batch translation job.
3. As part of your request, provide Amazon Translate with an IAM role that has read access to
   the input Amazon S3 folder and all its sub-folders. The role must also have read and write
   access to an output Amazon S3 bucket.
4. Monitor the progress of the batch translation job.
5. Retrieve the results of the batch translation job from the specified output
   bucket.

## Region availability

Batch translation is supported in the following AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)

###### Topics

- [Prerequisites for batch translation jobs](async-prereqs.md "async-prereqs.md")
- [Running a batch translation job](async-start.md "async-start.md")
- [Monitoring and analyzing batch translation jobs](async-monitor.md "async-monitor.md")
- [Getting batch translation results](async-results.md "async-results.md")
