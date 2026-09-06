

# Amazon EMR 7.5.0 - ZooKeeper release notes
<a name="ZooKeeper-release-history-750"></a>

## Amazon EMR 7.5.0 - ZooKeeper Changes
<a name="ZooKeeper-release-history-750-features"></a>
+ Starting with EMR-7.5.0, Zookeeper is set to Java 17 by default at runtime. To use a different version for the Java runtime, override the JVM settings in the `zookeeper-server` file and set `JAVA_HOME` to the desired version.