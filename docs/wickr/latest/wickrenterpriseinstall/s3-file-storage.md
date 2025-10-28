This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# S3 File storage

Wickr Enterprise requires an S3 compatible storage service. We recommend using an S3
service which is external to your Kubernetes cluster, such as Amazon S3, but you also have the option
of deploying an **Internal** S3 service inside of the Kubernetes cluster as a
part of the installation.

External S3 Settings

- **Bucket Name**: The name of the S3 bucket where file uploads will be
  stored.
- **Region**: The AWS region of the S3 bucket.
- **Endpoint**: Set the endpoint that Wickr will use to interact with the
  S3 API. Defaults to the region's S3 service endpoint.
- **Fileproxy Service Account Name**: Amazon S3 only. The name of an existing
  Kubernetes Service Account to use for authenticating to S3 using IAM roles for Service
  Accounts.
- **External S3 Access Key**: This is your existing S3 Access key.
- **External S3 Secret Key**: This is your existing S3 Secret key.
  **Internal S3 Settings**

The internal S3 type will deploy a default of 4 MinIO server pods that each contain 4
Persistent Volume Claims. The default configuration utilizes MinIO's Erasure Coding to increase
fault tolerance.

- **Internal S3 server count**: The number of MinIO server pods to create,
  the default is 4 for a fault tolerant deployment. This value can be set as low as 1 for a
  development/test deployment.
- **Internal S3 volume count**: The number of MinIO volumes to create in
  each MinIO server pod, the default is 4 for a fault tolerant deployment. This value can be set
  as low as 1 for a development/test deployment.
- **Internal S3 volume size**: The size in GB of the MinIO volumes created
  in the MinIO server pods, the default is 10GB.
- A default Internal S3 deployment will use 4 servers with 4 PVCs. Each PVC is 10 Gi
  yielding 160 Gi Raw storage with 120 Gi Erasure Coded storage available to users.
- Minio Erasure Coding calculator is available. For more information, see [Erasure Code Calculator](https://min.io/product/erasure-code-calculator "https://min.io/product/erasure-code-calculator").
