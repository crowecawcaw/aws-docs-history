# Obtain the list of current Docker images

CodeBuild frequently updates the list of Docker images to add the latest images and deprecate old images. To get the most current list, do one
of the following:

- In the CodeBuild console, in the **Create build project** wizard or
  **Edit Build Project** page, for **Environment
  image**, choose **Managed image**. Choose from the
  **Operating system**, **Runtime**, and
  **Runtime version** drop-down lists. For more information, see
  [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
  or [Change a build project's settings
  (console)](change-project.md#change-project-console "change-project.md#change-project-console").
- For the AWS CLI, run the `list-curated-environment-images`
  command:

```
aws codebuild list-curated-environment-images
```

- For the AWS SDKs, call the `ListCuratedEnvironmentImages`
  operation for your target programming language. For more information, see the [AWS SDKs and tools reference](sdk-ref.md "sdk-ref.md").
