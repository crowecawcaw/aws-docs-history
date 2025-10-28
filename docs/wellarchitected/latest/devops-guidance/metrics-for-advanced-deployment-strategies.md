# Metrics for advanced deployment strategies

- **Rollback
  frequency**: This metric measures how often
  changes need to be rolled back. While a higher rollback
  frequency may indicate issues with the deployment process
  or inadequate quality assurance capabilities, it can also
  suggest successful usage of advanced deployment strategy
  capabilities with automation facilitating fast rollbacks
  to minimize user risk. Track this by counting the number
  of rollbacks and comparing it to the total number of
  deployments.
- **Deployment lead
  time**: The average time required to successfully
  deploy a feature or service from the moment a deployment
  is triggered to when it is live in an environment. Using
  this metric, teams can pinpoint bottlenecks in the
  deployment process. Enhance this metric by optimizing
  deployment strategies, utilizing distributed
  architectures, or deploying in waves to strike a balance
  between speed and safety. Measure the duration from when
  the deployment is triggered to its completion, considering
  only successful deployments, and calculate the average
  over a specific time frame, such as weekly or monthly.
- **Release frequency**: The
  frequency at which changes become accessible to end users.
  This metric distinguishes between deployments, which
  introduces new code or configurations into an environment,
  and releases, which make those changes accessible to end
  users. A high release frequency can indicate mature DevOps
  capabilities which enable releasing small, incremental
  changes that are automatically deployed and verified with
  confidence. Measure release frequency by counting the
  number of releases to production over a specified period.
  Compare this metric to deployment frequency to understand
  the correlation and derive additional insights.
- **Mean time to recover
  (MTTR)**: The average time taken to restore a
  system after a failure. This metric provides insight into
  the team's ability to quickly detect and address
  production issues. A lower MTTR indicates safer deployment
  practices, the use of automated rollbacks, and effective
  governance, quality assurance, and observability
  capabilities. Measure the total amount of downtime and
  divide it by the total number of incidents within a
  specific time frame.
