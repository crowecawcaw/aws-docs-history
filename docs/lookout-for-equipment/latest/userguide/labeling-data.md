On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Labeling your data

You've made a decision about your [training and evaluation](configuring-input-data.md "configuring-input-data.md") settings. If you decided to use labeled data, now is the time to upload it.

- Create your labeled data.

Your labeled data indicates periods when your equipment did not function propertly. By alerting Lookout for Equipment to these actual trouble spots, you help it learn to recognize abnormal behavior in the future.

You store the label data as a .csv file that consists of two columns. The file has no header. The first column has the start time of the abnormal behavior. The second column has the end time.

The following example shows how your label data should appear as a .csv file.

```

2020-02-01T20:00:00.000000,2020-02-03T00:00:00.000000
2020-07-01T20:00:00.000000,2020-07-03T00:01:00.000000

```

- Upload your data labels to Amazon S3. Here you'll follow the same procedure as in Uploading your data to Amazon S3.

You can use the same Amazon S3 bucket or a different one. If you use the same one, it's a good practice to create a separate folder for your data labels.

- In the Lookout for Equipment console, on the **Provide data labels** page, indicate the location of your data labels.

![AWSLookout for Equipment console page for providing optional data labels with S3 location input.](images/provide-data-labels.png)

- Choose your IAM role.

This is the role that authorizes Lookout for Equipment to access the Amazon S3 bucket where your data labels are stored. If you're using the same bucket as before, you can choose the role that you already created. You can also select **Create an IAM role**, and the proper role will be created for you.

- Choose **Next**.
  The last step before training your model is to [review it](reviewing-settings.md "reviewing-settings.md").
