Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Port requirements for AWS services on a Snowball Edge

For AWS services to work properly on a AWS Snowball Edge device, you must
allow the network ports for the service.

The following is a list of network ports that are required for each AWS
service.

| Port         | Protocol | Comment                                              |
| ------------ | -------- | ---------------------------------------------------- |
| 22 (HTTP)    | TCP      | Device health check and for EC2 SSH                  |
| 443 (HTTPS)  | TCP      | S3 API and S3 Control API HTTPS endpoint             |
| 2049 (HTTP)  | TCP      | NFS endpoint                                         |
| 6078 (HTTP)  | TCP      | IAM HTTP endpoint                                    |
| 6089 (HTTPS) | TCP      | IAM HTTPS endpoint                                   |
| 7078 (HTTP)  | TCP      | STS HTTP endpoint                                    |
| 7089 (HTTPS) | TCP      | STS HTTPS endpoint                                   |
| 8080 (HTTP)  | TCP      | S3 adapter HTTP endpoint                             |
| 8008 (HTTP)  | TCP      | EC2 HTTP endpoint                                    |
| 8243 (HTTPS) | TCP      | EC2 HTTPS endpoint                                   |
| 8443 (HTTPS) | TCP      | S3 Adapter HTTPS endpoint                            |
| 9091 (HTTP)  | TCP      | Endpoint for device management                       |
| 9092         | TCP      | Inbound for EKS Anywhere and CAPAS device controller |
| 8242         | TCP      | Inbound for EC2 HTTPS endpoint for EKS Anywhere      |
| 6443         | TCP      | Inbound for EKS Anywhere Kubernetes API endpoint     |
| 2379         | TCP      | Inbound for EKS Anywhere Etcd API endpoint           |
| 2380         | TCP      | Inbound for EKS Anywhere Etcd API endpoint           |
