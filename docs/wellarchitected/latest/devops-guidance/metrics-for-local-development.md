# Metrics for local development

- **Local environment provisioning time:** The amount of time
  developers spend on setting up or troubleshooting their local development environment.
  This metric indicates inefficiencies in onboarding or local environment maintenance,
  which can negatively impact productivity. If you are centrally provisioning or fully
  automating this process, use observability tools to monitor the time dedicated to
  environment set up. If individual developers need to take action to set up their
  environment, conduct regular surveys or use time-tracking tools to gather additional
  data points.
- **Post-commit test failure rate:** The percentage of tests
  that fail in an integrated environment after a local commit. This metric allows teams to
  track and optimize the effectiveness of their local testing environments and workflows.
  Monitor this metric by calculating the number of tests that fail post-commit in
  integrated environment divided by the total number of tests run post-commit. Ideally,
  this metric should trend downwards over time, indicating that local environments are
  becoming more consistent with integrated environments and that developers are catching
  more issues before committing changes.
