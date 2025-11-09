This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Requirements

Before you start to install Wickr Enterprise, verify that the following requirements are
met.

## Hardware requirements

Wickr Enterprise requires a Kubernetes cluster to operate. It is possible to operate on a
single node with Low Resource Mode enabled, but this is not recommended for general production
use. In a Production deployment we recommend a minimum of three messaging worker nodes as well
as a minimum of two calling worker nodes.

A worker node should have the following minimum specifications.

- 2 to 4 CPU cores
- 8 GB of Ram
- 200 GB of disk space

**Minimum Hardware Requirements**

A single worker node cluster running in Low Resource Mode requires a minimum of 3000m CPU
and 5846Mi Ram. This does not include the kube-system pods.

**Resource Requirements By Pod**

| Pod Name        | Owner          | CPU  | Memory |
| --------------- | -------------- | ---- | ------ |
| admin-api       | Wickr          | 100m | 256Mi  |
| directory       | Wickr          | 100m | 128Mi  |
| expirer         | Wickr          | 100m | 128Mi  |
| fileproxy       | Wickr          | 100m | 256Mi  |
| oidc            | Wickr          | 100m | 128Mi  |
| opensearch      | Wickr          | 500m | 100Mi  |
| orville         | Wickr          | 50m  | 128Mi  |
| orville-redis   | Wickr          | 50m  | 128Mi  |
| push-device     | Wickr          | 100m | 128Mi  |
| rabbitmq        | Wickr          | 50m  | 256Mi  |
| react           | Wickr          | 100m | 64Mi   |
| receipts        | Wickr          | 250m | 128Mi  |
| redis           | Wickr          | 50m  | 128Mi  |
| server-api      | Wickr          | 250m | 256Mi  |
| switchboard     | Wickr          | 250m | 512Mi  |
| kotsadm         | KOTS           | 50m  | 50Mi   |
| kotsadm-minio   | KOTS           | 100m | 512Mi  |
| kotsadm-rqlite  | KOTS           | 200m | 1Gi    |
| minio-operator  | Internal S3    | 200m | 256Mi  |
| minio-tenant    | Internal S3    | 100m | 256Mi  |
| mysql-primary   | Internal MySQL | 100m | 512Mi  |
| mysql-secondary | Internal MySQL | 100m | 512Mi  |

**Storage Requirements**

Wickr Enterprise requires a default StorageClass to utilize when creating Persistent
Volume Claims. When deploying in an air-gapped environment or on premises you may need to
configure one for your cluster. One available option is [Longhorn](https://longhorn.io/ "https://longhorn.io/"). Recommended disk space requirements will vary based on the use of the
Internal S3 option and the Internal Mysql option and the amount of space you wish to have
available for file uploads.

- Internal Image caching: ~60 Gi
- RabbitMQ: 24 Gi Default / 8 Gi in Low Resource Mode
- Redis: 24 Gi Default / 8 Gi in Low Resource Mode
- OpenSearch: 24 Gi Default / 8 Gi in Low Resource Mode
- Internal Mysql: 80 Gi Default / 20Gi in Low Resource Mode
- Internal S3: 160 Gi Default / 2Gi in Low Resource Mode
- KOTS Minio: 4 Gi
- KOTS Rqlite: 1 Gi

**Minimum Storage Size**

- 377 Gi Default with Internal S3 and Internal Mysql
- 111 Gi in Low Resource Mode

**Kubernetes Version Requirements**

Wickr Enterprise relies on Replicated KOTS. Replicated, a commercial software
distribution platform, provides a list of the currently supported versions of Kubernetes. For
more information, see [Kubernetes Version Compatibility](https://docs.replicated.com/enterprise/installing-general-requirements#kubernetes-version-compatibility "https://docs.replicated.com/enterprise/installing-general-requirements#kubernetes-version-compatibility").

## Software requirements

Wickr Enterprise requires a Kubernetes cluster and KOTS to operate. Please refer to the
KOTS documentation for supported OS and Kubernetes versions. For more information, see [Minimum System Requirements](https://docs.replicated.com/enterprise/installing-general-requirements#minimum-system-requirements "https://docs.replicated.com/enterprise/installing-general-requirements#minimum-system-requirements").

**Developer Host System**

**Operating System** — The commands in this documentation are designed to
work on Linux, MacOS, or Windows with WSL (Windows Subsystem for Linux) installed.

**Internal Stateful Services**

Wickr Enterprise can provide internal services for both MySQL database and S3 compatible
storage however for general production use it is recommended you provide these services external
from the Kubernetes cluster.

- MySQL 5.7 Database
  - Amazon RDS MySQL 5.7 or MySQL 5.7 database (External)
  - Mysql Bitnami Helm Chart (Internal)

  - File Storage
    - Amazon S3 or S3 compatible storage provider (External)
    - Minio Operator Helm Chart (Internal)

## Network requirements

Wickr Enterprise requires a FQDN, SSL certificates, and specific open TCP and UDP
ports.

- FQDN: A domain or sub-domain to be used by the Wickr Enterprise deployment.
- SSL certificate: An SSL certificate key pair signed by a public CA or a self signed
  certificate key pair. The certificate must list the FQDN in the Common Name and also as a SAN
  DNS entry. The certificate must also enable the serverAuth extendedKeyUsage extension.
- Online installs will need egress access to Replicated and third party resources.
  Replicated maintains a list of their IP addresses. For more information, see [Replicated IP Addresses](https://github.com/replicatedhq/ips "https://github.com/replicatedhq/ips"). Replicated also
  maintains a list of third party resources needed. For more information, see [Firewall Openings for Online Installations](https://docs.replicated.com/enterprise/installing-general-requirements#firewall-openings-for-online-installations "https://docs.replicated.com/enterprise/installing-general-requirements#firewall-openings-for-online-installations").
- Air-gapped installs require access to a private container registry.

**Messaging Nodes**

Messaging nodes do not require a public IPV4 address and should be located in a private
subnet. Message traffic will enter the cluster through the LoadBalancer or Ingress.

**Calling Nodes**

Calling nodes require a public IPV4 address so they must be in a public subnet. Call media
is transferred via UDP by default. When TCP calling is enabled the TCP Proxy will accept
connections on TCP 443 and will proxy them to the Orville service.

- TCP : 443 Calling TCP Proxy
- UDP : 16384-16484 Audio/Video Streams

**Installation and Configuration access**

Access to the KOTS Admin Console for installation and configuration is done through a
Kubernetes port forward.

```
kubectl kots admin-console -n wickr
```

**License Requirements**

Installation will require a .yaml format license file, this will be provided to you by
Wickr Support.
