# Troubleshoot failed contact updates

When you call the [UpdateContact](../APIReference/API_UpdateContact.md "../APIReference/API_UpdateContact.md") API, AWS Ground Station performs
synchronous validation on the request. If validation passes, the update is processed
asynchronously to propagate changes to the antenna region. Synchronous validation errors
are returned directly in the HTTP response. Asynchronous failures are reported through
`failureCodes` and `failureMessage` fields on the contact version,
which you can view by calling [DescribeContactVersion](../APIReference/API_DescribeContactVersion.md "../APIReference/API_DescribeContactVersion.md") for the
version that failed to update.

For more information about contact versioning, see
[Update contacts and contact versioning](contacts.versioning.md "contacts.versioning.md").

## Synchronous validation errors

The following errors are returned directly in the HTTP response when the
[UpdateContact](../APIReference/API_UpdateContact.md "../APIReference/API_UpdateContact.md") request fails validation.

### ResourceNotFoundException: Contact not found

**Common cause**

The specified `contactId` does not exist or belongs to a different
AWS account.

**Resolution**

1. Verify that the `contactId` is correct.
2. Confirm that you are using credentials for the AWS account that owns the
   contact.
3. Use [ListContacts](../APIReference/API_ListContacts.md "../APIReference/API_ListContacts.md") to find the correct
   `contactId`.

### ConflictException: Cannot update contact

**Common cause**

The contact is in a state that does not allow updates. The [UpdateContact](../APIReference/API_UpdateContact.md "../APIReference/API_UpdateContact.md")
API can only be called when the contact is in the `SCHEDULED`,
`PREPASS`, or `PASS` state. This error also occurs if another
update is already in progress (the latest contact version is in the
`UPDATING` state).

**Resolution**

