# Writing the blueprint code

Each blueprint project that you create must contain at a minimum the following
files:

- A Python layout script that defines the workflow. The script contains a function that
  defines the entities (jobs and crawlers) in a workflow, and the dependencies between
  them.
- A configuration file, `blueprint.cfg`, which defines:
  - The full path of the workflow layout definition function.
  - The parameters that the blueprint accepts.

###### Topics

- [Creating the blueprint layout
  script](developing-blueprints-code-layout.md "developing-blueprints-code-layout.md")
- [Creating the configuration file](developing-blueprints-code-config.md "developing-blueprints-code-config.md")
- [Specifying blueprint
  parameters](developing-blueprints-code-parameters.md "developing-blueprints-code-parameters.md")
