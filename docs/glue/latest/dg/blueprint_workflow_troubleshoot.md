# Troubleshooting blueprint errors in

AWS Glue

If you encounter errors when using AWS Glue blueprints, use the following solutions to help you find the source of the problems and fix them.

###### Topics

- [Error: missing PySpark module](#blueprint-workflow-error-1 "#blueprint-workflow-error-1")
- [Error: missing blueprint config file](#blueprint-workflow-error-2 "#blueprint-workflow-error-2")
- [Error: missing imported file](#blueprint-workflow-error-3 "#blueprint-workflow-error-3")
- [Error: not authorized to perform iamPassRole on resource](#blueprint-workflow-error-4 "#blueprint-workflow-error-4")
- [Error: invalid cron schedule](#blueprint-workflow-error-5 "#blueprint-workflow-error-5")
- [Error: a trigger with the same name already exists](#blueprint-workflow-error-6 "#blueprint-workflow-error-6")
- [Error: workflow with name: foo already exists.](#blueprint-workflow-error-7 "#blueprint-workflow-error-7")
- [Error: module not found in specified layoutGenerator path](#blueprint-workflow-error-8 "#blueprint-workflow-error-8")
- [Error: validation error in Connections field](#blueprint-workflow-error-9 "#blueprint-workflow-error-9")

## Error: missing PySpark module

AWS Glue returns the error "Unknown error executing layout generator function ModuleNotFoundError: No module named 'pyspark'".

When you unzip the blueprint archive it could be like either of the following:

```
$ unzip compaction.zip
Archive:  compaction.zip
   creating: compaction/
  inflating: compaction/blueprint.cfg
  inflating: compaction/layout.py
  inflating: compaction/README.md
  inflating: compaction/compaction.py

$ unzip compaction.zip
Archive:  compaction.zip
  inflating: blueprint.cfg
  inflating: compaction.py
  inflating: layout.py
  inflating: README.md
```

In the first case, all the files related to the blueprint were placed under a folder named compaction and it was then converted into a zip file named _compaction.zip_.

In the second case, all the files required for the blueprint were not included into a folder and were added as root files under the zip file _compaction.zip_.

Creating a file in either of the above formats is allowed. However make sure that `blueprint.cfg` has the correct path to the name of the function in the script that generates the layout.

###### Examples

In case 1: `blueprint.cfg` should have `layoutGenerator` as the following:

```
layoutGenerator": "compaction.layout.generate_layout"
```

In case 2: `blueprint.cfg` should have `layoutGenerator` as the following

```
layoutGenerator": "layout.generate_layout"
```

If this path is not included correctly, you could see an error as indicated. For example, if you have the folder structure as mentioned in case 2 and you have the `layoutGenerator` indicated as in case 1, you can see the above error.

## Error: missing blueprint config file

AWS Glue returns the error "Unknown error executing layout generator function FileNotFoundError: [Errno 2] No such file or directory: '/tmp/compaction/blueprint.cfg'".

The blueprint.cfg should be placed at the root level of the ZIP archive or within a folder which has the same name as the ZIP archive.

When we extract the blueprint ZIP archive, blueprint.cfg is expected to be found in one of the following paths. If it is not found in one of the following paths, you can see the above error.

```
$ unzip compaction.zip
Archive:  compaction.zip
   creating: compaction/
  inflating: compaction/blueprint.cfg

$ unzip compaction.zip
Archive:  compaction.zip
  inflating: blueprint.cfg
```

## Error: missing imported file

AWS Glue returns the error "Unknown error executing layout generator function FileNotFoundError: [Errno 2] No such file or directory:\* \*'demo-project/foo.py'".

If your layout generation script has functionality to read other files, make sure you give a full path for the file to be imported. For example, the Conversion.py script may be referenced in Layout.py. For more information, see [Sample blueprint Project](developing-blueprints-sample.md "developing-blueprints-sample.md").

## Error: not authorized to perform iamPassRole on resource

AWS Glue returns the error "User: arn:aws:sts::123456789012:assumed-role/AWSGlueServiceRole/GlueSession is not authorized to perform: iam:PassRole on resource: arn:aws:iam::123456789012:role/AWSGlueServiceRole"

If the jobs and crawlers in the workflow assume the same role as the role passed to create workflow from the blueprint, then the blueprint role needs to include the `iam:PassRole` permission on itself.

If the jobs and crawlers in the workflow assume a role other than the role passed to create the entities of the workflow from the blueprint, then the blueprint role needs to include the `iam:PassRole` permission on that other role instead of on the blueprint role.

For more information, see [Permissions for blueprint Roles](blueprints-personas-permissions.md#blueprints-role-permissions "blueprints-personas-permissions.md#blueprints-role-permissions").

## Error: invalid cron schedule

AWS Glue returns the error "The schedule cron(0 0 \* \* \* \*) is invalid."

Provide a valid [cron](https://en.wikipedia.org/wiki/Cron "https://en.wikipedia.org/wiki/Cron") expression. For more information, see [Time-Based Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md").

## Error: a trigger with the same name already exists

AWS Glue returns the error "Trigger with name 'foo_starting_trigger' already submitted with different configuration".

A blueprint does not require you to define triggers in the layout script for workflow creation. Trigger creation is managed by the blueprint library based on the dependencies defined between two actions.

The naming for the triggers is as follows:

- For the starting trigger in the workflow the naming is <workflow_name>\_starting_trigger.
- For a node(job/crawler) in the workflow that depends on the completion of either one or multiple upstream nodes; AWS Glue defines a trigger with the name <workflow_name>\_<node_name>\_trigger

This error means a trigger with same name already exists. You can delete the existing trigger and re-run the workflow creation.

###### Note

Deleting a workflow doesn’t delete the nodes within the workflow. It is possible that though the workflow is deleted, triggers are left behind. Due to this, you may not receive a 'workflow already exists' error, but you may receive a 'trigger already exists' error in a case where you create a workflow, delete it and then try to re-create it with the same name from same blueprint.

## Error: workflow with name: foo already exists.

The workflow name should be unique. Please try with a different name.

## Error: module not found in specified layoutGenerator path

AWS Glue returns the error "Unknown error executing layout generator function ModuleNotFoundError: No module named 'crawl_s3_locations'".

```
layoutGenerator": "crawl_s3_locations.layout.generate_layout"
```

For example, if you have the above layoutGenerator path, then when you unzip the blueprint archive, it needs to look like the following:

```
$ unzip crawl_s3_locations.zip
Archive:  crawl_s3_locations.zip
   creating: crawl_s3_locations/
  inflating: crawl_s3_locations/blueprint.cfg
  inflating: crawl_s3_locations/layout.py
  inflating: crawl_s3_locations/README.md
```

When you unzip the archive, if the blueprint archive looks like the following, then you can get the above error.

```
$ unzip crawl_s3_locations.zip
Archive:  crawl_s3_locations.zip
  inflating: blueprint.cfg
  inflating: layout.py
  inflating: README.md
```

You can see that there is no folder named `crawl_s3_locations` and when the `layoutGenerator` path refers to the layout file via the module `crawl_s3_locations`, you can get the above error.

## Error: validation error in Connections field

AWS Glue returns the error "Unknown error executing layout generator function TypeError: Value ['foo'] for key Connections should be of type <class 'dict'>!".

This is a validation error. The `Connections` field in the `Job` class is expecting a dictionary and instead a list of values are provided causing the error.

```
User input was list of values
Connections= ['string']

Should be a dict like the following
Connections*=*{'Connections': ['string']}
```

To avoid these run time errors while creating a workflow from a blueprint, you can validate the workflow, job and crawler definitions as outlined in [Testing a blueprint](developing-blueprints-testing.md "developing-blueprints-testing.md").

Refer to the syntax in [AWS Glue blueprint Classes Reference](developing-blueprints-code-classes.md "developing-blueprints-code-classes.md") for defining the AWS Glue job, crawler and workflow in the layout script.
