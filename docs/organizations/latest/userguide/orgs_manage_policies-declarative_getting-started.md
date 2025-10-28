# Getting started with

declarative policies

Follow these steps to get started using declarative policies.

1. [Learn about the permissions you
   must have to perform declarative policy tasks](orgs_manage_policies_prereqs.md "orgs_manage_policies_prereqs.md").
2. [Enable declarative policies for your
   organization](enable-policy-type.md "enable-policy-type.md").

###### Note

**Enabling trust access is required**

You must enable trusted access for the service where the declarative
policy will enforce a baseline configuration. This creates a read-only
service-linked role that is used to generate the account status report of
what the existing configuration is for accounts across your
organization.

**Using the console**

If you use the Organizations console, this step is a part of the process for
enabling declarative policies.

**Using the AWS CLI**

If you use the AWS CLI, there are two separate APIs:

    * [EnablePolicyType](../APIReference/API_EnablePolicyType.md "../APIReference/API_EnablePolicyType.md"), which you use to enable declarative
     policies.
    * [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md"), which you use to enable trusted
     access.For more information on how to enable trusted access for a specific

service with the AWS CLI see, [AWS services that you can use with AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md"). 3. [Run the account
status report](orgs_manage_policies_declarative_status-report.md "orgs_manage_policies_declarative_status-report.md"). 4. [Create a declarative
policy](orgs_policies_create.md "orgs_policies_create.md"). 5. [Attach the declarative policy to your
organization's root, OU, or account](orgs_policies_attach.md "orgs_policies_attach.md"). 6. [View the combined effective
declarative policy that applies to an account](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").
For all of these steps, you sign in as an IAM user, assume an IAM role, or sign in
as the root user ([not
recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization's management account.

###### Other information

- [Learn declarative
  policy syntax and see example policies](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md")
