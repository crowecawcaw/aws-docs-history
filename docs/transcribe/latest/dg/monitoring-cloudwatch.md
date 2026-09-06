

# Monitoring Amazon Transcribe with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor Amazon Transcribe using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [*CloudWatch User Guide*](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

## Using Amazon CloudWatch metrics and dimensions with Amazon Transcribe
<a name="monitoring-cwmetrics"></a>

Amazon Transcribe supports CloudWatch metrics and dimensions, which are data that can help you monitor performance. Supported metrics categories include traffic, errors, data transfer, and latency associated with your transcription jobs. Supported metrics are located through CloudWatch in the **AWS/Transcribe** namespace.

**Note**  
CloudWatch monitoring metrics are free of charge and don't count against CloudWatch service quotas.

For more information on CloudWatch metrics, see [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html).


**CloudWatch metrics for Amazon Transcribe**  

| Metric | Service Type | Description | 
| --- | --- | --- | 
| TotalRequestCount | batch, streaming | Shows the number of transactions. Represents all successful and unsuccessful requests made to Transcribe.<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation`, `LanguageCode` | 
| SuccessfulRequestCount | batch | Shows the number of successful requests. The response code range for a successful request is 200-299.<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 
| SyncServerErrorCount | batch | Shows the number of server errors. The response code range for a server error is 500-599.<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 
| SyncUserErrorCount | batch | Shows the number of user errors, such as parameters, files, and permissions that are not valid, and throttling errors. The response code range for a user error is 400-499. <br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 
| ThrottledCount | batch, streaming | Shows the number of requests that return a **LimitExceededException** resulting from an exceeded transaction rate quota. Amazon Transcribe limits the number of requests a customer can make per second. If the quota limit set for your AWS account is frequently exceeded, you can request a quota increase. To request an increase, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 
| LimitExceededCount | batch, streaming | Shows the number of requests that return a **LimitExceededException** resulting from an exceeded non-rate quota. Amazon Transcribe limits the number of concurrent jobs, total number of transcriptions, maximum audio file size, etc. If the limit set for your AWS account is frequently exceeded, you can request a quota increase. To request an increase, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 
| ConcurrentJobsCount | batch | The number of concurrent transcription jobs.<br />**Unit**: count<br />**Relevant Statistics**: average, maximum<br />**Valid Dimensions**: `Domain`, `ServiceType` | 
| AsyncUserErrorCount | batch | The number of asynchronous (backend) user errors, such as: given audio format does not match that detected, invalid sample rate, customer Amazon S3 access error.<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation`<br />**Operations**: `StartCallAnalyticsJob`, `StartMedicalTranscriptionJob`, `StartTranscriptionJob`, `CreateMedicalVocabulary`, `CreateVocabulary`, `UpdateMedicalVocabulary`, `UpdateVocabulary` | 
| AsyncServerErrorCount | batch | The number of asynchronous (backend) server errors or, more specifically, automatic speech recognition (ASR) processing errors. <br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation`<br />**Operations**: `StartCallAnalyticsJob`, `StartMedicalTranscriptionJob`, `StartTranscriptionJob`, `CreateMedicalVocabulary`, `CreateVocabulary`, `UpdateMedicalVocabulary`, `UpdateVocabulary` | 
| AudioDurationTime | batch | The length, in seconds, of an audio or video file.<br />**Unit**: seconds<br />**Relevant Statistics**: average, minimum, maximum<br />**Valid Dimensions**: `Domain`, `ServiceType`, `LanguageCode` | 
| ConcurrentStreamsCount | streaming | Shows the number of concurrent streams currently being processed.<br />**Unit**: count<br />**Relevant Statistics**: average, maximum<br />**Valid Dimensions**: `Domain`, `ServiceType` | 
| ConcurrentPostStreamJobsCount | streaming | Shows the number of concurrent AWS HealthScribe post-stream analytics currently being processed.<br />**Unit**: count<br />**Relevant Statistics**: average, maximum<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 
| PostStreamJobLimitExceededCount | streaming | Shows the number of requests that return a `LimitExceededException` resulting from an exceeded quota on concurrent post stream job limit.<br />**Unit**: count<br />**Relevant Statistics**: sum, average<br />**Valid Dimensions**: `Domain`, `ServiceType`, `Operation` | 


**CloudWatch dimensions for Amazon Transcribe**  

| Dimension | Description | 
| --- | --- | 
| Domain | Only shows metrics with the specified Transcribe type.<br />**Valid Options**: Transcribe, Transcribe Medical, Transcribe Call Analytics | 
| ServiceType | Only shows metrics with the specified service type.<br />**Valid Options**: batch | 
| Operation | Only shows metrics with the specified operation.<br />**Valid Options**: any Amazon Transcribe API | 
| LanguageCode | Only shows metrics with the specified language.<br />**Valid Options**: any valid language code, in the form `en-US` | 