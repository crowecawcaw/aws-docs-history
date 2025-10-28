# Step 3: Create the application image and upload the Docker file to your Amazon ECR repository

In this step, you compile the example application, build a Docker image, and push the image to your Amazon ECR repository.

###### Build your application, build a Docker image, and submit it to Amazon Elastic Container Registry

1. Set environment variables for the build that define your AWS Region. Replace the Regions in the examples with
   your own.

```
export CASSANDRA_HOST=cassandra.`us-east-1`.amazonaws.com:9142
export CASSANDRA_DC=`us-east-1`
```

2. Compile your application with Apache Maven version 3.6.3 or higher using the following command.

```
mvn clean install
```

This creates a `JAR` file with all dependencies included in the `target` directory. 3. Retrieve your ECR repository URI that's needed for the next step with the following command.
Make sure to update the Region to the one you've been using.

```
aws ecr describe-repositories --region `us-east-1`
```

The output should look like in the following example.

```
`"repositories": [
 {
 "repositoryArn": "arn:aws:ecr:us-east-1:111122223333:repository/my-ecr-repository",
 "registryId": "111122223333",
 "repositoryName": "my-ecr-repository",
 "repositoryUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repository",
 "createdAt": "2023-11-02T03:46:34+00:00",
 "imageTagMutability": "MUTABLE",
 "imageScanningConfiguration": {
 "scanOnPush": false
 },
 "encryptionConfiguration": {
 "encryptionType": "AES256"
 }
 },`
```

4. From the application's root directory build the Docker image using the repository URI from the
   last step. Modify the Docker file as needed. In the build command, make sure to
   replace your account ID and set the AWS Region to the Region where the Amazon ECR
   repository `my-ecr-repository` is located.

```
docker build -t `111122223333`.dkr.ecr.`us-east-1`.amazonaws.com/`my-ecr-repository`:latest .
```

5. Retrieve an authentication token to push the Docker image to Amazon ECR. You can do so with the following command.

```
aws ecr get-login-password --region `us-east-1` | docker login --username AWS --password-stdin `111122223333`.dkr.ecr.`us-east-1`.amazonaws.com
```

6. First, check for existing images in your Amazon ECR repository. You can use the following command.

```
aws ecr describe-images --repository-name `my-ecr-repository` --region `us-east-1`
```

Then, push the Docker image to the repo. You can use the following command.

```
docker push `111122223333`.dkr.ecr.`us-east-1`.amazonaws.com/`my-ecr-repository`:latest
```
