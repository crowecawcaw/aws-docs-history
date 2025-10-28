# What is Access Management?

Access management is how AMS protects your resources by allowing only authorized and authenticated access. AMS uses a default IAM user role and
instance profile, as well as multi-factor authentication, security groups, DNS-friendly bastion names, and more to
keep your resources protected.

AMS focuses on three types of access that require management:

- Console access: Leveraging federation, users in the account’s Active Directory can access the
  console using single sign-on (SSO). If you have multi-factor authentication configured for these accounts, you can
  continue to require MFA to gain access to the console.
- Instance access with RDP or SSH: Leveraging an Active Directory trust, users in the account’s existing
  Active Directory can request access to an instance, and then successfully
  authenticate to a bastion and the instance by using their existing corporate credentials. If you have multi-factor
  authentication configured for those accounts, you can continue to require MFA to
  request access to an instance. AMS uses an MFA solution of its own to restrict
  AMS engineer access to instances.
- Application access: Varies by use case.

###### Topics

- [Why and when AMS accesses your account](access-justification.md "access-justification.md")
