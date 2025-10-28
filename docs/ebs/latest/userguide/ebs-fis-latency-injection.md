# Latency injection

Use the Latency Injection action (`aws:ebs:volume-io-latency`) in AWS FIS to simulate elevated
I/O latency on your Amazon EBS volumes to test how your applications respond to storage performance degradation.
This action allows you to specify the latency value to be injected as well as the percentage of I/O that
will be impacted on the target volume. With AWS FIS, you can use pre-configured latency experiment templates
to get started with testing different I/O latency patterns that may be observed during storage faults.
These templates are designed as an initial set of scenarios you can use to introduce disruptions to your
applications to test resiliency. They are not designed to encompass all types of impact your applications
can experience in the real world. We recommend that you to adapt them to run multiple different tests based
on the performance needs of your applications. You can customize the available templates or create new
experiment templates to test for your application specific requirements.

###### Pre-configured latency experiment templates

Amazon EBS provides the following latency experiment templates through the EBS Console and the [AWS FIS scenario library](../../../fis/latest/userguide/scenario-library-scenarios.md "../../../fis/latest/userguide/scenario-library-scenarios.md").
You can directly use these templates on your target volumes to run a latency injection experiment.

- **Sustained Latency** — Simulates constant latency. This experiment
  utilizes one latency injection action and has a total duration of 15 minutes. This experiment simulates
  persistent latency on 50 percent of read I/O and 100 percent of write I/O: 500 ms for 15 minutes.
- **Increasing Latency** — Simulates gradually increasing latency.
  This experiment utilizes five latency injection actions and has a total duration of 15 minutes. This
  experiment will simulate a gradual increase in latency on 10 percent of read I/O and 25 percent of write
  I/O: 50 ms for 3 minutes, 200 ms for 3 minutes, 700 ms for 3 minutes, 1 second for 3 minutes, and 15
  seconds for 3 minutes.
- **Intermittent Latency** — Simulates sharp intermittent latency
  spikes with periods of recovery in between. This experiment utilizes three latency injection actions
  and has a total duration of 15 minutes. This experiment will simulate three latency spikes on 0.1 percent of
  read and write I/O: 30 second spike that lasts for 1 minute, 10 second spike that lasts for 2 minutes,
  and 20 second spike that lasts for 2 minutes. There will be 5 minute periods of recovery between each
  latency spike.
- **Decreasing Latency** — Simulates gradually decreasing latency.
  This experiment utilizes five latency injection actions and has a total duration of 15 minutes. This
  experiment will simulate a gradual decrease in latency on 10 percent of read I/O and write I/O: 20 seconds
  for 3 minutes, 5 seconds for 3 minutes, 900 ms for 3 minutes, 300 ms for 3 minutes, and 40 ms for 3
  minutes.

###### Customize preconfigured scenarios

You customize the preconfigured templates above or create your own new experiment templates using the
following customizable parameters.

- `readIOPercentage` — Percentage of read I/O operations that latency will be injected
  on. This is the percentage of all read I/O operations on the volume that will be impacted by the action.

Range: Min 0.1%, Max 100%

- `readIOLatencyMilliseconds` — Amount of latency injected on read I/O operations.
  This is the latency value that will be observed on the specified percentage of the read I/O during the
  experiment.

Range: Min 1 ms (io2) / 10 ms (non-io2), Max 60 seconds

- `writeIOPercentage` — Percentage of write I/O operations that latency will be injected
  on. This is the percentage of all write I/O operations on the volume that will be impacted by the action.

Range: Min 0.1%, Max 100%

- `writeIOLatencyMilliseconds` — Amount of latency injected on write I/O operations.
  This is the latency value that will be observed on the specified percentage of the write I/O during
  the experiment.

Range: Min 1ms (io2) / 10ms (non-io2), Max 60 seconds

- `duration` — Duration for which the latency will be injected on the percentage
  of I/O selected.

Range: Min 1 second, Max 12 hours

###### Monitoring latency injection

You can monitor the performance impact on your volumes in the following ways:

- Use average latency metrics in CloudWatch to get per-minute average I/O latency. For more
  information, see [Monitor your EBS volumes using CloudWatch](using_cloudwatch_ebs.md "using_cloudwatch_ebs.md").
- Use EBS detailed performance statistics available through NVMe-CLI, CloudWatch agent, and
  Prometheus to get per-second average I/O latency. The detailed metrics also provide I/O latency
  histograms that you can use to analyze latency variance on your volumes. For more information,
  see [NVMe detailed performance statistics](nvme-detailed-performance-stats.md "nvme-detailed-performance-stats.md").
- Use the [Amazon EBS volume status checks](monitoring-volume-checks.md "monitoring-volume-checks.md").
  When you inject I/O latency, the volume's status transitions to the `warning` state.

###### Considerations

Consider the following when using EBS latency injection:

- Latency injection is supported on all [Nitro-based instance types](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md"), except:
  P4d, P5, P5e, Trn2u, G6, G6f, Gr6, Gr6f, M8i, M8i-flex, C8i-flex, R8i, R8i-flex, I8ge, Mac-m4pro,
  and Mac-m4.
- You might see up to 5 percent variance in the latency value specified in the experiment and the
  resultant latency observed.
- If you drive a very small number of I/O operations, the percentage of I/O specified in the
  action parameters might not match the actual percentage of I/O impacted by the action.

###### To run a latency injection experiment on an Amazon EBS volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volumes on which to run the experiment and choose **Actions**,
   **Resilience testing**, **Inject volume I/O latency**.

The AWS Fault Injection Service console opens. 4. In the **Create experiment** window, select the type of experiment to run:
**Intermittent**, **Increasing**, **Sustained**,
or **Decreasing**. 5. For **IAM role selection**, choose **Create a new role** to create
a new role that AWS FIS will use to conduct the experiments on your behalf. Alternatively, choose
**Use an existing IAM role** if you previously created an IAM role with the required
permissions. 6. The **Pricing estimate** section gives you an estimate of the cost of running the
experiment. With AWS FIS, you are charged per minute that an action runs, from start to finish, based
on the number of target accounts for your experiment. 7. Choose **Start experiment**.
