

# Using the Neptune ML AWS CloudFormation template to get started quickly in a new DB cluster
<a name="machine-learning-quick-start"></a>

The easiest way to get started with Neptune ML is to use the CloudFormation quick-start template. This template installs all necessary components, including a new Neptune DB cluster, all the necessary IAM roles, and a new Neptune graph-notebook to make working with Neptune ML easier.

**To create the Neptune ML quick-start stack**

1. To launch the CloudFormation stack on the CloudFormation console, choose one of the **Launch Stack** buttons in the following table:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-quick-start.html)

1.  On the **Select Template** page, choose **Next**.

1. On the **Specify Details** page, choose **Next**.

1. On the **Options** page, choose **Next**.

1. On the **Review** page, there are two check boxes that you need to check:
   + The first one acknowledges that AWS CloudFormation might create IAM resources with custom names.
   + The second acknowledges that AWS CloudFormation might require the `CAPABILITY_AUTO_EXPAND` capability for the new stack. `CAPABILITY_AUTO_EXPAND` explicitly allows CloudFormation to expand macros automatically when creating the stack, without prior review.

     Customers often create a change set from a processed template so that the changes made by macros can be reviewed before actually creating the stack. For more information, see the CloudFormation [CreateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html) API.

   Then choose **Create**.

The quick-start template creates and sets up the following:
+ A Neptune DB cluster.
+ The necessary IAM roles (and attaches them).
+ The necessary Amazon EC2 security group.
+ The necessary SageMaker AI VPC endpoints.
+ A DB cluster parameter group for Neptune ML.
+ The necessary parameters in that parameter group.
+ A SageMaker AI notebook with pre-populated notebook samples for Neptune ML. Note that not all instance sizes are available in every region, so you need to be sure that the notebook instance size selected is one that your region supports.
+ The Neptune-Export service.

When the quick-start stack is ready, go to the SageMaker AI notebook that the template created and check out the pre-populated examples. They will help you download sample datasets to use for experimenting with Neptune ML capabilities.

They can also save you a lot of time when you are using Neptune ML. For example, see the [%neptune\_ml](notebooks-magics.md#notebooks-line-magics-neptune_ml) line magic, and the [%%neptune\_ml](notebooks-magics.md#notebooks-cell-magics-neptune_ml) cell magic that these notebooks support.

You can also use the following AWS CLI command to run the quick-start CloudFormation template:

```
aws cloudformation create-stack \
  --stack-name neptune-ml-fullstack-$(date '+%Y-%m-%d-%H-%M') \
  --template-url https://aws-neptune-customer-samples.s3.amazonaws.com/v2/cloudformation-templates/neptune-ml-nested-stack.json \
  --parameters ParameterKey=EnableIAMAuthOnExportAPI,ParameterValue={{(true if you have IAM auth enabled, or false otherwise)}} \
               ParameterKey=Env,ParameterValue=test$(date '+%H%M')\
  --capabilities CAPABILITY_IAM \
  --region {{(the AWS region, like us-east-1)}} \
  --disable-rollback \
  --profile {{(optionally, a named CLI profile of yours)}}
```