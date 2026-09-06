

# Job lifecycle
<a name="job-lifecycle"></a>

Jobs progress through the following states:

Pending  
New jobs begin in this state while waiting for processing resources.

Running  
The job has started and is actively processing data.

Completed  
The job has finished successfully and results are available in your designated Amazon S3 output location.

Failed  
The job enters this state if errors occur during processing. You can obtain error details using the `GetJob` operation.

Cancelling  
The job enters this state temporarily when you explicitly cancel it using the `CancelJob` operation.

Cancelled  
The job enters this state when the `CancelJob` operation finishes stopping the job.