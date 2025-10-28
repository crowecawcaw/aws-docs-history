# Best practice 13.3 – Evaluate and adopt new cost-effective solutions

As AWS releases new services and features, it’s a best
practice to review your existing architectural decisions to
ensure that they remain cost effective. If a new or updated
service can support the same workload but in a much cheaper
way, consider implementing the change to reduce cost.

## Suggestion 13.3.1 – Set Service Quotas to control resource usage

Some AWS services allow setting Service Quotas per
account. Service Quotas should be established to prevent
runaway infrastructure deployment by accident. Ensure that
Service Quotas are set high enough to cover the expected
peak usage.

## Suggestion 13.3.2 – Pause and resume resources if the workload is not always required

Use automation to pause and resume resources when the
resource is unneeded. For example, stop development and
test Amazon RDS instances that are not used after working
hours.

## Suggestion 13.3.3 – Switch to a new service or take advantage of new features that can reduce cost

AWS consistently adds new capabilities to enable your
organization to leverage the latest technologies to
experiment and innovate more quickly. Your organization
should review new service releases frequently to
understand the price and performance, and determine if
such features can improve cost reduction.
