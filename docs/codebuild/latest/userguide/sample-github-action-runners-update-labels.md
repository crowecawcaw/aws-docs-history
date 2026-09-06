

# Label overrides supported with the CodeBuild-hosted GitHub Actions runner
<a name="sample-github-action-runners-update-labels"></a>

In your GitHub Actions workflow YAML, you can provide a variety of label overrides that modify your self-hosted runner build. Any builds not recognized by CodeBuild will be ignored but will not fail your webhook request. The following workflow YAML defines two jobs: `job1` uses overrides for image, instance size, fleet, and the buildspec, and `job2` uses only an image override. Give each job a unique label (`job1` and `job2`) so that GitHub routes each job to the runner created for it:

```
name: Hello World
on: [push]
jobs:
  job1:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
      - image:arm-3.0
      - instance-size:small
      - fleet:myFleet
      - buildspec-override:true
      - job1
    steps:
      - run: echo "Hello from Job 1!"
  job2:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
      - image:linux-5.0
      - job2
    steps:
      - run: echo "Hello from Job 2!"
```

You can also use a matrix strategy to run a single job across multiple configurations. The expansions of a single matrix job always have the same number of labels, so the runner matching issue does not affect them. However, if a workflow run contains more than one matrix job, give each matrix job its own unique custom label (for example, `matrix-job-1` and `matrix-job-2`) so that GitHub does not match a job to a runner created for a different matrix job:

```
name: Hello World
on: [push]
jobs:
  Hello-World-Job:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
      - image:${{ matrix.os }}
      - instance-size:${{ matrix.size }}
      - fleet:myFleet
      - buildspec-override:true
      - matrix-job-1
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

**Note**  
If your workflow job is hanging on GitHub, see [Troubleshoot the webhook](action-runner-troubleshoot-webhook.md) and [ Using custom labels to route jobs](https://docs.github.com/en/enterprise-server@3.12/actions/hosting-your-own-runners/managing-self-hosted-runners/using-self-hosted-runners-in-a-workflow?learn=hosting_your_own_runners&learnProduct=actions#using-custom-labels-to-route-jobs).

`codebuild-{{<project-name>}}-${{github.run_id}}-${{github.run_attempt}}` (required)
+ Example: `codebuild-fake-project-${{ github.run_id }}-${{ github.run_attempt }}`
+ Required for all GitHub Actions workflow YAMLs. {{<project name>}} should be equal to the name of the project for which the self-hosted runner webhook is configured.

`image:{{<environment-type>}}-{{<image-identifier>}}`
+ Example: `image:arm-3.0`
+ Overrides the image and environment type used when starting the self-hosted runner build with a curated image. To learn about supported values, see [Compute images supported with the CodeBuild-hosted GitHub Actions runner](sample-github-action-runners-update-yaml.images.md).
  + To override the image and environment type used with a custom image, use `image:custom-{{<environment-type>}}-{{<custom-image-identifier>}}`
  + Example: `image:custom-arm-public.ecr.aws/codebuild/amazonlinux-aarch64-standard:3.0`
**Note**  
If the custom image resides in a private registry, see [Configure a private registry credential for self-hosted runners](private-registry-sample-configure-runners.md).

`instance-size:{{<instance-size>}}`
+ Example: `instance-size:medium`
+ Overrides the instance type used when starting the self-hosted runner build. To learn about supported values, see [Compute images supported with the CodeBuild-hosted GitHub Actions runner](sample-github-action-runners-update-yaml.images.md).

`fleet:{{<fleet-name>}}`
+ Example: `fleet:myFleet`
+ Overrides the fleet settings configured on your project to use the specified fleet. For more information, see [Run builds on reserved capacity fleets](fleets.md).

`buildspec-override:{{<boolean>}}`
+ Example: `buildspec-override:true`
+ Allows the build to run buildspec commands in the `INSTALL`, `PRE_BUILD`, and `POST_BUILD` phases if set to `true`.

`{{<unique-label>}}` (recommended when a workflow run has multiple jobs)
+ Example: `job1`
+ A custom label that you define and that no other job in the same workflow run uses. Assigning each job a unique label ensures that GitHub routes each job only to the runner that was created for it. Without it, when jobs in the same workflow run have different numbers of label overrides, a job with fewer labels can be picked up by a runner created for a job with more labels, which leaves the second job without a runner. For more information, see [Troubleshoot the webhook](action-runner-troubleshoot-webhook.md).

## Single label override
<a name="sample-github-action-runners-update-single-labels"></a>

CodeBuild allows you to provide multiple overrides in a single label using the following:

**Note**  
Because all overrides are combined into a single label, each job's runner registers with exactly one label. This means the multiple-job runner matching issue described in [Troubleshoot the webhook](action-runner-troubleshoot-webhook.md) cannot occur with this format, even without a unique label on each job. Use the single-label format if you prefer this behavior and your jobs need only overrides that it supports. Do not use it when you need an override that it does not support. For example, custom images (including images in a private registry) can only be specified by using the `image:custom-{{<environment-type>}}-{{<custom-image-identifier>}}` label format. For those overrides, use the separate-label format described earlier in this topic.
+ To override your environment settings for an Amazon EC2/Lambda compute build, use the following syntax:

  ```
  runs-on: codebuild-{{<project-name>}}-${{ github.run_id }}-${{ github.run_attempt }}-{{<environment-type>}}-{{<image-identifier>}}-{{<instance-size>}}
  ```
+ To override your fleet settings for Amazon EC2 compute build, use the following syntax:

  ```
  runs-on: codebuild-{{<project-name>}}-${{ github.run_id }}-${{ github.run_attempt }}-fleet-{{<fleet-name>}}
  ```
+ To override both the fleet and the image used for the build, use the following syntax:

  ```
  runs-on: codebuild-{{<project-name>}}-${{ github.run_id }}-${{ github.run_attempt }}-{{image}}-{{<image-version>}}-fleet-{{<fleet-name>}}
  ```
+ To run buildspec commands during the build, `-with-buildspec` can be added as a suffix to the label:

  ```
  runs-on: codebuild-{{<project-name>}}-${{ github.run_id }}-${{ github.run_attempt }}-{{<image>}}-{{<image-version>}}-{{<instance-size>}}-with-buildspec
  ```
+ Optionally, you can provide an instance size override without overriding the image. For Amazon EC2 builds, you can exclude both environment type and image identifier. For Lambda builds, you can exclude the image identifier.