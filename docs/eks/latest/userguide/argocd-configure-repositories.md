**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure repository access

Before deploying applications, configure Argo CD to access your Git repositories and Helm chart registries.
Argo CD supports multiple authentication methods for GitHub, GitLab, Bitbucket, AWS CodeCommit, and AWS ECR.

###### Note

For direct AWS service integrations (ECR Helm charts, CodeCommit repositories, and CodeConnections), you can reference them directly in Application resources without creating Repository configurations.
The Capability Role must have the required IAM permissions.
See [Configure Argo CD permissions](argocd-permissions.md "argocd-permissions.md") for details.

## Prerequisites

- An EKS cluster with the Argo CD capability created
- Git repositories containing Kubernetes manifests
- `kubectl` configured to communicate with your cluster

###### Note

AWS CodeConnections can connect to Git servers located in AWS Cloud or on-premises.
For more information, see [AWS CodeConnections](../../../codeconnections/latest/userguide/welcome.md "../../../codeconnections/latest/userguide/welcome.md").

## Authentication methods

| Method                                        | Use Case                                                                                                     | IAM Permissions Required                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| **Direct integration with AWS services**      |
| CodeCommit                                    | Direct integration with AWS CodeCommit Git repositories. No Repository configuration needed.                 | `codecommit:GitPull`                                                |
| CodeConnections                               | Connect to GitHub, GitLab, or Bitbucket with managed authentication. Requires connection setup.              | `codeconnections:UseConnection`                                     |
| ECR OCI Artifacts                             | Direct integration with AWS ECR for OCI Helm charts and manifest images. No Repository configuration needed. | `arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly`        |
| **Repository configuration with credentials** |
| AWS Secrets Manager (Username/Token)          | Store personal access tokens or passwords. Enables credential rotation without Kubernetes access.            | `arn:aws:iam::aws:policy/AWSSecretsManagerClientReadOnlyAccess`     |
| AWS Secrets Manager (SSH Key)                 | Use SSH key authentication. Enables credential rotation without Kubernetes access.                           | `arn:aws:iam::aws:policy/AWSSecretsManagerClientReadOnlyAccess`     |
| AWS Secrets Manager (GitHub App)              | GitHub App authentication with private key. Enables credential rotation without Kubernetes access.           | `arn:aws:iam::aws:policy/AWSSecretsManagerClientReadOnlyAccess`     |
| Kubernetes Secret                             | Standard Argo CD method using in-cluster secrets                                                             | None (permissions handled by EKS Access Entry with Kubernetes RBAC) |

## Direct access to AWS services

For AWS services, you can reference them directly in Application resources without creating Repository configurations.
The Capability Role must have the required IAM permissions.

### CodeCommit repositories

Reference CodeCommit repositories directly in Applications:

```
 apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  source:
    repoURL: https://git-codecommit.<replaceable>region</replaceable>.amazonaws.com/v1/repos/<replaceable>repository-name</replaceable>
    targetRevision: main
    path: kubernetes/manifests
```

Required Capability Role permissions:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "codecommit:GitPull",
      "Resource": "arn:aws:codecommit:region:account-id:repository-name"
    }
  ]
}
```

### CodeConnections

Reference GitHub, GitLab, or Bitbucket repositories through CodeConnections.
The repository URL format is derived from the CodeConnections connection ARN.

The repository URL format is:

```
 apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  source:
    repoURL: https://codeconnections.<replaceable>region</replaceable>.amazonaws.com/git-http/<replaceable>account-id</replaceable>/<replaceable>region</replaceable>/<replaceable>connection-id</replaceable>/<replaceable>owner</replaceable>/<replaceable>repository</replaceable>.git
    targetRevision: main
    path: kubernetes/manifests
```

Required Capability Role permissions:

```
 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "codeconnections:UseConnection",
      "Resource": "arn:aws:codeconnections:region:account-id:connection/connection-id"
    }
  ]
}
```

### ECR Helm charts

ECR stores Helm charts as OCI artifacts. Argo CD supports two ways to reference them:

**Helm format** (recommended for Helm charts):

```
 apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app-helm
  namespace: argocd
