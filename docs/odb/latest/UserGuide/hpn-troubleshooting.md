

# Troubleshooting
<a name="hpn-troubleshooting"></a>

## Handling Insufficient Capacity Errors (ICE)
<a name="handling-ice-errors"></a>

If you receive an **Insufficient Instance Capacity Error (ICE)** when launching Amazon EC2 instances with the Oracle Database@AWS placement group:
+ **Retry with a different instance type** – ICE errors are typically instance-type specific. Retrying with a compatible alternative instance type often resolves the issue.
+ **Use [On-Demand Capacity Reservations (ODCR)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html)** – To minimize the risk of ICE occurrences, reserve capacity in advance using ODCR with your Oracle Database@AWS placement group.
+ **Use placement groups selectively** – Reserve placement group usage for workloads that truly require consistent sub-millisecond latency.