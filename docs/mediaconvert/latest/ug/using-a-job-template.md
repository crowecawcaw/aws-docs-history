# Creating a job from a template

Job templates apply to an entire transcoding job and provide values for settings that stay
the same across multiple jobs. You specify the input settings and the AWS Identity and Access Management (IAM)
service role in the job itself. These values are not saved in the template because they
are likely to vary from job to job.

###### To create a job using a job template

1. Open the [Job templates](https://console.aws.amazon.com/mediaconvert/home#/templates/list "https://console.aws.amazon.com/mediaconvert/home#/templates/list") page in the MediaConvert console.
2. In the **Job templates** pane, from the **Templates**
   dropdown list, choose **Custom job templates** or
   **System job templates**.

###### Note

Custom job templates appear only in the AWS Region where they are created. When you choose
**Custom job templates**, you see only the job
templates created in the AWS Region you chose at the beginning of this
procedure. 3. Choose the name of the job template that you want to use. 4. On the **Job template details** page, choose **Create
job**. 5. In the **Inputs** section of the **Job**
pane, choose **Add**. 6. Specify your input video, audio, and captions settings.

###### Note

Make sure that you specify your audio and captions selectors in a way that corresponds to
the outputs that are specified in the job
template. 7. In the **Job settings** section of the **Job
pane**, choose **Settings**. 8. In the **Job settings** pane, in the **IAM role**
dropdown list, choose the service role that you created to grant permissions to
MediaConvert to access your resources on your behalf. For instructions on creating this
role, see [Setting up IAM permissions](iam-role.md "iam-role.md") .