1. Call [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md") to check the
   current contact status.
2. If the contact is in a terminal state (for example, `COMPLETED`,
   `FAILED`, or `CANCELLED`), it cannot be updated. A contact
   can only be updated when it is in the `SCHEDULED`,
   `PREPASS`, or `PASS` state. For a complete list of
   terminal states, see
   [AWS Ground Station contact statuses](contacts.lifecycle.md#contact-statuses "contacts.lifecycle.md#contact-statuses").
3. If another update is in progress, wait for the current update to reach
   `ACTIVE` or `FAILED_TO_UPDATE` status before submitting
   another update. You can poll the [DescribeContactVersion](../APIReference/API_DescribeContactVersion.md "../APIReference/API_DescribeContactVersion.md")
   API, or use the `ContactUpdated` waiter convenience utilities provided
   by some AWS SDKs and the AWS Command Line Interface.

### InvalidParameterException: Invalid request parameters

**Common cause**

The request contains invalid parameters. Common causes include:

- Missing or empty `clientToken`.
- Multiple types of `ProgramTrackSettings` (azimuth/elevation, OEM,
  and TLE) included in a single request. Only one type is allowed per request.
- Setting `satelliteArn` to null without being approved for
  [azimuth elevation
  ephemeris](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md") at the contact's ground station.
- Missing `AzElProgramTrackSettings` when `satelliteArn`
  is null.
- Providing an `ephemerisId` that is not associated with the
  specified `satelliteArn`.
- The satellite does not have a valid visibility window from the ground station
  for the contact time range.
- The satellite is not onboarded to the ground station or does not have the
  licensing required by the mission profile.
- The mission profile includes
  [Antenna Downlink Demod Decode Config](how-it-works.config.md#how-it-works.config-antenna-downlink-demod-decode "how-it-works.config.md#how-it-works.config-antenna-downlink-demod-decode") configs, which
  are not supported for contact updates.

**Resolution**

1. Review the error message in the response for details about which parameter
   is invalid.
2. Ensure you provide exactly one type of `ProgramTrackSettings`
   per request.
3. If using azimuth/elevation pointing angles without a
   `satelliteArn`, confirm that your account is approved for this
   capability at the ground station. For more information, see
   [Provide azimuth elevation ephemeris data](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md").
4. Verify that the ephemeris you reference is associated with the correct
   satellite and covers the contact time range.

### ResourceLimitExceededException: Maximum version limit reached

**Common cause**

The contact has reached the maximum number of versions (128). Each call to
[UpdateContact](../APIReference/API_UpdateContact.md "../APIReference/API_UpdateContact.md") creates a new version, and a contact cannot exceed
this limit.

**Resolution**

1. This limit cannot be increased. If you need to make further changes,
   cancel the contact and reserve a new one.

## Asynchronous failure codes

The following failure codes appear in the `failureCodes` field of a contact
version with a `FAILED_TO_UPDATE` status. Use [DescribeContactVersion](../APIReference/API_DescribeContactVersion.md "../APIReference/API_DescribeContactVersion.md") to
retrieve these details. The `failureMessage` field provides additional
context about the failure.

| Failure code                          | Common cause                                                                                                                                                                                                                                                                                                                    | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `INTERNAL_ERROR`                      | An unexpected internal error occurred while processing the update.                                                                                                                                                                                                                                                              | Retry the update. If the issue persists, contact<br>[AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").                                                                                                                                                                                                                                                                                                                                                 |
| `INVALID_SATELLITE_ARN`               | The satellite ARN provided in the update request is not valid or does not<br>exist.                                                                                                                                                                                                                                             | Verify the satellite ARN and confirm that the satellite is registered in<br>your account.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `INVALID_UPDATE_CONTACT_REQUEST`      | The update request contains invalid parameters that were not caught during<br>synchronous validation.                                                                                                                                                                                                                           | Review the `failureMessage` for details and correct the<br>request parameters.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `EPHEMERIS_NOT_FOUND`                 | The ephemeris referenced in the tracking overrides does not exist.                                                                                                                                                                                                                                                              | Verify the `ephemerisId` and confirm that the ephemeris has<br>not been deleted.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `EPHEMERIS_TIME_RANGE_INVALID`        | The ephemeris does not cover the time range of the contact.                                                                                                                                                                                                                                                                     | Upload a new ephemeris that covers the full contact time range. If the<br>ephemeris time range cannot be extended, cancel the contact and reserve a new<br>one during the time span of the ephemeris. For more information, see<br>[Provide custom ephemeris data](providing-custom-ephemeris-data.md "providing-custom-ephemeris-data.md").                                                                                                                                                        |
| `EPHEMERIS_NOT_ENABLED`               | The referenced ephemeris is not in an `ENABLED` state.                                                                                                                                                                                                                                                                          | Check the ephemeris status and enable it before retrying the update.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `SATELLITE_DOES_NOT_MATCH_EPHEMERIS`  | The ephemeris is not associated with the satellite specified in the<br>update request.                                                                                                                                                                                                                                          | Ensure the `ephemerisId` belongs to the satellite specified<br>in `satelliteArn`.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `NOT_ONBOARDED_TO_AZEL_EPHEMERIS`     | Your account is not approved to use<br>[azimuth elevation<br>ephemeris data](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md") at the contact's<br>ground station. Azimuth elevation ephemeris is a restricted feature available<br>for a limited number of specialized use cases. | If azimuth elevation ephemeris is required for your use case, open an<br>AWS Support ticket through the [AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") to request access. Alternatively,<br>consider using<br>[TLE<br>ephemeris data](providing-tle-ephemeris-data.md "providing-tle-ephemeris-data.md") or<br>[OEM<br>ephemeris data](providing-oem-ephemeris-data.md "providing-oem-ephemeris-data.md") if they fit your use case. |
| `AZEL_EPHEMERIS_NOT_FOUND`            | The<br>[azimuth elevation<br>ephemeris](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md") referenced in the request does not exist.                                                                                                                                                | Verify the `ephemerisId` and confirm that the<br>azimuth elevation ephemeris has not been deleted.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `AZEL_EPHEMERIS_WRONG_GROUND_STATION` | The<br>[azimuth elevation<br>ephemeris](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md") was created for a different ground station than the one used<br>by the contact.                                                                                                          | Upload a new azimuth elevation ephemeris for the correct ground station,<br>or use an existing ephemeris that matches the contact's ground station.                                                                                                                                                                                                                                                                                                                                                 |
| `AZEL_EPHEMERIS_INVALID_STATUS`       | The<br>[azimuth elevation<br>ephemeris](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md") is not in a valid state for use.                                                                                                                                                         | Check the ephemeris status. It must be in an `ENABLED` state.<br>If the ephemeris failed validation, upload a corrected version.                                                                                                                                                                                                                                                                                                                                                                    |
| `AZEL_EPHEMERIS_TIME_RANGE_INVALID`   | The<br>[azimuth elevation<br>ephemeris](providing-azimuth-elevation-ephemeris-data.md "providing-azimuth-elevation-ephemeris-data.md") does not cover the time range of the contact.                                                                                                                                            | Upload a new azimuth elevation ephemeris that covers the full contact<br>time range. If the ephemeris time range cannot be extended, cancel the contact<br>and reserve a new one during the time span of the ephemeris.                                                                                                                                                                                                                                                                             |

## Checking the status of an update

After calling `UpdateContact`, the new contact version starts in the
`UPDATING` state. During this time, [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md") continues to return
the previously active version of the contact. The new version does not appear in
`DescribeContact` until it has been propagated to the antenna and reaches
`ACTIVE` status. To check the status of a specific version, use
[DescribeContactVersion](../APIReference/API_DescribeContactVersion.md "../APIReference/API_DescribeContactVersion.md").

To determine whether an update succeeded or failed:

1. Call [DescribeContactVersion](../APIReference/API_DescribeContactVersion.md "../APIReference/API_DescribeContactVersion.md")
   with the `contactId` and `versionId` returned by the
   `UpdateContact` response.
2. Check the `version.status` field. A status of `ACTIVE`
   means the update was applied successfully. A status of `FAILED_TO_UPDATE`
   means the update failed.
3. If the status is `FAILED_TO_UPDATE`, check the
   `version.failureCodes` and `version.failureMessage` fields
   for details about what went wrong.

###### Tip

Some AWS SDKs and the AWS Command Line Interface support a `ContactUpdated` waiter that
automatically polls `DescribeContactVersion` until the version reaches
`ACTIVE` or `FAILED_TO_UPDATE` status. For example, the
AWS Command Line Interface provides an
[aws groundstation
wait contact-updated](../../../cli/latest/reference/groundstation/wait/contact-updated.md "../../../cli/latest/reference/groundstation/wait/contact-updated.md") command. Use the waiter instead of implementing your
own polling logic.
