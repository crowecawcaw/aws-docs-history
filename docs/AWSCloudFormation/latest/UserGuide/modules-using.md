# Use modules from the CloudFormation private registry

This topic explains how to use modules in CloudFormation templates. Think of modules as
 pre-made bundles of resources that you can add to your templates.

To use a module, the steps are as follows:


* Register the module – You register modules in
 the CloudFormation registry as private extensions. Make sure it's registered in the
 AWS account and Region you’re working in. For more information, see [CloudFormation registry concepts](registry-concepts.md "registry-concepts.md").
* Include it in your template – Add the module to
 the [Resources](resources-section-structure.md "resources-section-structure.md") section of your CloudFormation template,
 just like you would with other resources. You'll also need to provide any required
 properties for the module.
* Create or update the stack – When you initiate a
 stack operation, CloudFormation generates a processed template that resolves any included
 modules into the appropriate resources.
* Preview changes – Before making changes, you can
 use a change set to see what resources will be added or changed. For more information, see
 [Update CloudFormation stacks using change
 sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md").
Consider the following example: you have a template that contains both resources and
 modules. The template contains one individual resource, `ResourceA`, as well as a
 module, `ModuleParent`. That module contains two resources, `ResourceB`
 and `ResourceC`, as well as a nested module, `ModuleChild`.
 `ModuleChild` contains a single resource, `ResourceD`. If you create a
 stack from this template, CloudFormation processes the template and resolves the modules to the
 appropriate resources. The resulting stack has four resources: `ResourceA`,
 `ResourceB`, `ResourceC`, and `ResourceD`.


![During a stack operation, CloudFormation resolves the two modules included in the stack template into the appropriate four resources.](images/modules-resource-inclusion.png)
CloudFormation keeps track of which resources in a stack were created from modules. You can
 view this information on the **Events**, **Resources**, and
 **Drifts** tabs for a given stack, and it's also included in change set
 previews.

Modules are distinguishable from resources in a template because they adhere to the
 following four-part naming convention, as opposed to the typical three-part convention used by
 resources:


```
`organization`::`service`::`use-case`::MODULE
```
