# Remediating EKS Protection findings

Amazon GuardDuty generates [findings](guardduty_findings.md "guardduty_findings.md") that indicate
potential Kubernetes security issues when EKS Protection is enabled for your account. For more
information, see [EKS Protection](kubernetes-protection.md "kubernetes-protection.md"). The following sections describe the
recommended remediation steps for these scenarios. Specific remediation actions are
described in the entry for that specific finding type. You can access the full information
about a finding type by selecting it from the [Active findings types table](guardduty_finding-types-active.md "guardduty_finding-types-active.md").

If any of the EKS Protection finding types were generated expectantly, you can consider adding
[Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md") to
prevent future alerts.

Different types of attacks and configuration issues can trigger GuardDuty EKS Protection findings.
This guide helps you identify the root causes of GuardDuty findings against your cluster and
outlines appropriate remediation guidance. The following are the primary root causes that
lead to GuardDuty Kubernetes findings:

- [Potential configuration issues](#compromised-kubernetes-config "#compromised-kubernetes-config")
- [Remediating potentially compromised Kubernetes
  users](#compromised-kubernetes-user "#compromised-kubernetes-user")
- [Remediating potentially compromised Kubernetes
  pods](#compromised-kubernetes-pod "#compromised-kubernetes-pod")
- [Remediating potentially compromised Kubernetes
  nodes](#compromised-kubernetes-node "#compromised-kubernetes-node")
- [Remediating potentially compromised
  container images](#compromised-kubernetes-image "#compromised-kubernetes-image")

###### Note

Before Kubernetes version 1.14, the `system:unauthenticated` group was
associated to `system:discovery` and `system:basic-user`
**ClusterRoles** by default. This may allow unintended access from
anonymous users. Cluster updates do not revoke these permissions, which means that even
if you have updated your cluster to version 1.14 or later, these permissions may still
be in place. We recommend that you disassociate these permissions from the
`system:unauthenticated` group.

For more information about removing these permissions, see
[Secure Amazon EKS clusters with best practices](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the
**Amazon EKS User Guide**.

## Potential configuration issues

If a finding indicates a configuration issue, see the remediation section of that
finding for guidance on resolving that particular issue. For more information, see the
following finding types that indicate configuration issues:

- [Policy:Kubernetes/AnonymousAccessGranted](guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-anonymousaccessgranted "guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-anonymousaccessgranted")
- [Policy:Kubernetes/ExposedDashboard](guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-exposeddashboard "guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-exposeddashboard")
- [Policy:Kubernetes/AdminAccessToDefaultServiceAccount](guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-adminaccesstodefaultserviceaccount "guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-adminaccesstodefaultserviceaccount")
- [Policy:Kubernetes/KubeflowDashboardExposed](guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-kubeflowdashboardexposed "guardduty-finding-types-eks-audit-logs.md#policy-kubernetes-kubeflowdashboardexposed")
- Any finding that ends in **SuccessfulAnonymousAccess**

## Remediating potentially compromised Kubernetes

users

A GuardDuty finding can indicate a compromised Kubernetes user when a user identified in the
finding has performed an unexpected API action. You can identify the user in the
**Kubernetes user details** section of a finding details in the console,
or in the
`resource.kubernetesDetails.kubernetesUserDetails` of
the findings JSON. These user details include `user name`, `uid`,
and the Kubernetes groups that the user belongs to.

If the user was accessing the workload using an IAM entity, you can use the
`Access Key details` section to identify the details of an IAM role or
user. See the following user types and their remediation guidance.

###### Note

You can use Amazon Detective to further investigate the IAM role or user identified in
the finding. While viewing the finding details in GuardDuty console, choose
**Investigate in Detective**. Then select AWS user or role from
the listed items to investigate it in Detective.

**Built-in Kubernetes admin** – The default
user assigned by Amazon EKS to the IAM identity that created the cluster. This user
type is identified by the user name `kubernetes-admin`.

**To revoke access of a built-in Kubernetes
admin:**

- Identify the `userType` from the `Access Key
details` section.
  - If the `userType` is **Role**
    and the role belongs to an EC2 instance role:
    - Identify that instance then follow the
      instructions in [Remediating a potentially compromised Amazon EC2
      instance](compromised-ec2.md "compromised-ec2.md").

  - If the `userType` is **User**,
    or is a **Role** that was assumed by a
    user:
    1. [Rotate the access key](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") of that
       user.
    2. Rotate any secrets that user had access to.
    3. Review the information in [My AWS account may be compromised](https://repost.aws/knowledge-center/potential-account-compromise "https://repost.aws/knowledge-center/potential-account-compromise") for
       further details.

**OIDC authenticated user** – A user
granted access through an OIDC provider. Typically an OIDC user has an email
address as a user name. You can check if your cluster uses OIDC with the
following command: `aws eks list-identity-provider-configs --cluster-name
 `your-cluster-name``

**To revoke access of an OIDC authenticated
user:**

1. Rotate the credentials of that user in the OIDC provider.
2. Rotate any secrets that user had access to.

**AWS-Auth ConfigMap defined user** – An
IAM user that was granted access through an AWS-auth ConfigMap. For more
information, see [Managing users or IAM roles
for your cluster](../../../eks/latest/userguide/add-user-role.md "../../../eks/latest/userguide/add-user-role.md") in the **Amazon EKS User Guide**.
You can review their
permissions using the following command: `kubectl edit configmaps aws-auth
 --namespace kube-system`

**To revoke access of an AWS ConfigMap
user:**

1. Use the following command to open the ConfigMap.

```
kubectl edit configmaps aws-auth --namespace kube-system
```

2. Identify the role or user entry under the **mapRoles** or **mapUsers** section with the same user name as the one
   reported in the Kubernetes user details section of your GuardDuty finding.
   See the following example, where the admin user has been identified
   in a finding.

```
apiVersion: v1
data:
  mapRoles: |
    - rolearn: arn:aws:iam::444455556666:role/eksctl-my-cluster-nodegroup-standard-wo-NodeInstanceRole-1WP3NUE3O6UCF
      user name: system:node:EC2_PrivateDNSName
      groups:
        - system:bootstrappers
        - system:nodes
  mapUsers: |
    `- userarn: arn:aws:iam::123456789012:user/admin
 username: admin
 groups:
 - system:masters`
    - userarn: arn:aws:iam::111122223333:user/ops-user
      username: ops-user
      groups:
        - system:masters
```

3. Remove that user from the ConfigMap. See the following example
   where the admin user has been removed.

```
apiVersion: v1
data:
  mapRoles: |
    - rolearn: arn:aws:iam::111122223333:role/eksctl-my-cluster-nodegroup-standard-wo-NodeInstanceRole-1WP3NUE3O6UCF
      username: system:node:{{EC2PrivateDNSName}}
      groups:
        - system:bootstrappers
        - system:nodes
  mapUsers: |
    - userarn: arn:aws:iam::111122223333:user/ops-user
      username: ops-user
      groups:
        - system:masters
```

4. If the `userType` is **User**, or is a
   **Role** that was assumed by a user:
   1. [Rotate the access key](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") of that user.
   2. Rotate any secrets that user had access to.
   3. Review the information in [My AWS account may be compromised](https://aws.amazon.com//premiumsupport/knowledge-center/potential-account-compromise/ "https://aws.amazon.com//premiumsupport/knowledge-center/potential-account-compromise/") for further
      details.

If the finding does not have a `resource.accessKeyDetails` section, the
user is a Kubernetes service account.

**Service account** – The service account
provides an identity for pods and can be identified by a user name with the
following format:
`system:serviceaccount:`namespace`:`service_account_name``.

**To revoke access to a service
account:**

1. Rotate the service account credentials.
2. Review the guidance for pod compromise in the following
   section.

## Remediating potentially compromised Kubernetes

pods

When GuardDuty specifies details of a pod or workload resource inside the
`resource.kubernetesDetails.kubernetesWorkloadDetails` section, that pod
or workload resource has been potentially compromised. A GuardDuty finding can indicate a
single pod has been compromised or that multiple pods have been compromised through a
higher-level resource. See the following compromise scenarios for guidance on how to
identify the pod or pods that have been compromised.

**Single pods compromise**

If the `type` field inside the
`resource.kubernetesDetails.kubernetesWorkloadDetails`
section is **pods**, the finding identifies a single pods.
The name field is the `name` of the pods and
`namespace` field is its namespace.

For information about identifying the worker
node running the pods, see [Identify the offending pods and worker node](../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_the_offending_pod_and_worker_node "../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_the_offending_pod_and_worker_node") in the _Amazon EKS
Best Practices Guide_.

**Pods compromised through workload
resource**

If the `type` field inside the
`resource.kubernetesDetails.kubernetesWorkloadDetails`
section identifies a **Workload Resource**,
such as a `Deployment`, it is likely that all of the pods within
that workload resource have been compromised.

For information about identifying all the pods
of the workload resource and the nodes on which they are running, see [Identify the offending pods and worker nodes using workload
name](../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_the_offending_pods_and_worker_nodes_using_workload_name "../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_the_offending_pods_and_worker_nodes_using_workload_name") in the _Amazon EKS Best Practices Guide_.

**Pods compromised through service
account**

If a GuardDuty finding identifies a Service Account in the
`resource.kubernetesDetails.kubernetesUserDetails` section,
it is likely that pods using the identified service account are compromised.
The user name reported by a finding is a service account if it has the
following format:
`system:serviceaccount:`namespace`:`service_account_name``.

For information about identifying all the pods
using the service account and the nodes on which they are running, see
[Identify the offending pods and worker nodes using service account
name](../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_the_offending_pods_and_worker_nodes_using_service_account_name "../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_the_offending_pods_and_worker_nodes_using_service_account_name") in the _Amazon EKS Best Practices Guide_.

After you have identified all the compromised pods and the
nodes on which they are running, see [Isolate the pod by creating a network policy that denies all ingress and egress traffic to
the pod](../../../eks/latest/best-practices/incident-response-and-forensics.md#_isolate_the_pod_by_creating_a_network_policy_that_denies_all_ingress_and_egress_traffic_to_the_pod "../../../eks/latest/best-practices/incident-response-and-forensics.md#_isolate_the_pod_by_creating_a_network_policy_that_denies_all_ingress_and_egress_traffic_to_the_pod") in the _Amazon EKS Best Practices Guide_.

###### To remediate a potentially compromised pod:

1. Identify the vulnerability that compromised the pods.
2. Implement the fix for that vulnerability and start new replacement
   pods.
3. Delete the vulnerable pods.

For more information, see [Redeploy compromised pod or workload resource](../../../eks/latest/best-practices/incident-response-and-forensics.md#_redeploy_compromised_pod_or_workload_resource "../../../eks/latest/best-practices/incident-response-and-forensics.md#_redeploy_compromised_pod_or_workload_resource")
in the _Amazon EKS Best Practices Guide_.

If the worker node has been assigned an IAM role that allows Pods to gain access to
other AWS resources, remove those roles from the instance to prevent further damage
from the attack. Similarly, if the Pod has been assigned an IAM role, evaluate whether
you can safely remove the IAM policies from the role without impacting other
workloads.

## Remediating potentially compromised

container images

When a GuardDuty finding indicates a pod compromise, the image used to launch the pod
could be potentially malicious or compromised. GuardDuty findings identify the container
image within the
`resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image`
field. You can determine if the image is malicious by scanning it for malware.

###### To remediate a potentially compromised container image:

1. Stop using the image immediately and remove it from your image
   repository.
2. Identify all pods using the potentially compromised image.

For more information, see [Identify pods with vulnerable or compromised images
and worker nodes](../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_pods_with_vulnerable_or_compromised_images_and_worker_nodes "../../../eks/latest/best-practices/incident-response-and-forensics.md#_identify_pods_with_vulnerable_or_compromised_images_and_worker_nodes") in the _Amazon EKS Best Practices Guide_. 3. Isolate the potentially compromised pods, rotate credentials, and gather data
for analysis. For more information, see [Isolate the pod by creating a network policy that denies all ingress
and egress traffic to the pod](../../../eks/latest/best-practices/incident-response-and-forensics.md#_isolate_the_pod_by_creating_a_network_policy_that_denies_all_ingress_and_egress_traffic_to_the_pod "../../../eks/latest/best-practices/incident-response-and-forensics.md#_isolate_the_pod_by_creating_a_network_policy_that_denies_all_ingress_and_egress_traffic_to_the_pod")
in the _Amazon EKS Best Practices Guide_. 4. Delete all pods using the potentially compromised image.

## Remediating potentially compromised Kubernetes

nodes

A GuardDuty finding can indicate a node compromise if the user identified in the finding
represents a node identity or if the finding indicates the use of a privileged
container.

The user identity is a worker node if the **username**
field has following format: `system:node:node name`. For example,
`system:node:ip-192-168-3-201.ec2.internal`. This indicates that the
adversary has gained access to the node and it is using the node’s credentials to talk
to the Kubernetes API endpoint.

A finding indicates the use of a privileged container if one or more of the containers
listed in the finding has the
`resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.privileged`
finding field set to `True`.

###### To remediate a potentially compromised node:

1. Isolate the pod, rotate its credentials, and gather data for forensic
   analysis.

For more information, see [Isolate the pod by creating a network policy that denies all ingress
and egress traffic to the pod](../../../eks/latest/best-practices/incident-response-and-forensics.md#_isolate_the_pod_by_creating_a_network_policy_that_denies_all_ingress_and_egress_traffic_to_the_pod "../../../eks/latest/best-practices/incident-response-and-forensics.md#_isolate_the_pod_by_creating_a_network_policy_that_denies_all_ingress_and_egress_traffic_to_the_pod")
in the _Amazon EKS Best Practices Guide_. 2. Identify the service accounts used by all of the pods running on the
potentially compromised node. Review their permissions and rotate the service
accounts if needed. 3. Terminate the potentially compromised node.
