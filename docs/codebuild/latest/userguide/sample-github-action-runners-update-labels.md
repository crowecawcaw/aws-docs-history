# Label overrides

supported with the CodeBuild-hosted GitHub Actions runner

In your GitHub Actions workflow YAML, you can provide a variety of label overrides that
modify your self-hosted runner build. Any builds not recognized by CodeBuild will be ignored but
will not fail your webhook request. For example, the following workflow YAML includes overrides
for image, instance size, fleet, and the buildspec:

```
name: Hello World
on: [push]
jobs:
  Hello-World-Job:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
        image:${{ matrix.os }}
        instance-size:${{ matrix.size }}
        fleet:myFleet
        buildspec-override:true
    strategy:
      matrix:
        include:
          - os: arm-3.0
            size: small
          - os: linux-5.0
            size: large
    steps:
      - run: echo "Hello World!"
```

###### Note

If your workflow job is hanging on GitHub, see
[Troubleshoot the webhook](action-runner-troubleshoot-webhook.md "action-runner-troubleshoot-webhook.md") and
[Using custom labels to route jobs](https://docs.github.com/en/enterprise-server@3.12/actions/hosting-your-own-runners/managing-self-hosted-runners/using-self-hosted-runners-in-a-workflow?learn=hosting_your_own_runners&learnProduct=actions#using-custom-labels-to-route-jobs "https://docs.github.com/en/enterprise-server@3.12/actions/hosting-your-own-runners/managing-self-hosted-runners/using-self-hosted-runners-in-a-workflow?learn=hosting_your_own_runners&learnProduct=actions#using-custom-labels-to-route-jobs").

`codebuild-`<project-name>`-${{github.run_id}}-${{github.run_attempt}}` (required)

- Example: `codebuild-fake-project-${{ github.run_id }}-${{ github.run_attempt }}`
- Required for all GitHub Actions workflow YAMLs. `<project name>` should be equal to the name
  of the project for which the self-hosted runner webhook is configured.
  `image:`<environment-type>`-`<image-identifier>``

- Example: `image:arm-3.0`
- Overrides the image and environment type used when starting the self-hosted runner build with a curated image. To learn about supported values, see
  [Compute images
  supported with the CodeBuild-hosted GitHub Actions runner](sample-github-action-runners-update-yaml.md "sample-github-action-runners-update-yaml.md").

      + To override the image and environment type used with a custom image, use
       `image:custom-`<environment-type>`-`<custom-image-identifier>``
      + Example: `image:custom-arm-public.ecr.aws/codebuild/amazonlinux-aarch64-standard:3.0`


      ###### Note

      If the custom image resides in a private registry, see
       [Configure a private registry
       credential for self-hosted runners](private-registry-sample-configure-runners.md "private-registry-sample-configure-runners.md").

  `instance-size:`<instance-size>``

- Example: `instance-size:medium`
- Overrides the instance type used when starting the self-hosted runner build. To learn about supported values, see
  [Compute images
  supported with the CodeBuild-hosted GitHub Actions runner](sample-github-action-runners-update-yaml.md "sample-github-action-runners-update-yaml.md").
  `fleet:`<fleet-name>``

- Example: `fleet:myFleet`
- Overrides the fleet settings configured on your project to use the specified fleet. For more information, see
  [Run builds on reserved capacity fleets](fleets.md "fleets.md").
  `buildspec-override:`<boolean>``

- Example: `buildspec-override:true`
- Allows the build to run buildspec commands in the `INSTALL`, `PRE_BUILD`, and
  `POST_BUILD` phases if set to `true`.

## Single label override (legacy)

CodeBuild allows you to provide multiple overrides in a single label using the following:

- To override your environment settings for an Amazon EC2/Lambda compute build, use the following syntax:

```
runs-on: codebuild-`<project-name>`-${{ github.run_id }}-${{ github.run_attempt }}-`<environment-type>`-`<image-identifier>`-`<instance-size>`
```

- To override your fleet settings for Amazon EC2 compute build, use the following syntax:

```
runs-on: codebuild-`<project-name>`-${{ github.run_id }}-${{ github.run_attempt }}-fleet-`<fleet-name>`
```

- To override both the fleet and the image used for the build, use the following syntax:

```
runs-on: codebuild-`<project-name>`-${{ github.run_id }}-${{ github.run_attempt }}-`image`-`<image-version>`-fleet-`<fleet-name>`
```

- To run buildspec commands during the build, `-with-buildspec` can be added as a suffix to the label:

```
runs-on: codebuild-`<project-name>`-${{ github.run_id }}-${{ github.run_attempt }}-`<image>`-`<image-version>`-`<instance-size>`-with-buildspec
```

- Optionally, you can provide an instance size override without overriding the image. For Amazon EC2
  builds, you can exclude both environment type and image identifier. For Lambda builds, you can exclude the
  image identifier.
