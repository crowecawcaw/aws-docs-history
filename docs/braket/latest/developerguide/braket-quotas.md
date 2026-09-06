

# Amazon Braket Quotas
<a name="braket-quotas"></a>

The following table lists the service quotas for Amazon Braket. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

Some quotas can be increased. For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).
+ Burst rate quotas cannot be increased.
+ The maximum rate increase for adjustable quotas (except burst rate, which cannot be adjusted) is 2X the specified default rate limit. For example, a default quota of 60 can be adjusted to a maximum of 120.
+ The adjustable quota for concurrent SV1 (DM1) quantum tasks allows a maximum of 60 per AWS Region.
+ The maximum allowed number of compute instances for a hybrid job is 1, and the quotas are adjustable.


| Resource | Description | Limits | Adjustable | 
| --- | --- | --- | --- | 
| Rate of API requests | The maximum number of requests per second that you can send in this account in the current Region. | 140 | Yes | 
| Burst rate of API requests | The maximum number of additional requests per second (RPS) that you can send in one burst in this account in the current Region. | 600 | No | 
| Rate of `CreateQuantumTask` requests | The maximum number of `CreateQuantumTask` requests you can send per second in this account per Region. | 20 per second | Yes | 
| Burst rate of `CreateQuantumTask` requests | The maximum number of additional `CreateQuantumTask` requests per second (RPS) that you can send in one burst in this account in the current Region. | 40 | No | 
| Rate of `SearchQuantumTasks` requests | The maximum number of `SearchQuantumTasks` requests you can send per second in this account per Region. | 5 per second | Yes | 
| Burst rate of `SearchQuantumTasks` requests | The maximum number of additional `SearchQuantumTasks` requests per second (RPS) that you can send in one burst in this account in the current Region. | 50 | No | 
| Rate of `GetQuantumTask` requests | The maximum number of `GetQuantumTask` requests you can send per second in this account per Region. | 100 per second | Yes | 
| Burst rate of `GetQuantumTask` requests | The maximum number of additional `GetQuantumTask` requests per second (RPS) that you can send in one burst in this account in the current Region. | 500 | No | 
| Rate of `CancelQuantumTask` requests | The maximum number of `CancelQuantumTask` requests you can send per second in this account per Region. | 2 per second | Yes | 
| Burst rate of `CancelQuantumTask` requests | The maximum number of additional `CancelQuantumTask` requests per second (RPS) that you can send in one burst in this account in the current Region. | 20 | No | 
| Rate of `GetDevice` requests | The maximum number of `GetDevice` requests you can send per second in this account per Region. | 5 per second | Yes | 
| Burst rate of `GetDevice` requests | The maximum number of additional `GetDevice` requests per second (RPS) that you can send in one burst in this account in the current Region. | 50 | No | 
| Rate of `SearchDevices` requests | The maximum number of `SearchDevices` requests you can send per second in this account per Region. | 5 per second | Yes | 
| Burst rate of `SearchDevices` requests | The maximum number of additional `SearchDevices` requests per second (RPS) that you can send in one burst in this account in the current Region. | 50 | No | 
| Rate of `CreateJob` requests | The maximum number of `CreateJob` requests you can send per second in this account per Region. | 1 per second | Yes | 
| Burst rate of `CreateJob` requests | The maximum number of additional `CreateJob` requests per second (RPS) that you can send in one burst in this account in the current Region. | 5 | No | 
| Rate of `SearchJobs` requests | The maximum number of `SearchJob` requests you can send per second in this account per Region. | 5 per second | Yes | 
| Burst rate of `SearchJobs` requests | The maximum number of additional `SearchJob` requests per second (RPS) that you can send in one burst in this account in the current Region. | 50 | No | 
| Rate of `GetJob` requests | The maximum number of `GetJob` requests you can send per second in this account per Region. | 5 per second | Yes | 
| Burst rate of `GetJob` requests | The maximum number of additional `GetJob` requests per second (RPS) that you can send in one burst in this account in the current Region. | 25 | No | 
| Rate of `CancelJob` requests | The maximum number of `CancelJob` requests you can send per second in this account per Region. | 2 per second | Yes | 
| Burst rate of `CancelJob` requests | The maximum number of additional `CancelJob` requests per second (RPS) that you can send in one burst in this account in the current Region. | 5 | No | 
| Number of concurrent ** SV1 ** quantum tasks | The maximum number of concurrent quantum tasks running on the state vector simulator (SV1) in the current Region. | 100 us-east-1,<br />50 us-west-1,<br />100 us-west-2,<br />50 eu-west-2 | No | 
| Number of concurrent ** DM1 ** quantum tasks | The maximum number of concurrent quantum tasks running on the density matrix simulator (DM1) in the current Region. | 100 us-east-1,<br />50 us-west-1,<br />100 us-west-2,<br />50 eu-west-2 | No | 
| Number of concurrent hybrid jobs | The maximum number of concurrent hybrid jobs in the current Region. | 3 | Yes | 
| Hybrid jobs runtime limit | The maximum amount of time in days that a hybrid job can run. | 5 | No | 

