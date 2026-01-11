# Resource control

policy examples

The example [resource control policies
(RCPs)](orgs_manage_policies_rcps.md "orgs_manage_policies_rcps.md") displayed in this topic are for information purposes only.

###### Before using these examples

Before you use these example RCPs in your organization, consider the following:

- [Resource control policies (RCPs)](orgs_manage_policies_rcps.md "orgs_manage_policies_rcps.md") are meant to be used as coarse-grained preventative controls, and they don't grant access. You must still attach [identity-based or resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") to IAM principals or resources in your accounts to actually grant permissions. The effective permissions are the logical intersection between the SCP/RCP and an identity policy or the SCP/RCP and a resource policy. You can get more details about RCP effects on permissions [here](orgs_manage_policies_rcps.md#rcp-effects-on-permissions "orgs_manage_policies_rcps.md#rcp-effects-on-permissions").
- The resource control policies in this repository are shown as examples. You should not attach RCPs without thoroughly testing the impact that the policy has on resources in your accounts. Once you have a policy ready that you would like to implement, we recommend testing in a separate organization or OU that can represent your production environment. Once tested, you should deploy changes to test OUs and then progressively deploy the changes to a broader set of OUs over time.
- The [RCPFullAWSAccess](https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy/p-RCPFullAWSAccess "https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy/p-RCPFullAWSAccess") policy is automatically attached to the organization root, every OU, and every account in your organization, when you enable resource control policies (RCPs). This default RCP allows all principals and actions access to pass through RCP evaluation. You can make use of Deny statements to restrict access to resources in your organization. You still also need to grant appropriate permissions to your principals by using identity-based or resource-based policies.
- A [Resource control policy (RCP)](orgs_manage_policies_rcps.md "orgs_manage_policies_rcps.md"), when attached to an organization root, organization unit, or an account offers a central control over the maximum available permissions for resources in your organization, organization unit or an account. As an RCP can be applied at multiple levels in an organization, understanding how [RCPs are evaluated](orgs_manage_policies_rcps_evaluation.md "orgs_manage_policies_rcps_evaluation.md") can help you write RCPs that yield the expected outcome.
  The example policies in this section demonstrate the implementation and use of RCPs. They're **_not_** intended to be interpreted as official AWS
  recommendations or best practices to be implemented exactly as shown. It is your
  responsibility to carefully test any policies for its suitability to
  solve the business requirements of your environment. Deny-based resource control
  policies can unintentionally limit or block your use of AWS services unless
  you add the necessary exceptions to the policy.

###### Tip

Before implementing RCPs, in addition to reviewing [AWS CloudTrail logs](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/"), assessing [IAM Access Analyzer external access findings](../../../IAM/latest/UserGuide/access-analyzer-findings-view.md#access-analyzer-findings-view-external "../../../IAM/latest/UserGuide/access-analyzer-findings-view.md#access-analyzer-findings-view-external") can help understand which resources are currently public or shared externally.

## GitHub repository

- [Resource control policy examples](https://github.com/aws-samples/resource-control-policy-examples "https://github.com/aws-samples/resource-control-policy-examples") - This GitHub repository contains example policies to get started or mature your usage of AWS RCPs
