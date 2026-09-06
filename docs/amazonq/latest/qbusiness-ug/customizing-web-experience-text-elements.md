

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Customizing text elements
<a name="customizing-web-experience-text-elements"></a>

This topic shows how to customize text elements using the AWS Management Console and the AWS CLI.

**Note**  
When using the console, you can preview changes in real-time as you customize your web experience.

**Topics**
+ [Using the AWS Management Console](#customizing-web-experience-text-elements-using-aws-management-console)
+ [Using the AWS CLI](#customizing-web-experience-text-elements-using-aws-cli)

## Using the AWS Management Console
<a name="customizing-web-experience-text-elements-using-aws-management-console"></a>

The following procedure shows how to update text elements using the console.

1. Sign in to the AWS Management Console and find the Amazon Q Business console.

1. From the Amazon Q Business **Applications** page, select *your application*, then choose **Customize web experience**.

1. In the **Customize web experience** section, choose **Customize web experience** from the right navigation panel.

1. Choose **Text** and enter the following information:
   + **Title**: A title for your web experience (visible to end users).
   + **Subtitle** (optional): Additional information for end users.
   + **Welcome message**: An optional message for end users (consider mentioning data sources and application capabilities).
   + **Display sample prompts**: Enable or disable the display of [sample prompts](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/quick-prompts.html) for the end user's conversation start screen.

1. Choose **Save**.

## Using the AWS CLI
<a name="customizing-web-experience-text-elements-using-aws-cli"></a>

The following code snippet shows how to customize text elements using the AWS CLI.

```
aws qbusiness update-web-experience \
--application-id application-id \
--web-experience-id web-experience-id \
--title optional-title \
--subtitle optional-subtitle \ 
--welcome-message optional-welcome-message \
--sample-prompts-control-mode ENABLED
```