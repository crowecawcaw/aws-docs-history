

# Set up in the CodeGuru Profiler console
<a name="setting-up-long"></a>

## Step 2: Create a CodeGuru Profiler profiling group
<a name="setting-up-step-2"></a>

A profiling group can profile one or more applications. Data is aggregated and displayed based on the whole profiling group.

For example, if you have a collection of microservices that handle restaurant recommendations, you can collect profile data and identify performance issues across all these microservices in a single profiling group named "Restaurant-Recommendations". 

**To create a profiling group from the CodeGuru Profiler console**

1. Sign in to the AWS Management Console, and then open the CodeGuru Profiler console at [https://console.aws.amazon.com/codeguru/profiler](https://console.aws.amazon.com/codeguru/profiler).

1. In the navigation pane on the left, choose **Profiler**, and then choose **Profiling groups**.

1. On the **Profiling groups** page, choose **Create profiling group**.

1. Provide a **Name** for the new profiling group. Choose the compute platform that on which your applications are running. If your applications run on AWS Lambda, choose the **AWS Lambda** option. Choose **Other** if your applications run on a compute platform other than AWS Lambda, such as Amazon EC2, on-premises servers, or a different platform. 

1. Choose **Create profiling group**.

## Step 3: Set permissions
<a name="setting-up-step-3"></a>

The CodeGuru Profiler profiling agent needs permissions to write data to the profiling group. 

You can add the necessary permissions by adding the following policy.

```
arn:aws:iam::aws:policy/AmazonCodeGuruProfilerAgentAccess
```

**To set permissions for the new CodeGuru Profiler agent:**

1. Start by choosing **Give access to users and roles**. Choose the IAM users and roles that can submit profiling data and configure the agent. 

1. If your applications run on AWS Lambda, choose the role that your AWS Lambda function uses. 

1. After you grant permissions for a user or role, you don't need to attach IAM policies for agent permissions.  
![Image: Manage user and role permissions to submit profiling data.](http://docs.aws.amazon.com/codeguru/latest/profiler-ug/images/manage-permissions.png)

   Use `IAM:ListUsers` and `IAM:ListRoles` permissions to see your users and roles. Otherwise, you can add a user or Amazon Resource Name (ARN) role. You'll see the following message.   
![Image: Error message on the manage permissions section. Cannot list users and roles.](http://docs.aws.amazon.com/codeguru/latest/profiler-ug/images/manage-permissions-error.png)

   Alternatively, you can add a policy like the following to the role that your application uses. For more information about roles, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html).

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "codeguru-profiler:ConfigureAgent",
                   "codeguru-profiler:PostAgentProfile"
               ],
               "Resource": "arn:aws:codeguru-profiler:{{us-east-1}}:{{123456789012}}:profilingGroup/{{profilingGroupName}}"
           }
       ]
   }
   ```

If your application is running in a Region that CodeGuru Profiler doesn't support and if you have the appropriate permissions, you can submit profiling data to one of the supported Regions. For more information about using CodeGuru Profiler in a Region it doesn't support, see [Working with unsupported Regions](working-with-unsupported-regions.md).

## Step 4: Start CodeGuru Profiler in your application
<a name="setting-up-step-4"></a>

### Run your application with the profiling agent
<a name="setting-up-agent"></a>

Run your application with the CodeGuru Profiler profiling agent. You can use CodeGuru Profiler on your Python or Java virtual machine (JVM)-based applications.

For your JVM-based application, you can either start the agent as a JVM agent, or start it manually with a code change in your application. To start profiling your application, see [Integrating with JVM](integrating-with-java.md).

To start profiling your Python application, see [Integrating with Python](integrating-with-python.md).

### Enable data collection for the heap summary visualization
<a name="setting-up-heap-summary"></a>

The CodeGuru Profiler heap summary shows your application's heap usage over time. This feature is available for JVM applications. For more information on the heap summary, see [Understanding the heap summary](working-with-visualizations-heap-summary.md).

Heap summary collection requires Java agent version 1.2.6 or greater. Opt in to heap summary data collection by completing the onboarding method used to enable the agent. The following are the onboarding methods from which you can choose.

#### Command line (-javaagent)
<a name="setting-up-heap-summary-cli"></a>

Add `heapSummaryEnabled:true`. The following example shows how to enable heap summary collection.

```
-javaagent:/path/to/codeguru-profiler-java-agent-standalone-1.2.6.jar="profilingGroupName:myProfilingGroup,heapSummaryEnabled:true"
```

#### Update your code
<a name="setting-up-heap-summary-code"></a>

Set `.withHeapSummary` to `true`. The following is an example of what your code might look like.

```
class MyClass {
    public static void main(String[] args) {
        Profiler.builder()
            .profilingGroupName("MyProfilingGroup")
            .withHeapSummary(true) // optional - to start without heap profiling set to false or remove line
            .build()
            .start();
        ...
    }
```

#### Environment variables
<a name="setting-up-heap-summary-variable"></a>

Set `AWS_CODEGURU_PROFILER_HEAP_SUMMARY_ENABLED` to `true`.