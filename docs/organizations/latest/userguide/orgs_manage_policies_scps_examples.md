# Service control

policy examples

The example [service control policies
(SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md") displayed in this topic are for information purposes only.

###### Before using these examples

Before you use these example SCPs in your organization, do the following:

- Carefully review and customize the SCPs for your unique requirements.
- Thoroughly test the SCPs in your environment with the AWS services that you
  use.

The example policies in this section demonstrate the implementation and use of
SCPs. They're **_not_** intended to be interpreted as official AWS
recommendations or best practices to be implemented exactly as shown. It is your
responsibility to carefully test any deny-based policies for its suitability to
solve the business requirements of your environment. Deny-based service control
policies can unintentionally limit or block your use of AWS services unless
you add the necessary exceptions to the policy. For an example of such an
exception, see the first example that exempts global services from the rules
that block access to unwanted AWS Regions.

- Remember that an SCP affects every user and role, including the root user, in
  every account that it's attached to.
- Remember that an SCP does not affect service-linked roles. Service-linked roles enable other AWS services to integrate with AWS Organizations and can't be restricted by SCPs.

###### Tip

You can use [service
last accessed data](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md") in [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") to update your SCPs to restrict access to only the AWS services
that you need. For more information, see [Viewing Organizations
Service Last Accessed Data for Organizations](../../../IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.md "../../../IAM/latest/UserGuide/access_policies_access-advisor-view-data-orgs.md") in the
_IAM User Guide._

Each of the following policies is an example of a [deny list policy](orgs_manage_policies_scps_evaluation.md#how_scps_deny "orgs_manage_policies_scps_evaluation.md#how_scps_deny") strategy. Deny list policies must be attached along with other
policies that allow the approved actions in the affected accounts. For example, the default
`FullAWSAccess` policy permits the use of all services in an account. This
policy is attached by default to the root, all organizational units (OUs), and all accounts.
It doesn't actually grant the permissions; no SCP does. Instead, it enables administrators
in that account to delegate access to those actions by attaching standard AWS Identity and Access Management (IAM)
permissions policies to users, roles, or groups in the account. Each of these deny list
policies then overrides any policy by blocking access to the specified services or
actions.

###### Contents

- [General examples](orgs_manage_policies_scps_examples_general.md "orgs_manage_policies_scps_examples_general.md")
  - [Deny access to AWS based on the requested
    AWS Region](orgs_manage_policies_scps_examples_general.md#example-scp-deny-region "orgs_manage_policies_scps_examples_general.md#example-scp-deny-region")
  - [Prevent IAM users and roles
    from making certain changes](orgs_manage_policies_scps_examples_general.md#example-scp-restricts-iam-principals "orgs_manage_policies_scps_examples_general.md#example-scp-restricts-iam-principals")
  - [Prevent IAM users and roles
    from making specified changes, with an exception for a specified admin role](orgs_manage_policies_scps_examples_general.md#example-scp-restricts-with-exception "orgs_manage_policies_scps_examples_general.md#example-scp-restricts-with-exception")
  - [Require MFA to perform an API operation](orgs_manage_policies_scps_examples_general.md#example-scp-mfa "orgs_manage_policies_scps_examples_general.md#example-scp-mfa")
  - [Block service access for the root user](orgs_manage_policies_scps_examples_general.md#example-scp-root-user "orgs_manage_policies_scps_examples_general.md#example-scp-root-user")
  - [Prevent member accounts from leaving the
    organization](orgs_manage_policies_scps_examples_general.md#example-scp-leave-org "orgs_manage_policies_scps_examples_general.md#example-scp-leave-org")

- [Example SCPs for Amazon Bedrock](orgs_manage_policies_scps_examples_bedrock.md "orgs_manage_policies_scps_examples_bedrock.md")
  - [Deny access to specific Amazon Bedrock models](orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-1 "orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-1")
  - [Restrict access to specific Amazon Bedrock models or model families
    across an entire organization](orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-2 "orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-2")
  - [Restrict creation and use of Amazon Bedrock API keys](orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-3 "orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-3")
  - [Restrict creation of long-term Amazon Bedrock API keys valid beyond
    30 days](orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-4 "orgs_manage_policies_scps_examples_bedrock.md#example-bedrock-4")

- [Example SCPs for
  Amazon Q Developer in chat applications](orgs_manage_policies_scps_examples_chatbot.md "orgs_manage_policies_scps_examples_chatbot.md")
  - [Deny all IAM operation](orgs_manage_policies_scps_examples_chatbot.md#example_cloudwatch_1 "orgs_manage_policies_scps_examples_chatbot.md#example_cloudwatch_1")
  - [Deny S3 bucket put requests from a specified Slack channel](orgs_manage_policies_scps_examples_chatbot.md#example_cloudwatch_2 "orgs_manage_policies_scps_examples_chatbot.md#example_cloudwatch_2")

- [Example SCPs for
  Amazon CloudWatch](orgs_manage_policies_scps_examples_cloudwatch.md "orgs_manage_policies_scps_examples_cloudwatch.md")
  - [Prevent users from disabling CloudWatch or
    altering its configuration](orgs_manage_policies_scps_examples_cloudwatch.md#example_cloudwatch_1 "orgs_manage_policies_scps_examples_cloudwatch.md#example_cloudwatch_1")

- [Example SCPs for
  AWS Config](orgs_manage_policies_scps_examples_config.md "orgs_manage_policies_scps_examples_config.md")
  - [Prevent users from disabling AWS Config or
    changing its rules](orgs_manage_policies_scps_examples_config.md#example_config_1 "orgs_manage_policies_scps_examples_config.md#example_config_1")

- [Example SCPs for Amazon Elastic Compute Cloud
  (Amazon EC2)](orgs_manage_policies_scps_examples_ec2.md "orgs_manage_policies_scps_examples_ec2.md")
  - [Require Amazon EC2 instances to use a specific type](orgs_manage_policies_scps_examples_ec2.md#example-ec2-1 "orgs_manage_policies_scps_examples_ec2.md#example-ec2-1")
  - [Prevent launching EC2 instances without IMDSv2](orgs_manage_policies_scps_examples_ec2.md#example-ec2-2 "orgs_manage_policies_scps_examples_ec2.md#example-ec2-2")
  - [Prevent disabling of default Amazon EBS encryption](orgs_manage_policies_scps_examples_ec2.md#example-ec2-3 "orgs_manage_policies_scps_examples_ec2.md#example-ec2-3")
  - [Prevent creating and attaching non-gp3 volumes](orgs_manage_policies_scps_examples_ec2.md#example-ec2-4 "orgs_manage_policies_scps_examples_ec2.md#example-ec2-4")

- [Example SCPs for
  Amazon GuardDuty](orgs_manage_policies_scps_examples_guardduty.md "orgs_manage_policies_scps_examples_guardduty.md")
  - [Prevent users from disabling GuardDuty or
    modifying its configuration](orgs_manage_policies_scps_examples_guardduty.md#example_guardduty_1 "orgs_manage_policies_scps_examples_guardduty.md#example_guardduty_1")

- [Example SCPs for AWS Resource Access Manager](orgs_manage_policies_scps_examples_ram.md "orgs_manage_policies_scps_examples_ram.md")
  - [Preventing external sharing](orgs_manage_policies_scps_examples_ram.md#example_ram_1 "orgs_manage_policies_scps_examples_ram.md#example_ram_1")
  - [Restrict resource sharing to specific account IDs](orgs_manage_policies_scps_examples_ram.md#example_ram_2 "orgs_manage_policies_scps_examples_ram.md#example_ram_2")
  - [Prevent sharing with organizations or
    organizational units (OUs)](orgs_manage_policies_scps_examples_ram.md#example_ram_3 "orgs_manage_policies_scps_examples_ram.md#example_ram_3")
  - [Allow sharing with only specified IAM users
    and roles](orgs_manage_policies_scps_examples_ram.md#example_ram_4 "orgs_manage_policies_scps_examples_ram.md#example_ram_4")

- [Example SCPs for Amazon Application Recovery Controller (ARC)](orgs_manage_policies_scps_examples_app_rec_con.md "orgs_manage_policies_scps_examples_app_rec_con.md")
  - [Prevent users from updating ARC routing control states](orgs_manage_policies_scps_examples_app_rec_con.md#example_app_rec_con "orgs_manage_policies_scps_examples_app_rec_con.md#example_app_rec_con")

- [Example SCPs for Amazon S3](orgs_manage_policies_scps_examples_s3.md "orgs_manage_policies_scps_examples_s3.md")
  - [Prevent Amazon S3 unencrypted object uploads](orgs_manage_policies_scps_examples_s3.md#example-s3-1 "orgs_manage_policies_scps_examples_s3.md#example-s3-1")

- [Example SCPs for tagging
  resources](orgs_manage_policies_scps_examples_tagging.md "orgs_manage_policies_scps_examples_tagging.md")
  - [Require a tag on specified
    created resources](orgs_manage_policies_scps_examples_tagging.md#example-require-tag-on-create "orgs_manage_policies_scps_examples_tagging.md#example-require-tag-on-create")
  - [Prevent tags from
    being modified except by authorized principals](orgs_manage_policies_scps_examples_tagging.md#example-require-restrict-tag-mods-to-admin "orgs_manage_policies_scps_examples_tagging.md#example-require-restrict-tag-mods-to-admin")

- [Example SCPs for Amazon Virtual Private Cloud
  (Amazon VPC)](orgs_manage_policies_scps_examples_vpc.md "orgs_manage_policies_scps_examples_vpc.md")
  - [Prevent users from deleting Amazon VPC flow
    logs](orgs_manage_policies_scps_examples_vpc.md#example_vpc_1 "orgs_manage_policies_scps_examples_vpc.md#example_vpc_1")
  - [Prevent any VPC that doesn't already have
    internet access from getting it](orgs_manage_policies_scps_examples_vpc.md#example_vpc_2 "orgs_manage_policies_scps_examples_vpc.md#example_vpc_2")
