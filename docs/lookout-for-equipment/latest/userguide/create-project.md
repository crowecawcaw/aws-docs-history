

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Creating your project
<a name="create-project"></a>

After you [set up your account](getting-started-brain.md), the next step is to create a project.

A project is a collection of resources associated with a single industrial asset that you want to monitor. Each project contains a dataset: a collection of historical data that you ingest into Amazon Lookout for Equipment.

![alt_text](http://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/images/L4E-project-start.png)


**To create a project**

1. Open [Amazon Lookout for Equipment console.](https://console.aws.amazon.com/lookoutequipment/home)

1. Choose **Create project**.

## Tagging your project
<a name="tag-project"></a>

 Optionally, you can assign tags to your project. Each tag is a label consisting of a user-defined key and value. Tags can help you associate your project with other resources in your account. To learn more, see [Tagging resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). 

![alt_text](http://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/images/L4E-project-start-tags.png)


Now that you've created your project, you'll need to [check the formatting of your data](formatting-data.md). Then you'll need to organize your files before you upload them to .