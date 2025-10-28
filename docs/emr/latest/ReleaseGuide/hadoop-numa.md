# Turn on non-uniform memory access awareness for YARN

containers

With Amazon EMR versions 6.x and later, you can use non-uniform memory access (NUMA) for
multiprocessing your data on clusters. NUMA is a computer memory design pattern where
the processor can access its own local memory faster than memory on another processor or
shared between processors. YARN containers have better performance with NUMA because
they can bind to a specific NUMA node that serves all subsequent memory allocations.
This reduces the amount of times that your cluster has to access remote memory.

You can turn on NUMA support for YARN container when the worker node machine is a
multi-NUMA node. To confirm if a worker node is a single-NUMA or multi-NUMA node, run
the following command.

```
lscpu | grep -i numa
NUMA node(s): 2
```

In general, instances that are larger than 12x have two NUMA nodes. This does not
apply to metal instances.

###### To turn on NUMA awareness for YARN containers

1. Use the following `yarn-site` configuration in your Amazon EMR 6.x
   cluster.

```
 [
	{
		"classification":"yarn-site",
			"properties":{
				"yarn.nodemanager.linux-container-executor.nonsecure-mode.local-user":"yarn",
				"yarn.nodemanager.linux-container-executor.group":"yarn",
				"yarn.nodemanager.container-executor.class":"org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor",
				"yarn.nodemanager.numa-awareness.enabled":"true",
				"yarn.nodemanager.numa-awareness.numactl.cmd":"/usr/bin/numactl",
				"yarn.nodemanager.numa-awareness.read-topology":"true"
			},
		"configurations":[]
	}
 ]
```

2. Provide the following bootstrap action in your cluster.

```
#!/bin/bash

sudo yum -y install numactl
echo 1 | sudo tee /proc/sys/kernel/numa_balancing

echo "banned.users=mapred,bin,hdfs" >> /etc/hadoop/conf/container-executor.cfg
rm -rf /var/log/hadoop-yarn/
sudo chown -R yarn:hadoop /var/log/hadoop-yarn/
sudo chmod 755 -R /var/log/hadoop-yarn/

sudo chmod 6050 /etc/hadoop/conf/container-executor.cfg

mkdir /mnt/yarn && sudo chmod 755 -R /mnt/yarn && sudo chown -R yarn:hadoop /mnt/yarn
mkdir /mnt1/yarn && sudo chmod 755 -R /mnt1/yarn && sudo chown -R yarn:hadoop /mnt1/yarn
mkdir /mnt2/yarn && sudo chmod 755 -R /mnt2/yarn && sudo chown -R yarn:hadoop /mnt2/yarn
```

3. Every container must be aware of NUMA. You can notify the Java virtual machine
   (JVM) in each container with a NUMA flag. For example, to notify the JVM to use
   NUMA in a MapReduce job, add the following properties in
   `mapred-site.xml`.

```
<property>
	<name>mapreduce.reduce.java.opts</name>
	<value>-XX:+UseNUMA</value>
</property>
<property>
	<name>mapreduce.map.java.opts</name>
	<value>-XX:+UseNUMA</value>
</property>
```

4. To verify that you turned NUMA on, search any of the NodeManager log files
   with the following command.

```
grep "NUMA resources allocation is enabled," *
```

To verify that NodeManager has assigned NUMA node resources to a container,
search the NodeManager log with the following command, replacing
`<container_id>` with your own
container ID.

```
grep "NUMA node" | grep `<container_id>`
```
