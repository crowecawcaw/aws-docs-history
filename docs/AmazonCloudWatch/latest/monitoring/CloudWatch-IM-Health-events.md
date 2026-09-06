

# View health events and metrics in Internet Monitor (Health events page)
<a name="CloudWatch-IM-Health-events"></a>

The **Health events** page in the Internet Monitor console provides a map of health events that impact the client locations and ASNs for your application. You can click circles on the map for more details about an event. The **Health events** tables lists locations that have been impacted by an event, and specifics about the impact.

**Internet traffic overview**  
The **Internet traffic overview** map shows you the internet traffic and health events that are specific to the locations and ASNs that your clients access your application from. The countries that are gray on the map are those that include traffic for your application.   
Each circle on the map indicates a health event in an area, for a time period that you select. Internet Monitor creates health events when it detects a problem, at a specific (but customizable) threshold, with connectivity between one of your resources hosted in AWS and a city-network where a client is accessing your application.  
Choose a circle on the map to display more details about the health event for that location. In addition, for clusters that have health events, you can see detailed information in the **Health events** table below the map.  
Note that Internet Monitor creates health events in a monitor when it determines that an event has significant impact on your application. The map is blank if there aren't any health events that exceed the threshold for impact on traffic for your client locations in the time period that you've selected. For more information, see [When Internet Monitor creates and resolves health events](CloudWatch-IM-inside-internet-monitor.md#IMHealthEventStartStop).

**Health events**  
The **Health events** table lists client locations that have been affected by health events, along with information about the events. The following columns are included in the table.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-Health-events.html)
If you choose one of the client locations in the **Health events** table, you can see more details about the health event at that location. For example, you can see when the event started, when it ended, and the local traffic impact.

**Network path visualization**  
If Internet Monitor has finished impairment analysis for an event, you can view **Network path visualization** to see the full network path for traffic to a client location. The full path shows you each node along the network path for your application for the health event, between the AWS location and the client, for a client-location pair.  
When Internet Monitor has determined the cause of an impairment, Internet Monitor adds a dashed red circle around the node. Impairments can be caused by ASNs, typically internet service providers (ISPs), or the cause can be AWS. If there were multiple causes for an impairment, multiple nodes are circled.