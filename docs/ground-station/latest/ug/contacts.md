# Understand contact lifecycle

Understanding the contact lifecycle can help to determine how to configure your automation and
during troubleshooting efforts. The following diagram shows the AWS Ground Station contact lifecycle as
well as Event Bridge Events emitted during the lifecycle. It is important to note that the
COMPLETED, FAILED, FAILED_TO_SCHEDULE, CANCELLED, AWS_CANCELLED, and AWS_FAILED are terminal
states. Contacts will not transition out of a terminal state. See the
[AWS Ground Station contact statuses](#contact-statuses "#contact-statuses")
for details on what each status indicates.

![State diagram showing AWS Ground Station contact event flow from scheduling to completion or failure.](images/contacts.state-machine.png)

## AWS Ground Station contact statuses

The status of an AWS Ground Station contact provides insight into what is happening to that contact
at a given time.

### Contact statuses

The following is the list of statuses that a contact can have:

- **AVAILABLE** - The contact is available to be reserved.
- **SCHEDULING** - The contact is in the process of
  scheduling.
- **SCHEDULED** - The contact was successfully scheduled.
- **FAILED_TO_SCHEDULE** - The contact failed to schedule.
- **PREPASS** - The contact is starting soon and resources
  are being prepared.
- **PASS** - The contact is currently executing and the
  satellite is being communicated with.
- **POSTPASS** - The communication has completed and
  resources used are being cleaned up.
- **COMPLETED** - The contact completed without error.
- **FAILED** - The contact failed because of an issue with
  your resource configuration.
- **AWS_FAILED** - The contact failed because of a problem
  in the AWS Ground Station service.
- **CANCELLING** - The contact is in the process of being
  cancelled.
- **AWS_CANCELLED** - The contact was cancelled by
  the AWS Ground Station service. Antenna or site maintenance, and ephemeris drift are examples of
  when this could happen.
- **CANCELLED** - The contact was cancelled by you.
