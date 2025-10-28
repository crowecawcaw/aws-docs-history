# Manage labeling requests with an Amazon SQS queue

When Ground Truth creates your streaming labeling job, it creates an Amazon SQS
queue in the AWS account used to create the labeling job. The queue name is
`GroundTruth-`labeling_job_name` where`labeling_job_name`` is the name of
your labeling job, in lowercase letters. When you send data objects to your
labeling job, Ground Truth either sends the data objects directly to workers or places
the task in your queue to be processed at a later time. If a data object is not
sent to a worker after 14 days, it expires and is removed from the queue. You
can setup an alarm in Amazon SQS to detect when objects expire and use this mechanism
to control the volume of objects you send to your labeling job.

###### Important

Modifying, deleting, or sending objects directly to the Amazon SQS
queue associated with your streaming labeling job may lead to job
failures.
