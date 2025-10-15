# Import AWS resources into a CloudFormation stack

You can import existing resources into a CloudFormation stack. This is useful if you want to start using CloudFormation to manage
 resources that were created outside of CloudFormation, without having to delete and recreate
 them.

CloudFormation offers the following options for importing existing resources into a stack:


* [IaC generator](generate-IaC.md "generate-IaC.md") is a tool that automatically scans your
 existing resources and generates a CloudFormation template based on their current state. This
 template can then be used to import those resources into a stack.
* [Resource import](import-resources-manually.md "import-resources-manually.md") is a manual process where
 you describe the existing resources in your CloudFormation template and then import them into a
 stack. This approach requires you to manually specify the resource properties and configurations
 in the template.
* [Auto-import](import-resources-automatically.md "import-resources-automatically.md") is an automatic process where
 you describe existing resources in your CloudFormation template and CloudFormation imports the ones with matching custom names into a
 stack.
* [Stack refactoring](stack-refactoring.md "stack-refactoring.md") is a feature that simplifies reorganizing 
 the resources in your CloudFormation stacks while still preserving the existing resource properties and data. With 
 stack refactoring, you can move resources between stacks, split monolithic stacks into smaller components, or 
 consolidate multiple stacks into one.
In addition to bringing existing resources under CloudFormation management, the resource import
 feature can be useful in the following scenarios:


* Moving resources between stacks – You can import
 resources from one stack into another, allowing you to reorganize your infrastructure as
 needed.
* Nesting existing stacks – You can import an existing
 stack as a nested stack within another stack, enabling modular and reusable infrastructure
 designs.
CloudFormation supports importing a wide range of resources. For more information, see [Resource type
 support](resource-import-supported-resources.md "resource-import-supported-resources.md").

###### Topics

* [Manually import AWS
 resources](import-resources-manually.md "import-resources-manually.md")
* [Automatically import AWS
 resources](import-resources-automatically.md "import-resources-automatically.md")
* [Reverting an import
 operation](resource-import-revert.md "resource-import-revert.md")
