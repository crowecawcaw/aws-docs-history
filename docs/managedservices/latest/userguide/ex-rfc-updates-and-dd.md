# Understand RFC update CTs and CloudFormation template drift detection

Resources provisioned in AMS use a modified CloudFormation template. If a
resource has a parameter changed directly through a service's AWS Management Console, then the
CloudFormation creation record of that resource becomes out of sync. If this
happens and you attempt to use an AMS update change type to update
the resource in AMS, then AMS references the original resource
configuration and potentially resets changed parameters. This reset might be
damaging, so AMS disallows RFCs with update change types if any extra AMS
configuration changes are detected.

For a list of update change types, use the console filter.

## Drift remediation FAQs

Questions and answers on AMS drift remediation. There are two change types that you can use to initiate drift
remediation, one is execution mode=manual or "managed automation," the other is execution mode=automated.

### Drift remediation supported resources (ct-3kinq0u4l33zf)

These are the resources that are supported by the drift remediation change type, (ct-3kinq0u4l33zf).  
For remediation of any resource, use the "managed automation" (ct-34sxfo53yuzah) change type instead.

```
AWS::EC2::Instance
AWS::EC2::SecurityGroup
AWS::EC2::VPC
AWS::EC2::Subnet
AWS::EC2::NetworkInterface
AWS::EC2::EIP
AWS::EC2::InternetGateway
AWS::EC2::NatGateway
AWS::EC2::NetworkAcl
AWS::EC2::RouteTable
AWS::EC2::Volume
AWS::AutoScaling::AutoScalingGroup
AWS::AutoScaling::LaunchConfiguration
AWS::AutoScaling::LifecycleHook
AWS::AutoScaling::ScalingPolicy
AWS::AutoScaling::ScheduledAction
AWS::ElasticLoadBalancing::LoadBalancer
AWS::ElasticLoadBalancingV2::Listener
AWS::ElasticLoadBalancingV2::ListenerRule
AWS::ElasticLoadBalancingV2::LoadBalancer
AWS::CloudWatch::Alarm
```

### Drift remediation change types

Questions and answers on using the AMS drift remediation change types.

For a list of supported resources for the drift remediation feature, see
[Drift remediation supported resources (ct-3kinq0u4l33zf)](#drift-remeditate-faqs-sr "#drift-remeditate-faqs-sr").

###### Important

Drift remediation modifies the stack template and/or parameters and it is mandatory to update your
local template repositories or any automation that is updating these stacks to use the latest stack
template and parameters. Using old template and/or parameters without syncing can cause damaging changes to
underlying resources.

The no managed automation, automated, CT (ct-3kinq0u4l33zf) supports remediating only 10 resources per RFC. To remediate
remaining resources in batches of 10 create new RFCs until all resources are remediated.

Which drift remediation change type should I use?
We recommend using the **no managed automation**, automated CT (ct-3kinq0u4l33zf)
when:

- You attempt to perform an update to an existing stack resource using an automated CT
  and the RFC gets rejected as the stack is `DRIFTED`.
- You used an Update CT in the past and it failed as the stack was DRIFTED.
  You do not need to attempt an update again and can use the managed automation, manual, CT
  instead.

We recommend using the **managed automation**, manual CT (ct-34sxfo53yuzah) only when
drifted resource types are not supported by the drift remediation no managed automation, automated, CT
(ct-3kinq0u4l33zf), or when the drift remediation no managed automation, automated,
CT fails.

What changes are performed to the stack during remediation?
Remediation requires updates to the stack template and/or parameters depending on
the properties that are drifted. Remediation also updates the stack policy of the stack
during remediation and restores the stack policy to its previous value once remediation is completed.

How can we see the changes performed to the stack template and/or parameters?
In the response to the RFC, a change summary is provided with the following information:

- `ChangeSummaryJson`: Contains change summary of Stack Template and/or Parameters
  as part of drift remediation. Remediation is performed in multiple phases. This change summary consists
  of changes for individual phases. If Remediation is successful check changes of the last phase. See
  ExecutionPlan in the JSON for phases executed in order. For example, RestoreReferences section when
  present is always executed at the end and contains JSON for post remediation changes. If remediation
  is run in DryRun mode none of these changes would have been applied to the stack.
- `PreRemediationStackTemplateAndConfigurationJson`: Contains configuration snapshot of
  CloudFormation Stack including Template, Parameters, Outputs, StackPolicyBody before remediation was
  triggered on the stack.

What do I need to do once remediation is performed?

###### Important

You need to update your local template repositories, or any automation, that would be
updating the remediated stack, with the latest template and parameters provided in the RFC summary. It
is very important to do this because using the old template and/or parameters can cause further
destructive changes on the stack resources.

Will my application be effected during this remediation?
Remediation is an offline process that is performed only on the CloudFormation stack
configuration. No updates are performed on the underlying resource.

Can I continue using Management | Other | Other RFCs to perform updates to resources after remediation?
We recommend that you always perform updates to stack resources using the available automated
Update CTs. When the available Update CTs do not support your use case, use
Management | Other | Other requests.

Does remediation create any new resources in the stack?
Remediation does not create any new resources in the stack. However, remediation
creates new outputs and updates the stack template
[metadata](../../../AWSCloudFormation/latest/UserGuide/metadata-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/metadata-section-structure.md")
section to store the remediation summary for your reference.

Will remediation always be successful?
Remediation requires careful analysis and validation of the template configuration to
determine if it can be performed. In scenarios where these validations fail, the
remediation process is stopped and no changes are performed to the stack template or
parameters. Also, remediation can only be performed on supported resource types.

How can I perform updates to stack resources if remediation is not successful?
You can use the Management | Other | Other | Update CT (ct-0xdawir96cy7k) to request changes.
AMS monitors such scenarios and works towards improving the remediation solution.

Can I remediate stacks that have both supported and unsupported resource types?
Yes. However, remediation is performed only if the supported resource types
are found DRIFTED in the stack. If any unsupported resource types are DRIFTED, remediation
does not continue.

Can I request remediation for stacks created through non-CFN Ingest CTs?
Yes. Remediation can be performed on stacks irrespective of the change type
used for creating the stack.

Can I know the changes that would be performed to the stack
before remediation?
Yes. Both change types provide a **DryRun** option that
you can use to request changes that would be performed if the stack was remediated. However, the final remediation
changes may differ depending on the drift present on the stack at the time of remediation.
