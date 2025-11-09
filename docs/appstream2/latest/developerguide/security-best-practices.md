# Security Best Practices in Amazon WorkSpaces Applications

Cloud security at Amazon Web Services (AWS) is the highest priority.
Security and compliance is a shared responsibility between AWS and
the customer. For more information, refer to the
[Shared Responsibility
Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"). As an AWS and
WorkSpaces Applications customer, it is important to implement security
measures on different layers such as stack, fleet, image, and
networking.

Due to its ephemeral nature, WorkSpaces Applications is often preferred as a
secure solution to application and desktop delivery. Consider
whether antivirus solutions that are commonplace in Windows
deployments are relevant in your use cases for an environment that
is predefined and purged at the end of a user session. Antivirus
adds overhead to virtualized instances, making it is a best practice
to mitigate unnecessary activities. For example, scanning the system
volume (which is ephemeral) at boot, for instance, does not add to
the overall security of WorkSpaces Applications.

The two key questions for security WorkSpaces Applications are centered on:

- Is persisting user state beyond the session a requirement?
- How much access should a user have within a session?

###### Topics

- [Securing Persistent Data](securing-persistent-data.md "securing-persistent-data.md")
- [Endpoint Security and Antivirus](endpoint-security-antivirus.md "endpoint-security-antivirus.md")
- [Network Exclusions](network-exclusions.md "network-exclusions.md")
- [Securing an WorkSpaces Applications Session](securing-session.md "securing-session.md")
- [Firewalls and Routing](firewalls-routing.md "firewalls-routing.md")
- [Data Loss Prevention](data-loss-prevention.md "data-loss-prevention.md")
- [Controlling egress traffic](controlling-egress-traffic.md "controlling-egress-traffic.md")
- [Using AWS services](using-services.md "using-services.md")
