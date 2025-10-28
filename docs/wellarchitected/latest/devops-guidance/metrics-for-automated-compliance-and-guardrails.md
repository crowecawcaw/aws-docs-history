# Metrics for automated compliance and guardrails

- **Billing variance**: The
  difference between forecasted and actual billing for cloud
  resources or other IT costs. This metric indicates
  potential inefficiencies or areas of cost-saving, as well
  as highlighting the accuracy of financial
  forecasting. Calculate by subtracting the actual billing
  amount by the forecasted billing amount, then divide by
  the forecasted billing amount and multiply by 100 to get
  the variance percentage.
- **Change failure
  rate**: The percentage of changes that fail. A
  change is considered a failure if it leads to degraded
  service or if it requires remediation, such as a hotfix or
  rollback. This metric provides insights into the quality
  and reliability of changes being made to a system. With
  effective automated governance in place, the expectation
  is that the change failure rate would decrease, as
  automated checks and balances catch potential issues
  before they're deployed into production. Calculate by
  dividing the number of failed changes by the total number
  of changes made within a given period and then multiply by
  100 to derive the percentage.
- **Guardrail effectiveness
  score**: The ratio of successful preventions or
  detections by a specific guardrail to the number of false
  positives or negatives it produces. By assessing the
  efficiency and precision of individual guardrails, you can
  determine which rules are the most effective and which
  might need refinement or deprecation. Improve this metric
  by regularly reviewing and adjusting guardrail
  configurations, parameters, or logic to decrease false
  positives and negatives. Calculate this metric for each
  guardrail by dividing the number of successful detections
  or preventions by the total number of detections or
  preventions. Multiply this by 100 to get the percentage.
- **Percentage of automated change
  approvals**: The proportion of change approvals
  that were granted automatically by tools without manual
  intervention. This metric indicates a shift from manual
  change management to automated governance practices.
  Improve this metric by integrating more governance checks
  into automated pipelines and reduce reliance on manual CAB
  verification. Calculate by dividing the number of
  automated change approvals by the total number, then
  multiply by 100 to get the percentage.
- **Non-compliance detection
  frequency**: The number of non-compliant findings
  detected over a given period. This metric can indicate the
  effectiveness of automated guardrails and the current risk
  level of the environment. Improve this metric by
  increasing the coverage and quality of automated checks
  and auto-remediation capabilities. Continuous review and
  refine controls based on detected findings. Measure by
  counting the number of detected findings on a
  regu**l**ar basis, such as
  monthly or quarterly.
- **Non-compliance response
  time**: The time taken from the detection of a
  non-compliance issue until initial remediation or
  response. Shorter non-compliance response times decrease
  the duration of potential exposure, minimizing potential
  risks and liabilities. Improve this metric by enhancing
  automated alerting systems, preparing clear escalation
  paths, and integrating automated remediation capabilities
  where possible. Measure the timestamp of when
  non-compliance is detected and when the first responsive
  action is taken. Average these durations over a given
  period to understand typical response times.
