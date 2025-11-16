# Integrate Amazon EMR with AWS IAM Identity Center

With Amazon EMR releases 6.15.0 and higher, you can use identities from AWS IAM Identity Center to
authenticate with an Amazon EMR cluster. The following sections provides a conceptual overview,
prerequisites, and steps required to launch an EMR cluster with Identity Center
integration.

###### Topics

- [Overview](#emr-idc-overview "#emr-idc-overview")
- [Features and benefits](#emr-idc-features "#emr-idc-features")
- [Getting started with AWS IAM Identity Center and Amazon EMR](emr-idc-start.md "emr-idc-start.md")
- [User background sessions](user-background-sessions.md "user-background-sessions.md")
- [Considerations and limitations for Amazon EMR with
  the Identity Center integration](emr-idc-considerations.md "emr-idc-considerations.md")

## Overview

[Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")
is the recommended approach for workforce authentication and authorization
on AWS for organizations of any size and type. With Identity Center, you can create and
manage user identities in AWS, or connect your existing identity source, including
Microsoft Active Directory, Okta, Ping Identity, JumpCloud, Google Workspace, and
Microsoft Entra ID (formerly Azure AD).

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

## Features and benefits

The Amazon EMR integration with IAM Identity Center provides the following benefits:

- Amazon EMR provides credentials to relay your Identity Center Identity to an
  EMR cluster.
- Amazon EMR configures all supported applications to authenticate with the cluster
  credentials.
- Amazon EMR configures and maintains the supported application security with the
  Kerberos protocol and no commands or scripts required by you.
- The ability to enforce Amazon S3 prefix-level authorization with Identity Center
  identities on S3 Access Grants-managed S3 prefixes.
- The ability to enforce table-level authorization with Identity Center identities on
  AWS Lake Formation managed AWS Glue tables.
