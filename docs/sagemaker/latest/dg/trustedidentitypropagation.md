# Trusted identity propagation with

Studio

Trusted identity propagation is an AWS IAM Identity Center feature that administrators of connected AWS
services can use to grant and audit access to service data. Access to this data is based on user
attributes such as group associations. Setting up trusted identity propagation requires
collaboration between the administrators of connected AWS services and the IAM Identity Center
administrator. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

The Amazon SageMaker Studio and IAM Identity Center administrators can collaborate to connect the services for
trusted identity propagation. Trusted identity propagation addresses enterprise authentication
needs across AWS services by simplifying:

- Enhanced auditing that tracks actions to specific users
- Access management for data science and machine learning workloads through integration
  with compatible AWS services
- Compliance requirements in regulated industries
  Studio supports trusted identity propagation for audit purposes and access control with
  connected AWS services. Trusted identity propagation in Studio does not directly handle
  authentication or authorization decisions within Studio itself. Instead, it propagates
  identity context information to compatible services that can use this information for access
  control.

When you use trusted identity propagation with Studio, your IAM Identity Center identity propagates
to connected AWS services, creating more granular permissions and security governance.

###### Topics

- [Trusted identity propagation
  architecture and compatibility](trustedidentitypropagation-compatibility.md "trustedidentitypropagation-compatibility.md")
- [Setting up trusted identity propagation for
  Studio](trustedidentitypropagation-setup.md "trustedidentitypropagation-setup.md")
- [Monitoring and auditing with
  CloudTrail](trustedidentitypropagation-auditing.md "trustedidentitypropagation-auditing.md")
- [User background
  sessions](trustedidentitypropagation-user-background-sessions.md "trustedidentitypropagation-user-background-sessions.md")
- [How to connect with other AWS
  services with trusted identity propagation enabled](trustedidentitypropagation-connect-other.md "trustedidentitypropagation-connect-other.md")
