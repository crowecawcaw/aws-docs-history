# I/O bandwidth

I/O bandwidth is the rate at which the CPU reads from input or writes
to output through a network interface card. Therefore, network inputs and
outputs affect I/O bandwidth. SDI inputs don't affect I/O bandwidth.

## Impact of I/O bandwidth

issues

Lack of the required input bandwidth typically results in dropped
frames in the output encodes.

You might not notice output bandwidth problems in Elemental Live. Instead, the downstream systems
will notice the problem.

## Measuring I/O bandwidth

- To measure I/O bandwidth on an Ethernet card, use the
  `iftop` command. This command shows the bandwidth for one
  card over a range of time (the last 2 seconds, 10 seconds, and 40
  seconds). It also shows a running total of bandwidth used since you
  entered the `iftop` command.

Enter the `iftop` command. For example, to show the results for `eth0`,
enter this command:

```
[elemental@encoder ~]$ sudo iftop -t -i eth0
```

To stop collecting data, press **Ctrl-C**.

- To measure I/O bandwidth on a Mellanox card, use the `mlnx_perf`
  command.

Following are the expected bandwidths on the Mellanox card:

    + Workflows with SMPTE 2110 inputs or outputs, and workflows with
     SMPTE 2022-6 inputs require a Mellanox card. This card has a declared
     maximum bandwidth of 25 Gbps. In practice, the maximum bandwidth (using
     the latest versions of Elemental Live) is as follows:
    + For SMPTE 2110 workflows, expect approximately 24.5 Gbps per
     Mellanox port.

## Expected bandwidth for

individual workflows

The following table illustrates the difference in bandwidth that's required for two
different inputs (SMPTE 2110 and SMPTE 2022-6) with two different output resolutions (HD and
4K).

Notice that the 4K output requires approximately four times as much
bandwidth as the HD output.

| Type of input           | Resolution of the output | Expected bandwidth (Gbps) for the workflow |
| ----------------------- | ------------------------ | ------------------------------------------ |
| SMPTE 2110 (video only) | HD (1080p60)             | 2.6                                        |
| 4Kp60                   | 10.5                     |
| SMPTE 2022-6            | 1080p60                  | 3                                          |
| 4Kp60                   | 12                       |
