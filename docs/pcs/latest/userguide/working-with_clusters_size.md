# Cluster size in AWS PCS

AWS PCS provides highly available and secure clusters, while automating key tasks such as patching, node provisioning, and updates.

When you create a cluster, you select a size for it based on two factors:

- The number of compute nodes it will manage
- The number of active and queued jobs that you expect to run on the cluster

###### Important

You can't change the cluster size after you create the cluster. If you need
to change the size, you must create a new cluster.

| Slurm cluster size | Number of instances managed | Number of active and queued jobs |
| ------------------ | --------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Small              | Up to 32                    | Up to 256                        |
| Medium             | Up to 512                   | Up to 8192                       |
| Large              | Up to 2048                  | Up to 16384                      | ###### Examples <br>• If your cluster will have up to 24 managed instances and run up to 100 jobs, choose **Small**. <br>• If your cluster will have up to 24 managed instances and run up to 1000 jobs, choose **Medium**. <br>• If your cluster will have up to 1000 managed instances and run up to 100 jobs, choose **Large**. <br>• If your cluster will have up to 1000 managed instances and run up to 10,000 jobs, choose **Large**. |
