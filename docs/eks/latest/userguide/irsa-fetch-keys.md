**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Fetch signing keys to validate OIDC tokens

Kubernetes issues a `ProjectedServiceAccountToken` to each Kubernetes Service Account. This token is an OIDC token, which is further a type of JSON web token (JWT). Amazon EKS hosts a public OIDC endpoint for each cluster that contains the signing keys for the token so external systems can validate it.

To validate a `ProjectedServiceAccountToken`, you need to fetch the OIDC public signing keys, also called the JSON Web Key Set (JWKS). Use these keys in your application to validate the token. For example, you can use the [PyJWT Python library](https://pyjwt.readthedocs.io/en/latest/ "https://pyjwt.readthedocs.io/en/latest/") to validate tokens using these keys. For more information on the `ProjectedServiceAccountToken`, see [IAM, Kubernetes, and OpenID Connect (OIDC) background information](iam-roles-for-service-accounts.md#irsa-oidc-background "iam-roles-for-service-accounts.md#irsa-oidc-background").

## Prerequisites

- An existing AWS Identity and Access Management (IAM) OpenID Connect (OIDC) provider for your cluster. To determine whether you already have one, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").
- **AWS CLI** — A command line tool for working with AWS services, including Amazon EKS. For more information, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") in the AWS Command Line Interface User Guide. After installing the AWS CLI, we recommend that you also configure it. For more information, see [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the AWS Command Line Interface User Guide.

## Procedure

1. Retrieve the OIDC URL for your Amazon EKS cluster using the AWS CLI.

```
$ aws eks describe-cluster --name my-cluster --query 'cluster.identity.oidc.issuer'
"https://oidc.eks.us-west-2.amazonaws.com/id/8EBDXXXX00BAE"
```

2. Retrieve the public signing key using curl, or a similar tool. The result is a [JSON Web Key Set (JWKS)](https://www.rfc-editor.org/rfc/rfc7517#section-5 "https://www.rfc-editor.org/rfc/rfc7517#section-5").

###### Important

Amazon EKS throttles calls to the OIDC endpoint. You should cache the public signing key. Respect the `cache-control` header included in the response.

###### Important

Amazon EKS rotates the OIDC signing key every seven days.

```
$ curl https://oidc.eks.us-west-2.amazonaws.com/id/8EBDXXXX00BAE/keys
{"keys":[{"kty":"RSA","kid":"2284XXXX4a40","use":"sig","alg":"RS256","n":"wklbXXXXMVfQ","e":"AQAB"}]}
```
