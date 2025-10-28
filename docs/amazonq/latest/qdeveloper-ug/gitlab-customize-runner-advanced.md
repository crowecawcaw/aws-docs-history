# Dynamically selecting a Java version

When Amazon Q code transformation opens a merge request in GitLab after completing, your project
pipeline runs whichever jobs are configured to run for merge requests. Since the updated code targets
Java 17, these jobs encounter build errors if the job attempts to build them using Java 8 or
Java 11.

The following is an advanced `.gitlab-ci.yml` that uses Docker and dynamically
chooses Java 17 when jobs are running on a merge request with a branch name starting with `q/transform-*`.
Once you decide to merge the opened request to your default branch, you need to modify your
`.gitlab-ci.yml` to use Java 17 by default.

```
variables:
  MAVEN_OPTS: >-
    -Dhttps.protocols=TLSv1.2
    -Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository
    -Dorg.slf4j.simpleLogger.showDateTime=true
    -Djava.awt.headless=true
    -Dmaven.install.skip=true

  MAVEN_CLI_OPTS: >-
    --batch-mode
    --errors
    --fail-at-end
    --show-version
    --no-transfer-progress
    -DinstallAtEnd=true
    -DdeployAtEnd=true

  BUILD_IMAGE: maven:3-openjdk-8

workflow:
  rules:
    - if: $CI_COMMIT_REF_NAME =~ /^q\/transform-/ && $CI_PIPELINE_SOURCE == 'merge_request_event'
      variables:
        BUILD_IMAGE: maven:3-openjdk-17
    - when: always

image: $BUILD_IMAGE

cache:
  paths:
    - .m2/repository

compile:
  stage: build
  script:
    - 'mvn $MAVEN_CLI_OPTS compile'

verify:
  stage: test
  script:
    - 'mvn $MAVEN_CLI_OPTS verify'

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
