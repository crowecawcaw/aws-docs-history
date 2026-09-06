

# `awsbout`
<a name="awsbatchcli.awsbout-v3"></a>

Shows the output of a given job.

```
awsbout [-h] [-c {{CLUSTER}}] [-hd {{HEAD}}] [-t {{TAIL}}] [-s] [-sp {{STREAM_PERIOD}}] {{job_id}}
```

## Positional Arguments
<a name="awsbatchcli.awsbout-v3.arguments"></a>

**{{job\_id}}**  
Specifies the job ID.

## Named Arguments
<a name="awsbatchcli.awsbout-v3.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**  
Indicates the cluster to use.

**-hd {{HEAD}}, --head {{HEAD}}**  
Gets the first {{HEAD}} lines of the job output.

**-t {{TAIL}}, --tail {{TAIL}}**  
Gets the last <tail> lines of the job output.

**-s, --stream**  
Gets the job output, and then waits for additional output to be produced. This argument can be used together with –tail to start from the latest <tail> lines of the job output.  
Default: False

**-sp {{STREAM\_PERIOD}}, --stream-period {{STREAM\_PERIOD}}**  
Sets the streaming period.  
Default: 5