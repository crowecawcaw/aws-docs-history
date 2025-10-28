# Use AWS Secrets and Configuration Provider CSI with IAM Roles for Service Accounts (IRSA)

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Set up access control](#integrating_ascp_irsa_access "#integrating_ascp_irsa_access")
- [Identify which secrets to mount](#integrating_ascp_irsa_mount "#integrating_ascp_irsa_mount")
- [Troubleshoot](#integrating_ascp_irsa_trouble "#integrating_ascp_irsa_trouble")

## Prerequisites

- Amazon EKS cluster (version 1.17 or later)
- Access to AWS CLI and Amazon EKS cluster via `kubectl`

## Set up access control

The ASCP retrieves the Amazon EKS Pod Identity and exchanges it for an IAM role. You set
permissions in an IAM policy for that IAM role. When the ASCP assumes the IAM role, it
gets access to the secrets you authorized. Other containers can't access the secrets unless
you also associate them with the IAM role.

###### To grant your Amazon EKS Pod access to secrets in Secrets Manager

1. Create a permissions policy that grants `secretsmanager:GetSecretValue` and
   `secretsmanager:DescribeSecret` permission to the secrets that the Pod needs to
   access. For an example policy, see [Example: Permission to read and describe individual secrets](auth-and-access_iam-policies.md#auth-and-access_examples-read-and-describe "auth-and-access_iam-policies.md#auth-and-access_examples-read-and-describe").
2. Create an IAM OpenID Connect (OIDC) provider for the cluster if you don't already
   have one. For more information, see [Create an IAM OIDC
   provider for your cluster](../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md "../../../eks/latest/userguide/enable-iam-roles-for-service-accounts.md") in the _Amazon EKS User Guide_.
3. Create an [IAM role for service
   account](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md") and attach the policy to it. For more information, see [Create
   an IAM role for a service account](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md") in the _Amazon EKS User
   Guide_.
4. If you use a private Amazon EKS cluster, make sure that the VPC that the cluster is in has
   an AWS STS endpoint. For information about creating an endpoint, see [Interface VPC endpoints](../../../IAM/latest/UserGuide/reference_interface_vpc_endpoints.md "../../../IAM/latest/UserGuide/reference_interface_vpc_endpoints.md") in the _AWS Identity and Access Management User Guide_.

## Identify which secrets to mount

To determine which secrets the ASCP mounts in Amazon EKS as files on the filesystem, you
create a [SecretProviderClass](ascp-examples.md#ascp-examples-secretproviderclass "ascp-examples.md#ascp-examples-secretproviderclass") YAML file. The
`SecretProviderClass` lists the secrets to mount and the file name to mount them
as. The `SecretProviderClass` must be in the same namespace as the Amazon EKS Pod it
references.

### Mount the secrets as files

The following instructions show how to mount secrets as files using example YAML files
[ExampleSecretProviderClass.yaml](https://github.com/aws/secrets-store-csi-driver-provider-aws/blob/main/examples/ExampleSecretProviderClass-IRSA.yaml "https://github.com/aws/secrets-store-csi-driver-provider-aws/blob/main/examples/ExampleSecretProviderClass-IRSA.yaml") and [ExampleDeployment.yaml](https://github.com/aws/secrets-store-csi-driver-provider-aws/blob/main/examples/ExampleDeployment-IRSA.yaml "https://github.com/aws/secrets-store-csi-driver-provider-aws/blob/main/examples/ExampleDeployment-IRSA.yaml").

###### To mount secrets in Amazon EKS

1. Apply the `SecretProviderClass` to the Pod:

```
kubectl apply -f ExampleSecretProviderClass.yaml
```

2. Deploy your Pod:

```
kubectl apply -f ExampleDeployment.yaml
```

3. The ASCP mounts the files.

## Troubleshoot

You can view most errors by describing the Pod deployment.

###### To see error messages for your container

1. Get a list of Pod names with the following command. If you aren't using the default
   namespace, use `-n `nameSpace``.

```
kubectl get pods
```

2. To describe the Pod, in the following command, for
   `podId` use the Pod ID from the Pods you found in the
   previous step. If you aren't using the default namespace, use `-n
`nameSpace``.

```
kubectl describe pod/`podId`
```

###### To see errors for the ASCP

- To find more information in the provider logs, in the following command, for
  `podId` use the ID of the _csi-secrets-store-provider-aws_ Pod.

```
kubectl -n kube-system get pods
kubectl -n kube-system logs Pod/`podId`
```

- ###### Verify that the `SecretProviderClass` CRD is installed:

```
kubectl get crd secretproviderclasses.secrets-store.csi.x-k8s.io
```

This command should return information about the `SecretProviderClass` custom resource
definition.

- ###### Verify that the SecretProviderClass object was created.

```
kubectl get secretproviderclass `SecretProviderClassName` -o yaml

```
