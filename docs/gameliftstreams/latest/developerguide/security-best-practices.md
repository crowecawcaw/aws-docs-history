# Security best practices for Amazon GameLift Streams

Amazon GameLift Streams provides a number of security features to consider as you develop and
implement your own security policies. The following best practices are general guidelines
and don't represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

- At this time, the operating system and runtime environment for a stream group is updated only when you create a new stream group. To
  patch, update, and secure the operating system and other applications that are part of the runtime environment, we recommend that you
  recycle stream groups every two to four weeks, regardless of application updates.
- [Best practices for security, identity, and
  compliance](https://aws.amazon.com/architecture/security-identity-compliance "https://aws.amazon.com/architecture/security-identity-compliance")
