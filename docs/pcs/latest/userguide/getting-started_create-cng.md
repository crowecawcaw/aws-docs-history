# Create compute node groups in AWS PCS

A compute node group is virtual collection of compute nodes (EC2 instances) that AWS PCS
launches and manages. When you define a compute node group, you specify common traits such as EC2
instance types, minimum and maximum instance count, target VPC subnets, preferred purchase option,
and custom launch configuration. AWS PCS eﬃciently launches, manages, and terminates compute nodes
in a compute node group, according to these settings. The demonstration cluster uses a compute
node group to provide login nodes for user access, and a separate compute node group to process
jobs. The following topics describe the procedures to set up these compute node groups in your
cluster.

###### Topics

- [Create an instance profile for AWS PCS](getting-started_create-cng_instance-profile.md "getting-started_create-cng_instance-profile.md")
- [Create launch templates for AWS PCS](getting-started_create-cng_launch-templates.md "getting-started_create-cng_launch-templates.md")
- [Create compute node group for login
  nodes in AWS PCS](getting-started_create-cng_login-nodes.md "getting-started_create-cng_login-nodes.md")
- [Create compute node group for running compute
  jobs in AWS PCS](getting-started_create-cng_workers.md "getting-started_create-cng_workers.md")
