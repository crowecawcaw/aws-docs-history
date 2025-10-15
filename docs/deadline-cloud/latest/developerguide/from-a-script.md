# Submit a job to Deadline Cloud using a script

 To automate submitting jobs to Deadline Cloud, you can script them using tools such as bash,
 Powershell, and batch files. 

You can add functionality like populating job parameters from environment variables or
 other applications. You can also submit multiple jobs in a row, or script the creation of a job
 bundle to submit. 


## Submit a job using Python


Deadline Cloud also has an open-source Python library to interact with the service. The [source code is available on
 GitHub](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud"). 


The library is available on pypi via pip (`pip install deadline`). It's the
 same library used by the Deadline Cloud CLI tool: 



```
from deadline.client import api

job_bundle_path = "/path/to/job/bundle"
job_parameters = [
    {
        "name": "parameter_name",
        "value": "parameter_value"
    },
]

job_id = api.create_job_from_job_bundle(
    job_bundle_path,
    job_parameters
)
print(job_id)
```

 To create a dialog like the `deadline bundle gui-submit` command, you can use
 of `show_job_bundle_submitter` function from the [`deadline.client.ui.job_bundle_submitter`.](https://github.com/aws-deadline/deadline-cloud/blob/mainline/src/deadline/client/ui/job_bundle_submitter.py "https://github.com/aws-deadline/deadline-cloud/blob/mainline/src/deadline/client/ui/job_bundle_submitter.py")



 The following example starts a Qt application and shows the job bundle submitter: 



```
# The GUI components must be installed with pip install "deadline[gui]"
import sys
from qtpy.QtWidgets import QApplication
from deadline.client.ui.job_bundle_submitter import show_job_bundle_submitter

app = QApplication(sys.argv)
submitter = show_job_bundle_submitter(browse=True)
submitter.show()
app.exec()
print(submitter.create_job_response)
```

To make your own dialog you can use the `SubmitJobToDeadlineDialog` class in
 [`deadline.client.ui.dialogs.submit_job_to_deadline_dialog`](https://github.com/aws-deadline/deadline-cloud/blob/mainline/src/deadline/client/ui/dialogs/submit_job_to_deadline_dialog.py "https://github.com/aws-deadline/deadline-cloud/blob/mainline/src/deadline/client/ui/dialogs/submit_job_to_deadline_dialog.py"). You can pass
 in values, embed your own job specific tab, and determine how the job bundle gets created (or
 passed in).
