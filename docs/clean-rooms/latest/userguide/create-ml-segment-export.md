

# Exporting a lookalike segment
<a name="create-ml-segment-export"></a>

After you have created a lookalike segment, you can export that data to an Amazon S3 bucket.

**To export a lookalike segment in AWS Clean Rooms**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. On the **With active membership** tab, choose a collaboration.

1. On the **ML Models** tab, select a lookalike segment and choose **Export**.

1. For **Export lookalike model**, for **Export lookalike model details** enter a **Name** and optional **Description**.

1. For **Segment size**, choose the size you want for the exported segment. 

1. Choose **Export**. 

For the corresponding API action, see [StartAudienceExportJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceExportJob.html).