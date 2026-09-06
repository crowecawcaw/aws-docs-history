

# Troubleshoot failed contact updates
<a name="troubleshooting-failed-to-update-contacts"></a>

 When you call the [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) API, AWS Ground Station performs synchronous validation on the request. If validation passes, the update is processed asynchronously to propagate changes to the antenna region. Synchronous validation errors are returned directly in the HTTP response. Asynchronous failures are reported through `failureCodes` and `failureMessage` fields on the contact version, which you can view by calling [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) for the version that failed to update. 

 For more information about contact versioning, see [Update contacts and contact versioning](contacts.versioning.md). 

## Synchronous validation errors
<a name="troubleshooting-update-contact-sync-errors"></a>

 The following errors are returned directly in the HTTP response when the [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) request fails validation. 

### ResourceNotFoundException: Contact not found
<a name="troubleshooting-update-contact-not-found"></a>

**Common cause**

 The specified `contactId` does not exist or belongs to a different AWS account. 

**Resolution**

1. Verify that the `contactId` is correct.

1. Confirm that you are using credentials for the AWS account that owns the contact.

1. Use [ListContacts](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContacts.html) to find the correct `contactId`.

### ConflictException: Cannot update contact
<a name="troubleshooting-update-contact-conflict"></a>

**Common cause**

 The contact is in a state that does not allow updates. The [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) API can only be called when the contact is in the `SCHEDULED`, `PREPASS`, or `PASS` state. This error also occurs if another update is already in progress (the latest contact version is in the `UPDATING` state). 

**Resolution**

1. Call [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html) to check the current contact status.

