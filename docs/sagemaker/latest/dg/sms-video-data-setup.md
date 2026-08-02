# Input Data Setup

###### Note

Amazon SageMaker Ground Truth is no longer open to new customers.
Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
Ground Truth, but we do not plan to introduce new features.

When you create a video frame labeling job, you need to let Ground Truth know where to look
for your input data. You can do this in one of two ways:

- You can store your input data in Amazon S3 and have Ground Truth automatically detect the
  input dataset used for your labeling job. See [Set up Automated Video Frame Input Data](sms-video-automated-data-setup.md "sms-video-automated-data-setup.md") to learn more about this
  option.
- You can create an input manifest file and sequence files and upload them to
  Amazon S3. See [Set up Video Frame Input Data Manually](sms-video-manual-data-setup.md "sms-video-manual-data-setup.md") to learn more about this
  option.

###### Topics

- [Set up Automated Video Frame Input Data](sms-video-automated-data-setup.md "sms-video-automated-data-setup.md")
- [Set up Video Frame Input Data Manually](sms-video-manual-data-setup.md "sms-video-manual-data-setup.md")
