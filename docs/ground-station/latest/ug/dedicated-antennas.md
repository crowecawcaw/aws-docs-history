

# AWS Ground Station Dedicated Antennas
<a name="dedicated-antennas"></a>

 AWS Ground Station Dedicated Antennas are custom-built antenna systems that AWS manages on your behalf. Unlike the public AWS Ground Station antennas where you share antenna time with other customers, a Dedicated Antenna provides you with dedicated access to an antenna built to your specifications. You can have one or more Dedicated Antennas. A Dedicated Antenna is connected to the global AWS network, and you interact with it using the same AWS Ground Station APIs and workflows that you use with public antennas, with the addition of enhanced visibility into antenna utilization. 

## What is a Dedicated Antenna
<a name="dedicated-antennas.overview"></a>

 A Dedicated Antenna is a physical antenna system that is custom-built for your organization and fully managed by AWS. You can have one or more Dedicated Antennas. A Dedicated Antenna differs from the public AWS Ground Station antennas in the following ways: 
+  **Custom-built** — A Dedicated Antenna is built to your specifications. The capabilities of a Dedicated Antenna are not limited to the capabilities of public antennas as described in [AWS Ground Station Site Capabilities](locations.capabilities.md). 
+  **Flexible location** — Dedicated Antennas are not restricted to existing AWS Ground Station antenna locations. A Dedicated Antenna can be connected to any existing AWS Region, including regions where AWS Ground Station is not currently available. You can work with AWS to determine the location and region that meet your requirements. 
+  **Dedicated access** — You have dedicated access to the antenna rather than sharing antenna time with other AWS Ground Station customers on a per-contact basis. 

 All AWS Ground Station antennas, including Dedicated Antennas, are fully managed by AWS. This includes maintenance and connectivity to the global AWS network. You interact with a Dedicated Antenna using the same AWS Ground Station APIs and workflows that you use with public antennas. You schedule contacts, configure mission profiles, and deliver data in the same way. 

 A Dedicated Antenna can be shared by multiple AWS accounts, where the customer who holds the Dedicated Antenna contract chooses which accounts to onboard. Each onboarded account can schedule contacts on the antenna independently, and has visibility into reservations across all accounts that share the antenna. 

 To learn more about Dedicated Antennas or to get started, contact AWS Support through the [AWS Support Center Console](https://console.aws.amazon.com/support). 

## Enhanced reservation visibility
<a name="dedicated-antennas.enhanced-visibility"></a>

 When you use the [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html) API against your Dedicated Antenna, you see additional information that is not available on public antennas. The following table summarizes the behavioral differences of the [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html) API for Dedicated Antennas in comparison to public AWS Ground Station antennas. 


| Behavior | Dedicated Antenna | Public antenna | 
| --- | --- | --- | 
| Your own contacts | Visible with full details, including contactId | Visible with full details, including contactId | 
| Other accounts' contacts | Visible with time slots only, without contactId | Not visible | 
| Maintenance windows | Visible with PLANNED or UNPLANNED maintenanceType | Not visible | 

 Maintenance windows represent periods when the antenna is unavailable for satellite communication. The `maintenanceType` field indicates whether the maintenance was `PLANNED` or `UNPLANNED`. When unplanned maintenance is scheduled, contacts that overlap with the maintenance window may be cancelled by AWS Ground Station. 

 When you view contacts from other AWS accounts that share your Dedicated Antenna, the reservation includes the time slot and antenna information, but the `contactId` is not included. 

**Important**  
 Enhanced reservation visibility applies only to your Dedicated Antenna. When you use public AWS Ground Station antennas, you have the same visibility as any other customer. You do not see maintenance windows or reservations from other accounts on public antennas. 

 For more information about listing reservations, see [View ground station reservations](locations.reservations.md). 

## Related resources
<a name="dedicated-antennas.additional-resources"></a>
+  [View ground station reservations](locations.reservations.md) 
+  [AWS Ground Station Locations](aws-ground-station-antenna-locations.md) 
+  [AWS Ground Station Site Capabilities](locations.capabilities.md) 
+  [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html) in the *AWS Ground Station API Reference* 