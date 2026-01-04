AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# How AWS Systems Manager works with

IAM

Before you use AWS Identity and Access Management (IAM) to manage access to AWS Systems Manager, you should
understand what IAM features are available to use with Systems Manager. To get a
high-level view of how Systems Manager and other AWS services work with IAM, see
[AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

###### Topics

- [Systems Manager identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Systems Manager resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Systems Manager tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Systems Manager IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Systems Manager identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions
and resources and the conditions under which actions are allowed or denied.
Systems Manager supports specific actions, resources, and condition keys. To
learn about all of the elements that you use in a JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Systems Manager use the following prefix before the
action: `ssm:`. For example, to grant someone
permission to create a Systems Manager parameter (SSM parameter) with the
Systems Manager `PutParameter` API operation, you include the
`ssm:PutParameter` action in their policy. Policy statements
must include either an `Action` or `NotAction`
element. Systems Manager defines its own set of actions that describe tasks
that you can perform with this service.

To specify multiple actions in a single statement, separate them with
commas as follows:

```
"Action": [
      "ssm:*action1*",
      "ssm:*action2*"
]
```

###### Note

The following tools in AWS Systems Manager use different prefixes before
actions.

- AWS AppConfig uses the prefix `appconfig:` before
  actions.
- Incident Manager uses the prefix `ssm-incidents:` or
  `ssm-contacts:` before actions.
- Systems Manager GUI Connect uses the prefix `ssm-guiconnect:` before
  actions.
- Quick Setup uses the prefix `ssm-quicksetup:` before
  actions.

You can specify multiple actions using wildcards (\*). For example, to
specify all actions that begin with the word `Describe`, include
the following action:

```
`"Action": "ssm:Describe*"`
```

To see a list of Systems Manager actions, see [Actions Defined by AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-actions-as-permissions "../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-actions-as-permissions") in
the _Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For example, the Systems Manager maintenance window resource has the
following ARN format.

```
arn:aws:ssm:`region`:`account-id`:maintenancewindow/`window-id`
```

To specify the mw-0c50858d01EXAMPLE maintenance windows in your statement in
the US East (Ohio) Region, you would use an ARN similar to
the following.

```
"Resource": "arn:aws:ssm:us-east-2:`123456789012`:maintenancewindow/mw-0c50858d01EXAMPLE"
```

To specify all maintenance windows that belong to a specific account, use
the wildcard (\*).

```
"Resource": "arn:aws:ssm:`region`:`123456789012`:maintenancewindow/*"
```

For `Parameter Store` API operations, you can provide or restrict
access to all parameters in one level of a hierarchy by using hierarchical
names and AWS Identity and Access Management (IAM) policies as follows.

```
"Resource": "arn:aws:ssm:`region`:123456789012:parameter/Dev/ERP/Oracle/*"
```

Some Systems Manager actions, such as those for creating resources, can't
be performed on a specific resource. In those cases, you must use the
wildcard (\*).

```
"Resource": "*"
```

Some Systems Manager API operations accept multiple resources. To specify
multiple resources in a single statement, separate their ARNs with commas as
follows.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

###### Note

Most AWS services treat a colon (:) or a forward slash (/) as the
same character in ARNs. However, Systems Manager requires an exact
match in resource patterns and rules. When creating event patterns, be
sure to use the correct ARN characters so that they match the resource's
ARN.

The table below describes the ARN formats for the resource types supported
by Systems Manager.

###### Note

Note the following exceptions to ARN formats.

- The following tools in AWS Systems Manager use different prefixes before
  actions.
  - AWS AppConfig uses the prefix `appconfig:` before
    actions.
  - Incident Manager uses the prefix
    `ssm-incidents:` or
    `ssm-contacts:` before actions.
  - Systems Manager GUI Connect uses the prefix `ssm-guiconnect`
    before actions.

- Documents and automation definition resources that are owned
  by Amazon, as well as public parameters that are provided by
  both Amazon and third-party sources, do not include account IDs
  in their ARN formats. For example:

      + The SSM document
       `AWS-RunPatchBaseline`:


      `arn:aws:ssm:us-east-2::document/AWS-RunPatchBaseline`
      + The automation runbook
       `AWS-ConfigureMaintenanceWindows`:


      `arn:aws:ssm:us-east-2::automation-definition/AWS-ConfigureMaintenanceWindows`
      + The public parameter
       `/aws/service/bottlerocket/aws-ecs-1-nvidia/x86_64/1.13.4/image_version`:


      `arn:aws:ssm:us-east-2::parameter/aws/service/bottlerocket/aws-ecs-1-nvidia/x86_64/1.13.4/image_version`

  For more information about these three resource types, see the
  following topics:

      + [Working with documents](documents-using.md "documents-using.md")
      + [Run an automated operation powered by Systems Manager
       Automation](running-simple-automations.md "running-simple-automations.md")
      + [Working with public parameters in
       Parameter Store](parameter-store-public-parameters.md "parameter-store-public-parameters.md")

- Quick Setup uses the prefix `ssm-quicksetup:` before
  actions.

| Resource type                                                                                   | ARN format                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application (AWS AppConfig)                                                                     | arn:aws:appconfig:`region`:`account-id`:application/`application-id`                                                                                                                                                                                                        |
| Association                                                                                     | arn:aws:ssm:`region`:`account-id`:association/`association-id`                                                                                                                                                                                                              |
| Automation execution                                                                            | arn:aws:ssm:`region`:`account-id`:automation-execution/`automation-execution-id`                                                                                                                                                                                            |
| Automation definition (with version subresource)                                                | arn:aws:ssm:`region`:`account-id`:automation-definition/`automation-definition-id`:`version-id`<br>**1**                                                                                                                                                                    |
| Configuration profile (AWS AppConfig)                                                           | arn:aws:appconfig:`region`:`account-id`:application/`application-id`/configurationprofile/`configurationprofile-id`                                                                                                                                                         |
| Contact (Incident Manager)                                                                      | arn:aws:ssm-contacts:`region`:`account-id`:contact/`contact-alias`                                                                                                                                                                                                          |
| Deployment strategy (AWS AppConfig)                                                             | arn:aws:appconfig:`region`:`account-id`:deploymentstrategy/`deploymentstrategy-id`                                                                                                                                                                                          |
| Document                                                                                        | arn:aws:ssm:`region`:`account-id`:document/`document-name`                                                                                                                                                                                                                  |
| Environment (AWS AppConfig)                                                                     | arn:aws:appconfig:`region`:`account-id`:application/`application-id`/environment/`environment-id`                                                                                                                                                                           |
| Incident                                                                                        | arn:aws:ssm-incidents:`region`:`account-id`:incident-record/`response-plan-name`/`incident-id`                                                                                                                                                                              |
| Maintenance window                                                                              | arn:aws:ssm:`region`:`account-id`:maintenancewindow/`window-id`                                                                                                                                                                                                             |
| Managed node                                                                                    | arn:aws:ssm:`region`:`account-id`:managed-instance/`managed-node-id`                                                                                                                                                                                                        |
| Managed node inventory                                                                          | arn:aws:ssm:`region`:`account-id`:managed-instance-inventory/`managed-node-id`                                                                                                                                                                                              |
| OpsItem                                                                                         | arn:aws:ssm:`region`:`account-id`:opsitem/`OpsItem-id`                                                                                                                                                                                                                      |
| Parameter                                                                                       | A one-level parameter:<br>• arn:aws:ssm:`region`:`account-id`:parameter/`parameter-name`/<br>A parameter named with a hierarchical<br>construction:<br>• arn:aws:ssm:`region`:`account-id`:parameter/`parameter-name-root`/`level-2`/`level-3`/`level-4`/`level-5`<br>**2** |
| Patch baseline                                                                                  | arn:aws:ssm:`region`:`account-id`:patchbaseline/`patch-baseline-id`                                                                                                                                                                                                         |
| Response plan                                                                                   | arn:aws:ssm-incidents:`region`:`account-id`:response-plan/`response-plan-name`                                                                                                                                                                                              |
| Session                                                                                         | arn:aws:ssm:`region`:`account-id`:session/`session-id`<br>**3**                                                                                                                                                                                                             |
| All Systems Manager resources                                                                   | arn:aws:ssm:\*                                                                                                                                                                                                                                                              |
| All Systems Manager resources owned by the specified<br>AWS account in the specified AWS Region | arn:aws:ssm:`region`:`account-id`:\*                                                                                                                                                                                                                                        |

###### Note

Automation definition resources are being deprecated. Please update your IAM policies
to include an allow for `ssm:StartAutomationExecution` or `ssm:StartChangeRequestExecution` on
`document` and `automation-execution` resources. To
view best practices and examples for setting up IAM permissions, refer to our
[Setting up identity based policies example](automation-setup-identity-based-policies.md "automation-setup-identity-based-policies.md") user guide.

**1** For
automation definitions, Systems Manager supports a second-level resource,
_version ID_. In AWS, these second-level resources
are known as _subresources_. Specifying a version
subresource for an automation definition resource allows you to provide
access to certain versions of an automation definition. For example, you
might want to ensure that only the latest version of an automation
definition is used in your node management.

**2** To organize
and manage parameters, you can create names for parameters with a
hierarchical construction. With hierarchical construction, a parameter name
can include a path that you define by using forward slashes. You can name a
parameter resource with a maximum of fifteen levels. We suggest that you
create hierarchies that reflect an existing hierarchical structure in your
environment. For more information, see [Creating Parameter Store parameters in
Systems Manager](sysman-paramstore-su-create.md "sysman-paramstore-su-create.md").

**3** In most
cases, the session ID is constructed using the ID of the account user who
started the session, plus an alphanumeric suffix. For example:

```
arn:aws:us-east-2:111122223333:session/JohnDoe-1a2b3c4sEXAMPLE
```

However, if the user ID isn't available, the ARN is constructed this way
instead:

```
arn:aws:us-east-2:111122223333:session/session-1a2b3c4sEXAMPLE
```

For more information about the format of ARNs, see [Amazon Resource
Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _Amazon Web Services General Reference_.

For a list of Systems Manager resource types and their ARNs, see
[Resources Defined by AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-resources-for-iam-policies") in the _Service Authorization Reference_. To
learn with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-actions-as-permissions "../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-actions-as-permissions").

### Condition keys for Systems Manager

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Systems Manager condition keys, see
[Condition Keys for AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-policy-keys "../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-policy-keys") in the _Service Authorization Reference_. To
learn with which actions and resources you can use a condition key, see
[Actions Defined by AWS Systems Manager](../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-actions-as-permissions "../../../service-authorization/latest/reference/list_awssystemsmanager.md#awssystemsmanager-actions-as-permissions").

For information about using the `ssm:resourceTag/*` condition
key, see the following topics:

- [Restricting access to
  root-level commands through SSM Agent](ssm-agent-restrict-root-level-commands.md "ssm-agent-restrict-root-level-commands.md")
- [Restricting Run Command access based on tags](run-command-setting-up.md#tag-based-access "run-command-setting-up.md#tag-based-access")
- [Restrict
  session access based on instance tags](getting-started-restrict-access-examples.md#restrict-access-example-instance-tags "getting-started-restrict-access-examples.md#restrict-access-example-instance-tags")

For information about using the `ssm:Recursive`,
`ssm:Policies`, and `ssm:Overwrite` condition
keys, see [Preventing access to Parameter Store
API operations](parameter-store-policy-conditions.md "parameter-store-policy-conditions.md").

### Examples

To view examples of Systems Manager identity-based policies, see [AWS Systems Manager
identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Systems Manager resource-based policies

Other AWS services, such as Amazon Simple Storage Service (Amazon S3), support resource-based
permissions policies. For example, you can attach a permissions policy to an S3
bucket to manage access permissions to that bucket.

Systems Manager doesn't support resource-based policies.

## Authorization based on

Systems Manager tags

You can attach tags to Systems Manager resources or pass tags in a request to
Systems Manager. To control access based on tags, you provide tag information
in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`ssm:resourceTag/`key-name``,
 `aws:ResourceTag/`key-name``,
`aws:RequestTag/`key-name``, or
 `aws:TagKeys` condition keys. You can add tags to the following
resource types when you create or update them:

- Document
- Managed node
- Maintenance window
- Parameter
- Patch baseline
- OpsItem

To view an example identity-based policy for limiting access to a resource
based on the tags on that resource, see [Viewing Systems Manager documents based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-documents-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-documents-tags").

## Systems Manager IAM

roles

An [IAM
role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific
permissions.

### Using

temporary credentials with Systems Manager

You can use temporary credentials to sign in with federation, assume an
IAM role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS Security Token Service (AWS STS) API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Systems Manager supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources
in other services to complete an action on your behalf. Service-linked roles
are listed in your IAM account and are owned by the service. An
administrator can view but not edit the permissions for service-linked
roles.

Systems Manager supports service-linked roles. For details about creating
or managing Systems Manager service-linked roles, see [Using service-linked roles for
Systems Manager](using-service-linked-roles.md "using-service-linked-roles.md").

### Service

roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to
access resources in other services to complete an action on your behalf.
Service roles are displayed in your IAM account and are owned by the
account. This means that an administrator can change the permissions for
this role. However, doing so might break the functionality of the
service.

Systems Manager supports service roles.

### Choosing an

IAM role in Systems Manager

For Systems Manager to interact with your managed nodes, you must choose
a role to allow Systems Manager to access nodes on your behalf. If you have
previously created a service role or service-linked role, then
Systems Manager provides you with a list of roles to choose from. It's
important to choose a role that allows access to start and stop managed
nodes.

To access EC2 instances, you must configure instance permissions. For
information, see [Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

To access non-EC2 nodes in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types"), the role your AWS account
needs is an IAM service role. For information, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md").

An Automation workflow can be initiated under the context of a service
role (or assume role). This allows the service to perform actions on your
behalf. If you don't specify an assume role, Automation uses the context of
the user who invoked the execution. However, certain situations require that
you specify a service role for Automation. For more information, see [Configuring a service role (assume
role) access for automations](automation-setup.md#automation-setup-configure-role "automation-setup.md#automation-setup-configure-role").

### AWS Systems Manager managed

policies

AWS addresses many common use cases by providing standalone IAM
policies that are created and administered by AWS. These AWS
_managed policies_ grant necessary permissions for
common use cases so you can avoid having to investigate which permissions
are needed. (You can also create your own custom IAM policies to allow
permissions for Systems Manager actions and resources.)

For more information about managed policies for Systems Manager, see [AWS managed policies for
AWS Systems Manager](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

For general information about managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.
