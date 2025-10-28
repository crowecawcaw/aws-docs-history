# Document and centralize architecture diagrams

To quickly and accurately respond to a security event, you need to understand how your
systems and networks are architected. Understanding these internal patterns is not only
important for incident response, but also for verifying consistency across applications
that the patterns are architected with, according to best practices. You should also
verify that this documentation is up to date and regularly updated in accordance with new
architecture patterns. You should develop documentation and internal repositories that
detail items such as:

- **AWS account structure** - You need to know:
  - How many AWS accounts do you have?
  - How are those AWS accounts organized?
  - Who are the business owners of the AWS accounts?
  - Do you use Service Control Policies (SCPs)? If so, what organizational guardrails are implemented by using SCPs?
  - Do you limit the Regions and services that can be used?
  - What differences are there between business units and environments (dev/test/prod)?

- **AWS service patterns**
  - What AWS services do you use?
  - What are the most widely used AWS services?

- **Architecture patterns**
  - What cloud architectures do you use?

- **AWS authentication patterns**
  - How do your developers typically authenticate to AWS?
  - Do you use IAM roles or users (or both)? Is your authentication to AWS connected to an identity provider (IdP)?
  - How do you map an IAM role or user to an employee or system?
  - How does access get revoked when someone is no longer authorized?

- **AWS authorization patterns**
  - What IAM policies do your developers use?
  - Do you use resource-based policies?

- **Logging and monitoring**
  - What logging sources do you use and where are they stored?
  - Do you aggregate AWS CloudTrail logs? If so, where are they stored?
  - How do you query CloudTrail logs?
  - Do you have Amazon GuardDuty enabled?
  - How do you access GuardDuty findings (for example, console, ticketing system, SIEM)?
  - Are findings or events aggregated in a SIEM?
  - Are tickets automatically created?
  - What tooling is in place to analyze logs for an investigation?

- **Network topology**
  - How are devices, endpoints, and connections on your network physically or logically arranged?
  - How does your network connect with AWS?
  - How is network traffic filtered between environments?

- **External infrastructure**
  - How are externally-facing applications deployed?
  - What AWS resources are publicly accessible?
  - What AWS accounts contain infrastructure that is externally facing?
  - What DDoS or external filtering is there?

Documenting internal technical diagrams and processes eases the incident
response analyst’s job, helping them quickly obtain the institutional knowledge
to respond to a security event. Thorough documentation of internal technical
processes not only simplifies security investigations, but also adjusts for
rationalization and evaluation of the processes.
