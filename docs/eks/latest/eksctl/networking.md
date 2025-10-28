# Networking

This chapter includes information about how Eksctl creates Virtual Private Cloud (VPC) networks for EKS clusters.

## Topics:

- [VPC Configuration](vpc-configuration.md "vpc-configuration.md")
  - Modify the VPC CIDR range and configure IPv6 addressing
  - Use an existing VPC
  - Customize the VPC, subnets, security groups, and NAT gateways for the new EKS cluster

- [Subnet Settings](vpc-subnet-settings.md "vpc-subnet-settings.md")
  - Use private subnets for the initial nodegroup to isolate it from the public internet
  - Customize subnet topology by listing multiple subnets per availability zone and specifying subnets in nodegroup configurations
  - Restrict nodegroups to specific named subnets in the VPC configuration
  - When using private subnets for nodegroups, set `privateNetworking` to `true`
  - Provide a complete subnet specification with both `public` and `private` configurations in the VPC spec
  - Only one of `subnets` or `availabilityZones` can be provided in nodegroup configuration

- [Cluster Access](vpc-cluster-access.md "vpc-cluster-access.md")
  - Manage public and private access to the Kubernetes API server endpoints in an EKS cluster
  - Restrict access to the EKS Kubernetes public API endpoint by specifying allowed CIDR ranges
  - Update the API server endpoint access configuration and public access CIDR restrictions for an existing cluster

- [Updating control plane subnets and security groups](cluster-subnets-security-groups.md "cluster-subnets-security-groups.md")
  - Update the subnets used by the EKS control plane for a cluster

- [IPv6 Support](vpc-ip-family.md "vpc-ip-family.md")
  - Specify the IP version (IPv4 or IPv6) to be used when creating a VPC with EKS cluster
