

# Resolution with AWS Entity Resolution
<a name="entity-resolution"></a>

 Amazon Connect Customer Profiles offers a *managed connector* that you can use to directly import matching results from AWS Entity Resolution. With this integration, you can use the powerful matching capabilities of AWS Entity Resolution while maintaining your customer profiles in Connect Customer. 

 AWS Entity Resolution helps you match and link related records across your various data sources using flexible matching techniques including rules, machine learning, or third-party data providers. By connecting Entity Resolution results to Customer Profiles, you can: 
+ Consolidate customer records from multiple systems more accurately
+ Apply sophisticated matching logic based on your specific business needs
+ Enhance customer profiles with linked data from various applications and channels
+ Maintain consistent customer views across your organization

 To get started using AWS Entity Resolution with Customer Profiles, you'll need to first set up your matching workflows in the AWS Entity Resolution console. [Learn more about AWS Entity Resolution](https://docs.aws.amazon.com/entityresolution/latest/userguide/create-matching-workflow.html). 

 To set this up you need the following prerequisites: 
+ Active Amazon Connect instance with Customer Profiles enabled
+ Customer data stored in Amazon S3
+ Appropriate IAM permissions to access AWS Entity Resolution

**To set up follow these steps:**

1. Create a Customer Profiles domain
   + If you haven't already, create a Customer Profiles domain in your Connect instance
   + Navigate to the Customer Profiles section in your Amazon Connect console
   + Note: You'll see a new section for AWS Entity Resolution after domain creation

1. Configure AWS Entity Resolution
   + In your Customer Profiles domain, locate the AWS Entity Resolution section
   + Choose "Set up AWS Entity Resolution"
   + You'll be redirected to the AWS Entity Resolution console.
     + Create a matching workflow
     + Configure your S3 data sources
     + Define matching criteria
     + Review and activate your matching workflow

1. Connect Entity Resolution results to Customer Profiles
   + Return to your Customer Profiles domain
   + Select your Entity Resolution workflow
   + Configure how matched records should be consolidated
   + Enable the integration