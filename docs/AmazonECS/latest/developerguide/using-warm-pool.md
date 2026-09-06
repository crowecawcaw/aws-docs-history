

# Configuring pre-initialized instances for your Amazon ECS Auto Scaling group
<a name="using-warm-pool"></a>

Amazon ECS supports Amazon EC2 Auto Scaling warm pools. A warm pool is a group of pre-initialized Amazon EC2 instances ready to be placed into service. Whenever your application needs to scale out, Amazon EC2 Auto Scaling uses the pre-initialized instances from the warm pool rather than launching cold instances, allows for any final initialization process to run, and then places the instance into service.

To learn more about warm pools and how to add a warm pool to your Auto Scaling group, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) *in the Amazon EC2 Auto Scaling User Guide*.

When you create or update a warm pool for an Auto Scaling group for Amazon ECS , you cannot set the option that returns instances to the warm pool on scale in (`ReuseOnScaleIn`). For more information, see [put-warm-pool](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-warm-pool.html) in the *AWS Command Line Interface Reference*.

To use warm pools with your Amazon ECS cluster, set the `ECS_WARM_POOLS_CHECK` agent configuration variable to `true` in the **User data** field of your Amazon EC2 Auto Scaling group launch template. 

The following shows an example of how the agent configuration variable can be specified in the **User data** field of an Amazon EC2 launch template for Linux instances. Replace {{MyCluster}} with the name of your cluster. For Windows instances, see [Using warm pools with Amazon ECS Windows instances](#using-warm-pool-windows-lifecycle-hooks).

```
#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
ECS_CLUSTER={{MyCluster}}
ECS_WARM_POOLS_CHECK=true
EOF
```

The `ECS_WARM_POOLS_CHECK` variable is only supported on agent versions `1.59.0` and later. For more information about the variable, see [Amazon ECS container agent configuration](ecs-agent-config.md).

## Using warm pools with Amazon ECS Windows instances
<a name="using-warm-pool-windows-lifecycle-hooks"></a>

When using warm pools with the **Stopped** pool state on Windows instances, use Amazon EC2 Auto Scaling lifecycle hooks to ensure user data execution completes before the instance is stopped. Without lifecycle hooks, the instance may be stopped before Amazon ECS initialization finishes.

To configure lifecycle hooks for Windows warm pool instances:

1. Add the following IAM policy to your container instance role to allow the instance to complete the lifecycle action:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "autoscaling:CompleteLifecycleAction"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

1. Add a lifecycle hook to your Auto Scaling group on *Instance Launching* with `ABANDON` as the default result and a heartbeat timeout that allows enough time for Amazon ECS initialization (for example, 10 minutes). For more information, see [Add lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/adding-lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

1. Use the following user data that creates a scheduled task to complete the lifecycle action after a delay. The delay ensures EC2Launch finishes saving its state before the instance is stopped. Replace {{MyCluster}}, {{my-lifecycle-hook}}, and {{my-asg-name}} with your values.

   ```
   <powershell>
   $lifecycleHookName = "{{my-lifecycle-hook}}"
   $autoScalingGroupName = "{{my-asg-name}}"
   
   $scriptContent = @'
   $token = Invoke-RestMethod -Method Put -Uri http://169.254.169.254/latest/api/token -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"}
   $instanceId = Invoke-RestMethod -Method Get -Uri http://169.254.169.254/latest/meta-data/instance-id -Headers @{"X-aws-ec2-metadata-token" = $token}
   $region = Invoke-RestMethod -Method Get -Uri http://169.254.169.254/latest/meta-data/placement/region -Headers @{"X-aws-ec2-metadata-token" = $token}
   $lifecycleHookName = "{{my-lifecycle-hook}}"
   $autoScalingGroupName = "{{my-asg-name}}"
   Complete-ASLifecycleAction -LifecycleHookName $lifecycleHookName -AutoScalingGroupName $autoScalingGroupName -InstanceId $instanceId -LifecycleActionResult 'CONTINUE' -Region $region
   '@
   Set-Content -Path "C:\ProgramData\Amazon\ECS\complete-lifecycle.ps1" -Value $scriptContent
   
   try
   {
       [Environment]::SetEnvironmentVariable("ECS_WARM_POOLS_CHECK", "true", "Machine")
       Import-Module ECSTools
       Initialize-ECSAgent -Cluster {{MyCluster}} -EnableTaskIAMRole
   
       $taskAction = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File C:\ProgramData\Amazon\ECS\complete-lifecycle.ps1"
       $taskTriggerOnce = New-ScheduledTaskTrigger -Once -At ((Get-Date).AddSeconds(60))
       $taskTriggerStartup = New-ScheduledTaskTrigger -AtStartup
       $taskTriggerStartup.Delay = "PT60S"
       $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable
       $taskPrincipal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
       Register-ScheduledTask -TaskName "CompleteLifecycleHook" -Action $taskAction -Trigger $taskTriggerOnce, $taskTriggerStartup -Principal $taskPrincipal -Settings $settings -Force
   }
   catch
   {
       $token = Invoke-RestMethod -Method Put -Uri http://169.254.169.254/latest/api/token -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"}
       $INSTANCE = Invoke-RestMethod -Method Get -Uri http://169.254.169.254/latest/meta-data/instance-id -Headers @{"X-aws-ec2-metadata-token" = $token}
       $region = Invoke-RestMethod -Method Get -Uri http://169.254.169.254/latest/meta-data/placement/region -Headers @{"X-aws-ec2-metadata-token" = $token}
       Complete-ASLifecycleAction -InstanceId $INSTANCE -LifecycleHookName $lifecycleHookName -AutoScalingGroupName $autoScalingGroupName -LifecycleActionResult ABANDON -Region $region
   }
   </powershell>
   ```

This user data script does the following:
+ Initializes the Amazon ECS agent with the warm pools check enabled.
+ Creates a scheduled task that waits 60 seconds after user data completes, and then signals the lifecycle hook to proceed.
+ Creates a scheduled task that runs on every subsequent reboot, and signals the lifecycle hook to proceed after 60 seconds.
+ If initialization fails, the lifecycle action is completed with `ABANDON` so the instance is terminated and replaced.