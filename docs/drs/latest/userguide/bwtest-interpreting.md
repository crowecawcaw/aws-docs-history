

# Interpreting the result
<a name="bwtest-interpreting"></a>

Before you quote a figure, be clear about what it represents and what it does not.

## What the figure represents, and what it does not
<a name="bwtest-figure-meaning"></a>

**Important**  
If a proxy sits between this source server and AWS, treat the result as provisional. The test client might be routed through the proxy while the Elastic Disaster Recovery agent's replication connection is not, so a passing result does not confirm that replication can reach the replication server over that path.
+ The figure is the upper limit of the path, not the replication rate to expect. The Elastic Disaster Recovery agent compresses replicated data with LZ4 before sending it, so a compressible workload can move more disk bytes per second than this figure suggests. At the same time, the agent sends one ordered stream that the receiver reassembles in strict order across the five sockets, so a single stalled socket stalls the whole channel and replication usually runs below this figure.
+ The replication server is itself a limit, and it is not the instance type of your test endpoint. By default the replication server is a `t3.small`. This test measures the path to an endpoint whose size you chose.
+ A short run on a small instance can briefly burst past what the path sustains, so do not quote it as a link speed.
+ A pass here covers only TCP port 1500. Replication also needs outbound TCP port 443 to the Elastic Disaster Recovery service endpoint and to Amazon S3, which this test does not exercise. For information about verifying port 443, see [Verifying network connectivity](verifying-network-connectivity.md).

## Optionally compare the browser and the CLI to find the bottleneck
<a name="bwtest-browser-vs-cli"></a>

If you did run both the command-line test and the browser against the same endpoint, comparing them is inexpensive and tells you which way to look.
+ If they disagree materially, the instrument is the limit, not the path. Against a fast private endpoint, the browser can report figures well below the CLI, for example roughly 37% low on download and 45% low on upload. Quote the CLI figure.
+ If they agree closely, something in the path is limiting both. Two independent implementations converging on the same number is the signature of a shaped or saturated path, and that number is the one to investigate.

## Do not compare headline figures between runs
<a name="bwtest-run-variance"></a>

A genuine allowance problem shows throughput declining within a single run, not between runs. Comparing one run's headline number against another's is unreliable: back-to-back 30-second runs on an unchanged idle path can decline by 20% or more and then recover on the next run.

To look for a real decline, watch one long run's own time series. On the endpoint, during the run, use the Linux `sar -n DEV 1` command, or read `/proc/net/dev` in a one-second loop:

```
sar -n DEV 1
```

Compare the first third of a phase against the last third. A decline that persists inside a single run is real; a difference between two runs' headline numbers is noise.