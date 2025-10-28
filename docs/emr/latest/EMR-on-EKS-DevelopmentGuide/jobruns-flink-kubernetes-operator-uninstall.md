# Uninstalling the Flink

Kubernetes operator for Amazon EMR on EKS

Follow these steps to uninstall the Flink Kubernetes operator.

1. Delete the operator.

```
helm uninstall flink-kubernetes-operator -n <NAMESPACE>
```

2. Delete Kubernetes resources that Helm doesn’t uninstall.

```
kubectl delete serviceaccounts, roles, rolebindings -l emr-containers.amazonaws.com/component=flink.operator --namespace <namespace>
kubectl delete crd flinkdeployments.flink.apache.org flinksessionjobs.flink.apache.org
```

3. (Optional) Delete the cert-manager.

```
kubectl delete -f https://github.com/jetstack/cert-manager/releases/download/v1.12.0/cert-manager.yaml
```
