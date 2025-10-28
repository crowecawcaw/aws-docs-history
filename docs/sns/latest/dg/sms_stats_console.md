# Viewing Amazon SNS SMS delivery statistics

You can use the Amazon SNS console to view statistics about your recent SMS deliveries.

1.  Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2.  In the console menu, set the region selector to a [region that
    supports SMS messaging](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md").
3.  On the navigation panel, choose **Text messaging (SMS)**.
4.  On the **Text messaging (SMS)** page, in the **Account
    stats** section, view the charts for your transactional and promotional
    SMS message deliveries. Each chart shows the following data for the preceding 15
    days:

        * Delivery rate (percentage of successful deliveries)
        * Sent (number of delivery attempts)
        * Failed (number of delivery failures)

    On this page, you can also choose the **Usage** button to go to the Amazon S3
    bucket where you store your daily usage reports. For more information, see [Subscribing to Amazon SNS daily SMS usage reports](sms_stats_usage.md "sms_stats_usage.md").
