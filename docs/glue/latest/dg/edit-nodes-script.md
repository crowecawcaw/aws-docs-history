# Editing or uploading a job script

Use the AWS Glue Studio visual editor to edit the job script or upload your own script.

You can use the visual editor to edit job nodes only if the jobs were created with AWS Glue Studio.
If the job was created using the AWS Glue console, through API commands, or with the command line
interface (CLI), you can use the script editor in AWS Glue Studio to edit the job script, parameters,
and schedule. You can also edit the script for a job created in AWS Glue Studio by converting the job
to script-only mode.

###### To edit the job script or upload your own script

1. If creating a new job, on the **Jobs** page, choose the
   **Spark script editor** option to create a Spark job or choose the
   **Python Shell script editor** to create a Python shell job. You can
   either write a new script, or upload an existing script. If you choose **Spark
   script editor**, you can write or upload either a Scala or Python script. If
   you choose **Python Shell script editor**, you can only write or upload a
   Python script.

After choosing the option to create a new job, in the **Options**
section that appears, you can choose to either start with a starter script
(**Create a new script with boilerplate code**), or you can upload a
local file to use as the job script.

If you chose **Spark script editor**, you can upload either Python or
Scala script files. Scala scripts must have the file extension `.scala`. Python
scripts must be recognized as files of type Python. If you chose **Python Shell
script editor**, you can upload only Python script files.

When you are finished making your choices, choose **Create** to
create the job and open the visual editor. 2. Go to the visual job editor for the new or saved job, and then choose the
**Script** tab. 3. If you didn't create a new job using one of the script editor options, and you have
never edited the script for an existing job, the **Script** tab
displays the heading **Script (Locked)**. This means the script editor is
in read-only mode. Choose **Edit script** to unlock the script for
editing.

To make the script editable, AWS Glue Studio converts your job from a visual job to a
script-only job. If you unlock the script for editing, you can't use the visual editor
anymore for this job after you save it.

In the confirmation window, choose **Confirm** to continue or
**Cancel** to keep the job available for visual editing.

If you choose **Confirm**, the **Visual**
tab no longer appears in the editor. You can use AWS Glue Studio to modify the script using the
script editor, modify the job details or schedule, or view job runs.

###### Note

Until you save the job, the conversion to a script-only job is not permanent. If you
refresh the console web page, or close the job before saving it and reopen it in the
visual editor, you will still be able to edit the individual nodes in the visual
editor. 4. Edit the script as needed.

When you are done editing the script, choose **Save** to save the job
and permanently convert the job from visual to script-only. 5. (Optional) You can download the script from the AWS Glue Studio console by choosing the
**Download** button on the **Script** tab.
When you choose this button, a new browser window opens, displaying the script from its
location in Amazon S3. The **Script filename** and
**Script path** parameters in the **Job details**
tab of the job determine the name and location of the script file in Amazon S3.

![The screen shot shows the visual editor in AWS Glue Studio with the Job details tab selected. The Advanced properties section on the page is expanded, and the parameters Script filename and Script path are displayed. The Script filename field shows Join test job.py and the Script path field shows s3://aws-glue-assets-111122223333-u.](images/job-details-script-location-params-screenshot.png)

When you save the job, AWS Glue save the job script at the location specified by these
fields. If you modify the script file at this location within Amazon S3, AWS Glue Studio
will load the modified script the next time you edit the job.

## Creating and editing Scala scripts in AWS Glue Studio

When you choose the script editor for creating a job, by default, the job programming
language is set to `Python 3`. If you choose to write a new script instead of
uploading a script, AWS Glue Studio starts a new script with boilerplate text written in Python. If
you want to write a Scala script instead, you must first configure the script editor to use
Scala.

###### Note

If you choose Scala as the programming language for the job and use the visual editor
to design your job, the generated job script is written in Scala, and no further actions
are needed.

###### To write a new Scala script in AWS Glue Studio

1. Create a new job by choosing the **Spark script editor**
   option.
2. Under **Options**, choose **Create a new script with
   boilerplate code**.
3. Choose the **Job details** tab and set
   **Language** to `Scala` (instead of `Python
3`).

###### Note

The **Type** property for the job is automatically set to
`Spark` when you choose the **Spark script editor**
option to create a job. 4. Choose the **Script** tab. 5. Remove the Python boilerplate text. You can replace it with the following Scala
boilerplate text.

```
import com.amazonaws.services.glue.{DynamicRecord, GlueContext}
import org.apache.spark.SparkContext
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job

object MyScript {
  def main(args: Array[String]): Unit = {
    val sc: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(sc)

    }
}
```

6. Write your Scala job script in the editor. Add additional `import`
   statements as needed.

## Creating and editing Python shell jobs in

AWS Glue Studio

When you choose the Python shell script editor for creating a job, you can upload an
existing Python script, or write a new one. If you choose to write a new script, boilerplate
code is added to the new Python job script.

###### To create a new Python shell job

Refer to the instructions at [Starting jobs in AWS Glue Studio](edit-nodes-chapter.md#create-jobs-start "edit-nodes-chapter.md#create-jobs-start").

The job properties that are supported for Python shell jobs are not the same as those
supported for Spark jobs. The following list describes the changes to the available job
parameters for Python shell jobs on the **Job details** tab.

- The **Type** property for the job is automatically set to
  `Python Shell` and can't be changed.
- Instead of **Language**, there is a **Python
  version** property for the job. Currently, Python shell jobs created in
  AWS Glue Studio use Python 3.6.
- The **Glue version** property is not available, because it does not
  apply to Python shell jobs.
- Instead of **Worker type** and **Number of
  workers**, a **Data processing units** property is shown
  instead. This job property determines how many data processing units (DPUs) are consumed
  by the Python shell when running the job.
- The **Job bookmark** property is not available, because it is not
  supported for Python shell jobs.
- Under **Advanced properties**, the following properties are not
  available for Python shell jobs.
  - **Job metrics**
  - **Continuous logging**
  - **Spark UI** and **Spark UI logs path**
  - **Dependent jars path**, under the heading
    **Libraries**
