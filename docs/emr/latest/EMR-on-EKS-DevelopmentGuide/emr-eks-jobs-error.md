

# Common errors when running jobs
<a name="emr-eks-jobs-error"></a>

The following errors may occur when you run `StartJobRun` API. The table lists each error and provides mitigation steps so you can address issues quickly.


| Error Message | Error Condition | Recommended Next Step | 
| --- | --- | --- | 
| error: argument --{{argument}} is required | Required parameters are missing. | Add the missing arguments to the API request. | 
| An error occurred (AccessDeniedException) when calling the StartJobRun operation: User: {{ARN}} is not authorized to perform: emr-containers:StartJobRun | Execution role is missing. | See Using [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md).  | 
| An error occurred (AccessDeniedException) when calling the StartJobRun operation: User: {{ARN}} is not authorized to perform: emr-containers:StartJobRun | Caller doesn't have permission to the execution role [valid / not valid format] via condition keys. | See [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md).  | 
| An error occurred (AccessDeniedException) when calling the StartJobRun operation: User: {{ARN}} is not authorized to perform: emr-containers:StartJobRun | Job submitter and Execution role ARN are from different accounts. | Ensure that job submitter and execution role ARN are from the same AWS account. | 
| 1 validation error detected: Value {{Role}} at 'executionRoleArn' failed to satisfy the ARN regular expression pattern: ^arn:(aws[a-zA-Z0-9-]\*):iam::(\\d{12})?:(role((\\u002F)\|(\\u002F[\\u0021-\\u007F]\+\\u002F))[\\w\+=,.@-]\+) | Caller has permissions for the execution role via condition keys, but the role does not satisfy the constraints of ARN format. | Provide the execution role following the ARN format. See [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md).  | 
| An error occurred (ResourceNotFoundException) when calling the StartJobRun operation: Virtual cluster {{Virtual Cluster ID}} doesn't exist. | Virtual cluster ID is not found. | Provide a virtual cluster ID registered with Amazon EMR on EKS. | 
| An error occurred (ValidationException) when calling the StartJobRun operation: Virtual cluster state {{state}} is not valid to create resource JobRun. | Virtual cluster is not ready to execute job. | See [Virtual cluster states](virtual-cluster.md#virtual-cluster-states).  | 
| An error occurred (ResourceNotFoundException) when calling the StartJobRun operation: Release {{RELEASE}} doesn't exist. | The release specified in job submission is incorrect. | See [Amazon EMR on EKS releases](emr-eks-releases.md).  | 
| An error occurred (AccessDeniedException) when calling the StartJobRun operation: User: {{ARN}} is not authorized to perform: emr-containers:StartJobRun on resource: {{ARN}} with an explicit deny.<br />An error occurred (AccessDeniedException) when calling the StartJobRun operation: User: {{ARN}} is not authorized to perform: emr-containers:StartJobRun on resource: {{ARN}} | User is not authorized to call StartJobRun. | See [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md).  | 
| An error occurred (ValidationException) when calling the StartJobRun operation: configurationOverrides.monitoringConfiguration.s3MonitoringConfiguration.logUri failed to satisfy constraint : %s | S3 path URI syntax is not valid. | logUri should be in the format of s3://...  | 

The following errors may occur when you run `DescribeJobRun` API before the job runs.


| Error Message | Error Condition | Recommended Next Step | 
| --- | --- | --- | 
| stateDetails: JobRun submission failed. <br />Classification {{classification}} not supported.<br />failureReason: VALIDATION\_ERROR<br />state: FAILED. | Parameters in StartJobRun are not valid. | See [Amazon EMR on EKS releases](emr-eks-releases.md).  | 
| stateDetails: Cluster {{EKS Cluster ID}} does not exist.<br />failureReason: CLUSTER\_UNAVAILABLE<br />state: FAILED | The EKS cluster is not available. | Check if the EKS cluster exists and has the right permissions. For more information, see [Setting up Amazon EMR on EKS](setting-up.md). | 
| stateDetails: Cluster {{EKS Cluster ID}} does not have sufficient permissions.<br />failureReason: CLUSTER\_UNAVAILABLE<br />state: FAILED | Amazon EMR does not have permissions to access the EKS cluster. | Verify that permissions are set up for Amazon EMR on the registered namespace. For more information, see [Setting up Amazon EMR on EKS](setting-up.md). | 
| stateDetails: Cluster {{EKS Cluster ID}} is currently not reachable.<br />failureReason: CLUSTER\_UNAVAILABLE<br />state: FAILED | EKS cluster is not reachable. | Check if EKS Cluster exists and has the right permissions. For more information, see [Setting up Amazon EMR on EKS](setting-up.md). | 
| stateDetails: JobRun submission failed due to an internal error.<br />failureReason: INTERNAL\_ERROR<br />state: FAILED | An internal error has occurred with the EKS cluster. | N/A | 
| stateDetails: Cluster {{EKS Cluster ID}} does not have sufficient resources.<br />failureReason: USER\_ERROR<br />state: FAILED | There are insufficient resources in the EKS cluster to run the job. | Add more capacity to the EKS node group or set up EKS Autoscaler. For more information, see [Cluster Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/cluster-autoscaler.html). | 

The following errors may occur when you run `DescribeJobRun` API after the job runs.


| Error Message | Error Condition | Recommended Next Step | 
| --- | --- | --- | 
| stateDetails: Trouble monitoring your JobRun. <br />Cluster {{EKS Cluster ID}} does not exist.<br />failureReason: CLUSTER\_UNAVAILABLE<br />state: FAILED | The EKS cluster does not exist. | Check if EKS Cluster exists and has the right permissions. For more information, see [Setting up Amazon EMR on EKS](setting-up.md). | 
| stateDetails: Trouble monitoring your JobRun.<br />Cluster {{EKS Cluster ID}} does not have sufficient permissions.<br />failureReason: CLUSTER\_UNAVAILABLE<br />state: FAILED | Amazon EMR does not have permissions to access the EKS cluster. | Verify that permissions are set up for Amazon EMR on the registered namespace. For more information, see [Setting up Amazon EMR on EKS](setting-up.md). | 
| stateDetails: Trouble monitoring your JobRun.<br />Cluster {{EKS Cluster ID}} is currently not reachable.<br />failureReason: CLUSTER\_UNAVAILABLE<br />state: FAILED | The EKS cluster is not reachable. | Check if EKS Cluster exists and has the right permissions. For more information, see [Setting up Amazon EMR on EKS](setting-up.md). | 
| stateDetails: Trouble monitoring your JobRun due to an internal error<br />failureReason: INTERNAL\_ERROR<br />state: FAILED | An internal error has occurred and is preventing JobRun monitoring. | N/A | 

The following error may occur when a job cannot start and the job waits in the SUBMITTED state for 15 minutes. This can be caused by a lack of cluster resources.


| Error Message | Error Condition | Recommended Next Step | 
| --- | --- | --- | 
| cluster timeout | The job has been in the SUBMITTED state for 15 minutes or more. | You can override the default setting of 15 minutes for this parameter with the configuration override shown below.  | 

Use the following configuration to change the cluster timeout setting to 30 minutes. Notice that you provide the new `job-start-timeout` value in seconds:

```
{
"configurationOverrides": {
  "applicationConfiguration": [{
      "classification": "emr-containers-defaults",
      "properties": {
          "job-start-timeout":"1800"
      }
  }]
}
```