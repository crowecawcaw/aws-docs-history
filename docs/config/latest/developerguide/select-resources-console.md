# Recording resources in the AWS Config console

You can use the AWS Config console to select the types of resources that AWS Config records with the
customer managed configuration recorder.

###### To select resources

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Settings** in the left navigation pane.
3. On the **Customer managed recorder** tab, choose
   **Edit**.
4. In the **Recording method** section, choose a recording strategy. You
   can specify the AWS resources that you want AWS Config to record.

All resource types with customizable overrides
Set up AWS Config to record configuration changes for all current and future supported
resource types in this Region. You can override the recording frequency for specific
resource types or exclude specific resource types from recording. For more
information, see [Supported
Resource Types](resource-config-reference.md "resource-config-reference.md").

    * **Default settings**


    Configure the default recording frequency for all current and future
     supported resource types. For more information see, [Recording Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").




    	+ Continuous recording – AWS Config will record configuration changes
    	 continuously whenever a change occurs.
    	+ Daily recording – You will receive a configuration item (CI)
    	 representing the most recent state of your resources over the last 24-hour
    	 period, only if it’s different from the previous CI recorded.
    ###### Note

    AWS Firewall Manager depends on continuous recording to monitor your resources. If
     you are using Firewall Manager, it is recommended that you set the recording frequency to
     Continuous.
    * **Override settings**


    Override the recording frequency for specific resource types, or exclude
     specific resource types from recording. If you change the recording frequency
     for a resource type or stop recording a resource type, the configuration items
     that were already recorded will remain unchanged.

Specific resource types
Set up AWS Config to record configuration changes for only the resource types that you
specify.

    * **Specific resource types**


    Choose a resource type to record and its frequency. For more information
     see, [Recording Frequency](select-resources.md#select-resources-recording-frequency "select-resources.md#select-resources-recording-frequency").




    	+ Continuous recording – AWS Config will record configuration changes
    	 continuously whenever a change occurs.
    	+ Daily recording – You will receive a configuration item (CI)
    	 representing the most recent state of your resources over the last 24-hour
    	 period, only if it’s different from the previous CI recorded.
    ###### Note

    AWS Firewall Manager depends on continuous recording to monitor your resources. If
     you are using Firewall Manager, it is recommended that you set the recording frequency to
     Continuous.


    If you change the recording frequency for a resource type or stop recording
     a resource type, the configuration items that were already recorded will remain
     unchanged.

5. Choose **Save** to save your changes.

## Considerations When Recording

Resources

**High Number of AWS Config Evaluations**

You might notice increased activity in your account during your initial month recording
with AWS Config when compared to subsequent months. During the initial bootstrapping
process, AWS Config runs evaluations on all the resources in your account that you have selected
for AWS Config to record.

If you are running ephemeral workloads, you may see increased activity from AWS Config as it
records configuration changes associated with creating and deleting these temporary
resources. An _ephemeral workload_ is a temporary use of computing
resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud (Amazon EC2) Spot
Instances, Amazon EMR jobs, and AWS Auto Scaling. . If you want to avoid the increased activity from
running ephemeral workloads, you can set up the customer managed configuration recorder to
exclude these resource types from being recorded, or run these types of workloads in a
separate account with AWS Config turned off to avoid increased configuration recording and rule
evaluations.

Considerations: All resource types with customizable overrides
**Globally recorded resource types | Aurora global clusters are initially
included in recording**

The `AWS::RDS::GlobalCluster` resource type will be recorded in all
supported AWS Config Regions where the customer managed configuration recorder is
enabled.

If you do not want to record `AWS::RDS::GlobalCluster` in all enabled
Regions, choose "AWS RDS GlobalCluster", and choose the override
"Exclude from recording".

**Global resource types | IAM resource types are initially excluded from
recording**

The global IAM resource types are initially excluded from recording to help you
reduce costs. This bundle includes IAM users, groups, roles, and customer managed
policies. Choose **Remove** to remove the override and include
these resources in your recording.

Additionally, the global IAM resource types (`AWS::IAM::User`,
`AWS::IAM::Group`, `AWS::IAM::Role`, and
`AWS::IAM::Policy`) cannot be recorded in Regions supported by AWS Config after
February 2022. For a list of those Regions, see [Recording AWS Resources | Global Resources](select-resources.md#select-resources-all "select-resources.md#select-resources-all").

**Limits**

You can add up to 100 frequency overrides and 600 exclusion overrides.

Daily recording is not supported for the following resource types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`

Considerations: Specific resource types
**Region Availability**

Before specifying a resource type for AWS Config to track, check [Resource Coverage by Region
Availability](what-is-resource-config-coverage.md "what-is-resource-config-coverage.md") to see if the resource type is supported in the AWS Region
where you set up AWS Config. If a resource type is supported by AWS Config in at least one Region,
you can enable the recording of that resource type in all Regions supported by AWS Config,
even if the specified resource type is not supported in the AWS Region where you set
up AWS Config.

**Limits**

No limits if all resource types have the same frequency. You can add up to 100
resource types with Daily frequency if at least one resource type is set to
Continuous.

The Daily frequency is not supported for the following resource types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`
