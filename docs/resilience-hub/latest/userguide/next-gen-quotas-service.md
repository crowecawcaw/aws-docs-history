

# Service quotas
<a name="next-gen-quotas-service"></a>

The following table lists the quotas for Next generation Resilience Hub.


| \# | Resource | Default quota | Adjustable | 
| --- | --- | --- | --- | 
| 1 | Systems per account per AWS Region | 500 | Yes | 
| 2 | Services per account per AWS Region | 100 | Yes | 
| 3 | User journeys per system | 20 | No | 
| 4 | Assessable Resources per service | 500 | Yes | 
| 5 | Total Resources per service | 2,000 | No | 
| 6 | Input sources per service | 20 | Yes | 
| 7 | Service functions per service | 20 | No | 
| 8 | Resilience policies per account per AWS Region | 100 | No | 
| 9 | Failure mode assessments included per service per month | 2 | No | 
| 10 | Dependencies tracked per service | 10,000 | No | 
| 11 | Cross-account role ARNs per service | 5 | No | 
| 12 | Service metrics per service | 10 | No | 
| 13 | Active test runs per service | 1 | No | 
| 14 | Test sources per test | 5 | No | 
| 15 | Tests per test template | 1 | No | 

Resilience tests run on AWS Fault Injection Service, so AWS FIS service quotas also apply to your test runs. These include quotas for the maximum number of active experiments and the maximum action duration. For more information, see [Quotas and limitations for AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/fis-quotas.html).