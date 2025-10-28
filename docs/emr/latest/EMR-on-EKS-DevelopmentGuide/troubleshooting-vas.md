# Troubleshooting Amazon EMR on EKS vertical

autoscaling

Refer to the following sections if you encounter problems when you set up the
Amazon EMR on EKS vertical autoscaling operator on an Amazon EKS cluster with Operator Lifecycle
Manager. For more information including steps to complete the installation, see [Using vertical autoscaling with Amazon EMR Spark jobs](jobruns-vas.md "jobruns-vas.md").

## 403 Forbidden error

If you followed the steps in [Install the Operator Lifecycle Manager (OLM) on
your Amazon EKS cluster](jobruns-vas-setup.md#jobruns-vas-install-olm "jobruns-vas-setup.md#jobruns-vas-install-olm"), ran the `olm status`
command, and it returned a `403 Forbidden` error like the one below, you
might not have obtained the authentication tokens to the Amazon ECR repository for the
operator.

To resolve this issue, repeat the step in [Install the Amazon EMR on EKS vertical autoscaling
operator](jobruns-vas-setup.md#jobruns-vas-install-operator "jobruns-vas-setup.md#jobruns-vas-install-operator") to obtain the tokens. Then, try
the installation again.

```
Error: FATA[0002] Failed to run bundle: pull bundle image: error pulling image `IMAGE`.
error resolving name : unexpected status code [manifests latest]: 403 Forbidden
```

## Kubernetes namespace not

found

When you [set up the Amazon EMR on EKS vertical
autoscaling operator](jobruns-vas-setup.md "jobruns-vas-setup.md") on an Amazon EKS cluster, you might get a
`namespaces not found` error like the one shown here:

```
FATA[0020] Failed to run bundle: create catalog: error creating catalog source: namespaces "`NAME`" not found.
```

If the namespace that you specify doesn't exist, OLM won't install the vertical
autoscaling operator. To resolve this issue, use the following command to create the
namespace. Then, try the installation again.

```
kubectl create namespace `NAME`
```

## Error saving Docker credentials

To [set up vertical autoscaling](jobruns-vas-setup.md "jobruns-vas-setup.md"), you must
authenticate and fetch your Amazon EMR on EKS vertical autoscaling-related Docker images.
When you do this, you might get an error like the following one if Docker isn't
running:

```
aws ecr get-login-password \
 --region $REGION | docker login \
 --username AWS \
 --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

Error saving credentials: error storing credentials - err: exit status 1
out: 'Post "http://ipc/registry/credstore-updated": dial unix backend.sock: connect: no such file or directory'
```

To resolve this issue, confirm that Docker is running or open Docker Desktop.
Then, try to save your credentials again.
