# Pull ECR images to your AWS account

Athena federation connector Lambda functions use container images that are stored in Athena-managed Amazon ECR repositories. To perform security scans on these container images, you must first copy them to an Amazon ECR repository in your account. This section provides step-by-step instructions on how to copy an image to your repository and configure your Lambda function to use the image.

## Prerequisites

- An Athena Federation Connector – The connector can be created through any source, provided it uses a container image.

###### Note

To verify image deployment, check the Image tab in your Athena Federation Connector Lambda

- Docker installed and running
- AWS CLI installed
- Account credentials with appropriate pull permissions

## How to transfer an image

1. Locate the Image URI from your Athena Federation Connector Lambda

###### Example

```
account_id_1.dkr.ecr.us-east-1.amazonaws.com/athena-federation-repository:2025.15.1
```

2. Generate a Docker authentication token for the Athena-managed account:

```
aws ecr get-login-password --region `regionID` | docker login --username AWS --password-stdin `athena-managed-registry`
```

Where:

    * `regionID` is your deployment region (e.g., us-east-1)
    * `athena-managed-registry` is the registry portion of the Image URI (e.g., account\_id\_1.dkr.ecr.us-east-1.amazonaws.com)

3. Pull the image from the Athena managed account:

```
docker pull `athenaImageURI`
```

4. Authenticate Docker to your registry:

```
aws ecr get-login-password --region `regionID` | docker login --username AWS --password-stdin `customer-registry`
```

Where `customer-registry` is your ECR registry (e.g., account_id_2.dkr.ecr.us-east-1.amazonaws.com) 5. Tag the pulled image for your repository:

```
docker tag `athenaImageURI` `yourImageURI`
```

6. Push the image to your repository:

```
docker push `yourImageURI`
```

7.  Update your Athena Federation Connector:

        1. Navigate to your Lambda function
        2. Select **Deploy New Image**
        3. Enter your new image URI

    The Athena federated connector image is now located in your account, which allows you to perform CVE scans on the image.
