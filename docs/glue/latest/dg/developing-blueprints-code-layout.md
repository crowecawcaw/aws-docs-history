# Creating the blueprint layout

script

The blueprint layout script must include a function that generates the entities in
your workflow. You can name this function whatever you like. AWS Glue uses the configuration
file to determine the fully qualified name of the function.

Your layout function does the following:

- (Optional) Instantiates the `Job` class to create `Job`
  objects, and passes arguments such as `Command` and `Role`. These
  are job properties that you would specify if you were creating the job using the AWS Glue
  console or API.
- (Optional) Instantiates the `Crawler` class to create
  `Crawler` objects, and passes name, role, and target arguments.
- To indicate dependencies between the objects (workflow entities), passes the
  `DependsOn` and `WaitForDependencies` additional arguments to
  `Job()` and `Crawler()`. These arguments are explained later in
  this section.
- Instantiates the `Workflow` class to create the workflow object that is
  returned to AWS Glue, passing a `Name` argument, an `Entities`
  argument, and an optional `OnSchedule` argument. The `Entities`
  argument specifies all of the jobs and crawlers to include in the workflow. To see how
  to construct an `Entities` object, see the sample project later in this
  section.
- Returns the `Workflow` object.
  For definitions of the `Job`, `Crawler`, and `Workflow`
  classes, see [AWS Glue blueprint classes
  reference](developing-blueprints-code-classes.md "developing-blueprints-code-classes.md").

The layout function must accept the following input arguments.

| Argument        | Description                                                                                                                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `user_params`   | Python dictionary of blueprint parameter names and values. For more<br>information, see [Specifying blueprint<br>parameters](developing-blueprints-code-parameters.md "developing-blueprints-code-parameters.md"). |
| `system_params` | Python dictionary containing two properties: `region` and<br>`accountId`.                                                                                                                                          |

Here is a sample layout generator script in a file named `Layout.py`:

```
import argparse
import sys
import os
import json
from awsglue.blueprint.workflow import *
from awsglue.blueprint.job import *
from awsglue.blueprint.crawler import *


def generate_layout(user_params, system_params):

    etl_job = Job(Name="{}_etl_job".format(user_params['WorkflowName']),
                  Command={
                      "Name": "glueetl",
                      "ScriptLocation": user_params['ScriptLocation'],
                      "PythonVersion": "2"
                  },
                  Role=user_params['PassRole'])
    post_process_job = Job(Name="{}_post_process".format(user_params['WorkflowName']),
                            Command={
                                "Name": "pythonshell",
                                "ScriptLocation": user_params['ScriptLocation'],
                                "PythonVersion": "2"
                            },
                            Role=user_params['PassRole'],
                            DependsOn={
                                etl_job: "SUCCEEDED"
                            },
                            WaitForDependencies="AND")
    sample_workflow = Workflow(Name=user_params['WorkflowName'],
                            Entities=Entities(Jobs=[etl_job, post_process_job]))
    return sample_workflow
```

The sample script imports the required blueprint libraries and includes a
`generate_layout` function that generates a workflow with two jobs. This is a
very simple script. A more complex script could employ additional logic and parameters to
generate a workflow with many jobs and crawlers, or even a variable number of jobs and
crawlers.

## Using the DependsOn

argument

The `DependsOn` argument is a dictionary representation of a dependency
that this entity has on other entities within the workflow. It has the following form.

```
DependsOn = {dependency1 : state, dependency2 : state, ...}
```

The keys in this dictionary represent the object reference, not the name, of the
entity, while the values are strings that correspond to the state to watch for. AWS Glue
infers the proper triggers. For the valid states, see [Condition Structure](aws-glue-api-jobs-trigger.md#aws-glue-api-jobs-trigger-Condition "aws-glue-api-jobs-trigger.md#aws-glue-api-jobs-trigger-Condition").

For example, a job might depend on the successful completion of a crawler. If you
define a crawler object named `crawler2` as follows:

```
crawler2 = Crawler(Name="my_crawler", ...)
```

Then an object depending on `crawler2` would include a constructor argument
such as:

```
DependsOn = {crawler2 : "SUCCEEDED"}
```

For example:

```
job1 = Job(Name="Job1", `...`, DependsOn = {crawler2 : "SUCCEEDED", ...})
```

If `DependsOn` is omitted for an entity, that entity depends on the
workflow start trigger.

## Using the

WaitForDependencies argument

The `WaitForDependencies` argument defines whether a job or crawler entity
should wait until _all_ entities on which it depends complete or until
_any_ completes.

The allowable values are "`AND`" or "`ANY`".

## Using the OnSchedule

argument

The `OnSchedule` argument for the `Workflow` class constructor
is a `cron` expression that defines the starting trigger definition for a
workflow.

If this argument is specified, AWS Glue creates a schedule trigger with the corresponding
schedule. If it isn't specified, the starting trigger for the workflow is an on-demand
trigger.
