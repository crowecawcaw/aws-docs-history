# Troubleshooting Amazon Keyspaces (for Apache Cassandra)

This guide covers troubleshooting steps for various scenarios when working with Amazon Keyspaces (for Apache Cassandra). It includes information on
resolving general errors, connection issues, capacity management problems, and Data Definition Language (DDL) errors.

- **General errors**
  - Troubleshooting top-level exceptions like `NoNodeAvailableException`, `NoHostAvailableException`,
    and `AllNodesFailedException`.
  - Isolating underlying errors from Java driver exceptions.
  - Implementing retry policies and configuring connections correctly.

- **Connection issues**
  - Resolving errors when connecting to Amazon Keyspaces endpoints using `cqlsh` or Apache Cassandra client drivers.
  - Troubleshooting VPC endpoint connections, Cassandra-stress connections, and IAM configuration errors.
  - Handling connection losses during data imports.

- **Capacity management errors**
  - Recognizing and resolving insufficient capacity errors related to tables, partitions, and connections.
  - Monitoring relevant Amazon Keyspaces metrics in Amazon CloudWatch Logs.
  - Optimizing connections and throughput for improved performance.

- **Data Definition Language (DDL) errors**

      + Troubleshooting errors when creating, accessing, or restoring keyspaces and tables.
      + Handling failures related to custom Time to Live (TTL) settings, column limits, and range deletes.
      + Considerations for heavy delete workloads.

  For troubleshooting guidance specific to IAM access, see [Troubleshooting Amazon Keyspaces identity
  and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"). For more information about security best practices, see [Security best practices for Amazon Keyspaces](best-practices-security.md "best-practices-security.md").

###### Topics

- [General errors](troubleshooting.md "troubleshooting.md")
- [Connection errors](troubleshooting.md "troubleshooting.md")
- [Capacity management errors](troubleshooting.md "troubleshooting.md")
- [Data definition language errors](troubleshooting.md "troubleshooting.md")
