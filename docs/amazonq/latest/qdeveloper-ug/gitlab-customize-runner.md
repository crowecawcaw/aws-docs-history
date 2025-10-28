# Customizing a CI/CD pipeline for code transformation

Amazon Q for code transformation performs some of its capabilities using static analysis, and this
requires your compile and test scope dependencies to be provided in addition to your project source
code. Code transformation for GitLab uses a [GitLab
CI/CD](https://docs.gitlab.com/ee/ci/pipelines/ "https://docs.gitlab.com/ee/ci/pipelines/") job to provide access to those dependencies.

Before you can invoke code transformation for your project, you need the following:

- At least one [GitLab Runner](https://docs.gitlab.com/runner/ "https://docs.gitlab.com/runner/").
- CI/CD feature must be enabled on the project.
- A `.gitlab-ci.yml` committed on the project’s default branch.
  **To customize a CI/CD pipeline for code transformation**

1. If your project doesn't already have a GitLab CI/CD pipeline, create one using the
   `Maven.gitlab-ci.yml`
   template provided by GitLab. For more information, see
   [Create
   a project pipeline.](https://docs.gitlab.com/ee/tutorials/create_register_first_runner/#create-a-project-pipeline "https://docs.gitlab.com/ee/tutorials/create_register_first_runner/#create-a-project-pipeline").
2. Update the `.gitlab-ci.yml` file with the following job:

```
q-code-transformation:
  stage: build
  script:
    - 'mvn $MAVEN_CLI_OPTS test-compile'
    - 'mvn $MAVEN_CLI_OPTS dependency:copy-dependencies -DoutputDirectory=dependencies -Dmdep.useRepositoryLayout=true -Dmdep.copyPom=true -Dmdep.addParentPoms=true'
  artifacts:
    name: q-code-transformation-dependencies
    paths:
      - dependencies/*
  rules:
    - if: $CI_COMMIT_REF_NAME =~ /^q\/transform-/ && $CI_PIPELINE_SOURCE == 'push'
      when: always
```

    * The first `mvn` invocation validates that your project compiles before Amazon Q code
     transformation attempts to process it. The goal may be one of test-compile, test, integration-test,
     or verify.
    * The second `mvn` invocation copies project dependencies to a staging directory to
     include them as job artifacts.
    * The `artifacts` section uploads the copied dependencies so they can be accessed by
     Amazon Q code transformation.
    * The `rules` section configures this job to only run on branch names that start with
     `q/transform-*` when a new commit is pushed. That isn't the case when a merge request is
     opened.