spec:
  source:
    repoURL: <replaceable>account-id</replaceable>.dkr.ecr.<replaceable>region</replaceable>.amazonaws.com/<replaceable>repository-name</replaceable>
    targetRevision: <replaceable>chart-version</replaceable>
    chart: <replaceable>chart-name</replaceable>
    helm:
      valueFiles:
        - values.yaml
```

Note: Do not include the `oci://` prefix when using Helm format. Use the `chart` field to specify the chart name.

**OCI format** (for OCI artifacts with Kubernetes manifests):

```
 apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app-oci
  namespace: argocd
spec:
  source:
    repoURL: oci://<replaceable>account-id</replaceable>.dkr.ecr.<replaceable>region</replaceable>.amazonaws.com/<replaceable>repository-name</replaceable>
    targetRevision: <replaceable>artifact-version</replaceable>
    path: <replaceable>path-to-manifests</replaceable>
```

Note: Include the `oci://` prefix when using OCI format. Use the `path` field instead of `chart`.

Required Capability Role permissions - attach the managed policy:

```
 arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPullOnly
```

This policy includes the necessary ECR permissions: `ecr:GetAuthorizationToken`, `ecr:BatchGetImage`, and `ecr:GetDownloadUrlForLayer`.

## Using AWS Secrets Manager

Store repository credentials in Secrets Manager and reference them in Argo CD Repository configurations.
Using Secrets Manager enables automated credential rotation without requiring Kubernetes RBAC access—credentials can be rotated using IAM permissions to Secrets Manager, and Argo CD automatically reads the updated values.

###### Note

