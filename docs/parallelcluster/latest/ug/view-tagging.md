

# View tags
<a name="view-tagging"></a>

Complete the following steps to view tags in the Amazon EC2 section of the AWS Management Console.

View tags

1. Navigate the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. To view all cluster tags, choose **Tags** in the navigation pane.

1. To view cluster tags by instance, choose **Instances** in the navigation pane.

1. Select a cluster instance.

1. Choose the **Manage tags** tab in the instance details and view the tags.

1. Choose the **Storage** tab in the instance details.

1. Select the **Volume ID**.

1. In **Volumes**, choose the volume.

1. Choose the **Tags** tab in the volume details and view the tags.


**AWS ParallelCluster head node instance tags**  

| Key | Tag value | 
| --- | --- | 
| `parallelcluster:cluster-name` | `{{clustername}}` | 
| `Name` | `HeadNode` | 
| `aws:ec2launchtemplate:id` | `{{lt-1234567890abcdef0}}` | 
| `aws:ec2launchtemplate:version` | `{{1}}` | 
| `parallelcluster:node-type` | `HeadNode` | 
| `aws:cloudformation:stack-name` | `{{clustername}}` | 
| `aws:cloudformation:logical-id` | `HeadNode` | 
| `aws:cloudformation:stack-id` | `arn:aws:cloudformation:{{region-id}}:{{ACCOUNTID}}:stack/{{clustername}}/{{1234abcd-12ab-12ab-12ab-1234567890abcdef0}}` | 
| `parallelcluster:version` | `{{3.15.1}}` | 


**AWS ParallelCluster head node root volume tags**  

| Tag key | Tag value | 
| --- | --- | 
| `parallelcluster:cluster-name` | `{{clustername}}` | 
| `parallelcluster:node-type` | `HeadNode` | 
| `parallelcluster:version` | `{{3.15.1}}` | 


**AWS ParallelCluster compute node instance tags**  

| Key | Tag value | 
| --- | --- | 
| `parallelcluster:cluster-name` | `{{clustername}}` | 
| `parallelcluster:compute-resource-name` | `{{compute-resource-name}}` | 
| `aws:ec2launchtemplate:id` | `{{lt-1234567890abcdef0}}` | 
| `aws:ec2launchtemplate:version` | `{{1}}` | 
| `parallelcluster:node-type` | `Compute` | 
| `parallelcluster:queue-name` | `{{queue-name}}` | 
| `parallelcluster:version` | `{{3.15.1}}` | 


**AWS ParallelCluster compute node root volume tags**  

| Tag key | Tag value | 
| --- | --- | 
| `parallelcluster:cluster-name` | `{{clustername}}` | 
| `parallelcluster:compute-resource-name` | `{{compute-resource-name}}` | 
| `parallelcluster:node-type` | `Compute` | 
| `parallelcluster:queue-name` | `{{queue-name}}` | 
| `parallelcluster:version` | `{{3.15.1}}` | 


**PCUI tags**  

| Tag key | Tag value | 
| --- | --- | 
| `parallelcluster-ui` | `true` | 