# Create SOCI indexes with nerdctl and

SOCI CLI example

The following page provides an example on how to create SOCI indexes with nerdctl and SOCI
CLI.

###### Create SOCI indexes example

1. First set your variables for the AWS CLI commands that follow. The following is an
   example of setting up your variables.

```
ACCOUNT_ID="`111122223333`"
REGION="`us-east-1`"
REPOSITORY_NAME="`repository-name`"
ORIGINAL_IMAGE_TAG="`original-image-tag`"
SOCI_IMAGE_TAG="`soci-indexed-image-tag`"
```

Variable definitions:

    * `ACCOUNT_ID` is your AWS account ID
    * `REGION` is the AWS Region of your Amazon ECR private registry
    * `REPOSITORY_NAME` is the name of your Amazon ECR private registry
    * `ORIGINAL_IMAGE_TAG` is the tag of your original image
    * `SOCI_IMAGE_TAG` is the tag of your SOCI-indexed image

2. Install required tools:

```
# Install SOCI CLI, containerd, and nerdctl
sudo yum install soci-snapshotter
sudo yum install containerd jq
sudo systemctl start soci-snapshotter
sudo systemctl restart containerd
sudo yum install nerdctl
```

3. Set your registry variables:

```
REGISTRY_USER=AWS
REGISTRY="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"
```

4. Export your region and authenticate to Amazon ECR:

```
export AWS_REGION=$REGION
REGISTRY_PASSWORD=$(/usr/local/bin/aws ecr get-login-password --region $AWS_REGION)
echo $REGISTRY_PASSWORD | sudo nerdctl login -u $REGISTRY_USER --password-stdin $REGISTRY
```

5. Pull your original container image:

```
sudo nerdctl pull $REGISTRY/$REPOSITORY_NAME:$ORIGINAL_IMAGE_TAG
```

6. Create the SOCI index:

```
sudo nerdctl image convert --soci $REGISTRY/$REPOSITORY_NAME:$ORIGINAL_IMAGE_TAG $REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG
```

7. Push the SOCI-indexed image:

```
sudo nerdctl push --platform linux/amd64 $REGISTRY/$REPOSITORY_NAME:$SOCI_IMAGE_TAG
```

This process creates two artifacts for the original container image in your ECR
repository:

- SOCI index - Metadata enabling lazy loading
- Image Index manifest - OCI-compliant manifest
