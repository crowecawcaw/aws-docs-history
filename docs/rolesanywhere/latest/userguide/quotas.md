# Quotas for AWS Identity and Access Management Roles Anywhere

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some
quotas, and other quotas cannot be increased.

To view the quotas for AWS Identity and Access Management Roles Anywhere, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services** and
select **IAM Roles Anywhere**.

To request a quota increase, see [Requesting a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

Your AWS account has the following quotas related to IAM Roles Anywhere and each quota is per AWS Region.

| Resource                               | Description                                                                                                                                                                                     | Default value | Adjustable |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Combined rate of trust anchor requests | The maximum transactions per second for ListTrustAnchors, CreateTrustAnchor, GetTrustAnchor, UpdateTrustAnchor, DeleteTrustAnchor, EnableTrustAnchor, and DisableTrustAnchor requests combined. | 1 per second  | Yes        |
| Combined rate of profile requests      | The maximum transactions per second for ListProfiles, CreateProfile, GetProfile, UpdateProfile, DeleteProfile, EnableProfile, and DisableProfile requests combined.                             | 1 per second  | Yes        |
| Combined rate of subject requests      | The maximum transactions per second for ListSubjects and GetSubject requests combined.                                                                                                          | 1 per second  | Yes        |
| Combined rate of tagging requests      | The maximum transactions per second for TagResource, UntagResource, and ListTagsForResource requests combined.                                                                                  | 1 per second  | Yes        |
| Combined rate of CRL requests          | The maximum transactions per second for ListCrls, GetCrl, ImportCrl, UpdateCrl, DeleteCrl, EnableCrl, and DisableCrl requests combined.                                                         | 1 per second  | Yes        |
| Rate of CreateSession requests         | The maximum transactions per second for CreateSession requests.                                                                                                                                 | 10 per second | Yes        |
| Trust anchors                          | The maximum number of trust anchors that you can create within an account.                                                                                                                      | 50            | Yes        |
| Profiles                               | The maximum number of profiles that you can create within an account.                                                                                                                           | 250           | Yes        |
| CRLs per trust anchor                  | The maximum number of Certificate Revocation Lists (CRLs) that you can create per trust anchor within an account.                                                                               | 2             | No         |
| Certificates per trust anchor          | The maximum number of certificates that you can create per trust anchor within an account.                                                                                                      | 2             | No         |
| Roles per profile                      | The maximum number of roles that you can create per profile within an account.                                                                                                                  | 250           | No         | ## Throttling Workloads obtain session credentials by using an endpoint that does not use AWS authenticated principals, which would typically be used to limit the rate of operations. IAM Roles Anywhere will limit the rate of calls to the credential endpoint by the authenticating certificate information and IP address (including VPC Endpoint, if applicable). |
