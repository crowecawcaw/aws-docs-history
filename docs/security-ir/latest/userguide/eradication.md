# Eradication

Eradication, in relation to security incident response, is the removal of suspicious
or unauthorized resources in efforts to return the account to a known safe state.
The eradication strategy depends on multiple factors, which depend on the business
requirements for your organization.

The [NIST SP
800-61 Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final") provides several steps for eradication:

1. Identify and mitigate all vulnerabilities that were exploited.
2. Remove malware, inappropriate materials, and other components.
3. If more affected hosts are discovered (for example, new malware infections), repeat
   the detection and analysis steps to identify all other affected hosts, then
   contain and eradicate the incident for them.

For AWS resources, this can be further refined through those events detected and
analyzed through available logs or automated tooling such as CloudWatch Logs and Amazon GuardDuty.
Those events should be the basis to determine which remediations should be performed to
properly restore the environment to a known safe state.

The first step of eradication is determining which resources have been affected within the
AWS account. This is accomplished through analysis of your available log data sources, resources, and automated tooling.

- Identify unauthorized actions taken by the IAM identities in your account.
- Identify unauthorized access or changes to your account.
- Identify the creation of unauthorized resources or IAM users.
- Identify systems or resources with unauthorized changes.

Once the list of resources is identified, you should assess each to determine the business
impact if the resource is deleted or restored. As an example, if a web server is hosting
your business application and deleting it would cause down time, then you should consider
recovering the resource from verified safe backups or re-launching the system from a clean
AMI before deleting the impacted server.

Once you have concluded your business impact analysis, then, using the events from your
log analysis, you should go into the accounts and perform the appropriate remediations, such as:

- Rotate or delete keys - this step removes the ability of the actor to continue performing activities within the account.
- Rotate potentially unauthorized IAM user credentials.
- Delete unrecognized or unauthorized resources.

###### Important

If you must keep resources for your investigation, consider backing up those resources.
For example, if you must retain an Amazon EC2 instance for regulatory, compliance, or legal reasons, then
[create an Amazon EBS snapshot](../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-creating-snapshot.md") before removing the instance.

- For malware infections, you might need to reach out to an AWS Partner or other vendor.
  AWS does not offer native tools for malware analysis or removal. However, if you’re using the
  GuardDuty Malware module for Amazon EBS, then recommendations might be available for provided findings.

Once you have eradicated the identified affected resources, AWS recommends you perform a
security review of your account. This can be done using AWS Config rules, using open-source
solutions such as Prowler and ScoutSuite, or through other vendors. You should also
consider performing vulnerability scans against your public-(internet) facing resources to
assess residual risk.

Eradication is one step of the incident response process and can be manual or automated,
depending on the incident and affected resources. The overall strategy should align with
an organization’s security policies and business needs, and verify that negative effects
are mitigated as inappropriate resources or configurations are removed.
