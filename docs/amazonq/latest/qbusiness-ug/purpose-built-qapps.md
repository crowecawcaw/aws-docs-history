

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Creating purpose-built *Amazon Q Apps*
<a name="purpose-built-qapps"></a>

**Important**  
As of July 1, 2024, Amazon Q Apps are available only to [Amazon Q Business Pro users](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#managing-sub-tiers). Amazon Q Business Lite users will no longer be able to create, run, or view Q Apps. To access, Q Apps, Lite users must upgrade to Amazon Q Business Pro.  
As of August 30, 2024, all Amazon Q Apps created by Lite users who did not upgrade their account to Amazon Q Business Pro have been deleted.

You and your web experience users can create lightweight, purpose-built *Amazon Q Apps* within your broader Amazon Q Business application environment. Using your enterprise data, users can create a generative AI-powered app that streamlines their tasks. These Q Apps can be easily created by anyone at the click of a button, transforming their conversations with an Amazon Q Business assistant into reusable and shareable Amazon Q Apps.

Teams across your organization can create Amazon Q Apps tailored to their specific workflows and business needs. When your Amazon Q Business assistant generates useful content, users can transform those conversations into reusable apps that automate repetitive tasks and ensure consistency. The following examples show how different teams might use Amazon Q Apps:

**Example Marketing content generator**  
A marketing team member creates a Amazon Q App that generates social media posts following company branding guidelines. The app includes:  
+ Input card: Product name and key features
+ Text output card: Generates professional post with company tone
+ Text output card: Creates social-media-friendly version
Result: Team members can quickly generate consistent branded content for any product launch.

**Example Employee onboarding assistant**  
An HR team creates a Amazon Q App to streamline new employee setup:  
+ Input card: Employee name, department, start date
+ Plugin card: Creates Jira ticket for IT equipment setup
+ Text output card: Generates personalized welcome email
+ File upload card: Processes signed documents

Amazon Q Apps is enabled by default when you create a new Amazon Q Business application environment using [IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) or [IAM Federation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html) in the Amazon Q Business console. Amazon Q Apps can be accessed through the web experience.

You can also create and manage Q Apps programmatically. For an more information, see [Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Operations_QApps.html) in the *Amazon Q Business API Reference*.

**Topics**
+ [Prerequisites for Amazon Q Apps](purpose-built-qapps-prerequisites.md)
+ [Managing Amazon Q Apps](purpose-built-qapps-manage.md)
+ [Using the web experience to create and run Amazon Q Apps](purpose-built-qapps-web-experience.md)
+ [Sharing Amazon Q Apps](qapps-private-sharing.md)
+ [Custom labels for Amazon Q Apps](qapps-custom-labels.md)
+ [Understanding and managing Verified Amazon Q Apps](verfied-apps-management.md)
+ [Data collection in Amazon Q Apps](q-apps-forms.md)
+ [Using plugins in Amazon Q Apps](qapps-plugins.md)