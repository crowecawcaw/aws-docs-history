

# Troubleshoot invalid ephemerides
<a name="troubleshooting-invalid-ephemerides"></a>

 When you upload ephemeris data to AWS Ground Station, it goes through an asynchronous validation workflow. If validation fails, the ephemeris status will change to `INVALID`. The error messaging in the [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) response provides detailed information to help you identify and resolve the issue. 

## Understanding ephemeris validation errors
<a name="w2aac74c19b5"></a>

 When an ephemeris fails validation, the [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) API response includes two fields to help diagnose the problem: 

errorCode  
A machine-readable code identifying the specific validation error. This can be used for programmatic error handling.

errorMessage  
A human-readable description of the validation error with specific details about what went wrong and guidance on how to fix it.

 Example [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) response for an invalid ephemeris: 

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
<a name="w2aac74c19b7"></a>

 The following are common validation errors encountered when uploading TLE ephemerides: 

Mismatched satellite catalog number  
 *Error:* "The satellite catalog number present in the ephemeris does not match the associated satellite's satellite catalog number"   
 *Solution:* Verify that the NORAD ID/satellite catalog number in your TLE lines matches the satellite catalog number of your satellite. Use `00000` for satellites without an assigned catalog number. 

Invalid mean motion  
 *Error:* "The mean motion of the provided ephemeris differs too greatly from the most recent reference ephemeris"   
 *Solution:* Verify that your TLE data is correct and represents a valid orbit. Ground Station uses Space-Track ephemerides as a reference during validation. 

## Common validation errors for OEM ephemerides
<a name="w2aac74c19b9"></a>

 The following are common validation errors encountered when uploading OEM ephemerides: 

Invalid reference frame  
 *Error:* "The REF\_FRAME is not supported"   
 *Solution:* Update your OEM file to use one of the supported reference frames: EME2000 or ITRF2000. 

Missing required fields  
 *Error:* "Metadata field missing: INTERPOLATION"   
 *Solution:* Add the INTERPOLATION and INTERPOLATION\_DEGREE fields to your OEM metadata section. These are required for AWS Ground Station to generate accurate antenna pointing angles. 

Unsupported time system  
 *Error:* "The TIME\_SYSTEM is not supported"   
 *Solution:* Ensure your OEM file uses UTC as the time system. 

Unsupported OEM version  
 *Error:* "The CCSDS\_OEM\_VERS is not supported"   
 *Solution:* Ensure your OEM file uses CCSDS OEM version 2.0. 

## Common validation errors for azimuth elevation ephemerides
<a name="w2aac74c19c11"></a>

 The following are common validation errors encountered when uploading azimuth elevation ephemerides: 

Missing azimuth/elevation data  
 *Error:* "No TimeAzEl fields were present in at least one AzElSegment"   
 *Solution:* Ensure each segment in your azimuth elevation data contains at least one time-tagged azimuth/elevation pair. 

Invalid azimuth angle range (degrees)  
 *Error:* "AzEl az must be greater than or equal to -180 and less or equal to 360 degrees"   
 *Solution:* Verify that azimuth angles are within [-180, 360] degrees. 

Invalid elevation angle range (degrees)  
 *Error:* "AzEl el must be greater than or equal to -90 and less than or equal to 90 degrees"   
 *Solution:* Verify that elevation angles are within [-90, 90] degrees. 

Invalid azimuth angle range (radians)  
 *Error:* "AzEl az must be greater than or equal to -pi and less than or equal to 2pi radians"   
 *Solution:* Verify that azimuth angles are within [-π, 2π] radians. 

Invalid elevation angle range (radians)  
 *Error:* "AzEl el must be greater than or equal to -pi/2 and less than or equal to pi/2 radians"   
 *Solution:* Verify that elevation angles are within [-π/2, π/2] radians. 

Non-monotonic time values  
 *Error:* "The TimeAzEl items within a AzElSegment must be temporally in order"   
 *Solution:* Ensure that the time values in each segment are strictly increasing. 

Segments out of order  
 *Error:* "AzElSegments must be temporally in order"   
 *Solution:* Ensure that segments are arranged in chronological order. 

