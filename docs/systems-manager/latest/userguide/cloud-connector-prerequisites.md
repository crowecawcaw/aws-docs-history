# Prerequisites

Before you create a Cloud Connector, complete the following prerequisites on both the
AWS side and the Azure side. These steps establish OIDC-based federated authentication
between AWS and Microsoft Azure.

###### Important

Make sure your AWS account is not in any service control policy (SCP) that
restricts the `sts:GetWebIdentityToken` action.
