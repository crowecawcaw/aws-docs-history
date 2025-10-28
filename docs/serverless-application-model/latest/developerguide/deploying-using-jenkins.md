# Using Jenkins to deploy with AWS SAM

To configure your [Jenkins](https://www.jenkins.io/ "https://www.jenkins.io/") pipeline to automate
the build and deployment of your AWS SAM application, your `Jenkinsfile` must
contain lines that do the following:

1. Reference a build container image with the necessary runtime from the available images.
   The following example uses the `public.ecr.aws/sam/build-nodejs20.x` build
   container image.
2. Configure the pipeline stages to run the necessary AWS SAM command line interface (CLI)
   commands. The following example runs two AWS SAM CLI commands: **sam build**
   and **sam deploy** (with necessary options).
   This example assumes that you have declared all functions and layers in your AWS SAM template
   file with `runtime: nodejs20.x`.

```
pipeline {
    agent { docker { image 'public.ecr.aws/sam/build-nodejs20.x' } }
    stages {
        stage('build') {
            steps {
                sh 'sam build'
                sh 'sam deploy --no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}
```

For a list of available Amazon Elastic Container Registry (Amazon ECR) build container images for different runtimes, see [Image repositories for AWS SAM](serverless-image-repositories.md "serverless-image-repositories.md").
