# Frequently asked questions about Slurm versions in

AWS PCS

AWS PCS maintains support for multiple Slurm versions. When a new Slurm version is
introduced, AWS PCS provides technical support and security patches until that version
reaches its end of support (EOS) from SchedMD. AWS PCS refers to the EOS date for a Slurm
version as end of life (EOL) to be consistent with AWS terminology.

###### How long does AWS PCS support a Slurm version?

AWS PCS support for Slurm versions aligns with SchedMD’s support cycles for major
versions. AWS PCS supports the current version and the 2 most recent previous major
versions. When SchedMD releases a new major version, AWS PCS ends support for the oldest
supported version. AWS PCS releases new major versions of Slurm as soon as possible but
there might be a delay between SchedMD's release and its availability in AWS PCS.

###### How do my clusters get new Slurm patch version releases?

To address bugs and security fixes, AWS PCS is designed to automatically apply
patches to cluster controllers that run in internal service-owned accounts. To install
patches on EC2 instances in your AWS account, update the Amazon Machine Image (AMI) for
your compute node groups and update the compute node groups to use the updated AMI. For
more information, see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").

###### Note

Slurm controllers are unavailable while we update them. Running jobs aren't affected.
Jobs submitted before the cluster's controller became unavailable are held until the
controller is available.

###### How am I informed about an upcoming Slurm version EOL event?

We send you an email message 6 months before the EOL date. We send you an email
message each month before the EOL, with a final email message 1 week before the EOL
date. After the EOL date, we send monthly email messages for 12 months to customers
running AWS PCS clusters with EOL Slurm versions. We might suspend a cluster with an EOL
Slurm version if security vulnerabilities are identified for that version.

###### How can I determine if the Slurm version used by my cluster is running an EOL Slurm

version?

We send you an email message to notify you that you have a running cluster with an EOL
Slurm version. We post an alert to the AWS Health Dashboard alerts that contains the details
of your clusters with EOL Slurm versions. You can also use the AWS PCS console to
identify the clusters with EOL Slurm versions.

###### What do I have to do if my Slurm version is near or beyond EOL?

Create a new cluster with a newer supported version of Slurm and update the Slurm
version in your compute node group AMIs. The Slurm version in your AMIs and running EC2
instances can’t be more than 2 versions behind the cluster’s Slurm version. For more
information, see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").

###### What will happen if I don’t switch to a newer version of Slurm by the EOL

date?

You can’t create new clusters with an EOL Slurm version. Existing clusters can operate
for up to 12 months without AWS support, and no immediate action is required to maintain
their operation. After the EOL date, support, security updates, and availability are not
guaranteed. We might suspend a cluster for security reasons. We strongly recommend
you use a supported Slurm version to maintain security and support for your AWS PCS
clusters.

###### What are the risks of operating a cluster with EOL Slurm versions?

Clusters with EOL Slurm versions present significant security and
operational risks. Without SchedMD's active monitoring, security vulnerabilities might
remain undetected or unaddressed. If critical vulnerabilities are discovered, we might
suspend your clusters immediately.

###### What happens to my jobs, cluster compute, storage and networking resources when my

cluster is suspended?

All resources managed by AWS PCS are terminated. This includes the Slurm controller,
compute node groups, and EC2 instances. Any jobs running on compute instances are
immediately terminated, and the cluster enters a suspended state. Customer-managed
resources, such as external file systems, remain intact. You can use the AWS PCS console
and API actions to access the cluster's configuration.

###### Can I restart a suspended cluster to resume its remaining jobs?

No, you can’t restart a suspended cluster. You can use your suspended cluster’s
configuration to create a new cluster with a supported Slurm version. You can run your
remaining jobs if you saved them in an external file system.

###### Can I request an extension beyond the 12-month grace period?

No, you can’t request an extension to run your cluster beyond the 12-month grace
period. We provide the extended time to help you switch to a supported Slurm version. To
avoid disruption to your cluster operations, we recommend you switch before your Slurm
version reaches EOL.
