On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Evaluating the output

After a model is trained, Lookout for Equipment evaluates its performance on a subset of the dataset
that you've specified for evaluation purposes. It displays results that provide an
overview of the performance and detailed information about the abnormal equipment
behavior events and how well the model performed when detecting those.

Using the data and failure labels that you provided for training and evaluating the
model, Lookout for Equipment reports how many times the model's predictions were true positives (how
often the model found the equipment anomaly that was noted within the ranges shown in
the labels). Within a labeled time range, the forewarning time represents the duration
between the earliest time when the model found an anomaly and the end of the labeled
time range.

For example, if Lookout for Equipment reports that "6/7 abnormal equipment behavior events were
detected within label ranges with an average forewarning time of 32 hrs," in 6 out of
the 7 labeled events, the model detected that event and averaged 32 hours of
forewarning. In one case, it did not detect the event.

Lookout for Equipment also reports the abnormal behavior events that were not related to a failure,
along with the duration of these abnormal behavior events. For example, if it reports
that "5 abnormal equipment behavior events were detected outside the label range with an
average duration of 4 hrs," the model thought an event was occurring in 5 cases. An
abnormal behavior event such as this one might be attributed to someone erroneously
operating the equipment for a period of time or a normal operating mode that you haven't
seen previously.

Lookout for Equipment also displays this information graphically on a chart that shows the days and
events and in a table.

Lookout for Equipment provides detailed information about the anomalous events that it detects. It
displays a list of sensors that provided the data to indicate an anomalous event. This
might help you determine which part of your asset is behaving abnormally.
