

# Seeing `An error occurred (VcpuLimitExceeded)` in `slurm_resume.log` when I fail to run a job, or in `clustermgtd.log`, when I fail to create a cluster
<a name="compute-node-initialization-vpc-limit-v3"></a>

Check the vCPU limits on your account for the specific Amazon EC2 instance type that you are using. If you see zero or fewer vCPUs than you are requesting, request an increase for your limits. For information about how to view current limits and request new limits, see [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide*.