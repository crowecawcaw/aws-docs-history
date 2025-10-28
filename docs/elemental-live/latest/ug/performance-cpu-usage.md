# CPU usage

CPU usage is the percentage of CPU power being used. CPU usage is
affected primarily by the complexity of the output encode.

## Measuring CPU usage from the command

line

To measure CPU usage, use one of these utilities:

- `top`, which is the default command line utility in the
  Linux operating system.
- `htop`, which is a Linux utility that you must install.

## Measuring CPU usage on the

web interface

The status bar at the top of the Elemental Live web interface includes a CPU usage
indicator. Hover over the indicator to view the percentage of CPU power that's being
used.

## Expected CPU usage for 4K

workflows

4K workflows can be run only on specific L8xx appliances. Don't run 4K
workflows on unsupported appliances.

When you monitor the CPU usage (using top or htop), you will notice
that the CPU load is always below the maximum. When you monitor core usage
(using htop), you will notice that the load for individual cores is also
below the maximum. However, do not assume that you can increase density.

The CPU on these appliances is optimized for 4K workflows. As the
event runs, there will be spikes in the CPU usage, due to the nature of a
4k workflow. Therefore, there must always be a buffer of CPU for these
peaks.

You might be able to add one more 4K encode if the appliance is
showing under the following CPU usage:

- 40% to 45% per CPU.

## Expected usage for SD and HD

workflows in L8xx appliances

With these workflows, the measured CPU usage is a good guide to the
possible number of events. You might be able to add one or more events if
the appliance is showing under the following CPU usage:

- 80–85% on GPU-based machines.
- 70% on CPU only encoders (L8xxx)

If you add more events, consider refining the encoding on the existing
events. See [Encoding parameters that affect
performance](performance-encoding-params.md "performance-encoding-params.md").
