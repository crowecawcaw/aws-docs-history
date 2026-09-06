

# `pcluster3-config-converter`
<a name="pcluster3-config-converter"></a>

Reads a AWS ParallelCluster version 2 configuration file and writes a AWS ParallelCluster version 3 configuration file.

```
pcluster3-config-converter [-h]                            
                [-t CLUSTER_TEMPLATE]
                [-c CONFIG_FILE]
                [--force-convert]
                [-o OUTPUT_FILE]
```

## Named arguments
<a name="pcluster3-config-converter.named.arguments"></a>

**-h, --help**  
Shows the help text for `pcluster3-config-converter`.

**-t {{CLUSTER\_TEMPLATE}}, --cluster-template {{CLUSTER\_TEMPLATE}}**  
Specifies the [`[cluster]` section](https://docs.aws.amazon.com/parallelcluster/v2/ug/cluster-definition.html) of the configuration file to convert. If not specified the script will look for the [cluster-template](https://docs.aws.amazon.com/parallelcluster/v2/ug/global.html#cluster-template) parameter in the [`[global]` section](https://docs.aws.amazon.com/parallelcluster/v2/ug/global.html) or will search for `[cluster default]`.

**-c {{CONFIG\_FILE}}, --config-file {{CONFIG\_FILE}}**  
Specifies the AWS ParallelCluster version 2 configuration file to be read.

**--force-convert**  
Enables a conversion even if one or more settings is not supported and not recommended.

**-o {{OUTPUT\_FILE}}, --output-file {{OUTPUT\_FILE}}**  
Specifies the AWS ParallelCluster version 3 configuration file to be written. If this parameter is not specified, the configuration is written to stdout.

**Note**  
The `pcluster3-config-converter` command was added in AWS ParallelCluster version 3.0.1.