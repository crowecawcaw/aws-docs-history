

# Zonal autoshift API operations
<a name="actions.zonalautoshift"></a>

The following table lists ARC API operations that you can use with zonal autoshift. For examples of using zonal autoshift API operations with the AWS CLI, see .

For examples of how to use common zonal autoshift API operations with the AWS Command Line Interface, see [Examples of using the AWS CLI with zonal autoshift](getting-started-cli-zonal-autoshift.md).


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Create a practice run configuration | See [Enabling or disabling zonal autoshift](arc-zonal-autoshift.start-cancel.md#arc-zonal-autoshift.configure) | See [CreatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CreatePracticeRunConfiguration.html) | 
| Delete a practice run configuration | See [Configuring, editing, or deleting a practice run configuration](arc-zonal-autoshift.edit-delete-practice-run.md) | See [DeletePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_DeletePracticeRunConfiguration.html) | 
| List autoshifts | See [Zonal autoshift in ARC](arc-zonal-shift.md) | See [ListAutoshifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html) | 
| List resources for zonal autoshift | See [Supported resources](arc-zonal-shift.resource-types.md) | See [ListManagedResources](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html) | 
| Get resources for zonal autoshift | See [Supported resources](arc-zonal-shift.resource-types.md) | See [GetManagedResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html) | 
| Edit a practice run configuration | See [Configuring, editing, or deleting a practice run configuration](arc-zonal-autoshift.edit-delete-practice-run.md) | See [UpdatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdatePracticeRunConfiguration.html) | 
| Enable or disable zonal autoshift | See [Enabling or disabling zonal autoshift](arc-zonal-autoshift.start-cancel.md#arc-zonal-autoshift.configure) | See [UpdateZonalAutoshiftConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalAutoshiftConfiguration.html) | 
| Enable or disable autoshift observer notification | See [Enabling and working with zonal autoshift](arc-zonal-autoshift.start-cancel.md) | See [UpdateAutoshiftObserverNotificationStatus](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateAutoshiftObserverNotificationStatus.html) | 
| Start a practice run | See [Starting a practice run zonal shift](arc-zonal-autoshift.start-cancel.md) | See [StartPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartPracticeRun.html) | 
| Cancel a practice run | See [Canceling a practice run zonal shift](arc-zonal-autoshift.start-cancel.md) | See [CancelPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelPracticeRun.html) | 