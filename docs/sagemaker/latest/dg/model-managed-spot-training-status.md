# Managed Spot Training Lifecycle

You can monitor a training job using `TrainingJobStatus` and
`SecondaryStatus` returned by [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md").
The list below shows how `TrainingJobStatus` and `SecondaryStatus` values
change depending on the training scenario:

- **Spot instances acquired with no interruption during
  training**
  1.  `InProgress`: `Starting`↠ `Downloading` ↠
      `Training` ↠ `Uploading`

- **Spot instances interrupted once. Later, enough spot instances were
  acquired to finish the training job.**
  1.  `InProgress`: `Starting` ↠ `Downloading` ↠
      `Training` ↠ `Interrupted` ↠ `Starting` ↠
      `Downloading` ↠ `Training` ↠ `Uploading`

- **Spot instances interrupted twice and
  `MaxWaitTimeInSeconds` exceeded.**
  1.  `InProgress`: `Starting` ↠ `Downloading` ↠
      `Training` ↠ `Interrupted` ↠ `Starting` ↠
      `Downloading` ↠ `Training` ↠ `Interrupted` ↠
      `Downloading` ↠ `Training`
  2.  `Stopping`: `Stopping`
  3.  `Stopped`: `MaxWaitTimeExceeded`

- **Spot instances were never launched.**
  1.  `InProgress`: `Starting`
  2.  `Stopping`: `Stopping`
  3.  `Stopped`: `MaxWaitTimeExceeded`
