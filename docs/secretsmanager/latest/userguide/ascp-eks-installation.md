# Install ASCP for Amazon EKS

This section explains how to install the AWS Secrets and Configuration Provider for Amazon EKS. With ASCP, you can mount
secrets from Secrets Manager and parameters from AWS Systems Manager as files in Amazon EKS Pods.

## Prerequisites

- An Amazon EKS cluster
  - Version 1.24 or later for Pod Identity
  - Version 1.17 or later for IRSA

- The AWS CLI installed and configured
- kubectl installed and configured for your Amazon EKS cluster
- Helm (version 3.0 or later)

## Install and configure the ASCP

The ASCP is available on GitHub in the [secrets-store-csi-provider-aws](https://github.com/aws/secrets-store-csi-driver-provider-aws "https://github.com/aws/secrets-store-csi-driver-provider-aws") repository. The repo also contains example YAML
files for creating and mounting a secret.

During installation, you can configure the ASCP to use a FIPS endpoint. For a list of
endpoints, see [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints").

###### To install the ASCP by using Helm

1. To make sure the repo is pointing to the latest charts, use `helm repo
update.`
2. Install the chart. The following is an example of the `helm install`
   command:

```
helm install -n kube-system secrets-provider-aws aws-secrets-manager/secrets-store-csi-driver-provider-aws
```

    1. To use a FIPS endpoint, add the following flag: `--set
     useFipsEndpoint=true`
    2. To configure throttling, add the following flag: `--set-json
     'k8sThrottlingParams={"qps": "`number of queries per
     second`", "burst": "`number of queries per
     second`"}'`
    3. If the Secrets Store CSI Driver is already installed on your cluster, add the following
     flag: `--set secrets-store-csi-driver.install=false`. This will skip
     installing Secrets Store CSI Driver as a dependency.

###### To install by using the YAML in the repo

- Use the following commands.

```
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install -n kube-system csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver
kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/deployment/aws-provider-installer.yaml
```

## Verify the installations

To verify the installations of your EKS cluster, Secrets Store CSI driver, and ASCP
plugin, follow these steps:

1. Verify the EKS cluster:

```
eksctl get cluster --name `clusterName`
```

This command should return information about your cluster. 2. Verify the Secrets Store CSI driver installation:

```
kubectl get pods -n kube-system -l app=secrets-store-csi-driver
```

You should see Pods running with names like
`csi-secrets-store-secrets-store-csi-driver-xxx`. 3. Verify the ASCP plugin installation:

YAML installation

```
`$` kubectl get pods -n kube-system -l app=csi-secrets-store-provider-aws
```

Example output:

```
NAME                                     READY   STATUS    RESTARTS   AGE
csi-secrets-store-provider-aws-12345      1/1     Running   0          2m
```

Helm installation

```
`$`  kubectl get pods -n kube-system -l app=secrets-store-csi-driver-provider-aws
```

Example output:

```
NAME                                              READY   STATUS    RESTARTS   AGE
secrets-provider-aws-secrets-store-csi-driver-provider-67890       1/1     Running   0          2m
```

You should see Pods in the `Running` state.

After running these commands, if everything is set up correctly, you should see all
components running without any errors. If you encounter any issues, you may need to
troubleshoot by checking the logs of the specific Pods that are having problems.

## Troubleshooting

1. To check the logs of the ASCP provider, run:

```
kubectl logs -n kube-system -l app=csi-secrets-store-provider-aws
```

2. Check the status of all pods in the `kube-system` namespace:

```
kubectl -n kube-system get pods
```

```
kubectl -n kube-system logs pod/`PODID`
```

All Pods related to the CSI driver and ASCP should be in the 'Running' state. 3. Check the CSI driver version:

```
kubectl get csidriver secrets-store.csi.k8s.io -o yaml
```

This command should return information about the installed CSI driver.

## Additional resources

For more information about using ASCP with Amazon EKS, see the following resources:

- [Using Pod Identity with Amazon EKS](../../../eks/latest/userguide/pod-identities.md "../../../eks/latest/userguide/pod-identities.md")
- [AWS
  Secrets Store CSI Driver on GitHub](https://github.com/aws/secrets-store-csi-driver-provider-aws "https://github.com/aws/secrets-store-csi-driver-provider-aws")
