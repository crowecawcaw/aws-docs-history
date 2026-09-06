# Connect a Deadline Cloud fleet to FSx for OpenZFS through a VPC resource endpoint

The smf\_vpc\_fsx CloudFormation template deploys a Deadline Cloud service-managed fleet
that connects to FSx for OpenZFS storage through a VPC resource endpoint.
The FSx cluster runs in a VPC, and a VPC Lattice resource configuration
establishes the connection between Deadline Cloud workers and the storage. The
resource configuration is shared with the Deadline Cloud service through AWS RAM. For
the template source, see
[smf\_vpc\_fsx](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/smf_vpc_fsx "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/smf_vpc_fsx")
on the GitHub website.

Use this pattern when you need Deadline Cloud workers to access the
following:

- Shared file storage such as FSx for Lustre, FSx for OpenZFS, or
  EFS.
- License servers running in your VPC.
- Other private resources that aren't accessible from the public
  internet.
  Deployment requires two steps because the FSx IP address is only
  available after the file system creates its network interface. After the
  initial stack reaches `CREATE_COMPLETE` (about 10–15 minutes
  for FSx), update the stack with the FSx IP to complete the
  configuration.
