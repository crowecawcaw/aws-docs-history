

# Understanding runtime reachability for your Amazon Inspector findings

**Note**  
 All new package vulnerability findings for Amazon ECR container images and Amazon EC2 instances include the `runtimeReachability` and `runtimeReachabilityReason` fields. Findings that existed before runtime reachability became available are updated with these fields over time, so some existing findings might not include them yet. 

 When Amazon Inspector generates a package vulnerability finding for an Amazon ECR container image or an Amazon EC2 instance, it also evaluates each vulnerable package in the finding for runtime reachability. The result can help you prioritize findings. This section describes the evidence that Amazon Inspector uses for each supported resource type, what each result means, and how to filter and suppress findings by runtime reachability. 

 In these findings, each package in the `vulnerablePackages` list can include the following fields: 
+  `runtimeReachability` – The runtime reachability status that Amazon Inspector set for the package. The value is `REACHABLE`, `NOT_REACHABLE`, or `UNKNOWN`. 
+  `runtimeReachabilityReason` – The evidence that Amazon Inspector used to set `runtimeReachability`. The possible values depend on the resource type and are listed in the following sections. This field isn't present when `runtimeReachability` is `UNKNOWN`. 

 Amazon Inspector evaluates each package separately, so packages in the same finding can have different values. 

**Important**  
 A status of `REACHABLE` or `NOT_REACHABLE` is based only on the evidence that `runtimeReachabilityReason` describes. It isn't a definitive signal and doesn't change the severity of a finding. Use it together with other finding details to prioritize findings. For example, `NOT_REACHABLE` doesn't mean that the package can't run or that the vulnerability can't be exploited. 

## Runtime reachability for Amazon ECR container images
<a name="findings-understanding-runtime-reachability-ecr"></a>

 For container images, Amazon Inspector compares the file path of each vulnerable package with the directories from the image's `WORKDIR`, `ENTRYPOINT`, and `CMD` instructions. Amazon Inspector doesn't run the container, so this evidence doesn't show which files the container loads when it runs. 

 The following table describes the runtime reachability values for container images. 


| Status | Reason | Meaning | 
| --- |--- |--- |
| REACHABLE | PACKAGE\_IN\_DOCKERFILE\_WORKLOAD\_PATH | The package's file path is inside a directory from the image's WORKDIR, ENTRYPOINT, or CMD instruction. This doesn't confirm that the container loads the package when it runs. | 
| NOT\_REACHABLE | PACKAGE\_NOT\_IN\_DOCKERFILE\_WORKLOAD\_PATH | The package's file path is outside all of those directories. The container might still load the package when it runs. | 
| UNKNOWN | No value | Amazon Inspector couldn't determine runtime reachability for the package. | 

## Runtime reachability for Amazon EC2 instances
<a name="findings-understanding-runtime-reachability-ec2"></a>

 For Amazon EC2 instances, Amazon Inspector looks for the vulnerable package running as a process or service when it scans the instance. This evidence doesn't show whether the package runs at any other time. Amazon Inspector sets the status again each time it scans the instance. The status can change between `REACHABLE` and `NOT_REACHABLE` depending on whether the package is running at the time of the scan. 

 The following table describes the runtime reachability values for Amazon EC2 instances. 


| Status | Reason | Meaning | 
| --- |--- |--- |
| REACHABLE | PROCESS\_OBSERVED\_IN\_EC2\_RUNTIME | Amazon Inspector observed the package running as a process or service when it scanned the instance. | 
| NOT\_REACHABLE | PROCESS\_NOT\_OBSERVED\_IN\_EC2\_RUNTIME | Amazon Inspector didn't observe the package running as a process or service when it scanned the instance. | 
| UNKNOWN | No value | Amazon Inspector couldn't determine runtime reachability for the package. | 

## Unsupported resource types
<a name="findings-understanding-runtime-reachability-unsupported"></a>

 Amazon Inspector evaluates runtime reachability only for the `AWS_ECR_CONTAINER_IMAGE` and `AWS_EC2_INSTANCE` resource types. Findings for the following resource types don't include `runtimeReachability` or `runtimeReachabilityReason`: 
+ `AWS_ECR_REPOSITORY`
+ `AWS_LAMBDA_FUNCTION`
+ `CODE_REPOSITORY`
+ `MACHINE_IMAGE`
+ `Microsoft.Compute/virtualMachines`
+ `Microsoft.ContainerRegistry/registry/containerImage`
+ `Microsoft.Web/sites`
+ `artifactregistry.googleapis.com/DockerImage`
+ `cloudfunctions.googleapis.com/Function`
+ `compute.googleapis.com/Instance`

