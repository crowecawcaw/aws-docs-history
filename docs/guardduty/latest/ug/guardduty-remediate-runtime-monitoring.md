# Remediating Runtime Monitoring findings

When you enable Runtime Monitoring for your account, Amazon GuardDuty may generate [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md "findings-runtime-monitoring.md") that indicate
potential security issues in your AWS environment. The potential security issues indicate either
a compromised Amazon EC2 instance, container workload, an Amazon EKS cluster, or a set of compromised
credentials in your AWS environment. The security agent monitors runtime events from multiple
resource types. To identify the potentially compromised resource, view **Resource
type** in the generated finding details in the GuardDuty console. The following section
describes the recommended remediation steps for each resource type.

Instance
If the **Resource type** in the finding details is
**Instance**, it indicates that either an EC2 instance or an EKS node is
potentially compromised.

- To remediate a compromised EKS node, see [Remediating potentially compromised Kubernetes
  nodes](guardduty-remediate-kubernetes.md#compromised-kubernetes-node "guardduty-remediate-kubernetes.md#compromised-kubernetes-node").
- To remediate a compromised EC2 instance, see [Remediating a potentially compromised Amazon EC2
  instance](compromised-ec2.md "compromised-ec2.md").

EKSCluster
If the **Resource type** in the finding details is
**EKSCluster**, it indicates that either a pod or a container inside an EKS
cluster is potentially compromised.

- To remediate a compromised pod, see [Remediating potentially compromised Kubernetes
  pods](guardduty-remediate-kubernetes.md#compromised-kubernetes-pod "guardduty-remediate-kubernetes.md#compromised-kubernetes-pod").
- To remediate a compromised container image, see [Remediating potentially compromised
  container images](guardduty-remediate-kubernetes.md#compromised-kubernetes-image "guardduty-remediate-kubernetes.md#compromised-kubernetes-image").

ECSCluster
If the **Resource type** in the finding details is
**ECSCluster**, it indicates that either an ECS task or a container inside an
ECS task is potentially compromised.

1. **Identify the affected ECS cluster**

The GuardDuty Runtime Monitoring finding provides the ECS cluster details in the finding's details
panel or in the `resource.ecsClusterDetails` section in the finding JSON. 2. **Identify the affected ECS task**

The GuardDuty Runtime Monitoring finding provides the ECS task details in the finding's details panel
or in the `resource.ecsClusterDetails.taskDetails` section in the finding
JSON. 3. **Isolate the affected task**

Isolate the impacted task by denying all ingress and egress traffic to the task. A deny
all traffic rule may help stop an attack that is already underway, by severing all
connections to the task. 4. **Remediate the compromised task**

    1. Identify the vulnerability that compromised the task.
    2. Implement the fix for that vulnerability and start new a replacement task.
    3. Stop the vulnerable task.

Container
If the **Resource type** in the finding details is
**Container**, it indicates that a standalone container is potentially
compromised.

- To remediate, see [Remediating a potentially
  compromised standalone container](remediate-compromised-standalone-container.md "remediate-compromised-standalone-container.md").
- If the finding is generated across multiple containers using the same container image,
  see [Remediating potentially compromised
  container images](guardduty-remediate-kubernetes.md#compromised-kubernetes-image "guardduty-remediate-kubernetes.md#compromised-kubernetes-image").
- If the container has accessed the underlying EC2 host, its associated instance
  credentials may have been compromised. For more information, see [Remediating potentially compromised AWS
  credentials](compromised-creds.md "compromised-creds.md").
- If a potentially malicious actor has accessed the underlying EKS node or an EC2
  instance, see the recommended remediation under the _EKSCluster_ and
  _Instance_ tabs.

## Remediating compromised container

images

When a GuardDuty finding indicates a task compromise, the image used to launch the task could be
malicious or compromised. GuardDuty findings identify the container image within the
`resource.ecsClusterDetails.taskDetails.containers.image` field. You can determine
whether or not the image is malicious by scanning it for malware.

###### To remediate a compromised container image

1. Stop using the image immediately and remove it from your image repository.
2. Identify all of the tasks that are using this image.
3. Stop all of the tasks that are using the compromised image. Update their task definitions
   so that they stop using the compromised image.
