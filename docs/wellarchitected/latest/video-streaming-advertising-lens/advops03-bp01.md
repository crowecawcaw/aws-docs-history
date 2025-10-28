# ADVOPS03-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload

Develop incident response playbooks that provide a structured
framework to manage common operational events and incidents. These
playbooks outline step-by-step procedures tailored to specific
types of incidents, which helps your teams act swiftly and
consistently and reduces the likelihood of human error.
Organizations can enhance their incident response capabilities by
incorporating best practices and using AWS services. These best
practices also enable them to mitigate risks and maintain
operational resilience in the face of challenges.

## Implementation guidance

Use auto scaling and load balancing features provided by AWS
services like Amazon EC2 Auto Scaling and Elastic Load Balancing
(ELB) to handle sudden traffic spikes and provide high
availability.

Auto scaling and load balancing may not always be sufficient to
address capacity constraints, especially for EC2 instances. In
such cases, consider the following:

- Implement a process to submit on-demand capacity requests (ODCRs) to secure
  additional Amazon EC2 capacity, particularly for anticipated high-traffic events like
  marketing campaigns.
- Monitor Amazon EC2 resource utilization and capacity metrics closely, and document
  runbooks for quickly scaling up or down resources as needed.
- Use AWS Auto Scaling for predictive scaling based on historical data and scheduled scaling
  for planned events to proactively adjust capacity.
- Incorporate capacity planning and optimization practices using AWS Cost Explorer and
  AWS Trusted Advisor to optimize resource utilization.
