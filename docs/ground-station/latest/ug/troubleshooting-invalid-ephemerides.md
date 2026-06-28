# Troubleshoot invalid ephemerides

When you upload ephemeris data to AWS Ground Station, it goes through an asynchronous validation workflow.
If validation fails, the ephemeris status will change to `INVALID`. The
error messaging in the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") response provides detailed information
to help you identify and resolve the issue.

## Understanding ephemeris validation errors

When an ephemeris fails validation, the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") API response includes
two fields to help diagnose the problem:

errorCode

A machine-readable code identifying the specific validation error. This can be used for programmatic error handling.

errorMessage

A human-readable description of the validation error with specific details about what went wrong and guidance on how to fix it.

Example [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") response for an invalid ephemeris:

```
{
    "ephemerisId": "abc12345-6789-def0-1234-567890abcdef",
    "name": "My Invalid Ephemeris",
    "status": "INVALID",
    "creationTime": 1620254718.765,
    "invalidReason": "METADATA_INVALID",
    "errorCode": "OBJECT_NAME_MISSING",
    "errorMessage": "Metadata field missing: OBJECT_NAME",
    "suppliedData": {
        "tle": {
            "ephemerisData": "[...]"
        }
    }
}
```

## Common validation errors for TLE ephemerides

The following are common validation errors encountered when uploading TLE ephemerides:

Mismatched satellite catalog number

_Error:_ "The satellite catalog number present in the ephemeris does not match the associated satellite's satellite catalog number"

_Solution:_ Verify that the NORAD ID/satellite catalog number in your TLE lines matches the
satellite catalog number of your satellite. Use `00000` for satellites without an assigned catalog number.

Invalid mean motion

_Error:_ "The mean motion of the provided ephemeris differs too greatly from the most recent reference ephemeris"

_Solution:_ Verify that your TLE data is correct and represents a valid orbit.
Ground Station uses Space-Track ephemerides as a reference during validation.

## Common validation errors for OEM ephemerides

The following are common validation errors encountered when uploading OEM ephemerides:

Invalid reference frame

_Error:_ "The REF\_FRAME is not supported"

_Solution:_ Update your OEM file to use one of the supported reference
frames: EME2000 or ITRF2000.

Missing required fields

_Error:_ "Metadata field missing: INTERPOLATION"

_Solution:_ Add the INTERPOLATION and INTERPOLATION\_DEGREE fields to
your OEM metadata section. These are required for AWS Ground Station to generate accurate antenna pointing angles.

Unsupported time system

_Error:_ "The TIME\_SYSTEM is not supported"

_Solution:_ Ensure your OEM file uses UTC as the time system.

Unsupported OEM version

_Error:_ "The CCSDS\_OEM\_VERS is not supported"

_Solution:_ Ensure your OEM file uses CCSDS OEM version 2.0.

## Common validation errors for azimuth elevation ephemerides

The following are common validation errors encountered when uploading azimuth elevation ephemerides:

Missing azimuth/elevation data

_Error:_ "No TimeAzEl fields were present in at least one AzElSegment"

_Solution:_ Ensure each segment in your azimuth elevation data contains at
least one time-tagged azimuth/elevation pair.

Invalid azimuth angle range (degrees)

_Error:_ "AzEl az must be greater than or equal to -180 and less or equal to 360 degrees"

_Solution:_ Verify that azimuth angles are within [-180, 360] degrees.

Invalid elevation angle range (degrees)

_Error:_ "AzEl el must be greater than or equal to -90 and less than or equal to 90 degrees"

_Solution:_ Verify that elevation angles are within [-90, 90] degrees.

Invalid azimuth angle range (radians)

_Error:_ "AzEl az must be greater than or equal to -pi and less than or equal to 2pi radians"

_Solution:_ Verify that azimuth angles are within [-π, 2π] radians.

Invalid elevation angle range (radians)

_Error:_ "AzEl el must be greater than or equal to -pi/2 and less than or equal to pi/2 radians"

_Solution:_ Verify that elevation angles are within [-π/2, π/2] radians.

Non-monotonic time values

_Error:_ "The TimeAzEl items within a AzElSegment must be temporally in order"

_Solution:_ Ensure that the time values in each segment
are strictly increasing.

Segments out of order

_Error:_ "AzElSegments must be temporally in order"

_Solution:_ Ensure that segments are arranged in chronological order.

Overlapping segments

_Error:_ "The time range of at least one segment overlaps with other segment time ranges"

_Solution:_ Ensure that each segment has a unique, non-overlapping time
range. The `endTime` of one segment should not exceed the `startTime`
of the next segment.

## Troubleshooting steps

If your ephemeris fails validation, follow these steps to resolve the issue:

1. Call [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") with your ephemeris ID to retrieve the
   `errorCode` and `errorMessage`.
2. Review the error message for specific details about what validation check failed.
3. Correct the identified issues in your ephemeris data.
4. Upload a new ephemeris with the corrected data using [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md").
5. Monitor the new ephemeris status until it reaches `ENABLED` state.
6. Delete the invalid ephemeris using [DeleteEphemeris](../APIReference/API_DeleteEphemeris.md "../APIReference/API_DeleteEphemeris.md") if it's no longer needed.

## Complete error code reference

The following sections provide a comprehensive mapping of all `errorCode` values
that may be returned when ephemeris validation fails, organized by the high-level
`invalidReason` category.

### Invalid Reason: `METADATA_INVALID`

These errors occur when required metadata fields are missing, incorrectly formatted, or contain
unsupported values in the ephemeris data.

| Error Code                     | Error Message                                                                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MISMATCHED\_SATCAT\_ID         | The satellite catalog number present in the TLE ephemeris does not match the associated satellite's satellite catalog number                                                                                          |
| OEM\_VERSION\_UNSUPPORTED      | The `CCSDS_OEM_VERS` in the OEM ephemeris is not supported. Supported values: [`2.0`]                                                                                                                                 |
| ORIGINATOR\_MISSING            | The `ORIGINATOR` header field is missing from the OEM ephemeris                                                                                                                                                       |
| CREATION\_DATE\_MISSING        | The `CREATION_DATE` header field is missing from the OEM ephemeris                                                                                                                                                    |
| OBJECT\_NAME\_MISSING          | The `OBJECT_NAME` metadata field is missing from the OEM ephemeris                                                                                                                                                    |
| OBJECT\_ID\_MISSING            | The `OBJECT_ID` metadata field is missing from the OEM ephemeris                                                                                                                                                      |
| REF\_FRAME\_UNSUPPORTED        | The `REF_FRAME` in the OEM ephemeris is not supported. Supported values: [`EME2000`, `ITRF2000`]                                                                                                                      |
| REF\_FRAME\_EPOCH\_UNSUPPORTED | The `REF_FRAME_EPOCH` metadata field in the OEM ephemeris is not supported. Please remove this field from the ephemeris                                                                                               |
| TIME\_SYSTEM\_UNSUPPORTED      | The `TIME_SYSTEM` in the OEM ephemeris is not supported. Supported values: [`UTC`]                                                                                                                                    |
| CENTER\_BODY\_UNSUPPORTED      | The `CENTER_BODY` in the OEM ephemeris is not supported. Supported values: [`Earth`]                                                                                                                                  |
| INTERPOLATION\_MISSING         | The `INTERPOLATION` metadata field is missing from the OEM ephemeris                                                                                                                                                  |
| INTERPOLATION\_DEGREE\_INVALID | The interpolation degree in the OEM ephemeris must be larger than 0 for the interpolation method                                                                                                                      |
| AZ\_EL\_SEGMENT\_LIST\_MISSING | The [`azElSegmentList`](../APIReference/API_AzElSegments.md "../APIReference/API_AzElSegments.md") field is missing                                                                                                   |
| INSUFFICIENT\_TIME\_AZ\_EL     | No [`TimeAzEl`](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") fields were present in at least one [`azElSegmentList`](../APIReference/API_AzElSegments.md "../APIReference/API_AzElSegments.md") |

### Invalid Reason: `TIME_RANGE_INVALID`

These errors occur when the ephemeris contains invalid time ranges, including issues with
start/end times, segment ordering, overlapping segments, or temporal inconsistencies.

| Error Code                                      | Error Message                                                                                                                                                                                                                                            |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| START\_TIME\_IN\_FUTURE                         | Ephemeris start time is in the future, but must be in the past                                                                                                                                                                                           |
| END\_TIME\_IN\_PAST                             | Ephemeris end time is in the past, but must be in the future                                                                                                                                                                                             |
| EXPIRATION\_TIME\_TOO\_EARLY                    | The provided expiration time is earlier than the ephemeris end time                                                                                                                                                                                      |
| START\_TIME\_METADATA\_TOO\_EARLY               | The `START_TIME` metadata value is earlier than the earliest time present in the OEM ephemeris data                                                                                                                                                      |
| STOP\_TIME\_METADATA\_TOO\_LATE                 | The `STOP_TIME` metadata value is later than the latest time present in the OEM ephemeris data                                                                                                                                                           |
| AZ\_EL\_SEGMENT\_END\_TIME\_BEFORE\_START\_TIME | The [`endTime`](../APIReference/API_ISO8601TimeRange.md "../APIReference/API_ISO8601TimeRange.md") of at least one data segment is before the segment's [`startTime`](../APIReference/API_ISO8601TimeRange.md "../APIReference/API_ISO8601TimeRange.md") |
| AZ\_EL\_SEGMENT\_TIMES\_OVERLAP                 | The time range of at least one segment overlaps with other segment time ranges                                                                                                                                                                           |
| AZ\_EL\_SEGMENTS\_OUT\_OF\_ORDER                | The segments are not temporally ordered                                                                                                                                                                                                                  |
| TIME\_AZ\_EL\_ITEMS\_OUT\_OF\_ORDER             | The [`TimeAzEl`](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") items within a [`AzElSegment`](../APIReference/API_AzElSegment.md "../APIReference/API_AzElSegment.md") must be temporally in order                                  |
| AZ\_EL\_SEGMENT\_REFERENCE\_EPOCH\_INVALID      | The reference epoch for a segment is invalid or incorrectly formatted                                                                                                                                                                                    |
| AZ\_EL\_SEGMENT\_START\_TIME\_INVALID           | The start time in a segment's valid time range does not start after the first segment                                                                                                                                                                    |
| AZ\_EL\_SEGMENT\_END\_TIME\_INVALID             | The end time in a segment's valid time range does not end after the last segment                                                                                                                                                                         |
| AZ\_EL\_SEGMENT\_VALID\_TIME\_RANGE\_INVALID    | The valid time range for a segment is invalid                                                                                                                                                                                                            |
| AZ\_EL\_SEGMENT\_END\_TIME\_TOO\_LATE           | The end time of a segment exceeds the maximum allowed duration from the reference epoch                                                                                                                                                                  |
| AZ\_EL\_TOTAL\_DURATION\_EXCEEDED               | The total duration across all segments exceeds the maximum allowed pointing angle duration                                                                                                                                                               |

### Invalid Reason: `TRAJECTORY_INVALID`

These errors occur when the ephemeris contains invalid trajectory data, including issues with
orbital parameters, angle ranges, or units.

| Error Code                               | Error Message                                                                                                                                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MEAN\_MOTION\_INVALID                    | The mean motion of the provided TLE ephemeris differs too greatly from the most recent reference ephemeris. Note: Ground Station uses Space-Track ephemerides as a reference during validation |
| TIME\_AZ\_EL\_AZ\_RADIAN\_RANGE\_INVALID | AzEl [`az`](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") must be greater than or equal to -π and less than or equal to 2π radians                                        |
| TIME\_AZ\_EL\_EL\_RADIAN\_RANGE\_INVALID | AzEl [`el`](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") must be greater than or equal to -π/2 and less than or equal to π/2 radians                                     |
| TIME\_AZ\_EL\_AZ\_DEGREE\_RANGE\_INVALID | AzEl [`az`](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") must be greater than or equal to -180 and less or equal to 360 degrees                                          |
| TIME\_AZ\_EL\_EL\_DEGREE\_RANGE\_INVALID | AzEl [`el`](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") must be greater than or equal to -90 degrees and less than or equal to 90 degrees                               |
| TIME\_AZ\_EL\_ANGLE\_UNITS\_INVALID      | Invalid AzEl angle units                                                                                                                                                                       |

### Invalid Reason: `KMS_KEY_INVALID`

These errors occur when there are issues with the AWS Key Management Service (KMS) key used
to encrypt the ephemeris data.

| Error Code                     | Error Message                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------- |
| INSUFFICIENT\_KMS\_PERMISSIONS | Ground Station does not have sufficient permissions to access this ephemeris' KMS key |

### Invalid Reason: `VALIDATION_ERROR`

These errors occur when there are general validation issues with the ephemeris data that
don't fall into the other specific categories.

| Error Code            | Error Message                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| INTERNAL\_ERROR       | Internal error occurred during ephemeris validation                                                                       |
| FILE\_FORMAT\_INVALID | The ephemeris file format is invalid or corrupted. Verify the file conforms to the expected format for the ephemeris type |
