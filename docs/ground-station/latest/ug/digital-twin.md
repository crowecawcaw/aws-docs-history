# Use the AWS Ground Station digital twin feature

The digital twin feature for AWS Ground Station provides you with an environment where you can test and
integrate your satellite mission management and command and control software. The digital twin feature allows you to test
scheduling, verification of configurations, and proper error handling without using production
antenna capacity. Testing your AWS Ground Station integration with the digital twin feature enables you to have increased confidence in
your system's ability to manage your satellite operations smoothly. It also allows you to test AWS Ground Station APIs
without using production capacity or requiring spectrum licensing.

To get started, follow [Onboard satellite](getting-started.md "getting-started.md"),
requesting to be onboarded to the digital twin feature. Once your satellite is onboarded to the digital twin feature, you can schedule
contacts against digital twin ground stations. The list of ground stations that you have access to can be retrieved
via the AWS SDK [ListGroundStations](../APIReference/API_ListGroundStations.md "../APIReference/API_ListGroundStations.md") response. Digital twin ground stations are exact copies of the ground stations listed in
[AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md")
with a modifying prefix to Ground Station Name of “Digital Twin ”. This includes their antenna capabilities and metadata,
including, but not limited to, site mask and actual GPS coordinates. At this time, the digital twin feature does not support data
delivery as described in [Work with dataflows](dataflows.md "dataflows.md").

Once onboarded, the digital twin feature emits the same Amazon EventBridge events and API responses as the production service as
described in [Automate AWS Ground Station with
Events](monitoring.md "monitoring.md").
These events will allow you to fine tune your configurations and dataflow endpoint groups.
