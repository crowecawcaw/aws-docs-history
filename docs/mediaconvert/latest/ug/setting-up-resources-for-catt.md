# Setting up AWS Elemental MediaConvert resources

for cost allocation through tagging

For all outputs that you produce using an on-demand queue, you can use the AWS Billing and Cost Management dashboard to set up a monthly cost allocation report. This report
shows what AWS charges you for transcoding, sorted by resource. You can set up your
jobs so that your job outputs are sorted by tags on the job or on a resource that you
use to create the job. That is, you can sort your bill by the tags that you put on the
job, on the queue that you submit the job to, on the job template that you create the
job from, or on the output presets that you use to set up the individual outputs of the
job.

###### To set up cost allocation through tagging for your AWS Elemental MediaConvert

charges

1. Tag the resources that you intend to sort your bill by. For instructions, see
   the other topics in this chapter.
2. Create your transcoding jobs, specifying how you want your costs allocated as
   follows:
   1. On the **Create job** page, in the **Job** pane on the left, under **Job settings**, choose
      **AWS integration**.
   2. In the **Job settings** section on the right, under **AWS integration**, for **Billing tag source**, choose which tags you want
      to use to sort the job's outputs. You can choose to sort by tags on a
      resource that you use to create the job—job template, output
      preset, or queue. Or you can choose **Job** to sort by
      the tags on the job itself.

   ###### Note

   Jobs, and the tags on them, persist for only 90 days. If your
   workflow references tags over longer periods of time, use tags on
   the queue, job template, or output preset rather than tags on the
   job.

3. Activate these tags on the AWS Billing and Cost Management dashboard. For more information, see
   [Activating user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") in the _Billing and Cost Management User Guide_.
4. Set up your report. For more information, see [Monthly cost allocation report](../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md "../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md") in the _Billing and Cost Management
   User Guide_.
