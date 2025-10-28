# Saving costs on Single-account landing zone (SALZ) bastions

AMS provides two SSH bastions and two RDP bastions in the default configuration for you to connect to your Amazon EC2
instances, and also deploys two DMZ bastions in the default configuration for service operations.
The bastions use m4. large Amazon EC2 instances by default. You have an option to change the Amazon EC2 instances used for bastions to t3.small, and save cost.

If you are using on-demand instances, or spot instances, or a savings plan, you should consider this feature,
and save costs. If you use Reserved Instances consider if using t3.small instances might lower your costs.
To change the instance type, submit an RFC with Management | Advanced stack components | EC2 instance stack | Resize (ct-15mazjj88xc69) CT from
your AMS account.

Contact your cloud service delivery manager (CSDM) for additional questions, or to check if you can benefit from this feature.
