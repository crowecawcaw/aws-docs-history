# Anti-patterns for non-functional testing

- **Mistaking infrastructure
  resilience with system reliability**: While
  architectural traits like high availability and fault
  tolerance enhance a system's resilience, enabling it to
  recover from external disruptions, they do not inherently
  ensure application reliability. While infrastructure
  resilience ensures a system can recover from failure,
  application reliability ensures that it can consistently
  meet runtime expectations, especially under varying loads.
  Assessing the reliability of a system requires targeted
  non-functional performance tests to evaluate
  responsiveness, stability, and speed under various loads.
  Measure the impact these factors have on the system, using
  observability tools that offer insights into real-time
  operational efficiency, aiding in optimization.
- **Overlooking real-world conditions
  during testing**: Testing exclusively in
  controlled environments without considering real-world
  variables and unpredictability can lead to a false sense
  of assurance. Tests must account for diverse user
  behaviors, different network conditions, and the wide
  range of device combinations. Integrating real-world
  variables into testing ensures that software releases are
  robust and reliable in actual deployment scenarios. The
  most effective strategy to achieve this is by balancing
  testing in controlled environments with testing in
  production.
- **Ignoring using observability for
  performance tuning**: Resource optimization
  shouldn't be restricted to the early stages of the
  development lifecycle. As applications are used in
  production, their resource requirements may scale and lead
  to different outcomes that were not tested in a controlled
  environment. Real data regarding non-functional
  attributes, such as resource allocation, performance,
  compliance, sustainability and cost should be periodically
  reviewed and adjusted after deployment. Tools
  like [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/"),
  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/"),
  and [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/ "https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/") can be used to
  tighten the relationship between quality assurance and
  observability.
- **Not gathering genuine user
  feedback**: Relying solely on internal feedback
  for non-functional aspects can introduce biases and
  overlook real user pain points. Collect, analyze, and act
  on genuine user feedback regarding performance, usability,
  and other non-functional attributes. This feedback loop
  ensures software development remains aligned with user
  expectations, optimizing the overall user experience.
