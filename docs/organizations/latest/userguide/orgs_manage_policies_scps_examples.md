# Service control

policy examples

The example [service control policies
(SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md") displayed in this topic are for information purposes only.

###### Before using these examples

Before you use these example SCPs in your organization, consider the following:

- [Service control policies (SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md") are meant to be used as coarse-grained guardrails, and they don't directly grant access. The administrator must still attach [identity-based or resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") to IAM principals or resources in your accounts to actually grant permissions. The effective permissions are the logical intersection between the Service control policy/Resource control policy and an identity policy or the Service control policy/Resource control policy and a resource policy. You can get more details about SCP effects on permissions [here](orgs_manage_policies_scps.md#scp-effects-on-permissions "orgs_manage_policies_scps.md#scp-effects-on-permissions").
- A [Service control policy (SCP)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md"), when attached to an organization, organization unit or an account offers a central control over the maximum available permissions for all accounts in your organization, organization unit or an account. As an SCP can be applied at multiple levels in an organization, understanding how [SCPs are evaluated](orgs_manage_policies_scps_evaluation.md "orgs_manage_policies_scps_evaluation.md") can help you write SCPs that yield the right outcome.
- The service control policies in this repository are shown as examples. You should not attach SCPs without thoroughly testing the impact that the policy has on accounts. Once you have a policy ready that you would like to implement, we recommend testing in a separate organization or OU that can be represent your production environment. Once tested, you should deploy changes to more specific OUs and then slowly deploy the changes to broader and broader OUs over time.
- The SCP examples in this repository use a [deny list strategy](orgs_manage_policies_scps_evaluation.md#strategy_using_scps "orgs_manage_policies_scps_evaluation.md#strategy_using_scps"), which means that you also need a [FullAWSAccess](https://console.aws.amazon.com/organizations/?#/policies/p-FullAWSAccess "https://console.aws.amazon.com/organizations/?#/policies/p-FullAWSAccess") policy or other policy that allows access attached to your organization entities to allow actions. You still also need to grant appropriate permissions to your principals by using identity-based or resource-based policies.

###### Tip

You can use [service
last accessed data](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md") in [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") to update your SCPs to restrict access to only the AWS services
that you need. For more information, see [Viewing Organizations
Service Last Accessed Data for Organizations](../../../IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.md "../../../IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.md") in the
_IAM User Guide._

## GitHub repository

- [Service control policy examples](https://github.com/aws-samples/service-control-policy-examples "https://github.com/aws-samples/service-control-policy-examples") - This GitHub repository contains example policies to get started or mature your usage of AWS SCPs
