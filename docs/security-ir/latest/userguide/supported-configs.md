# Supported configurations

AWS Security Incident Response supports the following language and region configurations:

- Language: AWS Security Incident Response provides dedicated English support. Japanese language support is limited
  to Japan Standard Time business hours and comes with specific restrictions:
- ###### Note

Japanese language support is provided on a best-effort basis during business hours
(09:00-17:00, Monday-Friday, excluding holidays)

- Supported AWS Regions:

AWS Security Incident Response is available in a subset of AWS Regions. In these supported Regions,
you create a membership, create and view cases, and access the dashboard.

    + US East (Ohio)
    + US West (Oregon)
    + US East (Virginia)
    + Europe (Frankfurt)
    + Europe (Ireland)
    + Europe (London)
    + Europe (Milan)
    + Europe (Paris)
    + Europe (Spain)
    + Europe (Stockholm)
    + Europe (Zurich)
    + Asia Pacific (Hong Kong)
    + Asia Pacific (Hyderabad)
    + Asia Pacific (Jakarta)
    + Asia Pacific (Melbourne)
    + Asia Pacific (Mumbai)
    + Asia Pacific (Seoul)
    + Asia Pacific (Singapore)
    + Asia Pacific (Sydney)
    + Asia Pacific (Tokyo)
    + Canada (Central)
    + Middle East (Bahrain)
    + Middle East (UAE)
    + South America (São Paulo)
    + Africa (Cape Town)

When you enable the monitoring and investigation feature, AWS Security Incident Response monitors Amazon GuardDuty findings from all
active commercial AWS Regions. As a security best practice, AWS recommends enabling GuardDuty in all
supported AWS Regions. This configuration allows GuardDuty to generate findings about unauthorized or unusual
activity, even in AWS Regions where you don't actively deploy resources. By doing so, you enhance your overall
security posture and maintain comprehensive threat detection coverage across your AWS environment.

###### Note

Amazon GuardDuty reports findings for configured regions. If you choose not to enable the service in
a specific region, then alerts will not be available.