Overlapping segments  
 *Error:* "The time range of at least one segment overlaps with other segment time ranges"   
 *Solution:* Ensure that each segment has a unique, non-overlapping time range. The `endTime` of one segment should not exceed the `startTime` of the next segment. 

## Troubleshooting steps
<a name="w2aac74c19c13"></a>

 If your ephemeris fails validation, follow these steps to resolve the issue: 

1. Call [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) with your ephemeris ID to retrieve the `errorCode` and `errorMessage`.

1. Review the error message for specific details about what validation check failed.

1. Correct the identified issues in your ephemeris data.

1. Upload a new ephemeris with the corrected data using [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html).

1. Monitor the new ephemeris status until it reaches `ENABLED` state.

1. Delete the invalid ephemeris using [DeleteEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DeleteEphemeris.html) if it's no longer needed.

## Complete error code reference
<a name="w2aac74c19c15"></a>

 The following sections provide a comprehensive mapping of all `errorCode` values that may be returned when ephemeris validation fails, organized by the high-level `invalidReason` category. 

### Invalid Reason: `METADATA_INVALID`
<a name="w2aac74c19c15b5"></a>

 These errors occur when required metadata fields are missing, incorrectly formatted, or contain unsupported values in the ephemeris data. 


| Error Code | Error Message | 
| --- | --- | 
| MISMATCHED\_SATCAT\_ID | The satellite catalog number present in the TLE ephemeris does not match the associated satellite's satellite catalog number | 
| OEM\_VERSION\_UNSUPPORTED | The CCSDS\_OEM\_VERS in the OEM ephemeris is not supported. Supported values: [2.0] | 
| ORIGINATOR\_MISSING | The ORIGINATOR header field is missing from the OEM ephemeris | 
| CREATION\_DATE\_MISSING | The CREATION\_DATE header field is missing from the OEM ephemeris | 
| OBJECT\_NAME\_MISSING | The OBJECT\_NAME metadata field is missing from the OEM ephemeris | 
| OBJECT\_ID\_MISSING | The OBJECT\_ID metadata field is missing from the OEM ephemeris | 
| REF\_FRAME\_UNSUPPORTED | The REF\_FRAME in the OEM ephemeris is not supported. Supported values: [EME2000, ITRF2000] | 
| REF\_FRAME\_EPOCH\_UNSUPPORTED | The REF\_FRAME\_EPOCH metadata field in the OEM ephemeris is not supported. Please remove this field from the ephemeris | 
| TIME\_SYSTEM\_UNSUPPORTED | The TIME\_SYSTEM in the OEM ephemeris is not supported. Supported values: [UTC] | 
| CENTER\_BODY\_UNSUPPORTED | The CENTER\_BODY in the OEM ephemeris is not supported. Supported values: [Earth] | 
| INTERPOLATION\_MISSING | The INTERPOLATION metadata field is missing from the OEM ephemeris | 
| INTERPOLATION\_DEGREE\_INVALID | The interpolation degree in the OEM ephemeris must be larger than 0 for the interpolation method | 
| AZ\_EL\_SEGMENT\_LIST\_MISSING | The [`azElSegmentList`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegments.html) field is missing | 
| INSUFFICIENT\_TIME\_AZ\_EL | No [`TimeAzEl`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html) fields were present in at least one [`azElSegmentList`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegments.html) | 

### Invalid Reason: `TIME_RANGE_INVALID`
<a name="w2aac74c19c15b7"></a>

 These errors occur when the ephemeris contains invalid time ranges, including issues with start/end times, segment ordering, overlapping segments, or temporal inconsistencies. 


