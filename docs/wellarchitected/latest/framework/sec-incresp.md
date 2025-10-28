# Incident response

Even with extremely mature preventive and detective controls, your
organization should still put processes in place to respond to and
mitigate the potential impact of security incidents. The
architecture of your workload strongly affects the ability of your
teams to operate effectively during an incident, to isolate or
contain systems, and to restore operations to a known good state.
Putting in place the tools and access ahead of a security
incident, then routinely practicing incident response through game
days, will help you verify that your architecture can accommodate
timely investigation and recovery.

In AWS, the following practices facilitate effective incident
response:

- Detailed logging is available that contains important content,
  such as file access and changes.
- Events can be automatically processed and launch tools that
  automate responses through the use of AWS APIs.
- You can pre-provision tooling and a “clean room” using AWS CloudFormation. This allows you to carry out forensics in a
  safe, isolated environment.

The following question focuses on these considerations for
security.

| SEC 10:  How do you anticipate, respond to, and recover from incidents?                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Preparation is critical to timely and effective investigation, response to, and recovery from security incidents to help minimize disruption to your organization. | Verify that you have a way to quickly grant access for your security team, and automate the isolation of instances as well as the capturing of data and state for forensics. |
