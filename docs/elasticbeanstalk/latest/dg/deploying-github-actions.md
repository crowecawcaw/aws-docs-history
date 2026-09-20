

# Using GitHub Actions to deploy to Elastic Beanstalk
<a name="deploying-github-actions"></a>

[GitHub Actions](https://docs.github.com/en/actions) can automatically deploy your application to Elastic Beanstalk when you push code changes to your repository. The [Elastic Beanstalk Deploy](https://github.com/aws-actions/aws-elasticbeanstalk-deploy) action provides a simple YAML interface that handles creating application versions and deploying them to your Elastic Beanstalk environment. You can use the action with either Elastic Beanstalk environment type. For a Beanstalk Standard environment, the action packages your repository into a source bundle and uploads it to Amazon S3. For a Beanstalk Cluster environment, the action creates the application version from a container image instead, either an image that your workflow has already built or one that Elastic Beanstalk builds from your source. The inputs that you set select the environment type.

## Example workflow: Beanstalk Standard environment
<a name="deploying-github-actions-example"></a>

The following example workflow deploys an application to a Beanstalk Standard environment each time you push to the `main` branch. Create a `.yml` file in your repository under `.github/workflows/`. The action creates the environment if it doesn't exist. In that case, `solution-stack-name` (or `platform-arn`) selects the platform, and `option-settings` must provide the instance profile and service role described in [Elastic Beanstalk Service roles, instance profiles, and user policies](concepts-roles.md). When the environment already exists, these inputs are optional.

**Example GitHub Actions workflow for a Beanstalk Standard environment**  

```
name: Deploy to Elastic Beanstalk

on:
  push:
    branches:
      - main

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::{{123456789012}}:role/{{my-github-actions-role}}
          aws-region: {{us-east-1}}

      - name: Deploy to Elastic Beanstalk
        uses: aws-actions/aws-elasticbeanstalk-deploy@v1
        with:
          aws-region: {{us-east-1}}
          application-name: {{my-application}}
          environment-name: {{my-application-env}}
          solution-stack-name: '{{64bit Amazon Linux 2023 v4.10.0 running Go 1}}'
          option-settings: |
            [
              {
                "Namespace": "aws:autoscaling:launchconfiguration",
                "OptionName": "IamInstanceProfile",
                "Value": "{{aws-elasticbeanstalk-ec2-role}}"
              },
              {
                "Namespace": "aws:elasticbeanstalk:environment",
                "OptionName": "ServiceRole",
                "Value": "{{aws-elasticbeanstalk-service-role}}"
              }
            ]
```

This workflow checks out your repository, uses [OpenID Connect (OIDC)](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) to authenticate with AWS through the [Configure AWS Credentials](https://github.com/aws-actions/configure-aws-credentials) action, and then deploys your application to Elastic Beanstalk. The deploy action packages your repository contents, uploads the source bundle to Amazon S3, creates a new application version, and creates or updates your environment. By default, it waits for the deployment to complete and the environment to return to a healthy state.

## Example workflow: Beanstalk Cluster environment
<a name="deploying-github-actions-cluster"></a>

A Beanstalk Cluster environment runs a container image, so a source bundle on its own can't be deployed to it. To deploy to a Beanstalk Cluster environment, set one of the following inputs instead of a solution stack or platform ARN:
+ `image-uri` – The URI of a container image that your workflow has already built and pushed to a registry, such as Amazon Elastic Container Registry (Amazon ECR). The action creates the application version directly from the image and doesn't upload a source bundle to Amazon S3.
+ `build-configuration` – A JSON object that tells Elastic Beanstalk how to build the image from your source, including the `CodeBuildServiceRole` that AWS CodeBuild assumes and the build type. The action uploads your source bundle to Amazon S3, creates the application version with the build configuration, and waits for the build to finish before deploying. For the build settings, see [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md).

The following example workflow builds an image, pushes it to Amazon ECR, and deploys it to a Beanstalk Cluster environment. The action creates the environment if it doesn't exist. In that case, `option-settings` must provide the cluster, node, and observability roles described in [Permissions for Beanstalk Cluster](beanstalk-cluster-permissions.md), and the role that GitHub Actions assumes must be allowed to pass them.

**Example GitHub Actions workflow for a Beanstalk Cluster environment**  

```
name: Deploy to Elastic Beanstalk

on:
  push:
    branches:
      - main

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::{{123456789012}}:role/{{my-github-actions-role}}
          aws-region: {{us-east-1}}

      - name: Login to Amazon ECR
        id: ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build and push container image
        run: |
          docker build --platform linux/amd64 -t ${{ steps.ecr.outputs.registry }}/{{my-app}}:${{ github.sha }} .
          docker push ${{ steps.ecr.outputs.registry }}/{{my-app}}:${{ github.sha }}

      - name: Deploy to Elastic Beanstalk
        uses: aws-actions/aws-elasticbeanstalk-deploy@v1
        with:
          aws-region: {{us-east-1}}
          application-name: {{my-cluster-app}}
          environment-name: {{my-cluster-env}}
          image-uri: ${{ steps.ecr.outputs.registry }}/{{my-app}}:${{ github.sha }}
          option-settings: |
            [
              {
                "Namespace": "aws:elasticbeanstalk:eks",
                "OptionName": "cluster-role",
                "Value": "${{ secrets.CLUSTER_ROLE_ARN }}"
              },
              {
                "Namespace": "aws:elasticbeanstalk:eks",
                "OptionName": "node-role",
                "Value": "${{ secrets.NODE_ROLE_ARN }}"
              },
              {
                "Namespace": "aws:elasticbeanstalk:eks:environment",
                "OptionName": "observability-role",
                "Value": "${{ secrets.OBSERVABILITY_ROLE_ARN }}"
              }
            ]
```

When `image-uri` or `build-configuration` is set, the `deployment-timeout` input defaults to 2400 seconds instead of 900. The first Beanstalk Cluster environment on a set of subnets provisions an Amazon EKS cluster, which takes 15–20 minutes; later environments on the same subnets reuse the cluster and deploy in a few minutes.

For the required permissions, the `build-configuration` example, the complete list of inputs, and more configuration options for both environment types, see the [Elastic Beanstalk Deploy action README](https://github.com/aws-actions/aws-elasticbeanstalk-deploy#readme) on GitHub.

## Additional resources
<a name="deploying-github-actions-resources"></a>
+ [Elastic Beanstalk Deploy action](https://github.com/aws-actions/aws-elasticbeanstalk-deploy) on GitHub
+ [Configure AWS Credentials action](https://github.com/aws-actions/configure-aws-credentials) on GitHub
+ [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) (GitHub documentation)
+ [Getting started with Beanstalk Cluster](beanstalk-cluster-getting-started.md)
+ [Building container images for Beanstalk Cluster environments](beanstalk-cluster-app-versions.md)