# Metrics for everything as code

- **Infrastructure code coverage**: The percentage of
  infrastructure components managed by infrastructure as code (IaC) compared to the total
  number. High infrastructure code coverage implies improved manageability,
  reproducibility, and automation capabilities for systems. Calculate by dividing the
  number of infrastructure components managed as code by the total number of
  infrastructure components and multiply by 100 to get the percentage.
- **Configuration drift
  rate**: The percentage of infrastructure
  components drifting from their intended configuration over
  time. Configuration drift can introduce security
  vulnerabilities, performance issues, and general system
  instability. Implement configuration management tools,
  routinely run drift detection processes, and automate
  corrective actions to improve this metric. Monitor
  infrastructure configurations regularly and calculate the
  drift rate by dividing the number of drifted
  configurations by the total number of configurations and
  multiplying by 100 to get the percentage.
- **Documentation update
  frequency**: The average frequency that
  documentation is updated relative to code or system
  changes. Stale or out-of-date documentation can lead to
  operational inefficiencies, onboarding issues, and system
  misuse. This metric can be improved by defining
  documentation as code, automating the release of
  documentation through a delivery pipeline, and prompting
  developers to update docs as part of the development
  lifecycle. Track the number of documentation changes over
  a set time frame and compare it to the number of system
  changes in that same time frame.
- **Time to provision infrastructure**: The time taken to
  provision a new infrastructure component or environment using IaC. A key advantage of
  using code to define infrastructure is improved change lead time and deployment
  frequency through the reduction of inconsistent and manual infrastructure provisioning
  practices. Use time-stamped logs to measure the time interval between the initiation and
  completion of infrastructure provisioning tasks.
- **Mean time to recover (MTTR)**: The average time taken to
  restore a system after a failure. Ensure IaC is testable, automate infrastructure
  provisioning, and maintain configuration consistency across deployments. Monitor
  downtime incidents and compute the average recovery time over a designated period.
