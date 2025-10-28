# Timing of AWS Network Firewall log delivery

A log file or log stream generally contains information about the requests that
your firewall received during a given time period. The timing of Network Firewall log delivery
varies by location type, averaging 3-6 minutes
for Amazon CloudWatch Logs and Amazon Data Firehose and 8-12 minutes for Amazon Simple Storage Service buckets. In some cases, logs may take longer than
these averages. When log entries are delayed, Network Firewall saves them
and then logs them according to the date and time of the period in which the
requests occurred, not the date and time when the logs are delivered.

###### Note

If your firewall doesn't filter traffic for a period of time, you don't
receive logs for that period.

When creating a log file or stream, Network Firewall consolidates information for
your firewall from all the endpoints that received traffic during the time period
that the log covers.
