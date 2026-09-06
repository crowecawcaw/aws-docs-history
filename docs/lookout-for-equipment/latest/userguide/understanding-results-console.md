

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Reviewing inference results in the console
<a name="understanding-results-console"></a>

## Using the main inference schedules page
<a name="inference-schedules-main-page"></a>

On the inference schedules main page you'll find your list of inference schedules, both active and inactive (on different tabs). For each schedule, you'll find the model name, data upload frequency, and latest results.

In this context, *latest results* means the results from the most recent inference run.

![Table showing active inference schedules with columns for schedule name, model name, data upload frequency, and latest results status.](http://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/images/inference-schedules-main.png)


To edit, delete, stop, or restart a schedule, see [Managing inference schedules](managing-inference-schedules.md).

## Using the inference schedule detail page
<a name="inference-schedules-detail-page"></a>

On the inference schedule detail page you'll find details about the anomalous behavior of your assets, as presented in the context of a particular inference schedule.

You'll also find metadata about the schedule itself.

![Inference schedule overview showing schedule name, active status, model name, ARN, and creation date.](http://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/images/inference-schedule-detail.png)


At the top of the results tab are the 7-day inference results. These results provide information about anomalous behavior that occurred over the past week.

*Latest results* refers to results from the latest inference run.

*7-day results* indicates the percentage of hours during the last seven days, during which an anomaly was detected.

Use the slider to zoom in on a particular event (red bar).

Click on a particular event (red bar) to view details about it.

After you click on a particular event, the **Event details** tab indicates which sensors contributed the most to that event.

![Bar chart showing Temperature1 at 27.5% as top contributor, followed by Vibration1 at 16.7%.](http://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/images/inference-event-details.png)