For credential reuse across multiple repositories (for example, all repositories under a GitHub organization), use repository credential templates with `argocd.argoproj.io/secret-type: repo-creds`.
This provides better UX than creating individual repository secrets.
For more information, see [Repository Credentials](https://argo-cd.readthedocs.io/en/stable/operator-manual/argocd-repo-creds-yaml/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/argocd-repo-creds-yaml/") in the Argo CD documentation.

### Username and token authentication

For HTTPS repositories with personal access tokens or passwords:

**Create the secret in Secrets Manager**:

```
 aws secretsmanager create-secret \
  --name argocd/my-repo \
  --description "GitHub credentials for Argo CD" \
  --secret-string '{"username":"your-username","token":"your-personal-access-token"}'
```

**Optional TLS client certificate fields** (for private Git servers):

```
 aws secretsmanager create-secret \
  --name argocd/my-private-repo \
  --secret-string '{
    "username":"your-username",
    "token":"your-token",
    "tlsClientCertData":"LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCi4uLgotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t",
    "tlsClientCertKey":"LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCi4uLgotLS0tLUVORCBQUklWQVRFIEtFWS0tLS0t"
  }'
```

###### Note

The `tlsClientCertData` and `tlsClientCertKey` values must be base64 encoded.

**Create a Repository Secret referencing Secrets Manager**:

```
 apiVersion: v1
kind: Secret
metadata:
  name: my-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/your-org/your-repo
  secretArn: arn:aws:secretsmanager:us-west-2:111122223333:secret:argocd/my-repo-AbCdEf
  project: default
```

### SSH key authentication

For SSH-based Git access, store the private key as plaintext (not JSON):

**Create the secret with SSH private key**:

```
 aws secretsmanager create-secret \
  --name argocd/my-repo-ssh \
  --description "SSH key for Argo CD" \
  --secret-string "-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
...
-----END OPENSSH PRIVATE KEY-----"
```

**Create a Repository Secret for SSH**:

```
 apiVersion: v1
kind: Secret
metadata:
  name: my-repo-ssh
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: git@github.com:your-org/your-repo.git
  secretArn: arn:aws:secretsmanager:us-west-2:111122223333:secret:argocd/my-repo-ssh-AbCdEf
  project: default
```

### GitHub App authentication

For GitHub App authentication with a private key:

**Create the secret with GitHub App credentials**:

```
 aws secretsmanager create-secret \
  --name argocd/github-app \
  --description "GitHub App credentials for Argo CD" \
  --secret-string '{
    "githubAppPrivateKeySecret":"LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQouLi4KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0=",
    "githubAppID":"123456",
    "githubAppInstallationID":"12345678"
  }'
```

###### Note

The `githubAppPrivateKeySecret` value must be base64 encoded.

**Optional field for GitHub Enterprise**:

```
 aws secretsmanager create-secret \
  --name argocd/github-enterprise-app \
  --secret-string '{
    "githubAppPrivateKeySecret":"LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQouLi4KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0=",
    "githubAppID":"123456",
    "githubAppInstallationID":"12345678",
    "githubAppEnterpriseBaseUrl":"https://github.example.com/api/v3"
  }'
```

**Create a Repository Secret for GitHub App**:

```
 apiVersion: v1
kind: Secret
metadata:
  name: my-repo-github-app
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/your-org/your-repo
  secretArn: arn:aws:secretsmanager:us-west-2:111122223333:secret:argocd/github-app-AbCdEf
  project: default
```

### Repository credential templates

For credential reuse across multiple repositories (for example, all repositories under a GitHub organization or user), use repository credential templates with `argocd.argoproj.io/secret-type: repo-creds`.
This provides better UX than creating individual repository secrets for each repository.

**Create a repository credential template**:

```
 apiVersion: v1
kind: Secret
metadata:
  name: github-org-creds
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repo-creds
stringData:
  type: git
  url: https://github.com/your-org
  secretArn: arn:aws:secretsmanager:us-west-2:111122223333:secret:argocd/github-org-AbCdEf
```

This credential template applies to all repositories matching the URL prefix `https://github.com/your-org`.
You can then reference any repository under this organization in Applications without creating additional secrets.

For more information, see [Repository Credentials](https://argo-cd.readthedocs.io/en/stable/operator-manual/argocd-repo-creds-yaml/ "https://argo-cd.readthedocs.io/en/stable/operator-manual/argocd-repo-creds-yaml/") in the Argo CD documentation.

###### Important

Ensure your IAM Capability Role has the managed policy `arn:aws:iam::aws:policy/AWSSecretsManagerClientReadOnlyAccess` attached, or equivalent permissions including `secretsmanager:GetSecretValue` and KMS decrypt permissions.
See [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") for IAM policy configuration.

## Using AWS CodeConnections

For CodeConnections integration, see [Connect to Git repositories with AWS CodeConnections](integration-codeconnections.md "integration-codeconnections.md").

CodeConnections provides managed authentication for GitHub, GitLab, and Bitbucket without storing credentials.

## Using Kubernetes Secrets

Store credentials directly in Kubernetes using the standard Argo CD method.

**For HTTPS with personal access token**:

```
 apiVersion: v1
kind: Secret
metadata:
  name: my-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/your-org/your-repo
  username: your-username
  password: your-personal-access-token
```

**For SSH**:

```
 apiVersion: v1
kind: Secret
metadata:
  name: my-repo-ssh
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: git@github.com:your-org/your-repo.git
  sshPrivateKey: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    ... your private key ...
    -----END OPENSSH PRIVATE KEY-----
```

## CodeCommit repositories

For AWS CodeCommit, grant your IAM Capability Role CodeCommit permissions (`codecommit:GitPull`).

Configure the repository:

```
 apiVersion: v1
kind: Secret
metadata:
  name: codecommit-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://git-codecommit.us-west-2.amazonaws.com/v1/repos/my-repo
  project: default
```

For detailed IAM policy configuration, see [Argo CD considerations](argocd-considerations.md "argocd-considerations.md").

## Verify repository connection

Check connection status through the Argo CD UI under Settings → Repositories.
The UI shows connection status and any authentication errors.

Repository Secrets do not include status information.

## Additional resources

- [Register target clusters](argocd-register-clusters.md "argocd-register-clusters.md") - Register target clusters for deployments
- [Create Applications](argocd-create-application.md "argocd-create-application.md") - Create your first Application
- [Argo CD considerations](argocd-considerations.md "argocd-considerations.md") - IAM permissions and security configuration
- [Private Repositories](https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/ "https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/") - Upstream repository configuration reference
