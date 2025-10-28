# FSIREL02: Are you practicing continuous resilience to ensure that your services

meet regulatory availability and recovery requirements?

Your workload, and the environment in which it operates, is constantly changing. To
keep pace, resiliency practices should not be considered a one-time effort. Make
resilience a regular part of your feature delivery and operational cadence throughout a
workload's lifetime.

## FSIREL02-BP01 Practice regular resilience testing

Resilience is not a one-time effort. Resilience should be part of your day-to-day
operations and practiced continuously. Perform chaos engineering experiments and scenario testing like AZ Availabilty Power Interruption or Cross-Region connectivity faults regularly to increase your team's understanding of how your workload behaves in adverse conditions such as excessive load, slow or failed network links, or a combination of adverse conditions. Continuous testing for resilience helps you to anticipate,
observe, and respond to faults, as well as find blind spots that you didn’t know
existed. By practicing continuous resilience testing and chaos engineering, your teams can improve observability and gain confidence in their ability to quickly detect and recover from incidents as recovery procedures are practiced and improved.

## FSIREL02-BP02 Implement an operational readiness review

process

To capture learnings from previous incidents and minimize reoccurrence across
teams, implement an [operational readiness review
process](../operational-readiness-reviews/wa-operational-readiness-reviews.md "../operational-readiness-reviews/wa-operational-readiness-reviews.md") within your organization. As part of your incident
analysis process, identify key questions that, if asked prior to the incident, may
have prevented the incident from occurring. Maintain a list of these key questions so
that, as new features are released, your developers can refer back to the list and
make sure that they don't repeat the same mistakes that have disrupted other
workloads.
