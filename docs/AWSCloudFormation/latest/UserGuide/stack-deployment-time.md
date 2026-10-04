

# Understand stack deployment time
<a name="stack-deployment-time"></a>

When you create, update, or delete a stack, CloudFormation provisions each resource in your template and reports that the stack operation is complete when your resources are ready to serve traffic. This topic describes how CloudFormation provisions a stack, what affects how long a stack operation takes, and how you can shorten deployment time.

**Topics**
+ [How CloudFormation provisions a stack](#how-cloudformation-provisions-a-stack)
+ [What affects deployment time](#what-affects-deployment-time)
+ [Ways to shorten deployment time](#ways-to-shorten-deployment-time)
+ [Related resources](#stack-deployment-time-related-resources)

## How CloudFormation provisions a stack
<a name="how-cloudformation-provisions-a-stack"></a>

CloudFormation reads the dependencies between resources in your template. A resource that references another resource, through `Ref`, `Fn::GetAtt`, or `DependsOn`, is provisioned after the resource it references. Resources that have no dependencies on each other are provisioned in parallel.

For each resource, CloudFormation applies the resource configuration and then confirms that the resource is ready to serve traffic. CloudFormation moves forward as soon as each resource is ready, so dependent resources start as early as possible. As a result, stacks with longer dependency chains see the largest improvement. When every resource in the stack is ready, CloudFormation reports that the stack operation is complete.

This behavior applies automatically to stack operations. You don't need to change your templates or set any parameters.

## What affects deployment time
<a name="what-affects-deployment-time"></a>

Dependency chains  
The longest chain of resources that depend on each other sets the minimum time for a stack operation. Resources that are not part of that chain are provisioned in parallel and usually don't add to the total time.

Resources that take longer to become ready  
Workloads that include resources such as Amazon RDS database instances, Elastic Load Balancing load balancers, NAT gateways, or Amazon CloudFront distributions spend most of their deployment time waiting for those resources to become ready to serve traffic.

Outputs that reference resource attributes  
If a stack output references a resource attribute, for example with `Fn::GetAtt`, CloudFormation waits until the attribute value is available before it completes the stack operation. This wait can add time to the operation.

## Ways to shorten deployment time
<a name="ways-to-shorten-deployment-time"></a>
+ **Use express mode for development iteration.** Express mode completes stack operations as soon as CloudFormation applies the resource configuration, and resources continue becoming ready in the background. For more information, see [Express mode](cloudformation-express-mode.md).
+ **Group resources by how often they change.** Place resources that take longer to become ready, such as databases, in separate stacks from resources that you update often. Updates to the frequently changed stack then don't include the longer-running resources.
+ **Remove dependencies that you don't need.** Declare `DependsOn` only when a resource must wait for another resource. Fewer dependencies let CloudFormation provision more resources in parallel.
+ **Reference resource attributes in outputs only when you need them.** Outputs that reference resource attributes can extend a stack operation until those values are available.

## Related resources
<a name="stack-deployment-time-related-resources"></a>
+ [How CloudFormation works](cloudformation-overview.md)
+ [Express mode](cloudformation-express-mode.md)
+ [Update CloudFormation stacks using change sets](using-cfn-updating-stacks-changesets.md)