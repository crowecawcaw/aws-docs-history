

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Journey status
<a name="journey-status"></a>

A migration journey can have any of the status values that appear in the following table. For information about how to change the status of a journey, see [Updating a journey](journey-updates.md).



| Status | Meaning | 
| --- | --- | 
| Creating | The service is creating the journey. You cannot perform any actions on the journey until the create operation is complete. | 
| Copying | The service is copying the journey. You cannot perform any actions on the journey until the copy operation is complete. | 
| Copy failed | There was an error that prevented the successful creation of the journey. If you see this status, delete the journey. | 
| Deleting | The service is deleting the journey. You cannot perform any actions on a journey that is in this state. | 
| Not started | This is the initial status of a migration journey after you create the journey. | 
| In progress | This status means that journey members have started working on the journey. | 
| Completed | This status marks the journey as complete. | 
| Transfer initiated | A journey member has initiated a transfer, but the invitee hasn't received the invitation yet. | 
| Transfer pending | An individual has received a journey-ownership-transfer invitation, but has neither accepted nor declined it yet. | 
| Transfer cancelled | A journey member has cancelled a pending ownership-transfer invitation. | 
| Transferring | The recipient of a journey-ownership-transfer invitation has accepted the invitation, and the service is in the process of transferring the ownership. You cannot perform any actions on the journey until the transfer is complete. | 
| Transfer declined | The recipient of a journey-ownership-transfer invitation has declined the invitation. | 
| Transfer failed | The recipient of a journey-ownership-transfer invitation accepted the invitation, but then the transfer failed due to an internal issue. | 