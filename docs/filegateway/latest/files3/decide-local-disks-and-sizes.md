# Deciding the amount of local disk

storage

When deploying an S3 File Gateway, consider how much cache disk to allocate.
S3 File Gateway uses a least recently used algorithm to automatically evict
data from the cache. The cache on an S3 File Gateway is shared between all of the file shares on
that gateway. If you have multiple active shares, it's important to note that heavy
utilization on one share could impact the amount of cache resources that another share
has access to, possibly impacting performance.

When determining how much cache disk you need for a given workload, it's important to
note that you can always add cache disk to your gateway (up to the current quotas on
S3 File Gateway), but you can't decrease the cache for a given gateway. You can
perform a basic analysis on the dataset to determine the right amount of cache disk, but
there's not a way to determine exactly how much data is ‘hot,’ and needs to be stored
locally, versus ‘cold’ and can be tiered to the cloud. Workloads change over time, and
S3 File Gateway provides flexibility and elasticity related to the amount of
resources that can be consumed. The amount of cache can always be increased, so starting
small and increasing as needed is often the most cost-effective approach.

You can use an initial approximation of 150 GiB to provision disks for the cache
storage during gateway setup. You can then use Amazon CloudWatch operational metrics to monitor
the cache storage usage and provision more storage as needed using the console. For
information on using the metrics and setting up alarms, see [Performance and optimization](Performance.md "Performance.md").

###### Note

Underlying physical storage resources are represented as a data store in VMware.
When you deploy the gateway VM, you choose a data store on which to store the VM
files. When you provision a local disk (for example, to use as cache storage), you
have the option to store the virtual disk in the same data store as the VM or a
different data store.

If you have more than one data store, we strongly recommend that you choose one
data store for the cache storage. A data store that is backed by only one underlying
physical disk can lead to poor performance in some situations when it is used to
back both the cache storage. This is also true if the backup is a less-performant
RAID configuration such as RAID1.
