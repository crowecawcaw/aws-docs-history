**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Assign an IAM role to a Kubernetes service account

This topic covers how to configure a Kubernetes service account to assume an AWS Identity and Access Management (IAM) role with EKS Pod Identity. Any Pods that are configured to use the service account can then access any AWS service that the role has permissions to access.

To create an EKS Pod Identity association, there is only a single step; you create the association in EKS through the AWS Management Console, AWS CLI, AWS SDKs, AWS CloudFormation and other tools. There isn’t any data or metadata about the associations inside the cluster in any Kubernetes objects and you don’t add any annotations to the service accounts.

**Prerequisites**

- An existing cluster. If you don’t have one, you can create one by following one of the guides in [Get started with Amazon EKS](getting-started.md "getting-started.md").
- The IAM principal that is creating the association must have `iam:PassRole`.
- The latest version of the AWS CLI installed and configured on your device or AWS CloudShell. You can check your current version with `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the AWS Command Line Interface User Guide. The AWS CLI version installed in the AWS CloudShell may also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the AWS CloudShell User Guide.
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").
- An existing `kubectl`
  `config` file that contains your cluster configuration. To create a `kubectl`
  `config` file, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md "create-kubeconfig.md").

## Create a Pod Identity association (AWS Console)

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to configure the EKS Pod Identity Agent add-on for.
3. Choose the **Access** tab.
4. In the **Pod Identity associations**, choose **Create**.
5. For the **IAM role**, select the IAM role with the permissions that you want the workload to have.

###### Note

The list only contains roles that have the following trust policy which allows EKS Pod Identity to use them.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
            "Effect": "Allow",
            "Principal": {
                "Service": "pods.eks.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ]
        }
    ]
}
```

`sts:AssumeRole` — EKS Pod Identity uses `AssumeRole` to assume the IAM role before passing the temporary credentials to your pods.

`sts:TagSession` — EKS Pod Identity uses `TagSession` to include _session tags_ in the requests to AWS STS.

You can use these tags in the _condition keys_ in the trust policy to restrict which service accounts, namespaces, and clusters can use this role.

