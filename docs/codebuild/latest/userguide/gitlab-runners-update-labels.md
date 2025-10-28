# Label overrides

supported with the CodeBuild-hosted GitLab runner

In your GitLab CI/CD pipeline YAML, you can provide a variety of label overrides that
modify your self-managed runner build. Any builds not recognized by CodeBuild will be ignored but
will not fail your webhook request. For example, the following YAML includes overrides
for image, instance size, fleet, and the buildspec:

```
workflow:
  name: HelloWorld
stages:
  - build

build-job:
  stage: build
  script:
    - echo "Hello World!"
  tags:
    - codebuild-myProject-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME
    - image:arm-3.0
    - instance-size:small
    - fleet:myFleet
    - buildspec-override:true
```

`codebuild-`<project-name>`-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME` (required)

- Example: `codebuild-myProject-$CI_PROJECT_ID-$CI_PIPELINE_IID-$CI_JOB_NAME`
- Required for all GitLab CI/CD pipeline YAMLs. `<project name>` should be equal to the name
  of the project for which the self-managed runner webhook is configured.
  `image:`<environment-type>`-`<image-identifier>``

- Example: `image:arm-3.0`
- Overrides the image and environment type used when starting the self-managed runner build. To learn about supported values, see
  [Compute images
  supported with the CodeBuild-hosted GitLab runner](sample-gitlab-runners-gitlab-ci.md "sample-gitlab-runners-gitlab-ci.md").

      + To override the image and environment type used with a custom image, use
       `image:custom-`<environment-type>`-`<custom-image-identifier>``
      + Example: `image:custom-arm-public.ecr.aws/codebuild/amazonlinux-aarch64-standard:3.0`


      ###### Note

      If the custom image resides in a private registry, see
       [Configure a private registry
       credential for self-hosted runners](private-registry-sample-configure-runners.md "private-registry-sample-configure-runners.md").

  `instance-size:`<instance-size>``

- Example: `instance-size:small`
- Overrides the instance type used when starting the self-managed runner build. To learn about supported values, see
  [Compute images
  supported with the CodeBuild-hosted GitLab runner](sample-gitlab-runners-gitlab-ci.md "sample-gitlab-runners-gitlab-ci.md").
  `fleet:`<fleet-name>``

- Example: `fleet:myFleet`
- Overrides the fleet settings configured on your project to use the specified fleet. For more information, see
  [Run builds on reserved capacity fleets](fleets.md "fleets.md").
  `buildspec-override:`<boolean>``

- Example: `buildspec-override:true`
- Allows the build to run buildspec commands in the `INSTALL`, `PRE_BUILD`, and
  `POST_BUILD` phases if set to `true`.
