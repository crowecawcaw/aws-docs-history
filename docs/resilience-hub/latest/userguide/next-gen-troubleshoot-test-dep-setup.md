# Dependency fault action fails with setup error

**Symptom:** A dependency fault action fails because the
required agent or sidecar is not configured.

**Cause:** Packet loss actions require SSM Agent on Amazon EC2,
an SSM container in Amazon ECS task definitions, or a Kubernetes service account for Amazon EKS
pods.

**Solution:** Follow the setup steps for your compute type in
the [AWS FIS
actions reference](../../../fis/latest/userguide/fis-actions-reference.md "../../../fis/latest/userguide/fis-actions-reference.md").
