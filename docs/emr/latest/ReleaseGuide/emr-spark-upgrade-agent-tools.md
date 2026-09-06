

# Using Spark Upgrade Tools
<a name="emr-spark-upgrade-agent-tools"></a>

## Available Upgrade Tools
<a name="emr-spark-upgrade-agent-available-tools"></a>

The MCP service provides several tools to assist with Spark upgrades. The major tools are the following:


|  | Tool name | Tool Category | Description | 
| --- | --- | --- | --- | 
| 1 | generate\_spark\_upgrade\_plan | Planner | Generate a EMR-EC2/EMR-S upgrade plan | 
| 2 | reuse\_existing\_spark\_upgrade\_plan | Planner | Reuse existing local upgrade plan | 
| 3 | update\_build\_configuration | Build | Upgrade build configuration files | 
| 4 | check\_and\_update\_build\_environment | Build | Check/update Java environment for Spark upgrade | 
| 5 | compile\_and\_build\_project | Build | Provide guidance for compiling/building project | 
| 6 | run\_validation\_job | Test | Submit Spark app to EMR-EC2/EMR-S | 
| 7 | check\_job\_status | Test | Check status of EMR-EC2 step or EMR-S job run | 
| 8 | check\_and\_update\_python\_environment | Spark code edit | Check/update Python env for Spark upgrade | 
| 9 | fix\_upgrade\_failure | Spark code edit | Analyze a failure and suggest fixes | 
| 10 | get\_data\_quality\_summary | Observablity | Retrieve the data quality summary after the application is upgraded | 
| 11 | describe\_upgrade\_analysis | Observablity | describe the given analysis | 
| 12 | list\_upgrade\_analyses | Observablity | list all analyses created by current account | 

For a full list of all the upgrade tools provided by the SMUS Managed MCP server, you may list all tools from the server.