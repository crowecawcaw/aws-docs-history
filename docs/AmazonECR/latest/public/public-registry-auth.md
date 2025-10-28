# Registry authentication in Amazon ECR public

You can use the AWS Management Console, the AWS CLI, or the AWS SDKs to create and manage public
repositories. You can also use those methods to perform some actions on images, such as
listing or deleting them. These clients use standard AWS authentication methods.
Although technically you can use the Amazon ECR Public API to push and pull images, you are
much more likely to use the Docker CLI or a language-specific Docker library.

The Docker CLI does not support native IAM authentication methods. Additional steps
must be taken so that Amazon ECR can authenticate and authorize Docker push and pull
requests.

The following registry authentication methods are available.

## Using an authorization token

The permission scope of an authorization token matches that of the IAM principal
used to retrieve the authentication token. An authentication token is used to access
any Amazon ECR public registry that your IAM principal has access to and is valid for
12 hours. The authentication token is also used to pull any images from a public
repository on the Amazon ECR Public Gallery. To obtain an authorization token, you must
use the [GetAuthorizationToken](../../../AmazonECRPublic/latest/APIReference/API_GetAuthorizationToken.md "../../../AmazonECRPublic/latest/APIReference/API_GetAuthorizationToken.md") API operation to retrieve a base64-encoded
authorization token containing the username `AWS` and an encoded
password. The AWS CLI `get-login-password` command simplifies this by
retrieving and decoding the authorization token which you can then pipe into a
**docker login** command to authenticate.

### To authenticate Docker to an Amazon ECR registry

with get-login-password

To authenticate Docker to an Amazon ECR registry with get-login-password, run the
**aws ecr-public get-login-password** command. When passing
the authentication token to the **docker login** command, use the
value `AWS` for the username and specify the Amazon ECR registry URI you
want to authenticate to. When authenticating to a public registry, always
authenticate to the `us-east-1` Region when using the AWS CLI.

###### Important

If you receive an error, install or upgrade to the latest version of the
AWS CLI. For more information, see [Installing the
AWS Command Line Interface](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md") in the _AWS Command Line Interface User Guide_.

[get-login-password](../../../cli/latest/reference/ecr/get-login-password.md "../../../cli/latest/reference/ecr/get-login-password.md") (AWS CLI)

```
`aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws`
```

## Using HTTP API authentication

Amazon ECR Public supports the [Docker Registry HTTP API](https://docs.docker.com/registry/spec/api/ "https://docs.docker.com/registry/spec/api/"), with the exception of the tags API. However,
you must provide an authorization token with every HTTP request. You can add an HTTP
authorization header using the `-H` option for **curl**
and pass the authorization token provided by the
**get-authorization-token** AWS CLI command.

###### To authenticate with the Amazon ECR HTTP API

1. Retrieve an authorization token with the AWS CLI and set it to an
   environment variable.

```
`TOKEN=$(aws ecr-public get-authorization-token --region us-east-1 --output=text --query 'authorizationData.authorizationToken')`
```

2. To authenticate to the API, pass the `$TOKEN` variable to the
   `-H` option of **curl**. For example, the
   following command lists the manifest details for an image in an Amazon ECR public
   repository. For more information, see the [Docker Registry HTTP
   API](https://docs.docker.com/registry/spec/api/ "https://docs.docker.com/registry/spec/api/") reference documentation.

```
`curl -i -H "Authorization: Bearer $TOKEN" https://public.ecr.aws/v2/`registry_alias``/`repository_name`/manifests/`image_tag`
```

Output:

```
HTTP/1.1 200 OK
Date: Mon, 30 Nov 2020 16:20:09 GMT
Content-Type: application/vnd.docker.distribution.manifest.v2+json
Content-Length: 1569
Connection: keep-alive
Docker-Distribution-Api-Version: registry/2.0

{
   "schemaVersion": 2,
   "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
   "config": {
      "mediaType": "application/vnd.docker.container.image.v1+json",
      "size": 3854,
      "digest": "sha256:2599adbc30c28b1ee5f25a5ebabcc40a37eb81bd89e6f837989ce0fEXAMPLE"
   },
   "layers": [
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 26708056,
         "digest": "sha256:f22ccc0b8772d8e1bcb40f137b373686bc27427a70c0e41dd22b3801EXAMPLE"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 850,
         "digest": "sha256:3cf8fb62ba5ffb221a2edb2208741346eb4d2d99a174138e4afbb69ceEXAMPLE"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 162,
         "digest": "sha256:e80c964ece6a3edf0db1cfc72ae0e6f0699fb776bbfcc92b708fbb945EXAMPLE"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 56322511,
         "digest": "sha256:9f379ca76d09bc8d1647896e7dc2d9de21b772fd49cb9f21114de76EXAMPLE"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 190,
         "digest": "sha256:d8a5f6eb23fabfe50ebb6facb8c46aa2b2ca0b3a455fe631c312034EXAMPLE"
      },
      {
         "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
         "size": 207,
         "digest": "sha256:69c1ea2550a94189f95691ed2538c44a2635f988b7cf0d5425f5b4aEXAMPLE"
      }
   ]
}
```
