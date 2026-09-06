

# Deploy Active Directory to a new or existing VPC (AWS CLI)
<a name="launch-wizard-ad-deploying-cli"></a>

You can use the AWS Launch Wizard [CreateDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_CreateDeployment.html) API operation to deploy Active Directory. To create a deployment, you must provide values for various *specifications*. Specifications are a collection of settings that define how your deployment should be created and configured. A workload will have one or more deployment patterns with differing required and optional specifications.

If you want to use the **Clone deployment** action on your deployment, you must create your deployment using the Launch Wizard console.

## Prerequisites for deploying Active Directory with the AWS CLI
<a name="launch-wizard-ad-deploying-cli-prereqs"></a>

Before deploying Active Directory with the AWS CLI, ensure you have met the following prerequisites:
+ Install and configure the AWS CLI. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Complete the steps in the previous section titled **Set up**. Some deployment patterns have requirements that must be met for a deployment to be successful.

## Create an Active Directory deployment with the AWS CLI
<a name="launch-wizard-ad-deploying-cli-example"></a>

You can create a deployment for your Active Directory application using the `CreateDeployment` Launch Wizard API operation.

**To create a deployment for Active Directory using the AWS CLI**

1. List the available workload names using the [ListWorkloads](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html) Launch Wizard API operation.

   The following example shows listing the available workloads:

   ```
   aws launchwizard list-workloads --region {{us-east-1}}
   {
       "workloads": [
           {
               "displayName": "Remote Desktop Gateway",
               "workloadName": "RDGW"
           },
           {
               "displayName": "MS SQL Server",
               "workloadName": "SQL"
           },
           {
               "displayName": "SAP",
               "workloadName": "SAP"
           },
           {
               "displayName": "Microsoft Active Directory",
               "workloadName": "MicrosoftActiveDirectory"
           }
           ...
       ]
   }
   ```

1. Specify the desired workload name with the [ListWorkloadDeploymentPatterns](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html) operation to describe the supported values for the deployment pattern names.

   The following example lists the available workload patterns for a given workload:

   ```
   aws launch-wizard list-workload-deployment-patterns --workload-name {{MicrosoftActiveDirectory}} --region {{us-east-1}}
   {
       "workloadDeploymentPatterns": [
           {
               "deploymentPatternName": "adAwsManagedExistingVpc",
               "description": "Example description.",
               "displayName": "ExampleDisplayName",
               "status": "ACTIVE",
               "workloadName": "MicrosoftActiveDirectory",
               "workloadVersionName": "2024-05-03-00-00-00"
           },
           ...
       ]
   }
   ```

1. Use the workload and deployment pattern names you discovered with the [GetWorkloadDeploymentPattern](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html) operation to list the specification details.

   The following example lists the workload specifications of a given workload and deployment pattern:

   ```
   aws launchwizard get-workload-deployment-pattern --workload-name {{MicrosoftActiveDirectory}} --deployment-pattern-name {{adAwsManagedExistingVpc}} --region {{us-east-1}}
   {
       "workloadDeploymentPattern": {
           "deploymentPatternName": "adAwsManagedExistingVpc",
           "description": "Example description.",
           "displayName": "ExampleDisplayName",
           "specifications": [
               {
                   "description": "Enter an SNS topic for AWS Launch Wizard to send notifications and alerts.",
                   "name": "AWS:LaunchWizard:TopicArn",
                   "required": "No"
               },
               {
                   "description": "When a deployment fails, your provisioned resources will be deleted/rolled back by default. If deactivated, the provisioned resources will be deleted when you delete your deployment from the Launch Wizard console.",
                   "name": "AWS:LaunchWizard:DisableRollbackFlag",
                   "required": "No"
               },
               {
                   "allowedValues": [
                       "true",
                       "false"
                   ],
                   "description": "Cloud Watch Application Insights monitoring",
                   "name": "SetupAppInsightsMonitoring",
                   "required": "Yes"
               },
               ...
           ]
       }
   }
   ```

1. With the workload specifications retrieved, you must provide values for any specification `name` with a `required` value of `Yes`. You can also provide any optional specifications you require for your deployment. We recommend that you pass inputs to the `specifications` parameter for your deployment as a file for easier usage.

   Your JSON file's format should resemble the following:

   ```
   {
     "{{ExampleName1}}": "{{ExampleValue1}}",
     "{{ExampleName2}}": "{{ExampleValue2}}",
     "{{ExampleName3}}": "{{ExampleValue3}}"
   }
   ```

1. With the specifications file created, you can create a deployment for your chosen workload and deployment pattern.

   The following example creates a deployment with specifications defined in a file:

   ```
   aws launch-wizard create-deployment --workload-name {{MicrosoftActiveDirectory}} --deployment-pattern-name {{adAwsManagedExistingVpc}} --name {{ExampleDeploymentName}} --region {{us-east-1}} --specifications file://{{specifications.json}}
   ```