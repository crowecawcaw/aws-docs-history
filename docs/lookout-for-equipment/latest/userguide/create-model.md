On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Training your model

###### Note

You can also train your model [with the
SDK](SDK-examples.md#create-model-sdk "SDK-examples.md#create-model-sdk").

You've ingested your dataset, and you've reviewed any issues with the job, the files, or
the sensors. You've also decided which sensors are providing the data that will be used to
train your model. Now it's time to move forward with creating the model.

First, you'll specify the details of your model, such as its name, encryption settings,
and tags.

Then, you'll configure your input data. During that process, you'll make decisions about
the balance between your training dataset and your evaluation dataset, and whether or not to
use data labels.

###### Topics

- [Specifying model details](specifying-model-details.md "specifying-model-details.md")
- [Configuring your input data](configuring-input-data.md "configuring-input-data.md")
