

# Hadoop daemon configuration settings
<a name="emr-hadoop-daemons"></a>

Hadoop daemon settings are different depending on the EC2 instance type that a cluster node uses. The following tables list the default configuration settings for each EC2 instance type.

To customize these settings, use the `hadoop-env` configuration classification. For more information, see [Configure applications](emr-configure-apps.md).

**Topics**
+ [c1 instances](#emr-hadoop-daemons-c1)
+ [c3 instances](#emr-hadoop-daemons-c3)
+ [c4 instances](#emr-hadoop-daemons-c4)
+ [c5 instances](#emr-hadoop-daemons-c5)
+ [c5a instances](#emr-hadoop-daemons-c5a)
+ [c5ad instances](#emr-hadoop-daemons-c5ad)
+ [c5d instances](#emr-hadoop-daemons-c5d)
+ [c5n instances](#emr-hadoop-daemons-c5n)
+ [c6a instances](#emr-hadoop-daemons-c6a)
+ [c6g instances](#emr-hadoop-daemons-c6g)
+ [c6gd instances](#emr-hadoop-daemons-c6gd)
+ [c6gn instances](#emr-hadoop-daemons-c6gn)
+ [c6i instances](#emr-hadoop-daemons-c6i)
+ [c6id instances](#emr-hadoop-daemons-c6id)
+ [c6in instances](#emr-hadoop-daemons-c6in)
+ [c7a instances](#emr-hadoop-daemons-c7a)
+ [c7g instances](#emr-hadoop-daemons-c7g)
+ [c7gd instances](#emr-hadoop-daemons-c7gd)
+ [c7gn instances](#emr-hadoop-daemons-c7gn)
+ [c7i instances](#emr-hadoop-daemons-c7i)
+ [c7i-flex instances](#emr-hadoop-daemons-c7i-flex)
+ [c8g instances](#emr-hadoop-daemons-c8g)
+ [c8gd instances](#emr-hadoop-daemons-c8gd)
+ [d2 instances](#emr-hadoop-daemons-d2)
+ [d3 instances](#emr-hadoop-daemons-d3)
+ [d3en instances](#emr-hadoop-daemons-d3en)
+ [f2 instances](#emr-hadoop-daemons-f2)
+ [g3 instances](#emr-hadoop-daemons-g3)
+ [g3s instances](#emr-hadoop-daemons-g3s)
+ [g4dn instances](#emr-hadoop-daemons-g4dn)
+ [g5 instances](#emr-hadoop-daemons-g5)
+ [g6 instances](#emr-hadoop-daemons-g6)
+ [g6e instances](#emr-hadoop-daemons-g6e)
+ [gr6 instances](#emr-hadoop-daemons-gr6)
+ [h1 instances](#emr-hadoop-daemons-h1)
+ [i2 instances](#emr-hadoop-daemons-i2)
+ [i3 instances](#emr-hadoop-daemons-i3)
+ [i3en instances](#emr-hadoop-daemons-i3en)
+ [i4g instances](#emr-hadoop-daemons-i4g)
+ [i4i instances](#emr-hadoop-daemons-i4i)
+ [i7i instances](#emr-hadoop-daemons-i7i)
+ [i7ie instances](#emr-hadoop-daemons-i7ie)
+ [i8g instances](#emr-hadoop-daemons-i8g)
+ [im4gn instances](#emr-hadoop-daemons-im4gn)
+ [is4gen instances](#emr-hadoop-daemons-is4gen)
+ [m1 instances](#emr-hadoop-daemons-m1)
+ [m2 instances](#emr-hadoop-daemons-m2)
+ [m3 instances](#emr-hadoop-daemons-m3)
+ [m4 instances](#emr-hadoop-daemons-m4)
+ [m5 instances](#emr-hadoop-daemons-m5)
+ [m5a instances](#emr-hadoop-daemons-m5a)
+ [m5ad instances](#emr-hadoop-daemons-m5ad)
+ [m5d instances](#emr-hadoop-daemons-m5d)
+ [m5dn instances](#emr-hadoop-daemons-m5dn)
+ [m5n instances](#emr-hadoop-daemons-m5n)
+ [m5zn instances](#emr-hadoop-daemons-m5zn)
+ [m6a instances](#emr-hadoop-daemons-m6a)
+ [m6g instances](#emr-hadoop-daemons-m6g)
+ [m6gd instances](#emr-hadoop-daemons-m6gd)
+ [m6i instances](#emr-hadoop-daemons-m6i)
+ [m6id instances](#emr-hadoop-daemons-m6id)
+ [m6idn instances](#emr-hadoop-daemons-m6idn)
+ [m6in instances](#emr-hadoop-daemons-m6in)
+ [m7a instances](#emr-hadoop-daemons-m7a)
+ [m7g instances](#emr-hadoop-daemons-m7g)
+ [m7gd instances](#emr-hadoop-daemons-m7gd)
+ [m7i instances](#emr-hadoop-daemons-m7i)
+ [m7i-flex instances](#emr-hadoop-daemons-m7i-flex)
+ [m8g instances](#emr-hadoop-daemons-m8g)
+ [m8gd instances](#emr-hadoop-daemons-m8gd)
+ [p2 instances](#emr-hadoop-daemons-p2)
+ [p3 instances](#emr-hadoop-daemons-p3)
+ [p4d instances](#emr-hadoop-daemons-p4d)
+ [p5 instances](#emr-hadoop-daemons-p5)
+ [r3 instances](#emr-hadoop-daemons-r3)
+ [r4 instances](#emr-hadoop-daemons-r4)
+ [r5 instances](#emr-hadoop-daemons-r5)
+ [r5a instances](#emr-hadoop-daemons-r5a)
+ [r5ad instances](#emr-hadoop-daemons-r5ad)
+ [r5b instances](#emr-hadoop-daemons-r5b)
+ [r5d instances](#emr-hadoop-daemons-r5d)
+ [r5dn instances](#emr-hadoop-daemons-r5dn)
+ [r5n instances](#emr-hadoop-daemons-r5n)
+ [r6a instances](#emr-hadoop-daemons-r6a)
+ [r6g instances](#emr-hadoop-daemons-r6g)
+ [r6gd instances](#emr-hadoop-daemons-r6gd)
+ [r6i instances](#emr-hadoop-daemons-r6i)
+ [r6id instances](#emr-hadoop-daemons-r6id)
+ [r6idn instances](#emr-hadoop-daemons-r6idn)
+ [r6in instances](#emr-hadoop-daemons-r6in)
+ [r7a instances](#emr-hadoop-daemons-r7a)
+ [r7g instances](#emr-hadoop-daemons-r7g)
+ [r7gd instances](#emr-hadoop-daemons-r7gd)
+ [r7i instances](#emr-hadoop-daemons-r7i)
+ [r7iz instances](#emr-hadoop-daemons-r7iz)
+ [r8g instances](#emr-hadoop-daemons-r8g)
+ [r8gd instances](#emr-hadoop-daemons-r8gd)
+ [x1 instances](#emr-hadoop-daemons-x1)
+ [x1e instances](#emr-hadoop-daemons-x1e)
+ [x2gd instances](#emr-hadoop-daemons-x2gd)
+ [x2idn instances](#emr-hadoop-daemons-x2idn)
+ [x2iedn instances](#emr-hadoop-daemons-x2iedn)
+ [x8g instances](#emr-hadoop-daemons-x8g)
+ [z1d instances](#emr-hadoop-daemons-z1d)

## c1 instances
<a name="emr-hadoop-daemons-c1"></a>


**c1.medium**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 192 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 96 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 128 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 128 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 192 | 
| HADOOP\_DATANODE\_HEAPSIZE | 96 | 


**c1.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 768 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 384 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 512 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 512 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 768 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 

## c3 instances
<a name="emr-hadoop-daemons-c3"></a>


**c3.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c3.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2396 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2396 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2396 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1740 | 
| HADOOP\_DATANODE\_HEAPSIZE | 757 | 


**c3.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2703 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2703 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2703 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3276 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1064 | 


**c3.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3317 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3317 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3317 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6348 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1679 | 

## c4 instances
<a name="emr-hadoop-daemons-c4"></a>


**c4.large**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 1152 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 1152 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 1152 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 1152 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 576 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 


**c4.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c4.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2396 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2396 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2396 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1740 | 
| HADOOP\_DATANODE\_HEAPSIZE | 757 | 


**c4.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2703 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2703 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2703 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3276 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1064 | 


**c4.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3317 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3317 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3317 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6348 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1679 | 

## c5 instances
<a name="emr-hadoop-daemons-c5"></a>


**c5.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2252 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2252 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2252 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1024 | 
| HADOOP\_DATANODE\_HEAPSIZE | 614 | 


**c5.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**c5.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**c5.9xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3563 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3563 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3563 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 7577 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1925 | 


**c5.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4055 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4055 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4055 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 10035 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2416 | 


**c5.18xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5038 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5038 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5038 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 14950 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3399 | 


**c5.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c5a instances
<a name="emr-hadoop-daemons-c5a"></a>


**c5a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c5a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c5a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c5a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c5a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4055 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4055 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4055 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 10035 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2416 | 


**c5a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c5a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c5ad instances
<a name="emr-hadoop-daemons-c5ad"></a>


**c5ad.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c5ad.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c5ad.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c5ad.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c5ad.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c5ad.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c5ad.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c5d instances
<a name="emr-hadoop-daemons-c5d"></a>


**c5d.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2252 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2252 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2252 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1024 | 
| HADOOP\_DATANODE\_HEAPSIZE | 614 | 


**c5d.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**c5d.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**c5d.9xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3563 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3563 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3563 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 7577 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1925 | 


**c5d.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4055 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4055 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4055 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 10035 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2416 | 


**c5d.18xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5038 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5038 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5038 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 14950 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3399 | 


**c5d.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c5n instances
<a name="emr-hadoop-daemons-c5n"></a>


**c5n.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2304 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2304 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2304 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1280 | 
| HADOOP\_DATANODE\_HEAPSIZE | 665 | 


**c5n.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2519 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2519 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2519 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 2355 | 
| HADOOP\_DATANODE\_HEAPSIZE | 880 | 


**c5n.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2949 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2949 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2949 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 4505 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1310 | 


**c5n.9xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4055 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4055 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4055 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 10035 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2416 | 


**c5n.18xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c6a instances
<a name="emr-hadoop-daemons-c6a"></a>


**c6a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c6a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c6a.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c6a.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c6g instances
<a name="emr-hadoop-daemons-c6g"></a>


**c6g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c6gd instances
<a name="emr-hadoop-daemons-c6gd"></a>


**c6gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c6gn instances
<a name="emr-hadoop-daemons-c6gn"></a>


**c6gn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6gn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6gn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6gn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6gn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6gn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c6i instances
<a name="emr-hadoop-daemons-c6i"></a>


**c6i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c6i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c6i.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c6id instances
<a name="emr-hadoop-daemons-c6id"></a>


**c6id.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6id.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6id.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6id.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6id.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6id.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c6id.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c6id.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c6in instances
<a name="emr-hadoop-daemons-c6in"></a>


**c6in.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c6in.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c6in.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c6in.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c6in.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c6in.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c6in.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c6in.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c7a instances
<a name="emr-hadoop-daemons-c7a"></a>


**c7a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c7a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c7a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c7a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c7a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c7a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c7a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c7a.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c7a.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c7g instances
<a name="emr-hadoop-daemons-c7g"></a>


**c7g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c7g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c7g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c7g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c7g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c7g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c7gd instances
<a name="emr-hadoop-daemons-c7gd"></a>


**c7gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c7gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c7gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c7gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c7gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c7gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c7gn instances
<a name="emr-hadoop-daemons-c7gn"></a>


**c7gn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c7gn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c7gn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c7gn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c7gn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c7gn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c7i instances
<a name="emr-hadoop-daemons-c7i"></a>


**c7i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c7i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c7i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c7i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c7i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c7i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c7i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c7i.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c7i-flex instances
<a name="emr-hadoop-daemons-c7i-flex"></a>


**c7i-flex.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c7i-flex.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c7i-flex.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c7i-flex.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c7i-flex.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c7i-flex.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 

## c8g instances
<a name="emr-hadoop-daemons-c8g"></a>


**c8g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c8g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c8g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c8g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c8g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c8g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c8g.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c8g.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## c8gd instances
<a name="emr-hadoop-daemons-c8gd"></a>


**c8gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2124 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2124 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2124 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 972 | 
| HADOOP\_DATANODE\_HEAPSIZE | 588 | 


**c8gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**c8gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**c8gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**c8gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**c8gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**c8gd.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**c8gd.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## d2 instances
<a name="emr-hadoop-daemons-d2"></a>


**d2.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**d2.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**d2.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**d2.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## d3 instances
<a name="emr-hadoop-daemons-d3"></a>


**d3.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**d3.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**d3.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**d3.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## d3en instances
<a name="emr-hadoop-daemons-d3en"></a>


**d3en.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**d3en.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**d3en.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**d3en.6xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**d3en.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**d3en.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## f2 instances
<a name="emr-hadoop-daemons-f2"></a>


**f2.6xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**f2.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**f2.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 42065 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 42065 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 42065 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 200089 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## g3 instances
<a name="emr-hadoop-daemons-g3"></a>


**g3.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**g3.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g3.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## g3s instances
<a name="emr-hadoop-daemons-g3s"></a>


**g3s.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 

## g4dn instances
<a name="emr-hadoop-daemons-g4dn"></a>


**g4dn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**g4dn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**g4dn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**g4dn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**g4dn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g4dn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## g5 instances
<a name="emr-hadoop-daemons-g5"></a>


**g5.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**g5.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**g5.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**g5.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**g5.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g5.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g5.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g5.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## g6 instances
<a name="emr-hadoop-daemons-g6"></a>


**g6.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2396 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2396 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2396 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1740 | 
| HADOOP\_DATANODE\_HEAPSIZE | 757 | 


**g6.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2703 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2703 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2703 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3276 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1064 | 


**g6.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3317 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3317 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3317 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6348 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1679 | 


**g6.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4567 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4567 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4567 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12595 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2928 | 


**g6.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5795 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5795 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5795 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18739 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7045 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7045 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7045 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 24985 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9543 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9543 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9543 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37478 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 16998 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 16998 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 16998 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 74752 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## g6e instances
<a name="emr-hadoop-daemons-g6e"></a>


**g6e.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**g6e.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**g6e.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**g6e.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6e.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6e.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6e.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**g6e.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## gr6 instances
<a name="emr-hadoop-daemons-gr6"></a>


**gr6.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4567 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4567 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4567 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12595 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2928 | 


**gr6.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7045 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7045 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7045 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 24985 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## h1 instances
<a name="emr-hadoop-daemons-h1"></a>


**h1.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**h1.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**h1.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**h1.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i2 instances
<a name="emr-hadoop-daemons-i2"></a>


**i2.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i2.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i2.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**i2.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i3 instances
<a name="emr-hadoop-daemons-i3"></a>


**i3.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i3.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i3.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**i3.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i3.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i3en instances
<a name="emr-hadoop-daemons-i3en"></a>


**i3en.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**i3en.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**i3en.3xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4055 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4055 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4055 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 10035 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2416 | 


**i3en.6xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i3en.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i3en.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17817 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17817 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17817 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 78848 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i4g instances
<a name="emr-hadoop-daemons-i4g"></a>


**i4g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i4g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i4g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**i4g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i4g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i4i instances
<a name="emr-hadoop-daemons-i4i"></a>


**i4i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i4i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i4i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**i4i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i4i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i4i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i4i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i4i.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i7i instances
<a name="emr-hadoop-daemons-i7i"></a>


**i7i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i7i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i7i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**i7i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7i.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i7ie instances
<a name="emr-hadoop-daemons-i7ie"></a>


**i7ie.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i7ie.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i7ie.3xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**i7ie.6xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7ie.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7ie.18xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 13332 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 13332 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 13332 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 56422 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7ie.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i7ie.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## i8g instances
<a name="emr-hadoop-daemons-i8g"></a>


**i8g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**i8g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**i8g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**i8g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i8g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i8g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i8g.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**i8g.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## im4gn instances
<a name="emr-hadoop-daemons-im4gn"></a>


**im4gn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**im4gn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**im4gn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**im4gn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**im4gn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## is4gen instances
<a name="emr-hadoop-daemons-is4gen"></a>


**is4gen.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2557 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2557 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2557 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 2547 | 
| HADOOP\_DATANODE\_HEAPSIZE | 919 | 


**is4gen.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3025 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3025 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3025 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 4889 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1387 | 


**is4gen.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**is4gen.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m1 instances
<a name="emr-hadoop-daemons-m1"></a>


**m1.small**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 256 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 96 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 192 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 128 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 192 | 
| HADOOP\_DATANODE\_HEAPSIZE | 96 | 


**m1.medium**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 384 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 192 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 256 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 256 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 384 | 
| HADOOP\_DATANODE\_HEAPSIZE | 192 | 


**m1.large**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 768 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 384 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 512 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 512 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 768 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 


**m1.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 1024 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 512 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 768 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 1024 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 2304 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 

## m2 instances
<a name="emr-hadoop-daemons-m2"></a>


**m2.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 1536 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 1024 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 1024 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 1024 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3072 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 


**m2.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 1536 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 1024 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 1024 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 1536 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6144 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 


**m2.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2048 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 1024 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 1536 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 1536 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12288 | 
| HADOOP\_DATANODE\_HEAPSIZE | 384 | 

## m3 instances
<a name="emr-hadoop-daemons-m3"></a>


**m3.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2396 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2396 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2396 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1740 | 
| HADOOP\_DATANODE\_HEAPSIZE | 757 | 


**m3.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2703 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2703 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2703 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3276 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1064 | 

## m4 instances
<a name="emr-hadoop-daemons-m4"></a>


**m4.large**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2252 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2252 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2252 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1024 | 
| HADOOP\_DATANODE\_HEAPSIZE | 614 | 


**m4.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**m4.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**m4.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**m4.10xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5365 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5365 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5365 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 16588 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3727 | 


**m4.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5 instances
<a name="emr-hadoop-daemons-m5"></a>


**m5.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**m5.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**m5.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**m5.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**m5.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5a instances
<a name="emr-hadoop-daemons-m5a"></a>


**m5a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**m5a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**m5a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**m5a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**m5a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5ad instances
<a name="emr-hadoop-daemons-m5ad"></a>


**m5ad.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m5ad.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m5ad.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m5ad.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m5ad.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5ad.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5ad.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5d instances
<a name="emr-hadoop-daemons-m5d"></a>


**m5d.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2416 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2416 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2416 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1843 | 
| HADOOP\_DATANODE\_HEAPSIZE | 778 | 


**m5d.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**m5d.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**m5d.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**m5d.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5d.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5d.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5dn instances
<a name="emr-hadoop-daemons-m5dn"></a>


**m5dn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m5dn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m5dn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m5dn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m5dn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5dn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5dn.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5n instances
<a name="emr-hadoop-daemons-m5n"></a>


**m5n.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m5n.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m5n.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m5n.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m5n.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5n.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m5n.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m5zn instances
<a name="emr-hadoop-daemons-m5zn"></a>


**m5zn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2396 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2396 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2396 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1740 | 
| HADOOP\_DATANODE\_HEAPSIZE | 757 | 


**m5zn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m5zn.3xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3025 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3025 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3025 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 4889 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1387 | 


**m5zn.6xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3962 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3962 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3962 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 9574 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2324 | 


**m5zn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6a instances
<a name="emr-hadoop-daemons-m6a"></a>


**m6a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6a.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6a.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6g instances
<a name="emr-hadoop-daemons-m6g"></a>


**m6g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5877 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5877 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5877 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19148 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6gd instances
<a name="emr-hadoop-daemons-m6gd"></a>


**m6gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5877 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5877 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5877 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19148 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6i instances
<a name="emr-hadoop-daemons-m6i"></a>


**m6i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5877 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5877 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5877 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19148 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6i.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6id instances
<a name="emr-hadoop-daemons-m6id"></a>


**m6id.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6id.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6id.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6id.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6id.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6id.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6id.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6id.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6idn instances
<a name="emr-hadoop-daemons-m6idn"></a>


**m6idn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6idn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6idn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6idn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6idn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6idn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6idn.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6idn.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m6in instances
<a name="emr-hadoop-daemons-m6in"></a>


**m6in.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m6in.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m6in.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m6in.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m6in.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5877 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5877 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5877 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19148 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6in.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6in.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m6in.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m7a instances
<a name="emr-hadoop-daemons-m7a"></a>


**m7a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m7a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m7a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m7a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m7a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7a.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7a.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m7g instances
<a name="emr-hadoop-daemons-m7g"></a>


**m7g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m7g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m7g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m7g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m7g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m7gd instances
<a name="emr-hadoop-daemons-m7gd"></a>


**m7gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m7gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m7gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m7gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m7gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m7i instances
<a name="emr-hadoop-daemons-m7i"></a>


**m7i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m7i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m7i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m7i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m7i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5877 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5877 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5877 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19148 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7i.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m7i-flex instances
<a name="emr-hadoop-daemons-m7i-flex"></a>


**m7i-flex.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m7i-flex.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m7i-flex.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m7i-flex.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m7i-flex.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m7i-flex.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m8g instances
<a name="emr-hadoop-daemons-m8g"></a>


**m8g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m8g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m8g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m8g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m8g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5877 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5877 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5877 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19148 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m8g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m8g.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m8g.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## m8gd instances
<a name="emr-hadoop-daemons-m8gd"></a>


**m8gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2401 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2401 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2401 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 1766 | 
| HADOOP\_DATANODE\_HEAPSIZE | 762 | 


**m8gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**m8gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**m8gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**m8gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 5836 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 5836 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 5836 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 18944 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m8gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m8gd.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**m8gd.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## p2 instances
<a name="emr-hadoop-daemons-p2"></a>


**p2.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**p2.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**p2.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## p3 instances
<a name="emr-hadoop-daemons-p3"></a>


**p3.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**p3.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**p3.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## p4d instances
<a name="emr-hadoop-daemons-p4d"></a>


**p4d.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 24576 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 24576 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 24576 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 112640 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## p5 instances
<a name="emr-hadoop-daemons-p5"></a>


**p5.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 42065 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 42065 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 42065 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 200089 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r3 instances
<a name="emr-hadoop-daemons-r3"></a>


**r3.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r3.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r3.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r3.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r4 instances
<a name="emr-hadoop-daemons-r4"></a>


**r4.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r4.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r4.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r4.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r4.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5 instances
<a name="emr-hadoop-daemons-r5"></a>


**r5.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**r5.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**r5.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**r5.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12574 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12574 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12574 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 52633 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17817 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17817 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17817 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 78848 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5a instances
<a name="emr-hadoop-daemons-r5a"></a>


**r5a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**r5a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**r5a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**r5a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12574 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12574 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12574 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 52633 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17817 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17817 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17817 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 78848 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5ad instances
<a name="emr-hadoop-daemons-r5ad"></a>


**r5ad.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r5ad.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r5ad.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r5ad.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5ad.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5ad.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12247 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12247 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12247 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50995 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5ad.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5b instances
<a name="emr-hadoop-daemons-r5b"></a>


**r5b.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r5b.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r5b.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r5b.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5b.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5b.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5b.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5d instances
<a name="emr-hadoop-daemons-r5d"></a>


**r5d.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**r5d.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**r5d.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4710 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4710 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4710 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 13312 | 
| HADOOP\_DATANODE\_HEAPSIZE | 3072 | 


**r5d.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7331 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7331 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7331 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 26419 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5d.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5d.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12574 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12574 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12574 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 52633 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5d.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17817 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17817 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17817 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 78848 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5dn instances
<a name="emr-hadoop-daemons-r5dn"></a>


**r5dn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r5dn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r5dn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r5dn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5dn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5dn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5dn.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r5n instances
<a name="emr-hadoop-daemons-r5n"></a>


**r5n.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r5n.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r5n.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r5n.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5n.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5n.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r5n.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6a instances
<a name="emr-hadoop-daemons-r6a"></a>


**r6a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6a.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6a.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6g instances
<a name="emr-hadoop-daemons-r6g"></a>


**r6g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6gd instances
<a name="emr-hadoop-daemons-r6gd"></a>


**r6gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6i instances
<a name="emr-hadoop-daemons-r6i"></a>


**r6i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6i.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 21544 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 21544 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 21544 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 97484 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6id instances
<a name="emr-hadoop-daemons-r6id"></a>


**r6id.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6id.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6id.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6id.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6id.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6id.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6id.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6id.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6idn instances
<a name="emr-hadoop-daemons-r6idn"></a>


**r6idn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6idn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6idn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6idn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6idn.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6idn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6idn.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6idn.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r6in instances
<a name="emr-hadoop-daemons-r6in"></a>


**r6in.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r6in.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r6in.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r6in.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6in.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6in.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6in.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r6in.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r7a instances
<a name="emr-hadoop-daemons-r7a"></a>


**r7a.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r7a.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r7a.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r7a.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7a.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7a.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7a.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7a.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7a.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r7g instances
<a name="emr-hadoop-daemons-r7g"></a>


**r7g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r7g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r7g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r7g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r7gd instances
<a name="emr-hadoop-daemons-r7gd"></a>


**r7gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r7gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r7gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r7gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r7i instances
<a name="emr-hadoop-daemons-r7i"></a>


**r7i.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r7i.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r7i.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r7i.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7i.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7i.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7i.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7i.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r7iz instances
<a name="emr-hadoop-daemons-r7iz"></a>


**r7iz.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r7iz.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r7iz.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r7iz.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7iz.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7iz.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r7iz.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 21544 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 21544 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 21544 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 97484 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r8g instances
<a name="emr-hadoop-daemons-r8g"></a>


**r8g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r8g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r8g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r8g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8g.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8g.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## r8gd instances
<a name="emr-hadoop-daemons-r8gd"></a>


**r8gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2713 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2713 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2713 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3328 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1075 | 


**r8gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**r8gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**r8gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9584 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9584 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9584 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 37683 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8gd.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**r8gd.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## x1 instances
<a name="emr-hadoop-daemons-x1"></a>


**x1.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 21544 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 21544 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 21544 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 97484 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x1.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 41000 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 41000 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 41000 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 194764 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## x1e instances
<a name="emr-hadoop-daemons-x1e"></a>


**x1e.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4520 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4520 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4520 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12364 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2882 | 


**x1e.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6952 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6952 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6952 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 24524 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x1e.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 11816 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 11816 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 11816 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 48844 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x1e.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 21544 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 21544 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 21544 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 97484 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x1e.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 41000 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 41000 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 41000 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 194764 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x1e.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 79912 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 79912 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 79912 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 389324 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## x2gd instances
<a name="emr-hadoop-daemons-x2gd"></a>


**x2gd.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**x2gd.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**x2gd.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2gd.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2gd.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2gd.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## x2idn instances
<a name="emr-hadoop-daemons-x2idn"></a>


**x2idn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2idn.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2idn.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 42065 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 42065 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 42065 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 200089 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## x2iedn instances
<a name="emr-hadoop-daemons-x2iedn"></a>


**x2iedn.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**x2iedn.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2iedn.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2iedn.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2iedn.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 42065 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 42065 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 42065 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 200089 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2iedn.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 62054 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 62054 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 62054 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 300032 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x2iedn.32xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 82042 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 82042 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 82042 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 399974 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## x8g instances
<a name="emr-hadoop-daemons-x8g"></a>


**x8g.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3338 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3338 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3338 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6451 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1699 | 


**x8g.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4587 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4587 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4587 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 12697 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2949 | 


**x8g.4xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 7086 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 7086 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 7086 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 25190 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x8g.8xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 12083 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 12083 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 12083 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 50176 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x8g.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 17080 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 17080 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 17080 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 75161 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x8g.16xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 22077 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 22077 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 22077 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 100147 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x8g.24xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 32071 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 32071 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 32071 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 150118 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**x8g.48xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 62054 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 62054 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 62054 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 300032 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 

## z1d instances
<a name="emr-hadoop-daemons-z1d"></a>


**z1d.xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 2744 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 2744 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 2744 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 3481 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1105 | 


**z1d.2xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 3399 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 3399 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 3399 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 6758 | 
| HADOOP\_DATANODE\_HEAPSIZE | 1761 | 


**z1d.3xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 4055 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 4055 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 4055 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 10035 | 
| HADOOP\_DATANODE\_HEAPSIZE | 2416 | 


**z1d.6xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 6021 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 6021 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 6021 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 19865 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 


**z1d.12xlarge**  

| Parameter | Value | 
| --- | --- | 
| YARN\_RESOURCEMANAGER\_HEAPSIZE | 9953 | 
| YARN\_PROXYSERVER\_HEAPSIZE | 9953 | 
| YARN\_NODEMANAGER\_HEAPSIZE | 2048 | 
| HADOOP\_JOB\_HISTORYSERVER\_HEAPSIZE | 9953 | 
| HADOOP\_NAMENODE\_HEAPSIZE  | 39526 | 
| HADOOP\_DATANODE\_HEAPSIZE | 4096 | 