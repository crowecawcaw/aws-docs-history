# Game session queues in the Amazon GameLift Servers console

You can view information on all queues, which are used to process requests for new game sessions. The queues page
shows game session queues in the currently selected AWS Region. From the **Queues** page, you
can create a new queue, delete existing queues, or open a details page for a selected queue.
Each queue details page contains the queue's configuration and metrics data. For more
information about queues, see [Managing game session placement with Amazon GameLift Servers queues](queues-intro.md "queues-intro.md").

The queues page displays the following summary information for each queue. You can adjust the table content as needed using the **Preferences**
tool (see the ![Gear icon representing settings or configuration options.](images/settings.png)
icon in the upper right corner of the table). Custom preferences are saved to your AWS
account user and are automatically applied whenever you view this page.

- **Queue name** – The name assigned to the queue. Requests
  for new game sessions specify a queue by this name.
- **Queue timeout** – Maximum length of time, in seconds,
  that a game session placement request remains in the queue before timing out.
- **Destinations in queue** – Number of fleets listed in the
  queue configuration. Amazon GameLift Servers places new game sessions on any fleet in the
  queue.

## View queue details

You can access detailed information on any queue, including the queue configuration and
metrics. To open a queue details page, go to the **Queues** page and choose
a queue name.

The queue detail page displays a summary table and tabs containing additional information.
On this page you can do the following:

- Update the queue's configuration, list of destinations and player latency
  policies. Choose **Edit**.
- Delete a queue. After you delete a queue, all requests for new game sessions that
  reference that queue name will fail. Choose **Delete**.

###### Note

To restore a deleted queue, create a new queue with the deleted queue's
name.

### Details

###### Overview

The **Overview** section displays the queue's Amazon Resource
Name (**ARN**) and the **Timeout**. You can use
the ARN when referencing the queue in other actions or areas of Amazon GameLift Servers. The timeout
is the maximum length of time, in seconds, that a game session placement request
remains in the queue before timing
out.

###### Event notification

The **Event notification** section lists the **SNS
topic** Amazon GameLift Servers publishes event notifications to and the **Event
data** that is added to all events created by this queue.

###### Tags

The **Tags** table displays the keys and values used to tag the
resource. For more information about tagging, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

### Metrics

The **Metrics** tab shows a graphical representation of queue metrics
over time.

Queue metrics include a range of information describing placement activity across the
queue, including successful placements organized by Region. You can use Region data to
understand where you are hosting your games. Regional placement metrics can help to
detect issues with the overall queue design.

Queue metrics are also available in Amazon CloudWatch. For descriptions of available metrics,
see [Amazon GameLift Servers metrics for queues](monitoring-cloudwatch.md#gamelift-metrics-queue "monitoring-cloudwatch.md#gamelift-metrics-queue").

### Destinations

The **Destinations** tab shows all fleets or aliases listed for the
queue.

When Amazon GameLift Servers searches the destinations for available resources to host a new game
session, it searches the default order listed here. As long as there is capacity on the
first destination listed, Amazon GameLift Servers places new game sessions there. You can have individual
game session placement requests override the default order by providing player latency
data. This data tells Amazon GameLift Servers to search for an available destination with the lowest
average player latency. For more information about designing your queues, see [Customize a game session queue](queues-design.md "queues-design.md").

### Session placement

###### Player latency policies

The **Player latency policies** section shows all policies that
the queue uses. The tables lists the policies in the order they're enforced.

###### Locations

The **Locations** section shows the locations that this queue can
put a game session in.

###### Priority

The **Priority** section shows the order that the queue evaluates
a game sessions details.

###### Location order

The **Location order** section shows the default order that the
queue uses when placing game sessions. The queue uses this order if you haven't
defined other types of priority.