## Filtering and suppressing findings by runtime reachability
<a name="findings-understanding-runtime-reachability-filtering"></a>

 You can use the `runtimeReachability` and `runtimeReachabilityReason` fields of `vulnerablePackages` in filters and suppression rules. Both fields support the `EQUALS` and `NOT_EQUALS` operators. For more information about filtering and suppressing findings, see [Filtering your Amazon Inspector findings](findings-managing-filtering.md) and [Suppressing Amazon Inspector findings](findings-managing-supression-rules.md). 

 Filters and suppression rules evaluate these fields differently, so a filter and a suppression rule with the same criteria can match different findings. The difference affects findings that have more than one package. It also affects `NOT_EQUALS` criteria on findings whose packages don't have the field. 

### Filters
<a name="findings-understanding-runtime-reachability-filters"></a>

 The following table describes when a filter on `runtimeReachability` or `runtimeReachabilityReason` returns a finding when you view or list findings. 


| Comparison | Returns a finding when | 
| --- |--- |
| EQUALS | At least one package has the value that you filter on. | 
| NOT\_EQUALS | No package has the value that you filter on. This includes findings whose packages don't have the field. | 

 For example, `runtimeReachability EQUALS NOT_REACHABLE` returns a finding that has one `REACHABLE` package and one `NOT_REACHABLE` package. `runtimeReachability NOT_EQUALS NOT_REACHABLE` doesn't return that finding, but it does return a Lambda function finding, which doesn't have a `runtimeReachability` field. 

### Suppression rules
<a name="findings-understanding-runtime-reachability-suppression"></a>

 A suppression rule on `runtimeReachability` or `runtimeReachabilityReason` considers all packages in a finding together. 

 The following table describes when a suppression rule on `runtimeReachability` suppresses a finding. 


| Rule | Suppresses a finding when | 
| --- |--- |
| EQUALS REACHABLE | At least one package is REACHABLE. | 
| EQUALS UNKNOWN | No package is REACHABLE and at least one package is UNKNOWN. | 
| EQUALS NOT\_REACHABLE | All packages are NOT\_REACHABLE. | 
| NOT\_EQUALS REACHABLE | No package is REACHABLE. | 
| NOT\_EQUALS UNKNOWN | At least one package is REACHABLE or all packages are NOT\_REACHABLE. | 
| NOT\_EQUALS NOT\_REACHABLE | At least one package is REACHABLE or UNKNOWN. | 

 The following table describes when a suppression rule on `runtimeReachabilityReason` suppresses a finding. 


| Rule | Suppresses a finding when | 
| --- |--- |
| EQUALS PACKAGE\_IN\_DOCKERFILE\_WORKLOAD\_PATH or EQUALS PROCESS\_OBSERVED\_IN\_EC2\_RUNTIME | At least one package has this reason. | 
| EQUALS PACKAGE\_NOT\_IN\_DOCKERFILE\_WORKLOAD\_PATH or EQUALS PROCESS\_NOT\_OBSERVED\_IN\_EC2\_RUNTIME | All packages have this reason. | 
| NOT\_EQUALS PACKAGE\_IN\_DOCKERFILE\_WORKLOAD\_PATH or NOT\_EQUALS PROCESS\_OBSERVED\_IN\_EC2\_RUNTIME | At least one package is REACHABLE with a different reason or all packages are NOT\_REACHABLE. | 
| NOT\_EQUALS PACKAGE\_NOT\_IN\_DOCKERFILE\_WORKLOAD\_PATH or NOT\_EQUALS PROCESS\_NOT\_OBSERVED\_IN\_EC2\_RUNTIME | At least one package is REACHABLE or all packages are NOT\_REACHABLE with a different reason. | 

 Other package fields in the same rule, such as `name`, `version`, or `purlQualifier`, still match individual packages. For example, consider a rule with `name EQUALS openssl` and `runtimeReachability EQUALS NOT_REACHABLE`. This rule suppresses a finding that has an openssl package only when all packages in the finding are `NOT_REACHABLE`. 

 Findings for unsupported resource types don't include `runtimeReachability` or `runtimeReachabilityReason`, so reachability suppression rules never suppress them. This includes rules that use `NOT_EQUALS`. For example, a rule with `runtimeReachability NOT_EQUALS REACHABLE` doesn't suppress a Lambda function finding. 