# Amazon EMR 7.5.0 - ZooKeeper release notes

## Amazon EMR 7.5.0 - ZooKeeper Changes

- Starting with EMR-7.5.0, Zookeeper is set to Java 17 by default at runtime. To use a different version for the Java runtime, override the JVM settings
  in the `zookeeper-server` file and set `JAVA_HOME` to the desired version.
