# Pulling an image from the Amazon ECR Public Gallery

If you would like to run a Docker image that is available in Amazon ECR Public, you can
pull it to your local environment with the **docker pull** command. You
can do this from any public repository. Every public repository created on Amazon ECR Public
is available on the Amazon ECR Public Gallery. Visit the Amazon ECR Public Gallery at [https://gallery.ecr.aws](https://gallery.ecr.aws "https://gallery.ecr.aws"). For more information,
see [Amazon ECR Public Gallery](public-gallery.md "public-gallery.md").

Amazon ECR Public supports both unauthenticated and authenticated pulls from public
repositories. There are separate service quotas for each type of image pull. For more
information, see [Amazon ECR Public service quotas](public-service-quotas.md "public-service-quotas.md").

- An unauthenticated pull is a pull without an auth token. You can confirm
  whether there is an auth token in your Docker configuration by checking your
  `~/.docker/config.json` file. If you've previously authenticated
  to Amazon ECR Public but you want to perform an unauthenticated pull, you can logout
  using the `docker logout public.ecr.aws` command which will remove
  the auth token from your Docker configuration file.
- An authenticated pull requires that you authenticate to Amazon ECR Public prior to
  the pull request. For more information, see [Registry authentication in Amazon ECR public](public-registry-auth.md "public-registry-auth.md").

###### Note

For authenticated pulls, Amazon ECR Public requires that users have permission to make
calls to the `ecr-public:GetAuthorizationToken` and
`sts:GetServiceBearerToken` API through an IAM policy before they
can authenticate to Amazon ECR Public and pull an image from a public repository.

###### To pull a public image from the Amazon ECR Public Gallery

1. Identify the image to pull. You can view the available public repositories on
   the Amazon ECR Public Gallery at [https://gallery.ecr.aws](https://gallery.ecr.aws "https://gallery.ecr.aws").
2. For authenticated pulls, you must authenticate your Docker client to the Amazon ECR
   public registry. Authentication tokens are valid for 12 hours. For more
   information, see [Registry authentication in Amazon ECR public](public-registry-auth.md "public-registry-auth.md").

###### Note

For unauthenticated pulls, you can skip this step. 3. Pull the image using the **docker pull** command. The image
name format should be
``registry_alias`/`repository`[:`tag`]`
 to pull by tag, or
 ``registry_alias`/`repository`[@`digest`]`
to pull by digest.

```
`docker pull public.ecr.aws/`registry_alias`/repository:tag`
```
