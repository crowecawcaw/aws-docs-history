# Customizing text

elements

This topic shows how to customize text elements using the AWS Management Console and the
AWS CLI.

###### Note

When using the console, you can preview changes in real-time as you customize your
web experience.

###### Topics

- [Using the AWS Management Console](#customizing-web-experience-text-elements-using-aws-management-console "#customizing-web-experience-text-elements-using-aws-management-console")
- [Using the
  AWS CLI](#customizing-web-experience-text-elements-using-aws-cli "#customizing-web-experience-text-elements-using-aws-cli")

## Using the AWS Management Console

The following procedure shows how to update text elements using the
console.

1. Sign in to the AWS Management Console and find the Amazon Q Business
   console.
2. From the Amazon Q Business
   **Applications** page, select _your
   application_, then choose **Customize web
   experience**.
3. In the **Customize web experience** section,
   choose **Customize web experience** from the
   right navigation panel.
4. Choose **Text** and enter the following
   information:
   - **Title**: A title for your web
     experience (visible to end users).
   - **Subtitle** (optional): Additional
     information for end users.
   - **Welcome message**: An optional
     message for end users (consider mentioning data sources and
     application capabilities).
   - **Display sample prompts**: Enable or
     disable the display of [sample
     prompts](../business-use-dg/quick-prompts.md "../business-use-dg/quick-prompts.md") for the end user's conversation start
     screen.

5. Choose **Save**.

## Using the

AWS CLI

The following code snippet shows how to customize text elements using the
AWS CLI.

```

aws qbusiness update-web-experience \
--application-id application-id \
--web-experience-id web-experience-id \
--title optional-title \
--subtitle optional-subtitle \
--welcome-message optional-welcome-message \
--sample-prompts-control-mode ENABLED

```
