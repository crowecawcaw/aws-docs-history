# Detective control implementations

It is important to understand how detective controls are implemented because they help determine how the alert will be used for the particular event. There are two main implementations of technical detective controls:

- **Behavioral detection** relies on mathematical models
  commonly referred to as machine learning (ML) or artificial intelligence (AI). The
  detection is made by inference; therefore, the alert might not necessarily reflect an
  actual event.
- **Rule-based detection** is deterministic; customers can
  set the exact parameters of what activity to be alerted on, and that is certain.

Modern implementations of detective systems, such as an intrusion detection system (IDS), generally come with both mechanisms. Following are some examples for rule-based and behavioral detections with GuardDuty.

- When the finding `Exfiltration:IAMUser/AnomalousBehavior` is generated,
  it informs you that “an anomalous API request was observed in your account.” As you
  look further into the documentation, it tells you that “The ML model evaluates all
  API requests in your account and identifies anomalous events that are associated with
  techniques used by adversaries,” indicating that this finding is of a behavioral nature.
- For the finding `Impact:S3/MaliciousIPCaller`, GuardDuty is analyzing API calls from the Amazon S3 service in CloudTrail,
  comparing the `SourceIPAddress` log element with a table of public IP addresses that includes
  threat intelligence feeds. Once it finds a direct match to an entry, it generates the finding.

We recommend implementing a mix of both behavioral and rule-based alerting because it is not always
possible to implement rule-based alerting for every activity within your threat model.
