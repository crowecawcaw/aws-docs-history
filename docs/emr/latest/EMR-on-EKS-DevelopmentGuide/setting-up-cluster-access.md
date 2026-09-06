

# Enable cluster access for Amazon EMR on EKS
<a name="setting-up-cluster-access"></a>

The following sections show a couple ways to enable cluster access. The first is by using Amazon EKS cluster access management (CAM) and the latter shows how to take manual steps to enable cluster access.

## Enable cluster access using EKS Access Entry (recommended)
<a name="setting-up-cluster-access-cam-integration"></a>

**Note**  
The `aws-auth` ConfigMap is deprecated. The recommended method to manage access to Kubernetes APIs is [Access Entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html).

Amazon EMR is integrated with [Amazon EKS cluster access management (CAM)](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html), so you can automate configuration of the necessary AuthN and AuthZ policies to run Amazon EMR Spark jobs in namespaces of Amazon EKS clusters. When you create a virtual cluster from an Amazon EKS cluster namespace, Amazon EMR automatically configures all of the necessary permissions, so you don't need to add any extra steps into your current workflows.

**Note**  
The Amazon EMR integration with Amazon EKS CAM is supported only for new Amazon EMR on EKS virtual clusters. You can't migrate existing virtual clusters to use this integration.

### Prerequisites
<a name="setting-up-cluster-access-cam-integration-prereqs"></a>
+ Make sure that you are running version 2.15.3 or higher of the AWS CLI
+ Your Amazon EKS cluster must be on version 1.23 or higher.

### Setup
<a name="setting-up-cluster-access-cam-integration-setup"></a>

