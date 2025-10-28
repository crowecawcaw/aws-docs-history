# Uninstalling the Spark operator for

Amazon EMR on EKS

Use the following steps to uninstall the Spark operator.

1. Delete the Spark operator using the correct namespace. For this example, the
   namespace is `spark-operator-demo`.

```
helm uninstall spark-operator-demo -n spark-operator
```

2. Delete the Spark operator service account:

```
kubectl delete sa emr-containers-sa-spark-operator -n spark-operator
```

3. Delete the Spark operator `CustomResourceDefinitions` (CRDs):

```
kubectl delete crd sparkapplications.sparkoperator.k8s.io
kubectl delete crd scheduledsparkapplications.sparkoperator.k8s.io
```
