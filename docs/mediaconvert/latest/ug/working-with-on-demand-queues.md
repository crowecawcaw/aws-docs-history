# Working with on-demand queues

Your account starts with one on-demand queue, which is the default queue when you create
jobs. With on-demand queues, you pay based on usage. For pricing details, see [AWS Elemental MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/").

This section describes processing multiple jobs in parallel, creating additional queues,
viewing queues, updating queues, pausing or activating queues, and deleting
queues.

###### Topics

- [Processing multiple jobs in parallel](#queue-resources "#queue-resources")
- [Creating a queue](creating-queues.md "creating-queues.md")
- [Updating queues](updating-queue-status.md "updating-queue-status.md")
- [Viewing queue details](listing-queues.md "listing-queues.md")
- [Deleting a queue](deleting-a-queue.md "deleting-a-queue.md")

## Processing multiple jobs in parallel

The total number of jobs that you can process concurrently depends on the following:

Service quota for **Concurrent jobs per account**

Your account has a service quota for the maximum number of jobs
that MediaConvert can process at one time, across _all_ of your on-demand queues in the
current AWS Region. You can request an increase to this quota by
using the [Service
Quotas](https://console.aws.amazon.com/servicequotas/home/services/mediaconvert/quotas "https://console.aws.amazon.com/servicequotas/home/services/mediaconvert/quotas") console.

Service quota for **Concurrent jobs per on-demand
queue**

Your account has a service quota for the maximum number of concurrent jobs that are
available to any _individual_ on-demand
queue in the current AWS Region. You can request an increase to this
quota by using the [Service
Quotas](https://console.aws.amazon.com/servicequotas/home/services/mediaconvert/quotas "https://console.aws.amazon.com/servicequotas/home/services/mediaconvert/quotas") console.

Queue configuration for **Concurrent
jobs**

Each of your on-demand queues has a setting for Concurrent jobs, which is the maximum
number of jobs it can process at one time. This setting is constrained
by both of the above service quotas. With any individual queue, you can
set Concurrent jobs up to your service quota for Concurrent jobs
_per on-demand queue_. With
multiple on-demand queues, the total number of concurrent jobs combined
must also be less than or equal to your service quota for Concurrent
jobs _per account_.

When your on-demand queue is running at its maximum concurrent job count and a job
completes, MediaConvert selects the next job to process based on the job's
_priority_. For more information, see [Setting job priority](setting-the-priority-of-a-job.md "setting-the-priority-of-a-job.md").

If a job stays in a `SUBMITTED` state for too long instead of moving to
`PROGRESSING`, then your on-demand queue is likely already processing
the maximum number of concurrent jobs that it can. To address this, first [check how many unallocated jobs that you have
available](listing-queues.md "listing-queues.md"). If you have unallocated jobs available, you can either [increase the Concurrent job count for your
queue](updating-queue-status.md "updating-queue-status.md"), or you can [create a new
queue](creating-queues.md "creating-queues.md"). If you don't have unallocated jobs available, you can request an
increase to your quotas by using the [Service Quotas](https://console.aws.amazon.com/servicequotas/home/services/mediaconvert/quotas "https://console.aws.amazon.com/servicequotas/home/services/mediaconvert/quotas")
console.

If you occasionally need to process jobs right away:

1. Use job priority. Submit most of your jobs with a low priority
   setting, and submit high priority jobs with a higher priority. When you
   choose this option, you must wait for jobs that are already processing to
   complete before the higher priority jobs begin. For more information, see
   [Setting job priority](setting-the-priority-of-a-job.md "setting-the-priority-of-a-job.md").
2. Use multiple queues. Submit most of your jobs to a queue with a high concurrent job
   count, and submit high priority jobs to a different queue with a low
   concurrent job count. When you choose this option, you keep some transcoding
   resources idle, but available, until you need them.

You can also organize your jobs with multiple on-demand queues. For example, you
might run jobs for different workflows in separate queues. MediaConvert processes
these jobs across multiple queues in parallel. You can use [Tags](tagging-mediaconvert-resources.md "tagging-mediaconvert-resources.md") to keep track of jobs with
different workflows as well.

###### Performance testing

We recommend that you test any workflow with specific performance requirements. By
default, MediaConvert optimizes the performance of your queue for the most
common job types. If your workflow primarily includes a large number of jobs
that complete quickly, or if you have a question about your queue's performance,
contact [AWS
support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
