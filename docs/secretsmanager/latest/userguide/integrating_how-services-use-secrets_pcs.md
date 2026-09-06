

# How AWS Parallel Computing Service uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_pcs"></a>

AWS Parallel Computing Service (AWS PCS) is a managed service that makes it easier to run and scale high performance computing (HPC) and distributed machine learning workloads on AWS.

To connect to the cluster job scheduler, AWS PCS creates a [managed secret](service-linked-secrets.md) with the prefix `pcs` to store the scheduler key. The cost of storing the secret is included with the charge for AWS PCS. AWS PCS automatically deletes the secret when you delete your AWS PCS cluster. For more information, see [Working with cluster secrets in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_secrets.html) in the *AWS PCS User Guide*.

**Important**  
Don't modify or delete AWS PCS cluster secrets.