For a list of Amazon EKS condition keys, see [Conditions defined by Amazon Elastic Kubernetes Service](../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md#amazonelastickubernetesservice-policy-keys "../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md#amazonelastickubernetesservice-policy-keys") in the _Service Authorization Reference_. To learn which actions and resources you can use a condition key with, see [Actions defined by Amazon Elastic Kubernetes Service](../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md#amazonelastickubernetesservice-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md#amazonelastickubernetesservice-actions-as-permissions"). 6. For the **Kubernetes namespace**, select the Kubernetes namespace that contains the service account and workload. Optionally, you can specify a namespace by name that doesn’t exist in the cluster. 7. For the **Kubernetes service account**, select the Kubernetes service account to use. The manifest for your Kubernetes workload must specify this service account. Optionally, you can specify a service account by name that doesn’t exist in the cluster. 8. (Optional) Select **Disable session tags** to disable the default session tags that Pod Identity automatically adds when it assumes the role. 9. (Optional) Toggle **Configure session policy** to configure an IAM policy to apply additional restrictions to this Pod Identity association beyond the permissions defined in the IAM policy attached to the IAM role.

###### Note

A session policy can only be applied when the **Disable session tags** setting is checked. 10. (Optional) For the **Tags**, choose **Add tag** to add metadata in a key and value pair. These tags are applied to the association and can be used in IAM policies.

You can repeat this step to add multiple tags. 11. Choose **Create**.

## Create a Pod Identity association (AWS CLI)

1. If you want to associate an existing IAM policy to your IAM role, skip to the next step.

Create an IAM policy. You can create your own policy, or copy an AWS managed policy that already grants some of the permissions that you need and customize it to your specific requirements. For more information, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

    1. Create a file that includes the permissions for the AWS services that you want your Pods to access. For a list of all actions for all AWS services, see the [Service Authorization Reference](../../../service-authorization/latest/reference.md "../../../service-authorization/latest/reference.md").


    You can run the following command to create an example policy file that allows read-only access to an Amazon S3 bucket. You can optionally store configuration information or a bootstrap script in this bucket, and the containers in your Pod can read the file from the bucket and load it into your application. If you want to create this example policy, copy the following contents to your device. Replace `my-pod-secrets-bucket` with your bucket name and run the command.



    ```
    {
        "Version":"2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::my-pod-secrets-bucket"
            }
        ]
    }
    ```
    2. Create the IAM policy.



    ```
    aws iam create-policy --policy-name my-policy --policy-document file://my-policy.json
    ```

2. Create an IAM role and associate it with a Kubernetes service account.
   1. If you have an existing Kubernetes service account that you want to assume an IAM role, then you can skip this step.

   Create a Kubernetes service account. Copy the following contents to your device. Replace `my-service-account` with your desired name and `default` with a different namespace, if necessary. If you change `default`, the namespace must already exist.

   ```
   cat >my-service-account.yaml <<EOF
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: my-service-account
     namespace: default
   EOF
   kubectl apply -f my-service-account.yaml
   ```

   Run the following command.

   ```
   kubectl apply -f my-service-account.yaml
   ```

   2. Run the following command to create a trust policy file for the IAM role.

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
               "Effect": "Allow",
               "Principal": {
                   "Service": "pods.eks.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:TagSession"
               ]
           }
       ]
   }
   ```

   3. Create the role. Replace `my-role` with a name for your IAM role, and `my-role-description` with a description for your role.

   ```
   aws iam create-role --role-name my-role --assume-role-policy-document file://trust-relationship.json --description "my-role-description"
   ```

   4. Attach an IAM policy to your role. Replace `my-role` with the name of your IAM role and `my-policy` with the name of an existing policy that you created.

   ```
   aws iam attach-role-policy --role-name my-role --policy-arn=arn:aws:iam::111122223333:policy/my-policy
   ```

   ###### Note

   Unlike IAM roles for service accounts, EKS Pod Identity doesn’t use an annotation on the service account. 5. Run the following command to create the association. Replace `my-cluster` with the name of the cluster, replace `my-service-account` with your desired name and `default` with a different namespace, if necessary.

   ```
   aws eks create-pod-identity-association --cluster-name my-cluster --role-arn arn:aws:iam::111122223333:role/my-role --namespace default --service-account my-service-account
   ```

   An example output is as follows.

   ```
   {
       "association": {
           "clusterName": "my-cluster",
           "namespace": "default",
           "serviceAccount": "my-service-account",
           "roleArn": "arn:aws:iam::111122223333:role/my-role",
           "associationArn": "arn:aws::111122223333:podidentityassociation/my-cluster/a-abcdefghijklmnop1",
           "associationId": "a-abcdefghijklmnop1",
           "tags": {},
           "createdAt": 1700862734.922,
           "modifiedAt": 1700862734.922
       }
   }
   ```

   ###### Note

   You can specify a namespace and service account by name that doesn’t exist in the cluster. You must create the namespace, service account, and the workload that uses the service account for the EKS Pod Identity association to function.

## Confirm configuration

1. Confirm that the IAM role’s trust policy is configured correctly.

```
aws iam get-role --role-name my-role --query Role.AssumeRolePolicyDocument
```

An example output is as follows.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Allow EKS Auth service to assume this role for Pod Identities",
            "Effect": "Allow",
            "Principal": {
                "Service": "pods.eks.amazonaws.com"
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession"
            ]
        }
    ]
}
```

2. Confirm that the policy that you attached to your role in a previous step is attached to the role.

```
aws iam list-attached-role-policies --role-name my-role --query 'AttachedPolicies[].PolicyArn' --output text
```

An example output is as follows.

```

               arn:aws:iam::111122223333:policy/my-policy
```

3. Set a variable to store the Amazon Resource Name (ARN) of the policy that you want to use. Replace `my-policy` with the name of the policy that you want to confirm permissions for.

```
export policy_arn=arn:aws:iam::111122223333:policy/my-policy
```

4. View the default version of the policy.

```
aws iam get-policy --policy-arn $policy_arn
```

An example output is as follows.

```
{
    "Policy": {
        "PolicyName": "my-policy",
        "PolicyId": "EXAMPLEBIOWGLDEXAMPLE",
        "Arn": "arn:aws:iam::111122223333:policy/my-policy",
        "Path": "/",
        "DefaultVersionId": "v1",
        [...]
    }
}
```

5. View the policy contents to make sure that the policy includes all the permissions that your Pod needs. If necessary, replace `1` in the following command with the version that’s returned in the previous output.

```
aws iam get-policy-version --policy-arn $policy_arn --version-id v1
```

An example output is as follows.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-pod-secrets-bucket"
        }
    ]
}
```

If you created the example policy in a previous step, then your output is the same. If you created a different policy, then the `example` content is different.

## Next Steps

[Configure Pods to access AWS services with service accounts](pod-id-configure-pods.md "pod-id-configure-pods.md")
