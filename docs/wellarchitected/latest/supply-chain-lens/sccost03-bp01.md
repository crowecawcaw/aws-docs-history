# SCCOST03-BP01 Compress and aggregate data whenever possible to reduce the amount of data that needs to be transmitted over the network

Maximizing processing and sanitation of data reduces the
amount of data to be sent and processed in the cloud, leading to
significant cost savings and improved performance.

**Desired outcome:** A well-defined
strategy on where data gets processed and transmitted to reduce
unnecessary load on the network and cloud

**Benefits of establishing this best
practice:** Reduced cost, optimized performance, and
better customer satisfaction

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Maximize processing and sanitation of the data in-situ, to
reduce the amount of data to be sent and processed in the cloud.
AWS IoT Greengrass v2 can help with processing and summarization
of data at the edge, while implementing data filtering and
aggregation at the edge using AWS IoT Core rules engine or AWS IoT Greengrass v2 components to send only relevant, summarized
data to the cloud. 

### Implementation steps

1. Identify data processing opportunities at the edge to
   reduce the volume of data transmitted to the cloud.
2. Deploy AWS IoT Greengrass v2 for local data processing,
   filtering, and aggregation at manufacturing facilities.
3. Implement data compression techniques and Combine multiple
   measurements into single messages to reduce transmission
   costs.
4. Configure AWS IoT Core rules engine to filter and route
   only relevant data to cloud storage and processing
   systems.
5. Establish data summarization processes that aggregate
   detailed operational data into meaningful insights before
   cloud transmission.
6. Monitor network usage and data transmission costs to
   continuously optimize edge processing strategies.
