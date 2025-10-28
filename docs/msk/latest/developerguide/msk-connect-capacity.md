# Understand connector capacity

The total capacity of a connector depends on the number of workers that the connector
has, as well as on the number of MSK Connect Units (MCUs) per worker. Each MCU represents 1 vCPU
of compute and 4 GiB of memory. The MCU memory pertains to the total memory of a worker instance and not the heap memory in use.

MSK Connect workers consume IP addresses in the customer-provided subnets. Each worker uses one IP address from one of the customer-provided subnets. You should ensure that you have enough available IP addresses in the subnets provided to a CreateConnector request to account for their specified capacity, especially when autoscaling connectors where the number of workers can fluctuate.

To create a connector, you must choose between one of
the following two capacity modes.

- _Provisioned_ - Choose this mode if you know the capacity
  requirements for your connector. You specify two values:
  - The number of workers.
  - The number of MCUs per worker.

- _Autoscaled_ - Choose this mode if the capacity
  requirements for your connector are variable or if you don't know them in
  advance. When you use autoscaled mode, Amazon MSK Connect overrides your connector's
  `tasks.max` property with a value that is proportional to the
  number of workers running in the connector and the number of MCUs per worker.

You specify three sets of values:

    + The minimum and maximum number of workers.
    + The scale-in and scale-out percentages for CPU utilization, which is
     determined by the `CpuUtilization` metric. When the
     `CpuUtilization` metric for the connector exceeds the
     scale-out percentage, MSK Connect increases the number of workers that
     are running in the connector. When the `CpuUtilization`
     metric goes below the scale-in percentage, MSK Connect decreases the
     number of workers. The number of workers always remains within the
     minimum and maximum numbers that you specify when you create the
     connector.
    + The number of MCUs per worker.

For more information about workers, see [Understand MSK Connect workers](msk-connect-workers.md "msk-connect-workers.md"). To
learn about MSK Connect metrics, see [Monitoring Amazon MSK Connect](mkc-monitoring-overview.md "mkc-monitoring-overview.md").
