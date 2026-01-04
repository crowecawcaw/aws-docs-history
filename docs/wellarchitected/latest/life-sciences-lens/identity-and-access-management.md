# Identity and access management

| LSSEC01: How do you accommodate separation of duties as part of your identity<br>and access management design? |
| -------------------------------------------------------------------------------------------------------------- |
|                                                                                                                |

Separation of duties, as it relates to security, has two primary objectives.

The first objective is the avoidance of conflict of interest, abuse, and errors.

The second objective is the detection of control failures that include security breaches,
information theft, and circumvention of security controls.

Separation of duties is also essential for demonstrating that data integrity has been
maintained. The FDA, for example, clearly states in its [guidance](https://www.fda.gov/media/119267/download "https://www.fda.gov/media/119267/download") that the system
administrator role should only be assigned to personnel who are not responsible for the record
content. This separation stops an individual whose role has a direct interest in the results
of the decision from having the ability to modify or delete critical data. This protects the
integrity of the data and avoids the risk of allegations of tampering.

###### Best practices

- [LSSEC01-BP01 Implement the principle of separation of
  duties](lssec01-bp01.md "lssec01-bp01.md")
- [LSSEC01-BP02 Maintain a history of IAM configurations and
  changes over time](lssec01-bp02.md "lssec01-bp02.md")
- [LSSEC01-BP03 Set up alerts for IAM configuration changes and
  perform audits](lssec01-bp03.md "lssec01-bp03.md")
