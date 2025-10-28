# Infrastructure security in ROSA

As a managed service, Red Hat OpenShift Service on AWS is protected by the AWS global network security.
For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security "https://aws.amazon.com/security").
To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar — AWS Well-Architected Framework_.

You use AWS published API calls to access ROSA through the AWS network. Clients must support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.
  Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal.
  Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference.md "../../../STS/latest/APIReference.md") (AWS STS) to generate temporary security credentials to sign requests.

## Cluster network isolation

Red Hat site reliability engineers (SREs) are responsible for the ongoing management and network security of the cluster and underlying application platform.
For more information on Red Hat responsibilities for ROSA, see [Overview of responsibilities for ROSA](rosa-responsibilities.md "rosa-responsibilities.md").

When you create a new cluster, ROSA provides the option of creating a public Kubernetes API server endpoint and application routes or a private Kubernetes API endpoint and application routes.
This connection is used to communicate with your cluster (using OpenShift management tools such as the ROSA CLI and OpenShift CLI).
A private connection allows all communication between your nodes and the API server to stay within your VPC.
If you enable private access to the API server and application routes, you must use an existing VPC and AWS PrivateLink to connect the VPC to the OpenShift backend service.

Kubernetes API server access is secured using a combination of AWS Identity and Access Management (IAM) and native Kubernetes role-based access control (RBAC).
For more information on Kubernetes RBAC, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "https://kubernetes.io/docs/reference/access-authn-authz/rbac/") in the Kubernetes documentation.

ROSA allows you to create secured application routes using several types of TLS termination to serve certificates to the client.
For more information, see [Secured routes](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/networking/configuring-routes#configuring-default-certificate "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/networking/configuring-routes#configuring-default-certificate") in the Red Hat documentation.

If you create a ROSA cluster in an existing VPC, you specify the VPC subnets and Availability Zones for your cluster to use.
You also define the CIDR ranges for the cluster network to use, and match these CIDR ranges to the VPC subnets.
For more information, see [CIDR range definitions](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/networking/cidr-range-definitions "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/networking/cidr-range-definitions") in the Red Hat documentation.

For clusters that use the public API endpoint, ROSA requires that your VPC is configured with a public and private subnet for each Availability Zone that you want the cluster deployed into.
For clusters that use the private API endpoint, only private subnets are required.

If you are using an existing VPC, you can configure your ROSA clusters to use an HTTP or HTTPS proxy server during or after cluster creation to encrypt cluster web traffic, adding another layer of security for your data. When you enable a proxy, the core cluster components are denied direct access to the internet.
The proxy does not deny internet access for user workloads.
For more information, see [Configuring a cluster-wide proxy](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/networking/configuring-a-cluster-wide-proxy "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/networking/configuring-a-cluster-wide-proxy") in the Red Hat documentation.

## Pod network isolation

If you are a cluster administrator, you can define network policies at the pod level that restrict traffic to pods in your ROSA cluster.
