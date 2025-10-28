On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Evaluating your model

You can view the ML models you've trained on the datasets containing the data from
your equipment. If you've used part of your dataset for training and the other part for
evaluation, you can see and evaluate the model's performance. You can also see which
sensors were used to create a model. If you need better performance, you can use
different sensors for training your next model.

Amazon Lookout for Equipment provides an overview of the model's performance and detailed information
about abnormal equipment behavior events. An abnormal equipment behavior event is a
situation where the model detected an anomaly in the sensor data that could lead to your
asset malfunctioning or failing. You can see how well the model performed in detecting
those events.

If you've provided Amazon Lookout for Equipment with label data for your dataset, you can see how the
model's predictions compare to the label data. It shows the average forewarning time
across all true positives. Forewarning time is the average length of time between when
the model first finds evidence that something might be going wrong and when it actually
detects the equipment abnormality.

For example, you can have a circumstance where Amazon Lookout for Equipment detects six of the seven
abnormal behavior events in your labeled evaluation data. In six out of the seven
events, on average, it might have provided an indication that something was off 32 hours
before it detected an abnormality. For this situation, we would say that Lookout for Equipment averaged
32 hours of forewarning.

Amazon Lookout for Equipment also reports the results where it incorrectly identified an abnormal
behavior event in the label data. The label data that you provide when you create a
dataset has a time range for abnormal equipment events. You specify the duration of the
abnormal events in the label data. In the evaluation data, the model used by Lookout for Equipment could
incorrectly identify abnormal events outside of the equipment range. You can see how
often the model identifies these events when you evaluate the model's
performance.

You can use the following procedure and example code to view the models you've
created. They also show you how to get information about a model, such as how well it
performed.

## Viewing a model

###### Note

You can also view a model [with the SDK](SDK-examples.md#view-model-sdk "SDK-examples.md#view-model-sdk").

###### To view a model:

You can use this procedure to view model metrics in the console. To evaluate
how the model performed, you must provide data labels. If you provide data labels,
you can see when the model detected abnormal equipment behavior events.

1. Sign in to AWS Management Console and open the Amazon Lookout for Equipment console at [Amazon Lookout for Equipment
   console](https://console.aws.amazon.com/lookoutequipment/home "https://console.aws.amazon.com/lookoutequipment/home").
2. Choose a dataset.
3. Choose a model. You can see whether the model is ready to monitor the
   equipment.
4. Navigate to **Training and evaluation**.

In the following image, you can see metrics related to the performance. You can
see how many times the model identified abnormal equipment behavior events
incorrectly. You can also see which sensors played the largest role in the model
identifying the abnormal equipment behavior events. The console displays the top 15
sensors that contributed to the model identifying an abnormal equipment behavior
event.

![Model performance dashboard showing detected events, labeled events, and top 15 contributing sensors.](images/model-performance-image-launch.png)
