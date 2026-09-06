

# Moving a job to a different queue
<a name="setting-up-queue-hopping-to-avoid-long-waits"></a>

A job stays in a `SUBMITTED` state, waiting to be processed, until the queue that you submit it to has available resources. To prevent long wait times, you can configure your job to automatically move to another queue after a set amount of time. This is called *queue hopping*. 

The most common use case for queue hopping is to move jobs from a reserved queue to an on-demand queue during a spike in usage. For example, you might automatically move jobs that sit in a `SUBMITTED` state for longer than 10 minutes.

Keep the following definitions in mind with queue hopping.

**Submission queue**  
The queue that you originally submit a job to is its *submission* queue.

**Destination queue**  
The queue that your job moves to when it hops queues is its *destination* queue.

**Wait time**  
The amount of time your job waits in its submission queue until it can hop to its destination queue.

**Hop**  
A job *hops* when it moves from its submission queue to its destination queue after its wait time elapses. A job that moves queues is also referred to as a *hopped job*.

**Note**  
When you set up queue hopping from a reserved queue to an on-demand queue, MediaConvert bills you according to the queue type that your job ultimately runs in. If your job runs in a reserved queue, MediaConvert doesn't bill you separately for the job because the cost is already covered by what you pay for your reserved queue. If your job runs in an on-demand queue, MediaConvert bills you for the job at the on-demand rate. 

**Topics**
+ [Setting up queue hopping](setting-up-queue-hopping.md)
+ [Setting priority for hopped jobs](job-priority-and-queue-hopping.md)
+ [Using accelerated transcoding with hopped jobs](accelerated-transcoding-queue-hopping.md)
+ [Viewing hopped job history](job-queue-hopping-history.md)
+ [Understanding queue hopping with paused queues](queue-hopping-with-paused-queues.md)