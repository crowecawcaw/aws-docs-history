# Adapt the 'Publish Docker image to Amazon ECR'

sample to push to Docker Hub

To adapt the 'Publish Docker image to Amazon ECR' sample so that the Docker image is pushed
to Docker Hub instead of Amazon ECR, edit the sample's code. For more information about the
sample, see ['Publish Docker image to an Amazon ECR image repository' sample
for CodeBuild](sample-docker.md "sample-docker.md") and [Run the 'Publish Docker image to Amazon ECR'
sample](sample-docker.md#sample-docker-running "sample-docker.md#sample-docker-running").

###### Note

If you are using a version of Docker earlier than 17.06, remove the
`--no-include-email` option.

1. Replace these Amazon ECR-specific lines of code in the
   `buildspec.yml` file:

```
...
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
      - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
...
```

With these Docker Hub-specific lines of code:

```
...
  pre_build:
    commands:
      - echo Logging in to Docker Hub...
      # Type the command to log in to your Docker Hub account here.
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
      - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $IMAGE_REPO_NAME:$IMAGE_TAG
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - docker push $IMAGE_REPO_NAME:$IMAGE_TAG
...
```

2. Upload the edited code to an S3 input bucket or an AWS CodeCommit, GitHub, or
   Bitbucket repository.

###### Important

Do not upload `(root directory
 name)`, just the files inside of
`(root directory
 name)`.

If you are using an S3 input bucket, be sure to create a ZIP file that
contains the files, and then upload it to the input bucket. Do not add
`(root directory
 name)` to the ZIP file, just the files inside of
`(root directory
 name)`. 3. Replace these lines of code from the JSON-formatted input to the
`create-project` command:

```
...
    "environmentVariables": [
      {
        "name": "AWS_DEFAULT_REGION",
        "value": "`region-ID`"
      },
      {
        "name": "AWS_ACCOUNT_ID",
        "value": "`account-ID`"
      },
      {
        "name": "IMAGE_REPO_NAME",
        "value": "`Amazon-ECR-repo-name`"
      },
      {
        "name": "IMAGE_TAG",
        "value": "latest"
      }
    ]
...
```

With these lines of code:

```
...
    "environmentVariables": [
      {
        "name": "IMAGE_REPO_NAME",
        "value": "`your-Docker-Hub-repo-name`"
      },
      {
        "name": "IMAGE_TAG",
        "value": "latest"
      }
    ]
...
```

4. Create a build environment, run the build, and view related build
   information.
5. Confirm that AWS CodeBuild successfully pushed the Docker image to the repository.
   Sign in to Docker Hub, go to the repository, and choose the
   **Tags** tab. The `latest` tag should contain a
   very recent **Last Updated** value.
