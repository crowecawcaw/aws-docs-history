

# Creating an Amazon SQS queue using CloudFormation
<a name="create-queue-cloudformation"></a>

Use the CloudFormation console along with a JSON or YAML template to create an Amazon SQS queue. For more details, see [Working with CloudFormation Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) and the [`AWS::SQS::Queue` Resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html) in the *AWS CloudFormation User Guide*.

**To use CloudFormation to create an Amazon SQS queue.**

1. Copy the following JSON code to a file named `MyQueue.json`. To create a standard queue, omit the `FifoQueue` and `ContentBasedDeduplication` properties. For more information on content-based deduplication, see [Exactly-once processing in Amazon SQS](FIFO-queues-exactly-once-processing.md).
**Note**  
The name of a FIFO queue must end with the `.fifo` suffix.

   ```
   {
      "AWSTemplateFormatVersion": "2010-09-09",
      "Resources": {
         "MyQueue": {
            "Properties": {
               "QueueName": "MyQueue.fifo",
               "FifoQueue": true,
               "ContentBasedDeduplication": true
                },
            "Type": "AWS::SQS::Queue"
            }
         },
      "Outputs": {
         "QueueName": {
            "Description": "The name of the queue",
            "Value": {
               "Fn::GetAtt": [
                  "MyQueue",
                  "QueueName"
               ]
            }
         },
         "QueueURL": {
            "Description": "The URL of the queue",
            "Value": {
               "Ref": "MyQueue"
            }
         },
         "QueueARN": {
            "Description": "The ARN of the queue",
            "Value": {
               "Fn::GetAtt": [
                  "MyQueue",
                  "Arn"
               ]
            }
         }
      }
   }
   ```

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation), and then choose **Create Stack**.

1. On the **Specify Template** panel, choose **Upload a template file**, choose your `MyQueue.json` file, and then choose **Next**.

1. On the **Specify Details** page, type `MyQueue` for **Stack Name**, and then choose **Next**.

1. On the **Options** page, choose **Next**.

1. On the **Review** page, choose **Create**.

   CloudFormation begins to create the `MyQueue` stack and displays the **CREATE\_IN\_PROGRESS** status. When the process is complete, CloudFormation displays the **CREATE\_COMPLETE** status.  
![The CloudFormation console displaying the CREATE_COMPLETE status.](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/sqs-tutorials-creating-queue-cfn-create-complete.png)

1. (Optional) To display the name, URL, and ARN of the queue, choose the name of the stack and then on the next page expand the **Outputs** section.