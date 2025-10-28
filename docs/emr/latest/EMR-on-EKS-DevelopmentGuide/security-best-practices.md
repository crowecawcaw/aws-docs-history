# Amazon EMR on EKS security best practices

Amazon EMR on EKS provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

###### Note

For more security best practices, see Amazon EMR on EKS security best practices.

## Apply principle of least privilege

Amazon EMR on EKS provides a granular access policy for applications using IAM roles, such as
execution roles. These execution roles are mapped to Kubernetes service accounts through the IAM
role’s trust policy. Amazon EMR on EKS creates pods within a registered Amazon EKS namespace that execute
user-provided application code. The job pods running the application code assume the execution
role when connecting to other AWS services. We recommend that execution roles be granted only the
minimum set of privileges required by the job, such as covering your application and access to
log destination. We also recommend auditing the jobs for permissions on a regular basis and upon
any change to application code.

## Access control list for endpoints

Managed endpoints can be created only for those EKS clusters that have been configured to use at least one private subnet in your VPC. This configuration restricts access to the load balancers created by managed endpoints so that they can only be accessed from your VPC. To further enhance security, we recommend that you configure security groups with these load balancers so that they can restrict incoming traffic to a selected set of IP addresses.

## Get the latest security updates for custom images

To use custom images with Amazon EMR on EKS, you can install any binaries and libraries on the image. You are responsible for the security patching of the binaries you add to the image. Amazon EMR on EKS images are regularly patched with latest security patches. To get the latest image, you must rebuild the custom images whenever there is a new base image version of the Amazon EMR release. For more information, see [Amazon EMR on EKS releases](emr-eks-releases.md "emr-eks-releases.md") and [Details for selecting a base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md").

## Limit pod credential access

Kubernetes supports several methods of assigning credentials to a pod. Provisioning multiple
credentials providers can increase the complexity of your security model. Amazon EMR on EKS has adopted
the use of [IAM
roles for services accounts (IRSA)](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md") as a standard credential provider within a registered
EKS namespace. Other methods are not supported, including [kube2iam](https://github.com/jtblin/kube2iam "https://github.com/jtblin/kube2iam"), [kiam](https://github.com/uswitch/kiam "https://github.com/uswitch/kiam") and using an EC2 instance profile of the
instance running on the cluster.

## Isolate untrusted application code

Amazon EMR on EKS does not inspect the integrity of the application code submitted by users of the system. If you are running a multi-tenanted virtual cluster that is configured using multiple execution roles that can be used to submit jobs by untrusted tenants running arbitrary code, there is a risk of a malicious application escalating its privileges. In this situation, consider isolating execution roles with similar privileges into a different virtual cluster.

## Role-based access control (RBAC) permissions

Administrators should strictly control Role-based access control (RBAC) permissions for
Amazon EMR on EKS managed namespaces. At a minimum, the following permissions should not be granted to
job submitters in Amazon EMR on EKS managed namespaces.

- Kubernetes RBAC permissions to modify configmap ‐ because Amazon EMR on EKS uses Kubernetes configmaps to generate managed pod templates that have the managed service account name. This attribute should not be mutated.
- Kubernetes RBAC permissions to exec into Amazon EMR on EKS pods ‐ to avoid giving access to managed pod templates that have the managed SA name. This attribute should not be mutated. This permission can also give access to the JWT token mounted into the pod which can then be used to retrieve the execution role credentials.
- Kubernetes RBAC permissions to create pods ‐ to prevent users from creating pods using a Kubernetes ServiceAccount which may be mapped to an IAM role with more AWS privileges than the user.
- Kubernetes RBAC permissions to deploy mutating webhook ‐ to prevent users from using the mutating webhook to mutate Kubernetes ServiceAccount name for pods created by Amazon EMR on EKS.
- Kubernetes RBAC permissions to read Kubernetes secrets ‐ to prevent users from reading confidential data stored in these secrets.

## Restrict access to nodegroup IAM role or instance

profile credentials

- We recommend that you assign minimum AWS permissions to nodegroup’s IAM role(s). This helps to avoid privilege escalation by code that may run using instance profile credentials of EKS worker nodes.
- To completely block access to instance profile credentials to all pods that runs in Amazon EMR on EKS managed namespaces, we recommend that you run `iptables` commands on EKS nodes. For more information, see [Restricting access to Amazon EC2 instance profile credentials](../../../eks/latest/userguide/restrict-ec2-credential-access.md "../../../eks/latest/userguide/restrict-ec2-credential-access.md"). However, it is important to properly scope your service account IAM roles so that your pods have all of the necessary permissions. For example, the node IAM role is assigned permissions to pull container images from Amazon ECR. If a pod isn't assigned those permissions, the pod can't pull container images from Amazon ECR. The VPC CNI plugin also needs to be updated. For more information, see [Walkthrough: Updating the VPC CNI plugin to use IAM roles for service accounts](../../../eks/latest/userguide/iam-roles-for-service-accounts-cni-walkthrough.md "../../../eks/latest/userguide/iam-roles-for-service-accounts-cni-walkthrough.md").
