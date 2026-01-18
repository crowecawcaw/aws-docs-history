**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure Pods to access AWS services with service accounts

If a Pod needs to access AWS services, then you must configure it to use a Kubernetes service account. The service account must be associated to an AWS Identity and Access Management (IAM) role that has permissions to access the AWS services.

- An existing cluster. If you don’t have one, you can create one using one of the guides in [Get started with Amazon EKS](getting-started.md "getting-started.md").
- An existing Kubernetes service account and an EKS Pod Identity association that associates the service account with an IAM role. The role must have an associated IAM policy that contains the permissions that you want your Pods to have to use AWS services. For more information about how to create the service account and role, and configure them, see [Assign an IAM role to a Kubernetes service account](pod-id-association.md "pod-id-association.md").
- The latest version of the AWS CLI installed and configured on your device or AWS CloudShell. You can check your current version with `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the AWS Command Line Interface User Guide. The AWS CLI version installed in the AWS CloudShell may also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the AWS CloudShell User Guide.
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- An existing `kubectl`
  `config` file that contains your cluster configuration. To create a `kubectl`
  `config` file, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md").

      1. Use the following command to create a deployment manifest that you can deploy a Pod to confirm configuration with. Replace the example values with your own values.



      ```
       cat >my-deployment.yaml <<EOF
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: my-app
      spec:
        selector:
          matchLabels:
            app: my-app
        template:
          metadata:
            labels:
              app: my-app
          spec:
            serviceAccountName: my-service-account
            containers:
            - name: my-app
              image: public.ecr.aws/nginx/nginx:X.XX
      EOF
      ```
      2. Deploy the manifest to your cluster.



      ```
       kubectl apply -f my-deployment.yaml
      ```
      3. Confirm that the required environment variables exist for your Pod.




      	1. View the Pods that were deployed with the deployment in the previous step.



      	```
      	 kubectl get pods | grep my-app
      	```

      	An example output is as follows.



      	```
      	 my-app-6f4dfff6cb-76cv9   1/1     Running   0          3m28s
      	```
      	2. Confirm that the Pod has a service account token file mount.



      	```
      	 kubectl describe pod my-app-6f4dfff6cb-76cv9 | grep AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE:
      	```

      	An example output is as follows.



      	```
      	 AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE:  /var/run/secrets/pods.eks.amazonaws.com/serviceaccount/eks-pod-identity-token
      	```
      4. Confirm that your Pods can interact with the AWS services using the permissions that you assigned in the IAM policy attached to your role.


      ###### Note

      When a Pod uses AWS credentials from an IAM role that’s associated with a service account, the AWS CLI or other SDKs in the containers for that Pod use the credentials that are provided by that role. If you don’t restrict access to the credentials that are provided to the [Amazon EKS node IAM role](create-node-role.md "create-node-role.md"), the Pod still has access to these credentials. For more information, see [Restrict access to the instance profile assigned to the worker node](https://aws.github.io/aws-eks-best-practices/security/docs/iam/#restrict-access-to-the-instance-profile-assigned-to-the-worker-node "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#restrict-access-to-the-instance-profile-assigned-to-the-worker-node").


      If your Pods can’t interact with the services as you expected, complete the following steps to confirm that everything is properly configured.




      	1. Confirm that your Pods use an AWS SDK version that supports assuming an IAM role through an EKS Pod Identity association. For more information, see [Use pod identity with the AWS SDK](pod-id-minimum-sdk.md "pod-id-minimum-sdk.md").
      	2. Confirm that the deployment is using the service account.



      	```
      	 kubectl describe deployment my-app | grep "Service Account"
      	```

      	An example output is as follows.



      	```
      	 Service Account:  my-service-account
      	```
