# Performing a failback with Elastic Disaster Recovery

Failback is the act of redirecting traffic from your recovery system to your primary system.
This is an operation that is performed outside of AWS Elastic Disaster Recovery. AWS Elastic Disaster Recovery assists you in performing the failback by ensuring that the state of your primary system is
up to date with the state of your recovery system.

Failback is only supported to AWS and non-AWS environments that can boot
up from an ISO. For non-AWS environments which do not support ISO boot, we recommend
that you convert the ISO to a suitable format. Examples - [Building a disaster recovery site on AWS for workloads on Microsoft Azure](https://aws.amazon.com/blogs/storage/building-a-disaster-recovery-site-on-aws-for-workloads-on-microsoft-azure/ "https://aws.amazon.com/blogs/storage/building-a-disaster-recovery-site-on-aws-for-workloads-on-microsoft-azure/")
and [Building a disaster recovery site on AWS for workloads on Google Cloud](https://aws.amazon.com/blogs/storage/building-a-disaster-recovery-site-on-aws-for-workloads-on-google-cloud-part-1/ "https://aws.amazon.com/blogs/storage/building-a-disaster-recovery-site-on-aws-for-workloads-on-google-cloud-part-1/").
These blog posts are not maintained or supported by &AWS; Premium Support and
guidance for these are provided on a best effort basis.

Before performing a failback, make sure that any data that was written to your
failover systems during the failover is replicated back to your original systems before
you perform the actual failback and before redirecting users to your primary systems.
AWS Elastic Disaster Recovery helps you prepare for failback by replicating the data from your Recovery
instances on &AWS; back to your source servers with the aid of the Failback Client.
