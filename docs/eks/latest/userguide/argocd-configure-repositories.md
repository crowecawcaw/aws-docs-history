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

For credential reuse across multiple repositories, you can use repository credential templates (repocreds). For more information, see [Private Repositories](https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/ "https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/") in the Argo CD documentation.

## Authentication methods

| Method                                        | Use Case                                                                                        | IAM Permissions Required                                                       |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Direct integration with AWS services**      |
| CodeCommit                                    | Direct integration with AWS CodeCommit Git repositories. No Repository configuration needed.    | `codecommit:GitPull`                                                           |
| CodeConnections                               | Connect to GitHub, GitLab, or Bitbucket with managed authentication. Requires connection setup. | `codeconnections:UseConnection`                                                |
| ECR Helm Charts                               | Direct integration with AWS ECR for OCI Helm charts. No Repository configuration needed.        | `ecr:GetAuthorizationToken`, `ecr:BatchGetImage`, `ecr:GetDownloadUrlForLayer` |
| **Repository configuration with credentials** |
| AWS Secrets Manager (Username/Token)          | Store personal access tokens or passwords                                                       | `secretsmanager:GetSecretValue`                                                |
| AWS Secrets Manager (SSH Key)                 | Use SSH key authentication                                                                      | `secretsmanager:GetSecretValue`                                                |
| AWS Secrets Manager (GitHub App)              | GitHub App authentication with private key                                                      | `secretsmanager:GetSecretValue`                                                |
| Kubernetes Secret                             | Standard Argo CD method using in-cluster secrets                                                | None (trust policy only)                                                       |

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
    repoURL: https://git-codecommit.`region`.amazonaws.com/v1/repos/`repository-name`
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
    repoURL: https://codeconnections.`region`.amazonaws.com/git-http/`account-id`/`region`/`connection-id`/`owner`/`repository`.git
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
    repoURL: `account-id`.dkr.ecr.`region`.amazonaws.com/`repository-name`
    targetRevision: `chart-version`
    chart: `chart-name`
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
    repoURL: oci://`account-id`.dkr.ecr.`region`.amazonaws.com/`repository-name`
    targetRevision: `artifact-version`
    path: `path-to-manifests`

```

Note: Include the `oci://` prefix when using OCI format. Use the `path` field instead of `chart`.

Required Capability Role permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Resource": "*"
    }
  ]
}
```

## Using AWS Secrets Manager

Store repository credentials in Secrets Manager and reference them in Argo CD Repository configurations.

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

###### Important

Ensure your IAM Capability Role has `secretsmanager:GetSecretValue` permissions for the secrets you create.
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

## Public repositories

No additional configuration needed for public repositories:

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: public-app
  namespace: argocd
spec:
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps
    targetRevision: HEAD
    path: guestbook
  # ... rest of configuration
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
