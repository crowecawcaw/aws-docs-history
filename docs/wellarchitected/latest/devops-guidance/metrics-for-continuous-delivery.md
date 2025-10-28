# Metrics for continuous delivery

- **Pipeline stability**: The
  percentage of deployments that encounter failures, which
  includes failed deployments, required rollbacks, and
  incidents directly linked to deployments. This metric
  provides insight into the reliability and efficiency of
  the continuous delivery pipeline, with a focus on its
  configuration, infrastructure, and the quality of the code
  being deployed. A high rate of these failures suggests the
  continuous delivery pipeline may need refinement. Examine
  the continuous delivery pipeline logs and calculate the
  failure percentage based on the total number of
  deployments over a specific period. This should account
  for both direct deployment failures and deployments that
  required subsequent rollbacks or led to incidents.
- **Mean time to production
  (MTTP):** The average time taken from the moment
  a code change is merged to when it's live in the
  production environment. This demonstrates how quickly
  features, bug fixes, or changes get delivered to end
  users. Improve this metric by streamlining deployment
  processes, automate testing, reduce manual interventions,
  and optimize infrastructure provisioning. Calculate this
  metric using timestamps from merge events and production
  deployment events, then calculate the average difference
  over a given period.
- **Operator
  interventions**: The number of deployments
  run without human intervention, signifying the level
  of automation and reliability in the deployment process. A
  higher count might indicate potential areas for automation
  or optimization. Improve this metric by reducing toil by
  increasing automation in the deployment pipeline, reducing
  manual testing and verification, and establishing trust in
  automated processes. Monitor deployment logs and count the
  number of deployments that required manual interventions.
  Aggregate the count over a set period, such as weekly or
  monthly.
- **Number of changes per
  release**: The number of changes included in each
  release of the software. It can include changes to code,
  configuration, or other components of the system. A high
  number of changes per release may indicate batching of
  work and a lack of continuous integration. This can lead
  to longer lead times, increased risk of defects, and
  reduced ability to troubleshoot issues. The ideal number
  of changes per release will depend on the specific needs
  of the organization and the system being developed, and
  should be continually evaluated and adjusted as needed.
  Track this metric using release notes, change logs, or
  commit metadata for each release. For each release, count
  the number of distinct changes that were included.
- **Deployment
  frequency**: The frequency at which code is
  deployed to a production environment. It helps teams
  understand how quickly they can deliver changes,
  enhancements, and fixes to users at a rapid pace. A higher
  deployment frequency often correlates with a faster
  feedback loop resulting not only from continuous delivery,
  but other mature DevOps practices like quality assurance
  and observability as well. Lower frequency of deployments
  may indicate manual or batched deployment processes,
  bottlenecks in the release pipeline, or a more cautious
  release strategy. Aim for a balance between high
  deployment frequency and system stability. Regularly
  review deployment logs to count the number of successful
  deployments over a given period, such as daily, weekly, or
  monthly.
