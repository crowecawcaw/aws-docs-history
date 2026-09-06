

# Understand contact lifecycle
<a name="contacts.lifecycle"></a>

 Understanding the contact lifecycle can help you to automate and troubleshoot various problems while using AWS Ground Station. The following diagram shows the AWS Ground Station contact lifecycle as well as Event Bridge Events emitted during the lifecycle. It is important to note that the COMPLETED, FAILED, FAILED\_TO\_SCHEDULE, CANCELLED, AWS\_CANCELLED, and AWS\_FAILED are terminal states. Contacts will not transition out of a terminal state. See the [AWS Ground Station contact statuses](#contact-statuses) for details on what each status indicates and whether it is stoppable or cancellable using [ CancelContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CancelContact.html).

 ![State diagram showing AWS Ground Station contact event flow from scheduling to completion or failure.](http://docs.aws.amazon.com/ground-station/latest/ug/images/contacts.state-machine.png) 

## AWS Ground Station contact statuses
<a name="contact-statuses"></a>

The status of an AWS Ground Station contact provides insight into what is happening to that contact at a given time. 

### Contact statuses
<a name="contact-statuses-enum"></a>

The following table describes the statuses that a contact can have:


| Status | Description | Terminal | Cancelable | Stoppable | 
| --- | --- | --- | --- | --- | 
| AVAILABLE | The contact is available to be reserved. | No | N/A | N/A | 
| SCHEDULING | The contact is in the process of scheduling. | No | Yes | No | 
| SCHEDULED | The contact was successfully scheduled. | No | Yes | No | 
| FAILED\_TO\_SCHEDULE | The contact failed to schedule. | Yes | No | No | 
| PREPASS | The contact is starting soon and resources are being prepared. | No | Yes | No | 
| PASS | The contact is currently executing and the satellite is being communicated with. | No | No | Yes | 
| POSTPASS | The communication has completed and resources used are being cleaned up. | No | No | No | 
| COMPLETED | The contact completed without error. | Yes | No | No | 
| FAILED | The contact failed because of an issue with your resource configuration. | Yes | No | No | 
| AWS\_FAILED | The contact failed because of a problem in the AWS Ground Station service. | Yes | No | No | 
| CANCELLING | The contact is in the process of being cancelled. | No | No | No | 
| AWS\_CANCELLED | The contact was cancelled by the AWS Ground Station service. Antenna or site maintenance, and ephemeris drift are examples of when this could happen. | Yes | No | No | 
| CANCELLED | The contact was cancelled by you. | Yes | No | No | 

**Note**  
 For information about billing implications of cancelled or stopped contacts, see [Understand contact billing](contacts.billing.md). 

## Contact Data Retention
<a name="contacts.retention"></a>

 AWS Ground Station retains contact data for 1 year after a [ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html) request is made to reserve a contact. After the 1 year period, the contact data is deleted. 

 If you need to retain contact data beyond one year, it is recommended to export your data before the retention period expires. For more information on how to access and export contact data, refer to: 
+  [AWS Ground Station API Reference](https://docs.aws.amazon.com/ground-station/latest/APIReference/Welcome.html) 
+  [AWS Ground Station CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/groundstation/index.html) 