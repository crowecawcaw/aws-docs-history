End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Frequently asked questions about custom containers

## Q1. What do I do if I want to change

the contents of my container?

- For a running simulation – You can't change the
  container for a running simulation. You must build a new container and start a new
  simulation that uses that container.
- For a new simulation – Build a new container,
  upload it to Amazon Elastic Container Registry (Amazon ECR), and start a new simulation that uses that container.

## Q2. How can I change the container image

for my simulation?

- For a running simulation – You can't change the
  container for a running simulation. You must start a new simulation that uses the
  new container.
- For a new simulation – Specify the new
  container image in your project's simulation schema. For more information, see
  [Modify a project
  to use a custom container](working-with_custom-containers_modify-project.md "working-with_custom-containers_modify-project.md").
