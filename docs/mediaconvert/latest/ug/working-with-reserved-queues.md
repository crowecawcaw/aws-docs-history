# Working with reserved queues in

AWS Elemental MediaConvert

With reserved queues, you can purchase transcoding capacity for a 12-month period. The
following topics provide information about working with reserved queues, such as
creating and deleting queues, and allocating resources.

Reserved queues differ from on-demand queues in how AWS Elemental MediaConvert allocates transcoding
resources for jobs and in how you pay for your transcoding.

###### Note

There are a few features that you can't use with jobs that you send to a
reserved queue. For more information, see [Limitations](feature-limitations-with-reserved-queues.md "feature-limitations-with-reserved-queues.md").

When you set up your reserved queue, you choose how many jobs it can run at once by
specifying the number of reserved transcode slots (RTS) in the queue. For
example, if you send five jobs to a reserved queue with two RTS, MediaConvert
immediately begins processing the first two jobs that you submit, and it holds
the other three in the queue. When one of the jobs that MediaConvert is
processing finishes, the service begins processing the next job.

Each RTS has its own dedicated computing resources. Therefore, when MediaConvert
processes a job that you send to a reserved queue, it takes the same amount of
time to process whether the queue has one RTS or multiple RTS.

When a job in a reserved queue finishes, MediaConvert selects the next job to
process based on the job's priority. You set the priority of a job when you
create it. If more than one job has the highest priority, MediaConvert begins
the one that you submitted first. For more information, see [Setting job priority](setting-the-priority-of-a-job.md "setting-the-priority-of-a-job.md").

###### Topics

- [Pricing for reserved queues](how-you-pay-for-reserved-queues.md "how-you-pay-for-reserved-queues.md")
- [Simulating a reserved
  queue](simulating-a-reserved-queue.md "simulating-a-reserved-queue.md")
- [Creating a reserved queue](creating-a-reserved-queue.md "creating-a-reserved-queue.md")
- [Editing a reserved queue](editing-reserved-queues.md "editing-reserved-queues.md")
- [Purchasing additional RTS](purchasing-additional-capacity-for-a-reserved-queue.md "purchasing-additional-capacity-for-a-reserved-queue.md")
- [Purchasing additional RTS for an expired reserved queue](purchasing-a-new-contract-for-an-existing-reserved-queue.md "purchasing-a-new-contract-for-an-existing-reserved-queue.md")
- [Listing reserved queues](listing-viewing-reserved-queues.md "listing-viewing-reserved-queues.md")
- [Deleting a reserved
  queue](deleting-a-reserved-queue.md "deleting-a-reserved-queue.md")
- [Limitations](feature-limitations-with-reserved-queues.md "feature-limitations-with-reserved-queues.md")
