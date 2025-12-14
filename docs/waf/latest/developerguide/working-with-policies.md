**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using AWS Firewall Manager policies

AWS Firewall Manager provides the following types of policies. For each policy type, you define the:

- **AWS WAF**
  **policy** – Firewall Manager supports AWS WAF and
  AWS WAF Classic policies. For both versions, you define which resources are
  protected by the policy.

      + The AWS WAF policy type takes sets of rule groups to run first and last in the web ACL.
       Then, in the accounts where you apply the web ACL, the account owner can add rules and rule groups to run in between the two sets.
      + The AWS WAF Classic policy type takes a single rule group to run in the web ACL.

- **Shield Advanced policy** – This policy type applies Shield Advanced protections throughout
  your organization for the resource types that you specify.
- **Amazon VPC security group policy** – This policy type gives you
  control over security groups that are in use throughout your organization
  and lets you enforce a baseline set of rules across your organization.
- **Amazon VPC network access control list (ACL) policy** – This policy type gives you
  control over network ACLs that are in use throughout your organization
  and lets you enforce a baseline set of network ACLs across your organization.
- **Network Firewall policy** – This policy type applies
  AWS Network Firewall protection to your organization's VPCs.
- **Amazon Route 53 Resolver DNS Firewall policy** – This policy applies
  DNS Firewall protections to your organization's VPCs.
- **Third-party firewall policy** – This policy type applies third-party firewall protections. Third-party firewalls are available by subscription through the AWS Marketplace console at [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

      + **Palo Alto Networks Cloud NGFW policy** – This policy type applies
       Palo Alto Networks Cloud Next Generation Firewall (NGFW) protections and Palo Alto Networks Cloud NGFW rulestacks to your organization's VPCs.
      + **Fortigate Cloud Native Firewall (CNF) as a Service policy** – This policy type applies
       Fortigate Cloud Native Firewall (CNF) as a Service protections. Fortigate CNF is a cloud-centered solution that blocks Zero-Day threats and secures cloud infrastructures with industry-leading advanced threat prevention, smart web application firewalls (WAF), and API protection.

  A Firewall Manager policy is specific to the individual policy type. If you want to enforce multiple
  policy types across accounts, you can create multiple policies. You can create more than one
  policy for each type.

If you add a new account to an organization that you created with AWS Organizations, Firewall Manager
automatically applies the policy to the resources in that account that are within scope of
the policy.

## General settings for AWS Firewall Manager policies

AWS Firewall Manager managed policies have some common settings and behaviors. For all, you specify a
name and define the scope of the policy, and you can use resource tagging to control
policy scope. You can choose to view the accounts and resources that are out of
compliance without taking corrective action or to automatically remediate noncompliant
resources.

For information about policy scope, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").
