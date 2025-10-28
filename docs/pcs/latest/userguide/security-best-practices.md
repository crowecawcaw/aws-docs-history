# Security best practices for AWS Parallel Computing Service

This section describes security best practices that are specific to AWS Parallel Computing Service (AWS PCS). To learn more
about security best practices in AWS, see [Best Practices
for Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance "https://aws.amazon.com/architecture/security-identity-compliance").

## AMI-related security

- Don’t use AWS PCS sample AMIs for production workloads.
  The sample AMIs are unsupported and only intended for testing.
- Regularly update the operating system and software in the AMI for
  your compute node groups to mitigate vulnerabilities.
- Only use authenticated official AWS PCS packages downloaded
  from official AWS sources.
- Regularly update AWS PCS packages in the AMI for compute node groups
  and update the compute nodes to use the updated AMI. Consider automating
  this process to minimize vulnerabilities.

For more information, see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").

## Slurm Workload Manager security

- Implement access controls and network restrictions
  to secure Slurm control and compute nodes.
  Only allow trusted users and systems to submit jobs and
  access Slurm management commands.
- Use Slurm's built-in security features, such as Slurm authentication, to
  ensure that job submissions and communications are authenticated.
- Update Slurm versions to maintain smooth operations and cluster
  support.

###### Important

Any cluster that uses a version of Slurm that has reached _end
of support life_ (EOSL) is stopped immediately. Use the link at
the top of the user guide pages to subscribe to the AWS PCS documentation RSS
feed to receive notification when a Slurm version approaches EOSL.

For more information, see [Slurm versions in AWS PCS](slurm-versions.md "slurm-versions.md").

- Regularly rotate cluster secrets to maintain security compliance and remediate potential security compromises. This is required for HIPAA and FedRAMP compliance.

For more information, see [Rotating cluster secrets in AWS PCS](cluster-secret-rotation.md "cluster-secret-rotation.md").

## Monitoring and logging

- Use Amazon CloudWatch Logs and AWS CloudTrail to monitor and record actions
  in your clusters and AWS account.
  Use the data for troubleshooting and auditing.

## Network security

- Deploy your AWS PCS clusters in a separate VPC to isolate your HPC
  environment from other network traffic.
- Use security groups and network access control lists (ACLs) to
  control inbound and outbound traffic to AWS PCS instances and subnets.
- Use AWS PrivateLink or VPC endpoints to keep network traffic to between your
  clusters and other AWS services inside the AWS network.
  For more information, see [Access AWS Parallel Computing Service using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
