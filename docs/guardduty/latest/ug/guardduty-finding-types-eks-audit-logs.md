# EKS Protection finding types

The following findings are specific to Amazon EKS resources and have a
**resource_type** of `EKSCluster`. The severity and details
of the findings differ based on finding type.

For all EKS audit logs type findings we recommend that you examine the resource in
question to determine if the activity is expected or potentially malicious. For guidance on
remediating a compromised EKS audit logs resource identified by a GuardDuty finding, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

###### Note

If the activity because of which these findings get generated is expected, consider
adding [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md") to prevent future alerts.

###### Topics

- [CredentialAccess:Kubernetes/MaliciousIPCaller](#credentialaccess-kubernetes-maliciousipcaller "#credentialaccess-kubernetes-maliciousipcaller")
- [CredentialAccess:Kubernetes/MaliciousIPCaller.Custom](#credentialaccess-kubernetes-maliciousipcallercustom "#credentialaccess-kubernetes-maliciousipcallercustom")
- [CredentialAccess:Kubernetes/SuccessfulAnonymousAccess](#credentialaccess-kubernetes-successfulanonymousaccess "#credentialaccess-kubernetes-successfulanonymousaccess")
- [CredentialAccess:Kubernetes/TorIPCaller](#credentialaccess-kubernetes-toripcaller "#credentialaccess-kubernetes-toripcaller")
- [DefenseEvasion:Kubernetes/MaliciousIPCaller](#defenseevasion-kubernetes-maliciousipcaller "#defenseevasion-kubernetes-maliciousipcaller")
- [DefenseEvasion:Kubernetes/MaliciousIPCaller.Custom](#defenseevasion-kubernetes-maliciousipcallercustom "#defenseevasion-kubernetes-maliciousipcallercustom")
- [DefenseEvasion:Kubernetes/SuccessfulAnonymousAccess](#defenseevasion-kubernetes-successfulanonymousaccess "#defenseevasion-kubernetes-successfulanonymousaccess")
- [DefenseEvasion:Kubernetes/TorIPCaller](#defenseevasion-kubernetes-toripcaller "#defenseevasion-kubernetes-toripcaller")
- [Discovery:Kubernetes/MaliciousIPCaller](#discovery-kubernetes-maliciousipcaller "#discovery-kubernetes-maliciousipcaller")
- [Discovery:Kubernetes/MaliciousIPCaller.Custom](#discovery-kubernetes-maliciousipcallercustom "#discovery-kubernetes-maliciousipcallercustom")
- [Discovery:Kubernetes/SuccessfulAnonymousAccess](#discovery-kubernetes-successfulanonymousaccess "#discovery-kubernetes-successfulanonymousaccess")
- [Discovery:Kubernetes/TorIPCaller](#discovery-kubernetes-toripcaller "#discovery-kubernetes-toripcaller")
- [Execution:Kubernetes/ExecInKubeSystemPod](#execution-kubernetes-execinkubesystempod "#execution-kubernetes-execinkubesystempod")
- [Impact:Kubernetes/MaliciousIPCaller](#impact-kubernetes-maliciousipcaller "#impact-kubernetes-maliciousipcaller")
- [Impact:Kubernetes/MaliciousIPCaller.Custom](#impact-kubernetes-maliciousipcallercustom "#impact-kubernetes-maliciousipcallercustom")
- [Impact:Kubernetes/SuccessfulAnonymousAccess](#impact-kubernetes-successfulanonymousaccess "#impact-kubernetes-successfulanonymousaccess")
- [Impact:Kubernetes/TorIPCaller](#impact-kubernetes-toripcaller "#impact-kubernetes-toripcaller")
- [Persistence:Kubernetes/ContainerWithSensitiveMount](#persistence-kubernetes-containerwithsensitivemount "#persistence-kubernetes-containerwithsensitivemount")
- [Persistence:Kubernetes/MaliciousIPCaller](#persistence-kubernetes-maliciousipcaller "#persistence-kubernetes-maliciousipcaller")
- [Persistence:Kubernetes/MaliciousIPCaller.Custom](#persistence-kubernetes-maliciousipcallercustom "#persistence-kubernetes-maliciousipcallercustom")
- [Persistence:Kubernetes/SuccessfulAnonymousAccess](#persistence-kubernetes-successfulanonymousaccess "#persistence-kubernetes-successfulanonymousaccess")
- [Persistence:Kubernetes/TorIPCaller](#persistence-kubernetes-toripcaller "#persistence-kubernetes-toripcaller")
- [Policy:Kubernetes/AdminAccessToDefaultServiceAccount](#policy-kubernetes-adminaccesstodefaultserviceaccount "#policy-kubernetes-adminaccesstodefaultserviceaccount")
- [Policy:Kubernetes/AnonymousAccessGranted](#policy-kubernetes-anonymousaccessgranted "#policy-kubernetes-anonymousaccessgranted")
- [Policy:Kubernetes/ExposedDashboard](#policy-kubernetes-exposeddashboard "#policy-kubernetes-exposeddashboard")
- [Policy:Kubernetes/KubeflowDashboardExposed](#policy-kubernetes-kubeflowdashboardexposed "#policy-kubernetes-kubeflowdashboardexposed")
- [PrivilegeEscalation:Kubernetes/PrivilegedContainer](#privilegeescalation-kubernetes-privilegedcontainer "#privilegeescalation-kubernetes-privilegedcontainer")
- [CredentialAccess:Kubernetes/AnomalousBehavior.SecretsAccessed](#credaccess-kubernetes-anomalousbehavior-secretsaccessed "#credaccess-kubernetes-anomalousbehavior-secretsaccessed")
- [PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated](#privesc-kubernetes-anomalousbehavior-rolebindingcreated "#privesc-kubernetes-anomalousbehavior-rolebindingcreated")
- [Execution:Kubernetes/AnomalousBehavior.ExecInPod](#execution-kubernetes-anomalousbehvaior-execinprod "#execution-kubernetes-anomalousbehvaior-execinprod")
- [PrivilegeEscalation:Kubernetes/AnomalousBehavior.WorkloadDeployed!PrivilegedContainer](#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer "#privesc-kubernetes-anomalousbehavior-workloaddeployed-privcontainer")
- [Persistence:Kubernetes/AnomalousBehavior.WorkloadDeployed!ContainerWithSensitiveMount](#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount "#privesc-kubernetes-anomalousbehavior-workloaddeployed-containerwithsensitivemount")
- [Execution:Kubernetes/AnomalousBehavior.WorkloadDeployed](#exec-kubernetes-anomalousbehavior-workloaddeployed "#exec-kubernetes-anomalousbehavior-workloaddeployed")
- [PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleCreated](#privesc-kubernetes-anomalousbehavior-rolecreated "#privesc-kubernetes-anomalousbehavior-rolecreated")
- [Discovery:Kubernetes/AnomalousBehavior.PermissionChecked](#discovery-kubernetes-anomalousbehavrior-permissionchecked "#discovery-kubernetes-anomalousbehavrior-permissionchecked")

###### Note

Before Kubernetes version 1.14, the `system:unauthenticated` group was
associated to `system:discovery` and `system:basic-user`
**ClusterRoles** by default. This association may allow unintended
access from anonymous users. Cluster updates do not revoke these permissions. Even if
you updated your cluster to version 1.14 or higher, these permissions may still be
enabled. We recommend that you disassociate these permissions from the
`system:unauthenticated` group. For guidance on revoking these
permissions, see [Security best practices for
Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_.

## CredentialAccess:Kubernetes/MaliciousIPCaller

### An API

commonly used to access credentials or secrets in a Kubernetes cluster was invoked
from a known malicious IP address.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is associated with known malicious activity. The API observed is commonly
associated with the credential access tactics where an adversary is attempting
to collect passwords, usernames, and access keys for your Kubernetes cluster.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## CredentialAccess:Kubernetes/MaliciousIPCaller.Custom

### An

API commonly used to access credentials or secrets in a Kubernetes cluster was
invoked from an IP address on a custom threat list.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is included on a threat list that you uploaded. The threat list associated
with this finding is listed in the **Additional Information**
section of a finding's details. The API observed is commonly associated with the
credential access tactics where an adversary is attempting to collect passwords,
usernames, and access keys for your Kubernetes cluster.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and and revoke the permissions, if needed, by
following the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## CredentialAccess:Kubernetes/SuccessfulAnonymousAccess

### An API commonly used to access credentials or secrets in a Kubernetes cluster was

invoked by an unauthenticated user.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was successfully invoked by the
`system:anonymous` user. API calls made by
`system:anonymous` are unauthenticated. The observed API is
commonly associated with the credential access tactics where an adversary is
attempting to collect passwords, usernames, and access keys for your Kubernetes
cluster. This activity indicates that anonymous or unauthenticated access is
permitted on the API action reported in the finding and may be permitted on
other actions. If this behavior is not expected, it may indicate a configuration
mistake or that your credentials are compromised.

**Remediation recommendations:**

You should examine the permissions that have been granted to the
`system:anonymous` user on your cluster and ensure that all the
permissions are needed. If the permissions were granted mistakenly or
maliciously, you should revoke access of the user and reverse any changes made
by an adversary to your cluster. For more information, see [Security best practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## CredentialAccess:Kubernetes/TorIPCaller

### An API

commonly used to access credentials or secrets in a Kubernetes cluster was invoked
from a Tor exit node IP address.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API was invoked from a Tor exit node IP
address. The API observed is commonly associated with the credential access
tactics where an adversary is attempting to collect passwords, usernames, and
access keys for your Kubernetes cluster. Tor is software for enabling anonymous
communication. It encrypts and randomly bounces communications through relays
between a series of network nodes. The last Tor node is called the exit node.
This can indicate unauthorized access to your Kubernetes cluster resources with the
intent of hiding the attacker's true identity.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## DefenseEvasion:Kubernetes/MaliciousIPCaller

### An API

commonly used to evade defensive measures was invoked from a known malicious IP
address.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is associated with known malicious activity. The API observed is commonly
associated with defense evasion tactics where an adversary is trying to hide
their actions to avoid detection.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## DefenseEvasion:Kubernetes/MaliciousIPCaller.Custom

### An

API commonly used to evade defensive measures was invoked from an IP address on
a custom threat list.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is included on a threat list that you uploaded. The threat list associated
with this finding is listed in the **Additional Information**
section of a finding's details. The API observed is commonly associated with
defense evasion tactics where an adversary is trying to hide their actions to
avoid detection.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## DefenseEvasion:Kubernetes/SuccessfulAnonymousAccess

### An

API commonly used to evade defensive measures was invoked by an unauthenticated
user.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was successfully invoked by the
`system:anonymous` user. API calls made by
`system:anonymous` are unauthenticated. The observed API is
commonly associated with defense evasion tactics where an adversary is trying to
hide their actions to avoid detection. This activity indicates that anonymous or
unauthenticated access is permitted on the API action reported in the finding
and may be permitted on other actions. If this behavior is not expected, it may
indicate a configuration mistake or that your credentials are compromised.

**Remediation recommendations:**

You should examine the permissions that have been granted to the
`system:anonymous` user on your cluster and ensure that all the
permissions are needed. If the permissions were granted mistakenly or
maliciously, you should revoke access of the user and reverse any changes made
by an adversary to your cluster. For more information, see [Security best practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## DefenseEvasion:Kubernetes/TorIPCaller

### An API commonly

used to evade defensive measures was invoked from a Tor exit node IP
address.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API was invoked from a Tor exit node IP
address. The API observed is commonly associated with defense evasion tactics
where an adversary is trying to hide their actions to avoid detection. Tor is
software for enabling anonymous communication. It encrypts and randomly bounces
communications through relays between a series of network nodes. The last Tor
node is called the exit node. This can indicate unauthorized access to your
Kubernetes cluster with the intent of hiding the adversary's true identity.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Discovery:Kubernetes/MaliciousIPCaller

### An API commonly

used to discover resources in a Kubernetes cluster was invoked from an IP
address.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is associated with known malicious activity. The observed API is commonly
used with the discovery stage of an attack wherein an attacker is gathering
information to determine if your Kubernetes cluster is susceptible to a broader
attack.

###### For unauthenticated access

MaliciousIPCaller findings are not generated for
unauthenticated access.

SuccessfulAnonymousAccess findings are generated for
unauthenticated or anonymous access.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Discovery:Kubernetes/MaliciousIPCaller.Custom

### An API

commonly used to discover resources in a Kubernetes cluster was invoked from an IP
address on a custom threat list.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API was invoked from an IP address that is
included on a threat list that you uploaded. The threat list associated with
this finding is listed in the **Additional Information**
section of a finding's details. The observed API is commonly used with the
discovery stage of an attack wherein an attacker is gathering information to
determine if your Kubernetes cluster is susceptible to a broader attack.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Discovery:Kubernetes/SuccessfulAnonymousAccess

### An API

commonly used to discover resources in a Kubernetes cluster was invoked by an
unauthenticated user.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API operation was successfully invoked by the
`system:anonymous` user. API calls made by
`system:anonymous` are unauthenticated. The observed API is
commonly associated with the discovery stage of an attack when an adversary is
gathering information on your Kubernetes cluster. This activity indicates that
anonymous or unauthenticated access is permitted on the API action reported in
the finding and may be permitted on other actions. If this behavior is not
expected, it may indicate a configuration mistake or that your credentials are
compromised.

This finding type excludes the health check API endpoints such as
`/healthz`, `/livez`, `/readyz`, and
`/version`.

**Remediation recommendations:**

You should examine the permissions that have been granted to the
`system:anonymous` user on your cluster and ensure that all the
permissions are needed. If the permissions were granted mistakenly or
maliciously, you should revoke access of the user and reverse any changes made
by an adversary to your cluster. For more information, see [Security best practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Discovery:Kubernetes/TorIPCaller

### An API commonly used

to discover resources in a Kubernetes cluster was invoked from a Tor exit node IP
address.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API was invoked from a Tor exit node IP
address. The observed API is commonly used with the discovery stage of an attack
wherein an attacker is gathering information to determine if your Kubernetes cluster
is susceptible to a broader attack. Tor is software for enabling anonymous
communication. It encrypts and randomly bounces communications through relays
between a series of network nodes. The last Tor node is called the exit node.
This can indicate unauthorized access to your Kubernetes cluster with the intent of
hiding the adversary's true identity.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the APIand revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Execution:Kubernetes/ExecInKubeSystemPod

### A command was

executed inside a pod within the `kube-system` namespace

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that a command was executed in a pod within the
`kube-system` namespace using **Kubernetes exec
API**. `kube-system` namespace is a default namespaces,
which is primarily used for system level components such as
`kube-dns` and `kube-proxy`. It is very uncommon to
execute commands inside pods or containers under `kube-system`
namespace and may indicate suspicious activity.

**Remediation recommendations:**

If the execution of this command is unexpected, the credentials of the user
identity used to execute the command may be compromised. Revoke access of the
user and reverse any changes made by an adversary to your cluster. For more
information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Impact:Kubernetes/MaliciousIPCaller

### An API commonly

used to tamper with resources in a Kubernetes cluster was invoked from a known
malicious IP address.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is associated with known malicious activity. The observed API is commonly
associated with impact tactics where an adversary is trying to manipulate,
interrupt, or destroy data within your AWS environment.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Impact:Kubernetes/MaliciousIPCaller.Custom

### An API

commonly used to tamper with resources in a Kubernetes cluster was invoked from an IP
address on a custom threat list.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is included on a threat list that you uploaded. The threat list associated
with this finding is listed in the **Additional Information**
section of a finding's details. The observed API is commonly associated with
impact tactics where an adversary is trying to manipulate, interrupt, or destroy
data within your AWS environment.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Impact:Kubernetes/SuccessfulAnonymousAccess

### An API

commonly used to tamper with resources in a Kubernetes cluster was invoked by an
unauthenticated user.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was successfully invoked by the
`system:anonymous` user. API calls made by
`system:anonymous` are unauthenticated. The observed API is
commonly associated with the impact stage of an attack when an adversary is
tampering with resources in your cluster. This activity indicates that anonymous
or unauthenticated access is permitted on the API action reported in the finding
and may be permitted on other actions. If this behavior is not expected, it may
indicate a configuration mistake or that your credentials are compromised.

**Remediation recommendations:**

You should examine the permissions that have been granted to the
`system:anonymous` user on your cluster and ensure that all the
permissions are needed. If the permissions were granted mistakenly or
maliciously, you should revoke access of the user and reverse any changes made
by an adversary to your cluster. For more information, see [Security best practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Impact:Kubernetes/TorIPCaller

### An API commonly used to

tamper with resources in a Kubernetes cluster was invoked from a Tor exit node IP
address.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API was invoked from a Tor exit node IP
address. The API observed is commonly associated with impact tactics where an
adversary is trying to manipulate, interrupt, or destroy data within your AWS
environment. Tor is software for enabling anonymous communication. It encrypts
and randomly bounces communications through relays between a series of network
nodes. The last Tor node is called the exit node. This can indicate unauthorized
access to your Kubernetes cluster with the intent of hiding the adversary's true
identity.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Persistence:Kubernetes/ContainerWithSensitiveMount

### A

container was launched with a sensitive external host path mounted
inside.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that a container was launched with a configuration
that included a sensitive host path with write access in the
`volumeMounts` section. This makes the sensitive host path
accessible and writable from inside the container. This technique is commonly
used by adversaries to gain access to the host's filesystem.

**Remediation recommendations:**

If this container launch is unexpected, the credentials of the user identity
used to launch the container may be compromised. Revoke access of the user and
reverse any changes made by an adversary to your cluster. For more information,
see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If this container launch is expected, it's recommended that you use a
suppression rule consisting of a filter criteria based on the
`resource.KubernetesDetails.KubernetesWorkloadDetails.containers.imagePrefix`
field. In the filter criteria the `imagePrefix` field should be same
as the `imagePrefix` specified in the finding. To learn more about
creating suppression rules see [Suppression
rules](findings_suppression-rule.md "findings_suppression-rule.md").

## Persistence:Kubernetes/MaliciousIPCaller

### An API

commonly used to obtain persistent access to a Kubernetes cluster was invoked from a
known malicious IP address.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is associated with known malicious activity. The API observed is commonly
associated with persistence tactics where an adversary has gained access to your
Kubernetes cluster and is attempting to maintain that access.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Persistence:Kubernetes/MaliciousIPCaller.Custom

### An API

commonly used to obtain persistent access to a Kubernetes cluster was invoked from an
IP address on a custom threat list.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API operation was invoked from an IP address
that is included on a threat list that you uploaded. The threat list associated
with this finding is listed in the **Additional Information**
section of a finding's details. The API observed is commonly associated with
persistence tactics where an adversary has gained access to your Kubernetes cluster
and is attempting to maintain that access.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Persistence:Kubernetes/SuccessfulAnonymousAccess

### An

API commonly used to obtain high-level permissions to a Kubernetes cluster was
invoked by an unauthenticated user.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that an API operation was successfully invoked by the
`system:anonymous` user. API calls made by
`system:anonymous` are unauthenticated. The observed API is
commonly associated with the persistence tactics where an adversary has gained
access to your cluster and is attempting to maintain that access. This activity
indicates that anonymous or unauthenticated access is permitted on the API
action reported in the finding and may be permitted on other actions. If this
behavior is not expected, it may indicate a configuration mistake or that your
credentials are compromised.

**Remediation recommendations:**

You should examine the permissions that have been granted to the
`system:anonymous` user on your cluster and ensure that all the
permissions are needed. If the permissions were granted mistakenly or
maliciously, you should revoke access of the user and reverse any changes made
by an adversary to your cluster. For more information, see [Security best practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Persistence:Kubernetes/TorIPCaller

### An API commonly

used to obtain persistent access to a Kubernetes cluster was invoked from a Tor exit
node IP address.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an API was invoked from a Tor exit node IP
address. The API observed is commonly associated with persistence tactics where
an adversary has gained access to your Kubernetes cluster and is attempting to
maintain that access. Tor is software for enabling anonymous communication. It
encrypts and randomly bounces communications through relays between a series of
network nodes. The last Tor node is called the exit node. This can indicate
unauthorized access to your AWS resources with the intent of hiding the
attacker's true identity.

**Remediation recommendations:**

If the user reported in the finding under the `KubernetesUserDetails`
section is `system:anonymous`, investigate why the anonymous user was
permitted to invoke the API and revoke the permissions, if needed, by following
the instructions in [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the user is an
authenticated user, investigate to determine if the activity was legitimate or
malicious. If the activity was malicious revoke access of the user and reverse
any changes made by an adversary to your cluster. For more information, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Policy:Kubernetes/AdminAccessToDefaultServiceAccount

### The default service account was granted admin privileges on a Kubernetes

cluster.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that the default service account for a namespace in
your Kubernetes cluster was granted admin privileges. Kubernetes creates a default service
account for all the namespaces in the cluster. It automatically assigns the
default service account as an identity to pods that have not been explicitly
associated to another service account. If the default service account has admin
privileges, it may result in pods being unintentionally launched with admin
privileges. If this behavior is not expected, it may indicate a configuration
mistake or that your credentials are compromised.

**Remediation recommendations:**

You should not use the default service account to grant permissions to pods.
Instead you should create a dedicated service account for each workload and
grant permission to that account on a needs basis. To fix this issue, you should
create dedicated service accounts for all your pods and workloads and update the
pods and workloads to migrate from the default service account to their
dedicated accounts. Then you should remove the admin permission from the default
service account. For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Policy:Kubernetes/AnonymousAccessGranted

### The

`system:anonymous` user was granted API permission on a Kubernetes
cluster.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that a user on your Kubernetes cluster successfully
created a `ClusterRoleBinding` or `RoleBinding` to bind
the user `system:anonymous` to a role. This enables unauthenticated
access to the API operations permitted by the role. If this behavior is not
expected, it may indicate a configuration mistake or that your credentials are
compromised

**Remediation recommendations:**

You should examine the permissions that have been granted to the
`system:anonymous` user or `system:unauthenticated`
group on your cluster and revoke unnecessary anonymous access. For more
information, see [Security best
practices for Amazon EKS](../../../eks/latest/userguide/security-best-practices.md "../../../eks/latest/userguide/security-best-practices.md") in the _Amazon EKS User Guide_. If the permissions were
granted maliciously, you should revoke access of the user that granted the
permissions and reverse any changes made by an adversary to your cluster. For
more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Policy:Kubernetes/ExposedDashboard

### The dashboard for a

Kubernetes cluster was exposed to the internet

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that Kubernetes dashboard for your cluster was exposed to
the internet by a Load Balancer service. An exposed dashboard makes the
management interface of your cluster accessible from the internet and allows
adversaries to exploit any authentication and access control gaps that may be
present.

**Remediation recommendations:**

You should ensure that strong authentication and authorization is enforced on
Kubernetes Dashboard. You should also implement network access control to restrict
access to the dashboard from specific IP addresses.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## Policy:Kubernetes/KubeflowDashboardExposed

### The

**Kubeflow** dashboard for a Kubernetes cluster was exposed to
the Internet

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that **Kubeflow** dashboard for your
cluster was exposed to the Internet by a Load Balancer service. An exposed
**Kubeflow** dashboard makes the management interface of
your **Kubeflow** environment accessible from the Internet and
allows adversaries to exploit any authentication and access control gaps that
may be present.

**Remediation recommendations:**

You should ensure that strong authentication and authorization is enforced on
**Kubeflow** Dashboard. You should also implement network
access control to restrict access to the dashboard from specific IP
addresses.

For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## PrivilegeEscalation:Kubernetes/PrivilegedContainer

### A

privileged container with root level access was launched on your Kubernetes
cluster.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that a privileged container was launched on your
Kubernetes cluster using an image has never before been used to launch privileged
containers in your cluster. A privileged container has root level access to the
host. Adversaries can launch privileged containers as a privilege escalation
tactic to gain access to and then compromise the host.

**Remediation recommendations:**

If this container launch is unexpected, the credentials of the user identity
used to launch the container may be compromised. Revoke access of the user and
reverse any changes made by an adversary to your cluster. For more information,
see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

## CredentialAccess:Kubernetes/AnomalousBehavior.SecretsAccessed

### A

Kubernetes API commonly used to access secrets was invoked in an anomalous
way.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that an anomalous API operation to retrieve sensitive
cluster secrets was invoked by a Kubernetes user in your cluster. The observed API is
commonly associated with credential access tactics that can lead to privileged
escalation and further access within your cluster. If this behavior is not
expected, it may indicate either a configuration mistake or that your AWS
credentials are compromised.

The observed API was identified as anomalous by the GuardDuty anomaly detection
machine learning (ML) model. The ML model evaluates all user API activity within
your EKS cluster and identifies anomalous events that are associated with
techniques used by unauthorized users. The ML model tracks multiple factors of
the API operation such as the user making the request, the location the request
was made from, user agent used, and the namespace that the user operated. You
can find the details of the API request that are unusual, in the finding details
panel in the GuardDuty console.

**Remediation recommendations:**

Examine the permissions granted to the Kubernetes user in your cluster and ensure
that all these permissions are needed. If the permissions were granted
mistakenly or maliciously, revoke user access and reverse any changes made by an
unauthorized user to your cluster. For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated

### A

RoleBinding or ClusterRoleBinding to an overly permissive role or sensitive
namespace was created or modified in your Kubernetes cluster.

**Default severity: Medium\***

###### Note

This finding's default severity is Medium. However, if a RoleBinding or
ClusterRoleBinding involves the ClusterRoles `admin` or
`cluster-admin`, the severity is High.

- **Feature:** EKS audit logs

This finding informs you that a user in your Kubernetes cluster created a
`RoleBinding` or `ClusterRoleBinding` to bind a user
to a role with admin permissions or sensitive namespaces. If this behavior is
not expected, it may indicate either a configuration mistake or that your AWS
credentials are compromised.

The observed API was identified as anomalous by the GuardDuty anomaly detection
machine learning (ML) model. The ML model evaluates all user API activity within
your EKS cluster. This ML model also identifies anomalous events that are
associated with the techniques used by an unauthorized user. The ML model also
tracks multiple factors of the API operation, such as the user making the
request, the location the request was made from, the user agent used, and the
namespace that the user operated. You can find the details of the API request
that are unusual, in the finding details panel in the GuardDuty console.

**Remediation recommendations:**

Examine the permissions granted to the Kubernetes user. These permissions are
defined in the role and subjects involved in `RoleBinding` and
`ClusterRoleBinding`. If the permissions were granted mistakenly
or maliciously, revoke user access and reverse any changes made by an
unauthorized user to your cluster. For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Execution:Kubernetes/AnomalousBehavior.ExecInPod

### A

command was executed inside a pod in an anomalous way.

**Default severity: Medium**

- **Feature:** EKS audit logs

This finding informs you that a command was executed in a pod using the Kubernetes
exec API. The Kubernetes exec API allows running arbitrary commands in a pod. If this
behavior is not expected for the user, namespace, or pod, it may indicate either
a configuration mistake or that your AWS credentials are compromised.

The observed API was identified as anomalous by the GuardDuty anomaly detection
machine learning (ML) model. The ML model evaluates all user API activity within
your EKS cluster. This ML model also identifies anomalous events that are
associated with the techniques used by an unauthorized user. The ML model also
tracks multiple factors of the API operation, such as the user making the
request, the location the request was made from, the user agent used, and the
namespace that the user operated. You can find the details of the API request
that are unusual, in the finding details panel in the GuardDuty console.

**Remediation recommendations:**

If the execution of this command is unexpected, the credentials of the user
identity used to execute the command may have been compromised. Revoke user
access and reverse any changes made by an unauthorized user to your cluster. For
more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## PrivilegeEscalation:Kubernetes/AnomalousBehavior.WorkloadDeployed!PrivilegedContainer

### A workload was launched with a privileged container in an anomalous

way.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that a workload was launched with a privileged
container in your Amazon EKS cluster. A privileged container has root level access to
the host. Unauthorized users can launch privileged containers as a privilege
escalation tactic to first gain access to the host and then compromise
it.

The observed container creation or modification was identified as anomalous by
the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates
all user API and container image activity within your EKS cluster. This ML model
also identifies anomalous events that are associated with the techniques used by
an unauthorized user. The ML model also tracks multiple factors of the API
operation, such as the user making the request, the location the request was
made from, the user agent used, container images observed in your account, and
the namespace that the user operated. You can find the details of the API
request that are unusual, in the finding details panel in the GuardDuty
console.

**Remediation recommendations:**

If this container launch is unexpected, the credentials of the user identity
used to launch the container may have been compromised. Revoke user access and
reverse any changes made by an unauthorized user to your cluster. For more
information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

If this container launch is expected, it is recommended that you use a
suppression rule with a filter criteria based on the
`resource.KubernetesDetails.KubernetesWorkloadDetails.containers.imagePrefix`
field. In the filter criteria, the `imagePrefix` field must have the
same value as the `imagePrefix` field specified in the finding. For
more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").

## Persistence:Kubernetes/AnomalousBehavior.WorkloadDeployed!ContainerWithSensitiveMount

### A workload was deployed in an anomalous way, with a sensitive host path mounted

inside the workload.

**Default severity: High**

- **Feature:** EKS audit logs

This finding informs you that a workload was launched with a container that
included a sensitive host path in the `volumeMounts` section. This
potentially makes the sensitive host path accessible and writable from inside
the container. This technique is commonly used by unauthorized users to gain
access to the host's file system.

The observed container creation or modification was identified as anomalous by
the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates
all user API and container image activity within your EKS cluster. This ML model
also identifies anomalous events that are associated with the techniques used by
an unauthorized user. The ML model also tracks multiple factors of the API
operation, such as the user making the request, the location the request was
made from, the user agent used, container images observed in your account, and
the namespace that the user operated. You can find the details of the API
request that are unusual, in the finding details panel in the GuardDuty
console.

**Remediation recommendations:**

If this container launch is unexpected, the credentials of the user identity
used to launch the container may have been compromised. Revoke user access and
reverse any changes made by an unauthorized user to your cluster. For more
information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

If this container launch is expected, it is recommended that you use a
suppression rule with a filter criteria based on the
`resource.KubernetesDetails.KubernetesWorkloadDetails.containers.imagePrefix`
field. In the filter criteria, the `imagePrefix` field must have the
same value as the `imagePrefix` field specified in the finding. For
more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").

## Execution:Kubernetes/AnomalousBehavior.WorkloadDeployed

### A

workload was launched in an anomalous way.

**Default severity: Low\***

###### Note

The default severity is Low. However, if the workload contains a
potentially suspicious image name, such as a known pentest tool, or a
container running a potentially suspicious command at launch, such as
reverse shell commands, then the severity of this finding type will be
considered as Medium.

- **Feature:** EKS audit logs

This finding informs you that a Kubernetes workload was created or modified in an
anomalous way, such as an API activity, new container images, or risky workload
configuration, within your Amazon EKS cluster. Unauthorized users can launch
containers as a tactic to execute arbitrary code to first gain access to the
host and then compromise it.

The observed container creation or modification was identified as anomalous by
the GuardDuty anomaly detection machine learning (ML) model. The ML model evaluates
all user API and container image activity within your EKS cluster. This ML model
also identifies anomalous events that are associated with the techniques used by
an unauthorized user. The ML model also tracks multiple factors of the API
operation, such as the user making the request, the location the request was
made from, the user agent used, container images observed in your account, and
the namespace that the user operated. You can find the details of the API
request that are unusual, in the finding details panel in the GuardDuty
console.

**Remediation recommendations:**

If this container launch is unexpected, the credentials of the user identity
used to launch the container may have been compromised. Revoke user access and
reverse any changes made by an unauthorized user to your cluster. For more
information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

If this container launch is expected, it is recommended that you use a
suppression rule with a filter criteria based on the
`resource.KubernetesDetails.KubernetesWorkloadDetails.containers.imagePrefix`
field. In the filter criteria, the `imagePrefix` field must have the
same value as the `imagePrefix` field specified in the finding. For
more information, see [Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md").

## PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleCreated

### A

highly permissive Role or ClusterRole was created or modified in an anomalous
way.

**Default severity: Low**

- **Feature:** EKS audit logs

This finding informs you that an anomalous API operation to create a
`Role` or `ClusterRole` with excessive permissions was
called by a Kubernetes user in your Amazon EKS cluster. Actors can use role creation with
powerful permissions to avoid using built-in admin-like roles and avoid
detection. The excessive permissions can lead to privileged escalation, remote
code execution, and potentially control over a namespace or cluster. If this
behavior is not expected, it may indicate either a configuration mistake or that
your credentials are compromised.

The observed API was identified as anomalous by the GuardDuty anomaly detection
machine learning (ML) model. The ML model evaluates all user API activity within
your Amazon EKS cluster and identifies anomalous events that are associated with the
techniques used by unauthorized users. The ML model also tracks multiple factors
of the API operation, such as the user making the request, the location the
request was made from, the user agent used, container images observed in your
account, and the namespace that the user operated. You can find the details of
the API request that are unusual, in the finding details panel in the GuardDuty
console.

**Remediation recommendations:**

Examine the permissions defined in `Role` or
`ClusterRole` to ensure that all the permissions are needed and
follow least privilege principles. If the permissions were granted mistakenly or
maliciously, revoke user access and reverse any changes made by an unauthorized
user to your cluster. For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").

## Discovery:Kubernetes/AnomalousBehavior.PermissionChecked

### A user checked their access permission in an anomalous way.

**Default severity: Low**

- **Feature:** EKS audit logs

This finding informs you that a user in your Kubernetes cluster successfully
checked whether or not the known powerful permissions that can lead to
privileged escalation and remote code execution, are allowed. For example, a
common command used to check permissions for a user is `kubectl auth
 can-i`. If this behavior is not expected, it may indicate either a
configuration mistake or that your credentials have been compromised.

The observed API was identified as anomalous by the GuardDuty anomaly detection
machine learning (ML) model. The ML model evaluates all user API activity within
your Amazon EKS cluster and identifies anomalous events that are associated with the
techniques used by unauthorized users. The ML model also tracks multiple factors
of the API operation, such as the user making the request, the location the
request was made from, permission being checked, and the namespace that the user
operated. You can find the details of the API request that are unusual, in the
finding details panel in the GuardDuty console.

**Remediation recommendations:**

Examine the permissions granted to the Kubernetes user to ensure that all the
permissions are needed. If the permissions were granted mistakenly or
maliciously, revoke user access and reverse any changes made by an unauthorized
user to your cluster. For more information, see [Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md").

If your AWS credentials are compromised, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md").
