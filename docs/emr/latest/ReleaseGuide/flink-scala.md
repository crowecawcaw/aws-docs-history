# Use the Scala shell

The Flink Scala shell for EMR clusters is only configured to start new YARN
sessions. You can use the Scala shell by following the procedure below.

###### Use the Flink Scala shell on the primary node

1. Log in to the primary node with SSH as described in [Connect to the primary
   node with SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md").
2. Type the following to start a shell:

In Amazon EMR version 5.5.0 and later, you can use the following command to start a
Yarn cluster for the Scala Shell with one TaskManager.

```
% flink-scala-shell yarn `1`
```

In earlier versions of Amazon EMR, use:

```
% /usr/lib/flink/bin/start-scala-shell.sh yarn `1`

```

This starts the Flink Scala shell so you can interactively use Flink. Just as
with other interfaces and options, you can scale the `-n` option
value used in the example based on the number of tasks you want to run from the
shell.

For more information, see [Scala REPL](https://ci.apache.org/projects/flink/flink-docs-release-1.10/ops/scala_shell.html "https://ci.apache.org/projects/flink/flink-docs-release-1.10/ops/scala_shell.html") in the official Apache Flink documentation.
