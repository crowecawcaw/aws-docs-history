

# Lambda event source mapping execution block
<a name="lambda-event-source-mapping-block"></a>

The Lambda event source mapping execution block allows you to enable or disable Lambda event source mappings as part of your recovery operations. Event source mappings are Lambda resources that read from event sources such as Amazon Kinesis, Amazon DynamoDB Streams, Amazon Simple Queue Service, and Amazon Managed Streaming for Apache Kafka (Amazon MSK), and invoke Lambda functions with batches of records.

**Note**  
This execution block manages event source mappings only. Lambda triggers, which are service-side event-driven invocations from services such as Amazon S3, Amazon Simple Notification Service, and Amazon Simple Email Service, are not supported by this execution block.

## Configuration
<a name="lambda-event-source-mapping-block-config"></a>

This block can be configured to perform one action (enable or disable) on one event source mapping resource at a time.

To configure a Lambda event source mapping execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Lambda event source mapping execution block sample policy](security_iam_region_switch_lambda_esm.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Action: **Choose whether to **Enable** or **Disable** the event source mapping when this step runs.

1. **Lambda event source mapping ARN to enable or disable when activating/deactivating {{Region-1}}: **Enter the event source mapping ARN to act on when you activate/deactivate {{Region-1}}.

1. **Lambda event source mapping ARN to enable or disable when activating/deactivating {{Region-2}}: **Enter the event source mapping ARN to act on when you activate/deactivate {{Region-2}}.

1. **Timeout: **Enter a timeout value.

1. **Ungraceful execution: **Choose whether to skip this execution block during ungraceful (unplanned) executions.

Then, choose **Save step.**

The event source mappings must be in one of the Regions that the plan is configured for. However, the Region you are activating and the Region where the event source mapping is acted on do not need to match.

For example, to disable event processing in the deactivating Region when you activate the other Region:
+ **Event source mapping ARN to disable when activating {{us-west-2}}**: `arn:aws:lambda:{{us-east-1}}:123456789012:event-source-mapping:uuid-1`.
+ **Event source mapping ARN to disable when activating {{us-east-1}}**: `arn:aws:lambda:{{us-west-2}}:123456789012:event-source-mapping:uuid-2`.

This block supports both graceful and ungraceful execution modes. Ungraceful mode is designed for unplanned failover scenarios. You typically enable skipping the step during ungraceful executions on this execution block when the step is configured to perform an action in the deactivating Region. During a failover, you may want to stop processing events in deactivating Region and start processing in activating Region. To achieve this, you set up two Lambda event source mapping execution blocks in a sequence: one to disable the event source mapping resource in deactivating Region, and one to enable the event source mapping resource in activating Region. 

## How it works
<a name="lambda-event-source-mapping-block-how"></a>

The Lambda event source mapping execution block enables or disables an event source mapping on a Lambda function. When the block is called during plan execution, Region switch invokes the Lambda `UpdateEventSourceMapping` API to perform the configured action (enable or disable) on the specified Lambda event source mapping. Region switch then waits until the event source mapping reaches the target state and updates the status of this step (complete or paused because of failure) before proceeding to the next step in the plan. If the mapping is already in the desired state, Region switch marks the step as complete immediately. When a plan containing this execution block configured for ungraceful execution is run in ungraceful mode, the plan skips the execution of this step.