The following are the default classical compute instance quotas for Hybrid Jobs. To raise these quotas, contact [Support](https://console.aws.amazon.com/servicequotas/home/services/braket/quotas). Additionally, the available regions are specified for each instance.


| Resource | Description | Limits | Adjustable | us-east-1 | us-west-1 | us-west-2 | eu-west-2 | eu-north-1 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Maximum number of instances of ml.c4.xlarge for hybrid jobs | The maximum number of instances of type ml.c4.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.c4.2xlarge for hybrid jobs | The maximum number of instances of type ml.c4.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.c4.4xlarge for hybrid jobs | The maximum number of instances of type ml.c4.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.c4.8xlarge for hybrid jobs | The maximum number of instances of type ml.c4.8xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | No | No | 
| Maximum number of instances of ml.c5.xlarge for hybrid jobs | The maximum number of instances of type ml.c5.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.c5.2xlarge for hybrid jobs | The maximum number of instances of type ml.c5.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.c5.4xlarge for hybrid jobs | The maximum number of instances of type ml.c5.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.c5.9xlarge for hybrid jobs | The maximum number of instances of type ml.c5.9xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.c5.18xlarge for hybrid jobs | The maximum number of instances of type ml.c5.18xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.c5n.xlarge for hybrid jobs | The maximum number of instances of type ml.c5n.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | No | No | 
| Maximum number of instances of ml.c5n.2xlarge for hybrid jobs | The maximum number of instances of type ml.c5n.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | No | No | 
| Maximum number of instances of ml.c5n.4xlarge for hybrid jobs | The maximum number of instances of type ml.c5n.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | No | No | 
| Maximum number of instances of ml.c5n.9xlarge for hybrid jobs | The maximum number of instances of type ml.c5n.9xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | No | No | 
| Maximum number of instances of ml.c5n.18xlarge for hybrid jobs | The maximum number of instances of type ml.c5n.18xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | No | No | 
| Maximum number of instances of ml.g4dn.xlarge for hybrid jobs | The maximum number of instances of type ml.g4dn.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.g4dn.2xlarge for hybrid jobs | The maximum number of instances of type ml.g4dn.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.g4dn.4xlarge for hybrid jobs | The maximum number of instances of type ml.g4dn.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.g4dn.8xlarge for hybrid jobs | The maximum number of instances of type ml.g4dn.8xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.g4dn.12xlarge for hybrid jobs | The maximum number of instances of type ml.g4dn.12xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.g4dn.16xlarge for hybrid jobs | The maximum number of instances of type ml.g4dn.16xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.xlarge for hybrid jobs | The maximum number of instances of type ml.g6.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.2xlarge for hybrid jobs | The maximum number of instances of type ml.g6.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.4xlarge for hybrid jobs | The maximum number of instances of type ml.g6.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.8xlarge for hybrid jobs | The maximum number of instances of type ml.g6.8xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.12xlarge for hybrid jobs | The maximum number of instances of type ml.g6.12xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.16xlarge for hybrid jobs | The maximum number of instances of type ml.g6.16xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.24xlarge for hybrid jobs | The maximum number of instances of type ml.g6.24xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6.48xlarge for hybrid jobs | The maximum number of instances of type ml.g6.48xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | No | Yes | Yes | Yes | 
| Maximum number of instances of ml.g6e.xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.2xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.4xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.8xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.8xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.12xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.12xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.16xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.16xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.24xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.24xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.g6e.48xlarge for hybrid jobs | The maximum number of instances of type ml.g6e.48xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 1 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.m4.xlarge for hybrid jobs | The maximum number of instances of type ml.m4.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.m4.2xlarge for hybrid jobs | The maximum number of instances of type ml.m4.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.m4.4xlarge for hybrid jobs | The maximum number of instances of type ml.m4.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 2 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.m4.10xlarge for hybrid jobs | The maximum number of instances of type ml.m4.10xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.m4.16xlarge for hybrid jobs | The maximum number of instances of type ml.m4.16xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | No | 
| Maximum number of instances of ml.m5.large for hybrid jobs | The maximum number of instances of type ml.m5.large allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.m5.xlarge for hybrid jobs | The maximum number of instances of type ml.m5.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.m5.2xlarge for hybrid jobs | The maximum number of instances of type ml.m5.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.m5.4xlarge for hybrid jobs | The maximum number of instances of type ml.m5.4xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.m5.12xlarge for hybrid jobs | The maximum number of instances of type ml.m5.12xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.m5.24xlarge for hybrid jobs | The maximum number of instances of type ml.m5.24xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.p2.xlarge for hybrid jobs | The maximum number of instances of type ml.p2.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.p2.8xlarge for hybrid jobs | The maximum number of instances of type ml.p2.8xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.p2.16xlarge for hybrid jobs | The maximum number of instances of type ml.p2.16xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.p4d.24xlarge for hybrid jobs | The maximum number of instances of type ml.p4d.24xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 0 | Yes | Yes | No | Yes | No | No | 
| Maximum number of instances of ml.t3.large for hybrid jobs | The maximum number of instances of type ml.t3.large allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.t3.xlarge for hybrid jobs | The maximum number of instances of type ml.t3.xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 
| Maximum number of instances of ml.t3.2xlarge for hybrid jobs | The maximum number of instances of type ml.t3.2xlarge allowed for all Amazon Braket Hybrid Jobs in this account and region. | 5 | Yes | Yes | Yes | Yes | Yes | Yes | 

 **Requesting limit updates** 

If you receive a ServiceQuotaExceeded exception for an instance type and do not have sufficient instances available for it, you may request a limit increase from the [Service Quotas](https://console.aws.amazon.com/servicequotas/home/) page in the AWS console and search for Amazon Braket under AWS Services.

**Note**  
If your hybrid job is unable to provision requested ML compute capacity, use another region. In addition, if you do not see an instance in the table, it is not available for Hybrid Jobs.

## Additional quotas and limits
<a name="braket-other-quotas"></a>
+ The Amazon Braket quantum task action is limited to 5MB in size.
+ For SV1, the maximum running duration is 3 hours for circuits up to 31 qubits, and 11 hours for circuits over 31 qubits.
+ The maximum number of shots per task allowed for SV1, DM1, and Rigetti devices is 50,000.
+ For AQT's IBEX-Q1 device, the maximum is 2000 shots per task.
+ For all IonQ's devices: When submitting tasks on-demand, the minimum number of shots per task is 100. The maximum number of gates per circuit is 2,000. The minimum number of shots per [error mitigation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-error-mitigation.html) task is 2,500. For a direct reservation, there is no minimum shot limit for tasks that do not use error mitigation. The maximum number of gates per circuit is 5,000. The minimum number of shots per error mitigation task is 500.
+ For QuEra's Aquila device, the maximum is 1,000 shots per task.
+ For IQM's Garnet and Emerald devices, the maximum is 20,000 shots per task.
+ For QPU devices, shots per task must be > 0.