To set up the integration between Amazon EMR and the AccessEntry API operations from Amazon EKS, make sure that you have completed the follow items:
+ Make sure that `authenticationMode` of your Amazon EKS cluster is set to `API_AND_CONFIG_MAP`.

  ```
  aws eks describe-cluster --name {{<eks-cluster-name>}}
  ```

  If it isn't already, set `authenticationMode` to `API_AND_CONFIG_MAP`.

  ```
  aws eks update-cluster-config 
      --name {{<eks-cluster-name>}} 
      --access-config authenticationMode=API_AND_CONFIG_MAP
  ```

  For more information about authentication modes, see [ Cluster authentication modes](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#authentication-modes).
+ Make sure that the [IAM role](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-iam.html) that you're using to run the `CreateVirtualCluster` and `DeleteVirtualCluster` API operations also has the following permissions:

  ```
  {
    "Effect": "Allow",
    "Action": [
      "eks:CreateAccessEntry"
    ],
    "Resource": "arn:{{<AWS_PARTITION>}}:eks:{{<AWS_REGION>}}:{{<AWS_ACCOUNT_ID>}}:cluster/{{<EKS_CLUSTER_NAME>}}"
  }, 
  {
    "Effect": "Allow",
    "Action": [
      "eks:DescribeAccessEntry",
      "eks:DeleteAccessEntry",
      "eks:ListAssociatedAccessPolicies",
      "eks:AssociateAccessPolicy",
      "eks:DisassociateAccessPolicy"
    ],
    "Resource": "arn:{{<AWS_PARTITION>}}:eks:<AWS_REGION>:<AWS_ACCOUNT_ID>:access-entry/<EKS_CLUSTER_NAME>/role/<AWS_ACCOUNT_ID>/AWSServiceRoleForAmazonEMRContainers/*"
  }
  ```
+ To create a least permissive policy, add the context keys `accessScope` and `namespaces`. The following example shows a policy with these context keys:

  ```
  {
              "Effect": "Allow",
              "Action": [
                  "eks:CreateAccessEntry"
              ],
              "Resource": [
                  "arn:{{<AWS_PARTITION>}}:eks:{{<AWS_REGION>}}:{{<AWS_ACCOUNT_ID>}}:cluster/{{<EKS_CLUSTER_NAME>}}"
  
              ]
          },
          {
              "Effect": "Allow",
              "Action": [
                  "eks:DescribeAccessEntry",
                  "eks:DeleteAccessEntry",
                  "eks:ListAssociatedAccessPolicies"
              ],
              "Resource": [
                  "arn:{{<AWS_PARTITION>}}:eks:{{<AWS_REGION>}}:{{<AWS_ACCOUNT_ID>}}:access-entry/{{<EKS_CLUSTER_NAME>}}/role/{{<AWS_ACCOUNT_ID>}}/AWSServiceRoleForAmazonEMRContainers/*"
              ]
          },
          {
              "Effect": "Allow",
              "Action": [
                  "eks:DisassociateAccessPolicy",
                  "eks:AssociateAccessPolicy"
              ],
              "Resource": [
                  "arn:{{<AWS_PARTITION>}}:eks:{{<AWS_REGION>}}:{{<AWS_ACCOUNT_ID>}}:access-entry/{{<EKS_CLUSTER_NAME>}}/role/{{<AWS_ACCOUNT_ID>}}/AWSServiceRoleForAmazonEMRContainers/*"
              ],
              "Condition": {
                  "StringEquals": {
                      "eks:accessScope": "namespace"
                  },
                  "ForAllValues:StringEquals": {
                      "eks:namespaces": [
                          "{{<EKS_NAMESPACE>}}"
                      ]
                  }
              }
          }
  ```

### Concepts and terminology
<a name="setting-up-cluster-access-cam-integration-concepts"></a>

The following is a list of terminologies and concepts related to Amazon EKS CAM.
+ Virtual cluster (VC) – logical representation of the namespace created in Amazon EKS. It’s a 1:1 link to an Amazon EKS cluster namespace. You can use it to run Amazon EMR workloads on a a Amazon EKS cluster within the specified namespace.
+ Namespace – mechanism to isolate groups of resources within a single EKS cluster.
+ Access policy – permissions that grant access and actions to an IAM role within an EKS cluster.
+ Access entry – an entry created with a role arn. You can link the access entry to an access policy to assign specific permissions in the Amazon EKS cluster.
+ EKS access entry integrated virtual cluster – the virtual cluster created using [access entry API operations](https://docs.aws.amazon.com/eks/latest/APIReference/API_Operations_Amazon_Elastic_Kubernetes_Service.html) from Amazon EKS.

## Enable cluster access using `aws-auth`
<a name="setting-up-cluster-access-aws-auth"></a>

You must allow Amazon EMR on EKS access to a specific namespace in your cluster by taking the following actions: creating a Kubernetes role, binding the role to a Kubernetes user, and mapping the Kubernetes user with the service linked role [`AWSServiceRoleForAmazonEMRContainers`](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/using-service-linked-roles.html). These actions are automated in `eksctl` when the IAM identity mapping command is used with `emr-containers` as the service name. You can perform these operations easily by using the following command.

```
eksctl create iamidentitymapping \
    --cluster {{my_eks_cluster}} \
    --namespace {{kubernetes_namespace}} \
    --service-name "emr-containers"
```

Replace {{my\_eks\_cluster}} with the name of your Amazon EKS cluster and replace {{kubernetes\_namespace}} with the Kubernetes namespace created to run Amazon EMR workloads. 

**Important**  
You must download the latest eksctl using the previous step [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) to use this functionality. 

### Manual steps to enable cluster access for Amazon EMR on EKS
<a name="setting-up-cluster-access-manual"></a>

You can also use the following manual steps to enable cluster access for Amazon EMR on EKS.

1. **Create a Kubernetes role in a specific namespace**

------
#### [ Amazon EKS 1.22 - 1.29 ]

   With Amazon EKS 1.22 - 1.29, run the following command to create a Kubernetes role in a specific namespace. This role grants the necessary RBAC permissions to Amazon EMR on EKS.

   ```
   namespace=my-namespace
   cat - >>EOF | kubectl apply -f - >>namespace "${namespace}"
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: emr-containers
     namespace: ${namespace}
   rules:
     - apiGroups: [""]
       resources: ["namespaces"]
       verbs: ["get"]
     - apiGroups: [""]
       resources: ["serviceaccounts", "services", "configmaps", "events", "pods", "pods/log"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
     - apiGroups: [""]
       resources: ["secrets"]
       verbs: ["create", "patch", "delete", "watch"]
     - apiGroups: ["apps"]
       resources: ["statefulsets", "deployments"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
     - apiGroups: ["batch"]
       resources: ["jobs"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
     - apiGroups: ["extensions", "networking.k8s.io"]
       resources: ["ingresses"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
     - apiGroups: ["rbac.authorization.k8s.io"]
       resources: ["roles", "rolebindings"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
     - apiGroups: [""]
       resources: ["persistentvolumeclaims"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete",  "deletecollection", "annotate", "patch", "label"]
   EOF
   ```

------
#### [ Amazon EKS 1.21 and below ]

   With Amazon EKS 1.21 and below, run the following command to create a Kubernetes role in a specific namespace. This role grants the necessary RBAC permissions to Amazon EMR on EKS.

   ```
   namespace=my-namespace
   cat - >>EOF | kubectl apply -f - >>namespace "${namespace}"
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: emr-containers
     namespace: ${namespace}
   rules:
     - apiGroups: [""]
       resources: ["namespaces"]
       verbs: ["get"]
     - apiGroups: [""]
       resources: ["serviceaccounts", "services", "configmaps", "events", "pods", "pods/log"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
     - apiGroups: [""]
       resources: ["secrets"]
       verbs: ["create", "patch", "delete", "watch"]
     - apiGroups: ["apps"]
       resources: ["statefulsets", "deployments"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
     - apiGroups: ["batch"]
       resources: ["jobs"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
     - apiGroups: ["extensions"]
       resources: ["ingresses"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "annotate", "patch", "label"]
     - apiGroups: ["rbac.authorization.k8s.io"]
       resources: ["roles", "rolebindings"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
     - apiGroups: [""]
       resources: ["persistentvolumeclaims"]
       verbs: ["get", "list", "watch", "describe", "create", "edit", "delete", "deletecollection", "annotate", "patch", "label"]
   EOF
   ```

------

1. **Create a Kubernetes role binding scoped to the namespace**

   Run the following command to create a Kubernetes role binding in the given namespace. This role binding grants the permissions defined in the role created in the previous step to a user named `emr-containers`. This user identifies [service-linked roles for Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/using-service-linked-roles.html) and thus allows Amazon EMR on EKS to perform actions as defined by the role you created.

   ```
   namespace={{my-namespace}}
   
   cat - <<EOF | kubectl apply -f - --namespace "${namespace}"
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: emr-containers
     namespace: ${namespace}
   subjects:
   - kind: User
     name: emr-containers
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: Role
     name: emr-containers
     apiGroup: rbac.authorization.k8s.io
   EOF
   ```

1. **Update Kubernetes `aws-auth` conﬁguration map**

   You can use one of the following options to map the Amazon EMR on EKS service-linked role with the `emr-containers` user that was bound with the Kubernetes role in the previous step.

   **Option 1: Using `eksctl`**

   Run the following `eksctl` command to map the Amazon EMR on EKS service-linked role with the `emr-containers` user.

   ```
   eksctl create iamidentitymapping \
       --cluster {{my-cluster-name}} \
       --arn "arn:aws:iam::{{my-account-id}}:role/AWSServiceRoleForAmazonEMRContainers" \
       --username emr-containers
   ```

   **Option 2: Without using eksctl**

   1. Run the following command to open the `aws-auth` configuration map in text editor. 

      ```
      kubectl edit -n kube-system configmap/aws-auth
      ```
**Note**  
If you receive an error stating `Error from server (NotFound): configmaps "aws-auth" not found`, see the steps in [Add user roles](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html) in the Amazon EKS User Guide to apply the stock ConfigMap. 

   1. Add Amazon EMR on EKS service-linked role details to the `mapRoles` section of the `ConfigMap`, under `data`. Add this section if it does not already exist in the file. The updated `mapRoles` section under data looks like the following example.

      ```
      apiVersion: v1
      data:
        mapRoles: |
          - rolearn: arn:aws:iam::<your-account-id>:role/AWSServiceRoleForAmazonEMRContainers
            username: emr-containers
          - ... <other previously existing role entries, if there's any>.
      ```

   1. Save the file and exit your text editor.

## Enable cluster access for Amazon SageMaker Unified Studio
<a name="setting-up-cluster-access-smus"></a>

Amazon EMR on EKS and Amazon SageMaker Unified Studio require access to an Amazon EKS cluster. Please follow the steps at [Enable EKS cluster access for EMR on EKS and SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/enable-eks-cluster-access-for-emr-on-eks-and-sagemaker-unified-studio.html) to provide access.