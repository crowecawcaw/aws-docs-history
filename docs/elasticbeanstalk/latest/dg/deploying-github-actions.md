

# Using GitHub Actions to deploy to Elastic Beanstalk
<a name="deploying-github-actions"></a>

[GitHub Actions](https://docs.github.com/en/actions) can automatically deploy your application to Elastic Beanstalk when you push code changes to your repository. The [Elastic Beanstalk Deploy](https://github.com/aws-actions/aws-elasticbeanstalk-deploy) action provides a simple YAML interface that handles creating application versions, uploading source bundles to Amazon S3, and deploying to your Elastic Beanstalk environment.

## Example workflow
<a name="deploying-github-actions-example"></a>

The following example workflow deploys an application to an Elastic Beanstalk environment each time you push to the `main` branch. Create a `.yml` file in your repository under `.github/workflows/` .

**Example GitHub Actions workflow for Elastic Beanstalk deployment**  

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
        uses: aws-actions/aws-elasticbeanstalk-deploy@v1.0.0
        with:
          aws-region: {{us-east-1}}
          application-name: {{my-application}}
          environment-name: {{my-application-env}}
```

This workflow checks out your repository, uses [OpenID Connect (OIDC)](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) to authenticate with AWS through the [Configure AWS Credentials](https://github.com/aws-actions/configure-aws-credentials) action, and then deploys your application to Elastic Beanstalk. The deploy action packages your repository contents, uploads the source bundle to Amazon S3, creates a new application version, and creates or updates your environment. By default, it waits for the deployment to complete and the environment to return to a healthy state.

For more configuration options and advanced examples, see the [Elastic Beanstalk Deploy action README](https://github.com/aws-actions/aws-elasticbeanstalk-deploy#readme) on GitHub.

## Additional resources
<a name="deploying-github-actions-resources"></a>
+ [Elastic Beanstalk Deploy action](https://github.com/aws-actions/aws-elasticbeanstalk-deploy) on GitHub
+ [Configure AWS Credentials action](https://github.com/aws-actions/configure-aws-credentials) on GitHub
+ [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) (GitHub documentation)