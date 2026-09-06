

# How AWS Ground Station works
<a name="how-it-works"></a>

 AWS Ground Station operates ground-based *antennas* to facilitate communication with your *satellite*. The physical characteristics of what the antennas can do are abstracted and are referred to as *capabilities*. The physical location of the antenna along with its current capabilities can be referenced in the [AWS Ground Station Locations](aws-ground-station-antenna-locations.md) section. Please contact us through the [AWS Support Center Console](https://console.aws.amazon.com/support) if your use case requires additional capabilities, additional location offerings, or more precise antenna locations. 

 To use one of the AWS Ground Station antennas you must reserve a time at a specific location. This reservation is referred to as a *contact*. To successfully schedule a contact, AWS Ground Station requires additional data to ensure its success. 
+  **Your satellite must be onboarded to one or more locations** – This ensures you have approval to operate the various capabilities at the requested location. 
+  **Your satellite must have a valid *ephemeris*** – This ensures the antennas have line of sight and can accurately point at your satellite during the contact. 
+  **You must have a valid *mission profile*** – This allows you to customize how this contact will behave including how you will receive and send data to your satellite. You may utilize multiple mission profiles for the same vehicle to create different contacts to fit different operating postures or scenarios you encounter. 

## Satellite onboarding
<a name="how-it-works.onboarding"></a>

 Onboarding a satellite into AWS Ground Station is a multistep process involving data collection, technical validation, spectrum licensing, with integration and testing. The [Satellite onboarding](getting-started.step1.md) section of the guide will walk you through this process. 

## Mission profile composition
<a name="how-it-works.mission-profile"></a>

 The satellite frequency information, [data plane](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html) information, and other details are encapsulated into a mission profile. The mission profile is a collection of *config* components. This allows you to reuse config components across different mission profiles as suits your use case. Since mission profiles don't directly reference individual satellites, but instead only have information about their technical capabilities, mission profiles can also be reused by multiple satellites that have the same configuration. 

 A valid mission profile will have a *tracking config* and one or more *dataflows*. The tracking config will specify your preference for tracking during a contact. Each config pair within a dataflow establishes a source and destination. Depending on your satellite and its operational modes, the exact number of dataflows will vary in a mission profile to represent your uplink and downlink communication paths as well as any data processing aspects. 
+  For more information on configuring your Amazon VPC, Amazon S3, and Amazon EC2 resources that will be used during a contact, see [Work with dataflows](dataflows.md). 
+  For details on how each config behaves, see [Use AWS Ground Station Configs](how-it-works.config.md). 
+  For specific details on all parameters expected, see [Use AWS Ground Station Mission Profiles](how-it-works-mission-profile.md). 
+  For examples on how various mission profiles can be created to support your use case, see [Example mission profile configurations](examples.md). 

 The following diagram shows an example mission profile and additional resources needed. Note that the example shows a dataflow endpoint which is not needed for this mission profile, named *unusedEndpoint*, to demonstrate the flexibility. The example supports the following dataflows: 
+  Synchronous downlink of digital intermediate frequency data to an Amazon EC2 instance that you manage. Denoted by the name *digIfDownlink*. 
+  Asynchronous downlink of digital intermediate frequency data to an Amazon S3 bucket. Denoted by the bucket name *aws-groundstation-demo*. 
+  Synchronous downlink of demodulated and decoded data to an Amazon EC2 instance that you manage. Denoted by the name *demodDecodeDownlink*. 
+  Synchronous uplink of data from an Amazon EC2 instance that you manage to a AWS Ground Station managed antenna. Denoted by the name *digIfUplink*. 

 ![An example mission profile and additional resources needed.](http://docs.aws.amazon.com/ground-station/latest/ug/images/mission-profile-composition.png) 

## Contact scheduling
<a name="how-it-works.contact-scheduling"></a>

 With a valid mission profile, you can request a contact with your onboarded satellites. The contact reservation request is asynchronous to allow time for the global antenna service to achieve a consistent schedule across all AWS Regions involved. During this process, various antennas at the requested ground station location are evaluated to determine if they are available and capable to process the contact. During this process, your configured *dataflow endpoints* are also evaluated to determine their availability. While this evaluation is occurring, the contact status will be in SCHEDULING. 

 This asynchronous scheduling process will finish within five minutes of the request, but typically finishes within one minute. Please review [Automate AWS Ground Station with Events](monitoring.automating-events.md) for event-based monitoring during scheduling time. 

 ![The contact reservation request is asynchronous to allow time for the global antenna service to achieve a consistent schedule across all AWS Regions involved.](http://docs.aws.amazon.com/ground-station/latest/ug/images/scheduling.png) 

 Contacts which can be performed and have availability result in *SCHEDULED* contacts. With a scheduled contact, the resources which are needed to perform your contact have been reserved across the needed AWS Regions as defined by your mission profile. Contacts which cannot be performed, or have unavailable parts will result in *FAILED\_TO\_SCHEDULE* contacts. See [Troubleshoot FAILED\_TO\_SCHEDULE contacts](troubleshooting-failed-to-schedule-contacts.md) for debugging details. 

## Contact execution
<a name="how-it-works.contact-execution"></a>

 AWS Ground Station will automatically orchestrate your AWS managed resources during your contact reservation. If applicable, you are responsible for orchestrating EC2 resources defined by your mission profile as dataflow endpoints. AWS Ground Station provides [AWS EventBridge Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) for automating orchestration of your resources to reduce costs. See [Automate AWS Ground Station with Events](monitoring.automating-events.md) for more details. 

 During the contact, telemetry about your contact performance is delivered to AWS CloudWatch. For information about how to monitor your contact during execution, please see [Understand monitoring with AWS Ground Station](monitoring.md). 

 The following diagram continues the previous example by showing the same resources orchestrated during the contact. 

**Note**  
 Not all the antenna capabilities were used in this example. For instance, there are more than a dozen antenna downlink capabilities available at each antenna that support multiple frequencies and polarizations. For more details about the number of each capability type available from AWS Ground Station antennas, and their supported frequencies and polarizations, see [AWS Ground Station Site Capabilities](locations.capabilities.md). 

 ![Resources from the previous example orchestrated during the contact.](http://docs.aws.amazon.com/ground-station/latest/ug/images/contact-orchestration-simplified.png) 

 At the end of your contact, AWS Ground Station will assess the performance of your contact and will determine a final contact status. Contacts where no errors are detected will result in a *COMPLETED* contact status. Contacts where service errors have caused data delivery issues during the contact will result in an *AWS\_FAILED* status. Contacts where client or user errors have caused data delivery issues during the contact will result in a *FAILED* status. Errors outside a contact time, that is during pre-pass or post-pass, are not taken into account during the adjudication. 

 See [Understand contact lifecycle](contacts.lifecycle.md) for more information. 

## Digital twin
<a name="how-it-works.digital-twin"></a>

 The digital twin feature for AWS Ground Station allows you to schedule contacts against virtual ground station locations. These virtual ground stations are exact replicas of production ground stations including antenna capabilities, site masks, and actual GPS coordinates. The digital twin feature enables you to test your contact orchestration workflow for a fraction of the cost compared to production ground stations. See [Use the AWS Ground Station digital twin feature](digital-twin.md) for more information. 