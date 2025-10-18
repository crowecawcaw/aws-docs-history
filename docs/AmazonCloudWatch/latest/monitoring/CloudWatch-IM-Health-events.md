# View health events and metrics in Internet Monitor (Health events page)

The **Health events** page in the Internet Monitor console provides a map of health events that
 impact the client locations and ASNs for your application. You can click circles on the map for more details
 about an event. The **Health events** tables lists locations that have been impacted by
 an event, and specifics about the impact.



**Internet traffic overview**
The **Internet traffic overview** map shows you the 
 internet traffic and health events that are specific to the locations and ASNs that your clients access your 
 application from. The countries that are gray on the map are those that include traffic for your application. 


Each circle on the map indicates a health event in an area, for a time period that you select. Internet Monitor creates health 
 events when it detects a problem, at a specific (but customizable) threshold, with connectivity between one of 
 your resources hosted in AWS and a city-network where a client is accessing your application.


Choose a circle on the map to display more details about the health event for that location. In addition, 
 for clusters that have health events, you can see detailed information in the **Health events** 
 table below the map.


Note that Internet Monitor creates health events in a monitor when it determines that an event has significant
 impact on your application. The map is blank if there aren't any health events that exceed the threshold for 
 impact on traffic for your client locations in the time period that you've selected. For more information, 
 see [When Internet Monitor creates and resolves health events](CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop "CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop").


**Health events**
The **Health events** table lists client locations that have been affected by health events, along with
 information about the events. The following columns are included in the table.




| Column | Description |
| --- | --- |
| Event type | Specifies whether current events are *overall* health events or *local* health events, or if the health event is in the *past*. |
| Client location | The location of the end users who were impacted by the event, who experienced increased latency or reduced availability. To learn more about client location accuracy in Internet Monitor, see [Geolocation information and accuracy in Internet Monitor](CloudWatch-IM-inside-internet-monitor.md#IMGeolocationSourceAccuracy "CloudWatch-IM-inside-internet-monitor.md#IMGeolocationSourceAccuracy"). |
| ISP name (ASN) | The network that the traffic traveled over. Typically, this is the internet service provider (ISP) or Autonomous System Number (ASN) for the network traffic. |
| Service location | The AWS location for the network traffic, which can be an AWS Region or an internet edge location. |
| Traffic impact | How much impact was caused by the event, in increased latency or reduced availability. For latency, this is the percentage of how much latency increased during the event compared to typical performance for traffic, from this client location to this AWS location using this client network. |
| Impact type | The type of impact for the health event. Health events are typically caused by latency increases (performance issues) or reachability (availability issues). You might also be able to click on the impact type to see the cause of the impairment. When possible, Internet Monitor analyzes the origin of a health event, to determine whether it was caused by AWS or an ASN (internet service provider). Note that this analysis continues after the event is resolved. Internet Monitor can update events with new information for up to an hour. | If you choose one of the client locations in the **Health events** table, you can see more details about the health event at that location. For example, you can see when the event started, when it ended, and the local traffic impact. **Network path visualization** If Internet Monitor has finished impairment analysis for an event, you can view **Network path visualization** to see the full network path for traffic to a client location. The full path shows you each node along the network path for your application for the health event, between the AWS location and the client, for a client-location pair. When Internet Monitor has determined the cause of an impairment, Internet Monitor adds a dashed red circle around the node. Impairments can be caused by ASNs, typically internet service providers (ISPs), or the cause can be AWS. If there were multiple causes for an impairment, multiple nodes are circled.