| Error Code | Error Message | 
| --- | --- | 
| START\_TIME\_IN\_FUTURE | Ephemeris start time is in the future, but must be in the past | 
| END\_TIME\_IN\_PAST | Ephemeris end time is in the past, but must be in the future | 
| EXPIRATION\_TIME\_TOO\_EARLY | The provided expiration time is earlier than the ephemeris end time | 
| START\_TIME\_METADATA\_TOO\_EARLY | The START\_TIME metadata value is earlier than the earliest time present in the OEM ephemeris data | 
| STOP\_TIME\_METADATA\_TOO\_LATE | The STOP\_TIME metadata value is later than the latest time present in the OEM ephemeris data | 
| AZ\_EL\_SEGMENT\_END\_TIME\_BEFORE\_START\_TIME | The [`endTime`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ISO8601TimeRange.html) of at least one data segment is before the segment's [`startTime`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ISO8601TimeRange.html) | 
| AZ\_EL\_SEGMENT\_TIMES\_OVERLAP | The time range of at least one segment overlaps with other segment time ranges | 
| AZ\_EL\_SEGMENTS\_OUT\_OF\_ORDER | The segments are not temporally ordered | 
| TIME\_AZ\_EL\_ITEMS\_OUT\_OF\_ORDER | The [`TimeAzEl`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html) items within a [`AzElSegment`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegment.html) must be temporally in order | 
| AZ\_EL\_SEGMENT\_REFERENCE\_EPOCH\_INVALID | The reference epoch for a segment is invalid or incorrectly formatted | 
| AZ\_EL\_SEGMENT\_START\_TIME\_INVALID | The start time in a segment's valid time range does not start after the first segment | 
| AZ\_EL\_SEGMENT\_END\_TIME\_INVALID | The end time in a segment's valid time range does not end after the last segment | 
| AZ\_EL\_SEGMENT\_VALID\_TIME\_RANGE\_INVALID | The valid time range for a segment is invalid | 
| AZ\_EL\_SEGMENT\_END\_TIME\_TOO\_LATE | The end time of a segment exceeds the maximum allowed duration from the reference epoch | 
| AZ\_EL\_TOTAL\_DURATION\_EXCEEDED | The total duration across all segments exceeds the maximum allowed pointing angle duration | 

### Invalid Reason: `TRAJECTORY_INVALID`
<a name="w2aac74c19c15b9"></a>

 These errors occur when the ephemeris contains invalid trajectory data, including issues with orbital parameters, angle ranges, or units. 


| Error Code | Error Message | 
| --- | --- | 
| MEAN\_MOTION\_INVALID | The mean motion of the provided TLE ephemeris differs too greatly from the most recent reference ephemeris. Note: Ground Station uses Space-Track ephemerides as a reference during validation | 
| TIME\_AZ\_EL\_AZ\_RADIAN\_RANGE\_INVALID | AzEl [`az`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html) must be greater than or equal to -π and less than or equal to 2π radians | 
| TIME\_AZ\_EL\_EL\_RADIAN\_RANGE\_INVALID | AzEl [`el`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html) must be greater than or equal to -π/2 and less than or equal to π/2 radians | 
| TIME\_AZ\_EL\_AZ\_DEGREE\_RANGE\_INVALID | AzEl [`az`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html) must be greater than or equal to -180 and less or equal to 360 degrees | 
| TIME\_AZ\_EL\_EL\_DEGREE\_RANGE\_INVALID | AzEl [`el`](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html) must be greater than or equal to -90 degrees and less than or equal to 90 degrees | 
| TIME\_AZ\_EL\_ANGLE\_UNITS\_INVALID | Invalid AzEl angle units | 

### Invalid Reason: `KMS_KEY_INVALID`
<a name="w2aac74c19c15c11"></a>

 These errors occur when there are issues with the AWS Key Management Service (KMS) key used to encrypt the ephemeris data. 


| Error Code | Error Message | 
| --- | --- | 
| INSUFFICIENT\_KMS\_PERMISSIONS | Ground Station does not have sufficient permissions to access this ephemeris' KMS key | 

### Invalid Reason: `VALIDATION_ERROR`
<a name="w2aac74c19c15c13"></a>

 These errors occur when there are general validation issues with the ephemeris data that don't fall into the other specific categories. 


| Error Code | Error Message | 
| --- | --- | 
| INTERNAL\_ERROR | Internal error occurred during ephemeris validation | 
| FILE\_FORMAT\_INVALID | The ephemeris file format is invalid or corrupted. Verify the file conforms to the expected format for the ephemeris type | 