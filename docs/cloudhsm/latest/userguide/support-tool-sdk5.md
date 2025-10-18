# AWS CloudHSM Client SDK 5 support tool

The script for AWS CloudHSM Client SDK 5 extracts the following information:


* The configuration file for the Client SDK 5 component
* Available log files
* Current version of the operating system
* Package information

## Running the info tool for Client SDK 5


Client SDK 5 includes a client support tool for each component, but all tools
 function the same. Run the tool to create an output file with all the gathered
 information. 


The tools use a syntax like this: 



```
[ `pkcs11` | `dyn` | `jce` | `ksp` | `cli`]_info
```

For example, to gather information for support from a Linux host running PKCS #11 library
 and have the system write to the default directory, you would run this command: 



```
`/opt/cloudhsm/bin/pkcs11_info`
```

The tool creates the output file inside the `/tmp`
 directory.



AWS CloudHSM CLI
###### To gather support data for AWS CloudHSM CLI on Linux

* Use the support tool to gather data. 



```
`/opt/cloudhsm/bin/cli_info`
```

###### To gather support data for AWS CloudHSM on Windows

* Use the support tool to gather data. 



```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cli_info.exe"`
```


PKCS #11 library
###### To gather support data for PKCS #11 library on Linux

* Use the support tool to gather data. 



```
`/opt/cloudhsm/bin/pkcs11_info`
```

###### To gather support data for PKCS #11 library on Windows

* Use the support tool to gather data. 



```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\pkcs11_info.exe"`
```


OpenSSL Dynamic Engine
###### To gather support data for OpenSSL Dynamic Engine on Linux

* Use the support tool to gather data. 



```
`/opt/cloudhsm/bin/dyn_info`
```


JCE provider
###### To gather support data for JCE provider on Linux

* Use the support tool to gather data. 



```
`/opt/cloudhsm/bin/jce_info`
```

###### To gather support data for JCE provider on Windows

* Use the support tool to gather data. 



```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\jce_info.exe"`
```


Key Storage Provider
###### To gather support data for Key Storage Provider on Windows

* Use the support tool to gather data. 



```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\ksp_info.exe"`
```



## Retrieving logs from a serverless environment


To configure for serverless environments, like Fargate or Lambda, we recommend you configure your AWS CloudHSM log type to `term`. Once configured to `term`, the serverless 
 environment will be able to output to CloudWatch.


To get the client logs from CloudWatch, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html") in the Amazon CloudWatch Logs User Guide.
