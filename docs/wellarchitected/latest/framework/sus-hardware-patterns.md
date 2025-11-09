# Hardware and services

Look for opportunities to reduce workload sustainability impacts by making changes to your hardware management practices. Minimize the amount of hardware needed to provision and deploy, and select the most efficient hardware and services for your individual workload.

The following question focuses on these considerations for sustainability:

| SUS 5:  How do you select and use cloud hardware and services in your architecture to support your sustainability goals?                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Look for opportunities to reduce workload sustainability impacts by making changes to your hardware management practices. Minimize the amount of hardware needed to provision and deploy, and select the most efficient hardware and services for your individual workload. |

Use the minimum amount of hardware to meet your needs: Using the capabilities of the
cloud, you can make frequent changes to your workload implementations. Update deployed
components as your needs change.

Use instance types with the least impact: Continually monitor the release of new
instance types and take advantage of energy efficiency improvements, including those
instance types designed to support specific workloads such as machine learning training and
inference, and video transcoding.

Use managed services: Managed services shift responsibility for maintaining high average
utilization, and sustainability optimization of the deployed hardware, to AWS. Use managed
services to distribute the sustainability impact of the service across all tenants of the
service, reducing your individual contribution.

Optimize your use of GPUs: Graphics processing units (GPUs) can be a source of
high-power consumption, and many GPU workloads are highly variable, such as rendering,
transcoding, and machine learning training and modeling. Only run GPUs instances for the
time needed, and decommission them with automation when not required to minimize resources
consumed.
