

# How the playground works
<a name="playground-how-it-works"></a>

The playground uses two resources in your account:
+ An IAM service role named `ElementalInferencePlaygroundServiceRole`. You create this role from the **Create job** page before your first job. The role applies to every AWS Region.
+ The first time you submit a job in an AWS Region, the console creates a dedicated MediaConvert queue named `ElementalInferencePlaygroundQueue`. This queue allows a maximum of one concurrent feed. As a result, playground jobs run one at a time and use no more than one feed from your Elemental Inference quota.

We recommend that you don't delete this queue, so that your job history remains available.

After these resources exist, each job that you submit does the following:
+ The console submits an MediaConvert job.
+ MediaConvert briefly creates and then deletes an Elemental Inference feed to analyze the video.
+ MediaConvert writes the reframed output to your Amazon S3 location.

Jobs appear in the **Playground Jobs** table with a status of **Queued**, **Processing**, **Complete**, **Canceled**, or **Error**.