

# Quotas and limits in account access manager
<a name="aam-quotas"></a>

The following tables describe quotas within account access manager. Quota increase requests must come from a management or delegated administrator account. To increase a quota, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

## Group assignment quota
<a name="aam-quotas-group-assignments"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| Maximum number of groups assigned to an IAM role | 20 | Yes | 

## Throttle limits
<a name="aam-quotas-throttle-limits"></a>


| Resource | Default quota | Can be increased | 
| --- | --- | --- | 
| Account access API | The account access API has a collective throttle limit of 20 transactions per second (TPS). For read APIs, you can open a support case to request a limit increase. The write API operations have a limit of 15 outstanding asynchronous calls. This limit cannot be increased. | Yes | 