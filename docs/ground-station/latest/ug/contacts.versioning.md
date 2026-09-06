

# Update contacts and contact versioning
<a name="contacts.versioning"></a>

 AWS Ground Station supports updating contacts with a `SCHEDULED`, `PREPASS`, or `PASS` [contact status](contacts.lifecycle.md#contact-statuses). You can use the [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) API to specify an ephemeris override for a contact — including azimuth/elevation, OEM, or TLE tracking data — without cancelling and rescheduling it. This is useful for geosynchronous (GEO) satellite operations where you need to retask an antenna to a different satellite during a contact, or for Launch and Early Operations (LEOPs) where pointing adjustments are required. 

 Each time you reserve or update a contact, AWS Ground Station creates a new contact version. Contact versions provide a history of changes made to a contact and allow you to track the status of each update. 

## How contact versioning works
<a name="contacts.versioning.how-it-works"></a>

 When you call [ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html), AWS Ground Station creates the first version of the contact (version 1) and returns the `versionId` in the response. Each subsequent call to [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) creates a new version with an incremented version number. 

 The [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html) API returns the currently `ACTIVE` [contact version](#contacts.versioning.version-statuses), including version information in the `version` field of the response. The [ListContacts](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContacts.html) API also includes version information for each contact. 

 To view a specific version of a contact, use the [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) API. To list all versions of a contact, use the [ListContactVersions](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContactVersions.html) API. 

## Updating a contact
<a name="contacts.versioning.update-contact"></a>

 You can call [UpdateContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateContact.html) when a contact is in the SCHEDULED, PREPASS, or PASS state. The API accepts the following parameters: 
+ **contactId** — The identifier of the contact to update.
+ **clientToken** — An idempotency token that ensures the request is processed only once. If you retry a request with the same client token, AWS Ground Station returns the original response without performing the update again. Many AWS SDKs automatically generate a client token for you if one is not provided.
+ **trackingOverrides** — The new tracking configuration for the contact. This includes program track settings (azimuth/elevation, TLE, or OEM ephemeris).
+ **satelliteArn** — The ARN of the satellite for the contact. When changing the target satellite along with the program track settings, provide the ARN of the new satellite. Only customers approved for azimuth/elevation pointing angles can set this value to null. All other customers must include the satellite ARN of the contact.

**Important**  
 The `UpdateContact` API applies all parameters in the request. Any parameter that is omitted or explicitly set to null is treated as a request to clear that value, not to leave it unchanged. For example, if you provide `trackingOverrides` but omit `satelliteArn`, the satellite ARN is cleared. Make sure to include all desired values in each update request. 

 You can change the target satellite during a contact by providing a new `satelliteArn` along with the corresponding `trackingOverrides`. The new satellite must be visible from the ground station for the duration of the contact, because the contact start and end time do not change with this API. The new satellite must also be onboarded to the ground station and have the licensing required by the mission profile. The mission profile of the contact cannot be changed, so switching satellites is only applicable when both satellites use the same mission profile. 

**Important**  
 The `UpdateContact` API does not support changing the start time, end time, or mission profile of a contact. To change these values, cancel the contact and reserve a new one. The `UpdateContact` API is designed for retasking the antenna pointing configuration, such as switching between satellites or updating ephemeris data. 

**Important**  
 The `UpdateContact` API does not support contacts that have a mission profile that uses [Antenna Downlink Demod Decode Config](how-it-works.config.md#how-it-works.config-antenna-downlink-demod-decode) configs. To change the configuration of these contacts, cancel the contact and reserve a new one. 

 The `UpdateContact` API returns the `contactId` and the new `versionId`. The update is processed asynchronously. Use [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) to check the status of the update. Some AWS SDKs and the AWS Command Line Interface provide a `ContactUpdated` waiter that polls until the version reaches ACTIVE or FAILED\_TO\_UPDATE status. 

**Note**  
 Only one update can be in progress at a time. If the latest contact version is in the UPDATING state, the API returns a `ConflictException`. Wait for the current update to reach ACTIVE or FAILED\_TO\_UPDATE status before submitting another update. 

## Contact version statuses
<a name="contacts.versioning.version-statuses"></a>

Each contact version has one of the following statuses:


| Status | Description | 
| --- | --- | 
| UPDATING | The version is being applied to the contact. The update has been submitted and is being processed by AWS Ground Station. | 
| ACTIVE | The version is the currently active configuration for the contact. The ground station is using this version's settings. | 
| SUPERSEDED | The version was previously active but has been replaced by a newer version. | 
| FAILED\_TO\_UPDATE | The update could not be applied. The contact reverts to the previously active version. Check the failureCodes and failureMessage fields for details. | 

## Code examples
<a name="contacts.versioning.examples"></a>

 The following examples demonstrate how to use the contact versioning APIs with the AWS SDK for Python (Boto3). 

### Example: Update a contact
<a name="contacts.versioning.examples.update-contact"></a>

 The following example updates a contact with new tracking overrides and waits for the update to complete using the Boto3 `ContactUpdated` waiter. 

```
import boto3
import uuid

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# The contact ID of an existing scheduled contact to update
contact_id = "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"

# Generate a unique client token for idempotency.
# If you retry the same request with the same client token,
# the API returns the same response without creating a duplicate version.
client_token = str(uuid.uuid4())

# Update the contact to use a different TLE ephemeris for tracking.
# The UpdateContact API applies all parameters in the request.
# Any parameter set to null is treated as a request to clear that value,
# not to leave it unchanged. Include all desired values in each request.
print(f"Updating contact {contact_id}...")

update_response = ground_station_client.update_contact(
    contactId=contact_id,
    clientToken=client_token,
    satelliteArn="arn:aws:groundstation::111122223333:satellite/a88611b0-f755-404e-b60d-57d8aEXAMPLE",
    trackingOverrides={
        "programTrackSettings": {
            "tle": {"ephemerisId": "b2c3d4e5-6789-01ab-cdef-EXAMPLE22222"}
        }
    },
)

contact_id = update_response["contactId"]
version_id = update_response["versionId"]
print(f"Update submitted. Contact: {contact_id}, Version: {version_id}")

# Wait for the update to complete using the ContactUpdated waiter.
# The waiter polls DescribeContactVersion until the version reaches
# ACTIVE (success) or FAILED_TO_UPDATE (failure) status.
# The waiter raises WaiterError if the version reaches FAILED_TO_UPDATE
# or if MaxAttempts is exceeded, so we use try/except to handle both cases.
print("Waiting for update to complete...")

from botocore.exceptions import WaiterError

waiter = ground_station_client.get_waiter("contact_updated")

try:
    waiter.wait(
        contactId=contact_id,
        versionId=version_id,
        WaiterConfig={
            "Delay": 5,
            "MaxAttempts": 180,
        },
    )
    print(f"Contact updated successfully. Version {version_id} is now active.")
except WaiterError as e:
    # WaiterError is raised when the version reaches FAILED_TO_UPDATE
    # or when MaxAttempts is exceeded. Retrieve the current version to inspect.
    version_response = ground_station_client.describe_contact_version(
        contactId=contact_id,
        versionId=version_id,
    )
    version_status = version_response["version"]["status"]
    if version_status == "FAILED_TO_UPDATE":
        failure_codes = version_response["version"].get("failureCodes", [])
        failure_message = version_response["version"].get("failureMessage", "")
        print(f"Update failed. Codes: {failure_codes}, Message: {failure_message}")
    else:
        print(f"Waiter timed out. Current version status: {version_status}. Error: {e}")
```

### Example: Describe a contact version
<a name="contacts.versioning.examples.describe-contact-version"></a>

 The following example retrieves the details of a specific contact version, including its status, configuration, and any failure information. 

```
import boto3

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

contact_id = "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
version_id = 2

# Describe a specific version of a contact.
# Use this API to check the status of an update or to view the
# configuration that was active at a specific point in time.
print(f"Describing version {version_id} of contact {contact_id}...")

response = ground_station_client.describe_contact_version(
    contactId=contact_id,
    versionId=version_id,
)

# Display version details
version = response["version"]
print(f"Version ID: {version['versionId']}")
print(f"Status: {version['status']}")
print(f"Created: {version.get('created', 'N/A')}")

if version.get("activated"):
    print(f"Activated: {version['activated']}")

if version.get("superseded"):
    print(f"Superseded: {version['superseded']}")

# Display contact details for this version
print(f"\nContact ID: {response['contactId']}")
print(f"Contact Status: {response['contactStatus']}")
print(f"Ground Station: {response['groundStation']}")
print(f"Start Time: {response['startTime']}")
print(f"End Time: {response['endTime']}")

if response.get("satelliteArn"):
    print(f"Satellite ARN: {response['satelliteArn']}")

if response.get("trackingOverrides"):
    print(f"Tracking Overrides: {response['trackingOverrides']}")

# Check for failure details if the version failed to update
if version["status"] == "FAILED_TO_UPDATE":
    failure_codes = version.get("failureCodes", [])
    failure_message = version.get("failureMessage", "")
    print(f"\nFailure Codes: {failure_codes}")
    print(f"Failure Message: {failure_message}")
```

### Example: List contact versions
<a name="contacts.versioning.examples.list-contact-versions"></a>

 The following example lists all versions of a contact to view the full history of changes, using pagination to handle large result sets. 

```
import boto3

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

contact_id = "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"

# List all versions of a contact to view the full history of changes.
# Results are paginated. Use the nextToken to retrieve additional pages.
print(f"Listing versions for contact {contact_id}...")

paginator = ground_station_client.get_paginator("list_contact_versions")
page_iterator = paginator.paginate(
    contactId=contact_id,
    PaginationConfig={
        "MaxItems": 100,
        "PageSize": 20,
    },
)

for page in page_iterator:
    for version in page["contactVersionsList"]:
        version_id = version["versionId"]
        status = version["status"]
        created = version.get("created", "N/A")

        print(f"  Version {version_id}: status={status}, created={created}")

        if version.get("activated"):
            print(f"    Activated: {version['activated']}")

        if version.get("superseded"):
            print(f"    Superseded: {version['superseded']}")

        if status == "FAILED_TO_UPDATE":
            failure_codes = version.get("failureCodes", [])
            failure_message = version.get("failureMessage", "")
            print(f"    Failure Codes: {failure_codes}")
            print(f"    Failure Message: {failure_message}")

        if status == "UPDATING":
            print(f"    Update is currently in progress.")
```

## Considerations
<a name="contacts.versioning.considerations"></a>
+  Contacts created before the contact versioning feature was introduced do not have version information. Calling [DescribeContactVersion](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContactVersion.html) or [ListContactVersions](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContactVersions.html) for these contacts returns a `ResourceNotFoundException`. 
+  When you update the tracking overrides of an in-progress contact, there is a brief transition period while the antenna adjusts to the new pointing configuration. During this time, signal reception or transmission may be interrupted. 
+  Contact versions cannot be deleted. Use [ListContactVersions](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListContactVersions.html) to view the full history of changes made to a contact. 
+  The `UpdateContact` API can only be called from the scheduling region of the contact. 