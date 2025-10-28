# Label overrides supported with the

CodeBuild-hosted Buildkite runner

In your Buildkite pipeline steps agent tag labels, you can provide a variety of label
overrides that modify your self-hosted runner build. Any builds not recognized by CodeBuild
will be ignored but will not fail your webhook request. For example, the following
workflow YAML includes overrides for image, instance size, fleet, and the
buildspec:

```
agents:
  queue: "myQueue"
steps:
  - command: "echo \"Hello World\""
    agents:
      project: "codebuild-myProject"
      image: "{{matrix.os}}"
      instance-size: "{{matrix.size}}"
      buildspec-override: "true"
    matrix:
      setup:
        os:
          - "arm-3.0"
          - "al2-5.0"
        size:
          - "small"
          - "large"
```

`project:codebuild-`<project-name>``
(required)

- Example: `project: "codebuild-myProject"`
- Required for all Buildkite pipeline step configurations.
  `<project name>` should be equal to the name of
  the project for which the self-hosted runner webhook is configured.
  `queue: "`<queue-name>`"`

- Example: `queue:
"`<queue-name>`"`
- Used to route Buildkite jobs to a specific queue. See the [Buildkite
  Agent Queue Tag](https://buildkite.com/docs/agent/v3/cli-start#the-queue-tag "https://buildkite.com/docs/agent/v3/cli-start#the-queue-tag") for more information.

`image:
 "`<environment-type>`-`<image-identifier>`"`

- Example: `image: "arm-3.0"`
- Overrides the image and environment type used when starting the self-hosted
  runner build with a curated image. To learn about supported values, see [Compute images supported with the
  CodeBuild-hosted Buildkite runner](buildkite-runner-update-yaml.md "buildkite-runner-update-yaml.md").
  1.  To override the image and environment type used with a custom image,
      use `image:
"custom-`<environment-type>`-`<custom-image-identifier>`"`
  2.  Example:

  ```
  image:
        "custom-arm-public.ecr.aws/codebuild/amazonlinux-aarch64-standard:3.0"
  ```

###### Note

If the custom image resides in a private registry, you must configure the
appropriate registry credentials in your CodeBuild project.
`instance-size: "`<instance-size>`"`

- Example: `instance-size: "medium"`
- Overrides the instance type used when starting the self-hosted runner build.
  To learn about supported values, see [Compute images supported with the
  CodeBuild-hosted Buildkite runner](buildkite-runner-update-yaml.md "buildkite-runner-update-yaml.md").
  `fleet: "`<fleet-name>`"`

- Example: `fleet: "myFleet"`
- Overrides the fleet settings configured on your project to use the specified
  fleet. For more information, see [Run builds on reserved capacity fleets](fleets.md "fleets.md") .
  `buildspec-override: "`<boolean>`"`

- Example: `buildspec-override: "true"`
- Allows the build to run buildspec commands in the `INSTALL`,
  `PRE_BUILD`, and `POST_BUILD` phases if set to
  `true`.
