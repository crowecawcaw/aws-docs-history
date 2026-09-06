

# Creating target EMR Cluster/EMR-S application from existing ones
<a name="emr-spark-upgrade-agent-target-cluster"></a>

If you already have an EMR-EC2 cluster running the source Spark version, you can clone it to create a new cluster with the same configuration but an updated EMR release version to run the validation steps during the Upgrade process.

## Steps:
<a name="emr-spark-upgrade-agent-clone-cluster-steps"></a>

1. Sign in to the AWS Management Console and open the Amazon EMR console.

1. In the left navigation pane, choose Clusters under EMR on EC2.

1. From the cluster list:
   + Use search or filters if needed to find your cluster.
   + Select the check box next to the cluster you want to clone.
   + The Clone option will appear at the top of the list. Choose Clone.
   + If the cluster has steps configured, choose Include steps and then Continue to clone the steps along with the other cluster settings.

1. Review the settings for the new cluster that have been copied from the original cluster.

1. Update the Amazon EMR release version to the target version.

1. As a best practice for cost efficiency, consider enabling autoscaling when configuring the cluster to automatically adjust capacity based on workload demands.

1. When you're satisfied with the configuration, select Create cluster to launch the new cluster.

1. Wait for the cluster to reach the Running status and note the cluster ID. Provide this ID to the agent when prompted to validate the updated application.

1. If you prefer to create a new cluster from scratch, please refer to the EMR documentation: [ https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html ](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html).

## Cloning an EMR Serverless application to the target Release Version
<a name="emr-spark-upgrade-agent-clone-serverless"></a>

There is no direct way to clone an EMR Serverless application to a new one with a different EMR release version. Instead, you can use the EMR Serverless SDK/CLI or the console to create a new application and reuse the configuration from an existing one.

Here are some helper CLI commands to get started:

```
aws emr-serverless get-application --application-id XXX > old-config.json  
cat old-config.json | jq '{  
  name: (.application.name + "<suffix to differentiate name from old application>"),  
  releaseLabel: "<target EMR release version>",  
  type: .application.type,  
  initialCapacity: .application.initialCapacity,  
  maximumCapacity: .application.maximumCapacity,  
  autoStartConfiguration: .application.autoStartConfiguration,  
  autoStopConfiguration: .application.autoStopConfiguration,  
  tags: .application.tags,  
  architecture: .application.architecture,  
  runtimeConfiguration: .application.runtimeConfiguration,  
  monitoringConfiguration: .application.monitoringConfiguration  
}' > new-config.json  
aws emr-serverless create-application --cli-input-json file://new-config.json
```

**Note:** Ensure that the job execution role for the new application allows EMR Serverless to assume the role. Review the role's trust policy. If you are reusing the same job execution role from the old application, update the trust policy to include the new application as shown below:

```
#Replace the old application id and new application id in the policy  
{  
    "Version": "2012-10-17",		 	 	  
    "Statement": [  
        {  
            "Sid": "ServerlessTrustPolicy",  
            "Effect": "Allow",  
            "Principal": {  
                "Service": "emr-serverless.amazonaws.com"  
            },  
            "Action": "sts:AssumeRole",  
            "Condition": {  
                "StringLike": {  
                    "aws:SourceArn": [  
                        "arn:aws:emr-serverless:us-east-1:<account>:/applications/<old application id>",  
                        "arn:aws:emr-serverless:us-east-1:<account>:/applications/<new application id>"  
                    ]  
                }  
            }  
        }  
    ]  
}
```