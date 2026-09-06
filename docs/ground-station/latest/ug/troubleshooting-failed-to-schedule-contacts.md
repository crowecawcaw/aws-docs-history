

# Troubleshoot FAILED\_TO\_SCHEDULE contacts
<a name="troubleshooting-failed-to-schedule-contacts"></a>

 A contact will end in a **FAILED\_TO\_SCHEDULE** state when AWS Ground Station detects an issue either with your resource configuration or within the internal system. A contact that ends in a **FAILED\_TO\_SCHEDULE** state will optionally provide an `errorMessage` for additional context. For information about describing contacts, see the [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html) API. 

 The common use cases that can cause **FAILED\_TO\_SCHEDULE** contacts are provided below, along with steps to help troubleshoot. 

**Note**  
 This guide is specifically for the **FAILED\_TO\_SCHEDULE** contact status - and is not intended for other failure statuses, such as **AWS\_FAILED**, **AWS\_CANCELLED**, or **FAILED**. For more information on contact statuses, see [AWS Ground Station contact statuses](contacts.lifecycle.md#contact-statuses) 

## The settings specified in your Antenna Downlink Demod Decode Config are not supported
<a name="unmatched-demod-decode"></a>

The [mission profile](how-it-works-mission-profile.md) that was used to schedule this contact had an [antenna-downlink-demod-decode config](how-it-works.config.md#how-it-works.config-antenna-downlink-demod-decode) that was not valid. 

 **Previously existing AntennaDownlinkDemodDecode config**
+  If your antenna-downlink-demod-decode configs have recently been changed - roll back to a previously working version before attempting to schedule. 
+  If this was an intentional change on an existing config, or a previously existing config that is no longer successfully scheduling - follow the next step on how to onboard a new AntennaDownlinkDemodDecode config. 

 **Newly created AntennaDownlinkDemodDecode config**

Contact AWS Ground Station directly to onboard your new config. Create a case with [AWS Support](https://aws.amazon.com/support/createCase) including the `contactId` that ended in the **FAILED\_TO\_SCHEDULE** state

## General Troubleshooting Steps
<a name="additional-steps"></a>

If the preceding troubleshooting steps did not resolve your issue: 
+  Re-attempt scheduling the contact or schedule another contact using the same mission profile. For information about how to reserve a contact, see [ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html). 
+  If you continue to receive a **FAILED\_TO\_SCHEDULE** status for this mission profile, [contact AWS Support](https://aws.amazon.com/support/createCase) 