1. If the contact is in a terminal state (for example, `COMPLETED`, `FAILED`, or `CANCELLED`), it cannot be updated. A contact can only be updated when it is in the `SCHEDULED`, `PREPASS`, or `PASS` state. For a complete list of terminal states, see [AWS Ground Station contact statuses](contacts.lifecycle.md#contact-statuses).

1. If another update is in progress, wait for the current update to reach `ACTIVE` or `FAILED_TO_UPDATE` status before submitting another update. You can poll the [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) API, or use the `ContactUpdated` waiter convenience utilities provided by some AWS SDKs and the AWS Command Line Interface.

### InvalidParameterException: Invalid request parameters
<a name="troubleshooting-update-contact-invalid-params"></a>

**Common cause**

 The request contains invalid parameters. Common causes include: 
+ Missing or empty `clientToken`.
+ Multiple types of `ProgramTrackSettings` (azimuth/elevation, OEM, and TLE) included in a single request. Only one type is allowed per request.
+ Setting `satelliteArn` to null without being approved for [azimuth elevation ephemeris](providing-azimuth-elevation-ephemeris-data.md) at the contact's ground station.
+ Missing `AzElProgramTrackSettings` when `satelliteArn` is null.
+ Providing an `ephemerisId` that is not associated with the specified `satelliteArn`.
+ The satellite does not have a valid visibility window from the ground station for the contact time range.
+ The satellite is not onboarded to the ground station or does not have the licensing required by the mission profile.
+ The mission profile includes [Antenna Downlink Demod Decode Config](how-it-works.config.md#how-it-works.config-antenna-downlink-demod-decode) configs, which are not supported for contact updates.

**Resolution**

1. Review the error message in the response for details about which parameter is invalid.

1. Ensure you provide exactly one type of `ProgramTrackSettings` per request.

1. If using azimuth/elevation pointing angles without a `satelliteArn`, confirm that your account is approved for this capability at the ground station. For more information, see [Provide azimuth elevation ephemeris data](providing-azimuth-elevation-ephemeris-data.md).

1. Verify that the ephemeris you reference is associated with the correct satellite and covers the contact time range.

### ResourceLimitExceededException: Maximum version limit reached
<a name="troubleshooting-update-contact-version-limit"></a>

**Common cause**

 The contact has reached the maximum number of versions (128). Each call to [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) creates a new version, and a contact cannot exceed this limit. 

**Resolution**

1. This limit cannot be increased. If you need to make further changes, cancel the contact and reserve a new one.

## Asynchronous failure codes
<a name="troubleshooting-update-contact-async-failures"></a>

 The following failure codes appear in the `failureCodes` field of a contact version with a `FAILED_TO_UPDATE` status. Use [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) to retrieve these details. The `failureMessage` field provides additional context about the failure. 


| Failure code | Common cause | Resolution | 
| --- | --- | --- | 
| INTERNAL\_ERROR | An unexpected internal error occurred while processing the update. | Retry the update. If the issue persists, contact [AWS Support](https://console.aws.amazon.com/support). | 
| INVALID\_SATELLITE\_ARN | The satellite ARN provided in the update request is not valid or does not exist. | Verify the satellite ARN and confirm that the satellite is registered in your account. | 
| INVALID\_UPDATE\_CONTACT\_REQUEST | The update request contains invalid parameters that were not caught during synchronous validation. | Review the failureMessage for details and correct the request parameters. | 
| EPHEMERIS\_NOT\_FOUND | The ephemeris referenced in the tracking overrides does not exist. | Verify the ephemerisId and confirm that the ephemeris has not been deleted. | 
| EPHEMERIS\_TIME\_RANGE\_INVALID | The ephemeris does not cover the time range of the contact. | Upload a new ephemeris that covers the full contact time range. If the ephemeris time range cannot be extended, cancel the contact and reserve a new one during the time span of the ephemeris. For more information, see [Provide custom ephemeris data](providing-custom-ephemeris-data.md). | 
| EPHEMERIS\_NOT\_ENABLED | The referenced ephemeris is not in an ENABLED state. | Check the ephemeris status and enable it before retrying the update. | 
| SATELLITE\_DOES\_NOT\_MATCH\_EPHEMERIS | The ephemeris is not associated with the satellite specified in the update request. | Ensure the ephemerisId belongs to the satellite specified in satelliteArn. | 
| NOT\_ONBOARDED\_TO\_AZEL\_EPHEMERIS | Your account is not approved to use [azimuth elevation ephemeris data](providing-azimuth-elevation-ephemeris-data.md) at the contact's ground station. Azimuth elevation ephemeris is a restricted feature available for a limited number of specialized use cases. | If azimuth elevation ephemeris is required for your use case, open an AWS Support ticket through the [AWS Support Center Console](https://console.aws.amazon.com/support) to request access. Alternatively, consider using [TLE ephemeris data](providing-tle-ephemeris-data.md) or [OEM ephemeris data](providing-oem-ephemeris-data.md) if they fit your use case. | 
| AZEL\_EPHEMERIS\_NOT\_FOUND | The [azimuth elevation ephemeris](providing-azimuth-elevation-ephemeris-data.md) referenced in the request does not exist. | Verify the ephemerisId and confirm that the azimuth elevation ephemeris has not been deleted. | 
| AZEL\_EPHEMERIS\_WRONG\_GROUND\_STATION | The [azimuth elevation ephemeris](providing-azimuth-elevation-ephemeris-data.md) was created for a different ground station than the one used by the contact. | Upload a new azimuth elevation ephemeris for the correct ground station, or use an existing ephemeris that matches the contact's ground station. | 
| AZEL\_EPHEMERIS\_INVALID\_STATUS | The [azimuth elevation ephemeris](providing-azimuth-elevation-ephemeris-data.md) is not in a valid state for use. | Check the ephemeris status. It must be in an ENABLED state. If the ephemeris failed validation, upload a corrected version. | 
| AZEL\_EPHEMERIS\_TIME\_RANGE\_INVALID | The [azimuth elevation ephemeris](providing-azimuth-elevation-ephemeris-data.md) does not cover the time range of the contact. | Upload a new azimuth elevation ephemeris that covers the full contact time range. If the ephemeris time range cannot be extended, cancel the contact and reserve a new one during the time span of the ephemeris. | 

## Checking the status of an update
<a name="troubleshooting-update-contact-checking-status"></a>

 After calling `UpdateContact`, the new contact version starts in the `UPDATING` state. During this time, [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html) continues to return the previously active version of the contact. The new version does not appear in `DescribeContact` until it has been propagated to the antenna and reaches `ACTIVE` status. To check the status of a specific version, use [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html). 

To determine whether an update succeeded or failed:

1. Call [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) with the `contactId` and `versionId` returned by the `UpdateContact` response.

1. Check the `version.status` field. A status of `ACTIVE` means the update was applied successfully. A status of `FAILED_TO_UPDATE` means the update failed.

1. If the status is `FAILED_TO_UPDATE`, check the `version.failureCodes` and `version.failureMessage` fields for details about what went wrong.

**Tip**  
 Some AWS SDKs and the AWS Command Line Interface support a `ContactUpdated` waiter that automatically polls `DescribeContactVersion` until the version reaches `ACTIVE` or `FAILED_TO_UPDATE` status. For example, the AWS Command Line Interface provides an [aws groundstation wait contact-updated](https://docs.aws.amazon.com/cli/latest/reference/groundstation/wait/contact-updated.html) command. Use the waiter instead of implementing your own polling logic. 