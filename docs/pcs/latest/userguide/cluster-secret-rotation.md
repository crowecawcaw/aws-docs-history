

# Rotating cluster secrets in AWS PCS
<a name="cluster-secret-rotation"></a>

Use AWS Secrets Manager Managed Rotation to rotate cluster secrets in AWS PCS. Regular secret rotation is a security best practice for maintaining strong security posture in HPC environments. This capability enables you to meet industry compliance standards including HIPAA and FedRAMP, which mandate regular credential rotation.

The cluster secret serves dual purposes: authenticating compute nodes joining the cluster and as the JWT key for Slurm REST API authentication. When rotated, both aspects are affected simultaneously.

## How cluster secret rotation works
<a name="cluster-secret-rotation-overview"></a>

Prepare manually to maintain cluster stability during secret rotation:

1. **Preparation** – Scale all compute node groups to 0 capacity and ensure no jobs are running

1. **Rotation** – Initiate rotation through Secrets Manager console or API

1. **Monitoring** – Track progress through CloudTrail events

1. **Recovery** – Scale compute node groups back to desired capacity

During rotation, your cluster remains in `ACTIVE` state and billing continues normally. The process typically takes a few minutes.

## Requirements and limitations
<a name="cluster-secret-rotation-requirements"></a>

Before rotating cluster secrets, complete these requirements:
+ Cluster must be in `ACTIVE` or `UPDATE_FAILED` state
+ IAM role must have `secretsmanager:RotateSecret` permission
+ All compute node groups must be scaled to 0 capacity
+ Stop all jobs before rotation

Limitations:
+ Manual preparation required for each rotation
+ Existing JWT tokens become invalid and require reissuance
+ BYO login nodes require manual secret update after rotation

**Topics**
+ [How cluster secret rotation works](#cluster-secret-rotation-overview)
+ [Requirements and limitations](#cluster-secret-rotation-requirements)
+ [Rotate a cluster secret in AWS PCS](cluster-secret-rotation-procedure.md)
+ [Frequently asked questions about cluster secret rotation in AWS PCS](cluster-secret-rotation-faq.md)
+ [Troubleshooting cluster secret rotation in AWS PCS](cluster-secret-rotation-troubleshooting.md)