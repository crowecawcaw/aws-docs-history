

# Uninstalling Apache Livy with Amazon EMR on EKS

Follow these steps to uninstall Apache Livy.

1. Delete the Livy setup using the names of your namespace and application name. In this example, the application name is `livy-demo` and the namespace is `livy-ns`.

   ```bash,sh,zsh
   helm uninstall {{livy-demo}} -n {{livy-ns}}
   ```

1. When uninstalling, Amazon EMR on EKS deletes the Kubernetes service in Livy, the AWS load balancers, and the target groups that you created during installation. Deleting resources can take a few minutes. Make sure that the resources are deleted before installing Livy on the namespace again.

1. Delete the Spark namespace.

   ```bash,sh,zsh
   kubectl delete namespace spark-ns
   ```