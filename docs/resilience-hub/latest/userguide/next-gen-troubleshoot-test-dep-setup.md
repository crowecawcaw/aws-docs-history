

# Dependency fault action fails with setup error
<a name="next-gen-troubleshoot-test-dep-setup"></a>

**Symptom:** A dependency fault action fails because the required agent or sidecar is not configured.

**Cause:** Packet loss actions require SSM Agent on Amazon EC2, an SSM container in Amazon ECS task definitions, or a Kubernetes service account for Amazon EKS pods.

**Solution:** Follow the setup steps for your compute type in the [AWS FIS actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html). For Amazon EKS pods, the service account must exist in every targeted namespace, and the execution role must be mapped to the cluster from the account that contains the cluster. Complete the **(Optional) Resilience testing** parts of the Amazon EKS permissions steps. For more information, see [Required IAM permissions and roles](next-gen-iam-permissions.md).