# Installing the

Flink Kubernetes operator for Amazon EMR on EKS

This topic helps you start to use the Flink Kubernetes operator on Amazon EKS by preparing a
Flink deployment.

## Install the Kubernetes operator

Use the following steps to install the Kubernetes operator for Apache Flink.

1. If you haven't already, complete the steps in [Setting up the Flink Kubernetes
   operator for Amazon EMR on EKS](jobruns-flink-kubernetes-operator-setup.md "jobruns-flink-kubernetes-operator-setup.md").
2. Install the `cert-manager` (once per Amazon EKS cluster) to
   enable adding the webhook component.

```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml
```

3. Install the Helm chart.

```
export VERSION=7.12.0 # The Amazon EMR release version
export NAMESPACE=`The Kubernetes namespace to deploy the operator`

helm install flink-kubernetes-operator \
oci://public.ecr.aws/emr-on-eks/flink-kubernetes-operator \
--version $VERSION \
--namespace $NAMESPACE
```

Example output:

```
NAME: flink-kubernetes-operator
LAST DEPLOYED: Tue May 31 17:38:56 2022
NAMESPACE: $NAMESPACE
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

4. Wait for the deployment to be complete and verify the chart installation.

```
kubectl wait deployment flink-kubernetes-operator --namespace $NAMESPACE --for condition=Available=True --timeout=30s
```

5. You should see the following message when deployment is complete.

```
deployment.apps/flink-kubernetes-operator condition met
```

6. Use the following command to see the deployed operator.

```
helm list --namespace $NAMESPACE
```

The following shows example output, where the app version `x.y.z-amzn-n`
would correspond with the Flink operator version for your Amazon EMR on EKS release. For more
information, see [Supported releases for Amazon EMR on EKS with
Apache Flink](jobruns-flink-security-release-versions.md "jobruns-flink-security-release-versions.md").

```
NAME                              NAMESPACE    REVISION    UPDATED                                STATUS      CHART                                   APP VERSION
flink-kubernetes-operator    $NAMESPACE   1           2023-02-22 16:43:45.24148 -0500 EST    deployed    flink-kubernetes-operator-emr-7.12.0    x.y.z-amzn-n
```

### Upgrade the Kubernetes operator

To upgrade the version of the Flink operator, follow these steps:

1. Uninstall the old `flink-kubernetes-operator`: `helm uninstall flink-kubernetes-operator -n <NAMESPACE>`.
2. Delete CRD (since helm will not automatically delete the old CRD): `kubectl delete crd flinkdeployments.flink.apache.org flinksessionjobs.flink.apache.org`.
3. Re-install `flink-kubernetes-operator` with the newer version.
