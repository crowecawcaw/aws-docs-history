# Project profiles in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, a project profile defines an uber template for projects in your Amazon
SageMaker unified domains. A project profile is a collection of [blueprints](blueprints.md "blueprints.md") which are configurations used to create projects. A project profile can
define if a particular blueprint is enabled during the creation of the project, or available
later for the project users to enable on-demand.

You must be an administrator of an Amazon SageMaker unified domain to create and manage
project profiles. In the current release of Amazon SageMaker Unified Studio, you can create a set of template project
profiles. These templates serve as pre-defined configurations that include specific combinations
of capabilities. When you select a template, Amazon SageMaker creates the corresponding project
profile in your domain based on that template's definition. Additionally, you can create custom
project profiles that include any combination of capabilities tailored to your specific needs.
In Amazon SageMaker Unified Studio, you can create the following template project profiles:

- [All capabilities project profile](all-capabilities.md "all-capabilities.md")
- [SQL analytics project profile](sql-analytics.md "sql-analytics.md")
- [Generative AI application development project
  profile](genai-application-development.md "genai-application-development.md")
- [Custom project profile](custom.md "custom.md")
