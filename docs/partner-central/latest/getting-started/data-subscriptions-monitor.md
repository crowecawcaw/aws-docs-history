

# Monitoring delivery

The **Data sharing** page shows the dataset, the destination bucket, the delivery status, the date through which you have received data, and the time of the last delivery for each subscription. Choose a subscription to see its details, including the delivery path in your bucket. The following table describes the delivery statuses.


| Status | Meaning | 
| --- | --- | 
| Active | Your bucket is current. You receive new files every day. | 
| Initial delivery in progress | AWS Partner Central is delivering the dataset's history. The status shows how many days are done. | 
| Delayed | The latest delivery is more than 48 hours behind. AWS Partner Central keeps retrying and usually catches up on its own. If the status stays Delayed for more than a day, confirm that your bucket and your key still exist and that the policies in [Prerequisites](data-subscriptions-prerequisites.md) are still applied. | 
| Action needed | Your bucket policy or your key policy no longer allows delivery, so you aren't receiving files. The message explains what to fix. | 
| Cancelled | You cancelled the subscription. Delivery stopped. The files that were already delivered stay in your bucket. | 

If a subscription needs action, choose **Check delivery access**. The page lists the required policies for each destination. After you restore the policies, AWS Partner Central retries delivery every hour. The next delivery includes the days that were missed. You don't need to recreate the subscription.