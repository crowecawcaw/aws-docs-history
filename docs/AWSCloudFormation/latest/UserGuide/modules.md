# Create reusable resource configurations that can be included across
 templates with CloudFormation modules

*Modules* are a way for you to package resource configurations for
 inclusion across stack templates, in a transparent, manageable, and repeatable way. Modules can
 encapsulate common service configurations and best practices as modular, customizable building
 blocks for you to include in your stack templates. Modules enable you to include resource
 configurations that incorporate best practices, expert domain knowledge, and accepted guidelines
 (for areas such as security, compliance, governance, and industry regulations) in your
 templates, without having to acquire deep knowledge of the intricacies of the resource
 implementation.

For example, a domain expert in networking could create a module that contains built-in
 security groups and ingress/egress rules that adhere to security guidelines. You could then
 include that module in your template to provision secure networking infrastructure in your
 stack—without having to spend time figuring out how VPCs, subnets, security groups, and
 gateways work. And because modules are versioned, if security guidelines change over time, the
 module author can create a new version of the module that incorporates those changes.

Characteristics of using modules in your templates include:


* Predictability – A module must adhere to the
 schema it registers in the CloudFormation registry, so you know what resources it can resolve to
 once you include it in your template.
* Reusability – You can use the same module across
 multiple templates and accounts.
* Traceability – CloudFormation retains knowledge of
 which resources in a stack were provisioned from a module, enabling you to easily understand
 the source of resource changes.
* Manageability – Once you've registered a module,
 you can manage it through the CloudFormation registry, including versioning and account and
 regional availability.
A module can contain:


* One or more resources to be provisioned from the module, along with any associated data,
 such as outputs or conditions.
* Any module parameters, which enable you to specify custom values whenever the module is
 used.
For information about developing modules, see [Developing modules](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html") in the
 *CloudFormation CLI User Guide*.

###### Topics

* [Considerations when using modules](#module-considerations "#module-considerations")
* [Understand module versioning](module-versioning.md "module-versioning.md")
* [Use modules from the CloudFormation private registry](modules-using.md "modules-using.md")
* [Use parameters to specify module values](module-using-params.md "module-using-params.md")
* [Reference module resources in CloudFormation
 templates](module-ref-resources.md "module-ref-resources.md")

## Considerations when using modules



* There is no additional charge for using modules. You pay only for the resources those
 modules resolve to in your stacks.
* CloudFormation quotas, such as the maximum number of resources allowed in a stack, or the
 maximum size of the template body, apply to the processed template whether the resources
 included in that template come from modules or not. For more information, see [Understand CloudFormation quotas](cloudformation-limits.md "cloudformation-limits.md").
* Tags you specify at the stack level are assigned to the individual resources derived
 from the module.
* Helper scripts specified at the module level don't propagate to the individual
 resources contained in the module when CloudFormation processes the template.
* Outputs specified in the module are propagated to outputs at the template
 level.


Each output will be assigned a logical ID that's a concatenation of the module logical
 name and the output name as defined in the module. For more information, see [Get exported outputs from a deployed CloudFormation
 stack](using-cfn-stack-exports.md "using-cfn-stack-exports.md").
* Parameters specified in the module aren't propagated to parameters at the template
 level.


However, you can create template-level parameters that reference module-level
 parameters. For more information, see [Use parameters to specify module values](module-using-params.md "module-using-params.md").
