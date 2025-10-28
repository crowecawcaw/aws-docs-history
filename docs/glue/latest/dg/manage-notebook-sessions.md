# Managing notebook sessions

Notebooks in AWS Glue Studio are based on the interactive sessions feature of
AWS Glue. There is a cost for using interactive sessions. To help manage your
costs, you can monitor the sessions created for your account, and configure the default
settings for all sessions.

## Change the default timeout for all notebook

sessions

By default, the provisioned AWS Glue Studio notebook times out after 12 hours if the notebook was launched and no cells have been executed.
There is no cost associated to it and the timeout is not configurable.

Once you execute a cell this will start an interactive session. This session has a default timeout of 48 hours. This timeout can be configured by
passing an `%idle_timeout` magic before executing a cell.

###### To modify the default session timeout for notebooks in

AWS Glue Studio

1. In the notebook, enter the `%idle_timeout` magic in a cell and specify the timeout value in minutes.
2. For example: `%idle_timeout 15` will change the default timeout to 15 minutes. If the session
   is not used in 15 minutes, the session is automatically stopped.

## Installing additional Python modules

If you would like to install additional modules to your session using pip you can do so by using `%additional_python_modules`
to add them to your session:

```

%additional_python_modules awswrangler, s3://amzn-s3-demo-bucket/mymodule.whl

```

All arguments to additional_python_modules are passed to `pip3 install -m <>`

For a list of available Python modules, see
[Using Python libraries with AWS Glue](aws-glue-programming-python-libraries.md "aws-glue-programming-python-libraries.md").

## Changing AWS Glue Configuration

You can use magics to control AWS Glue job configuration values. If you want to change a job configuration value you
have to use the proper magic in the notebook. See
[Magics supported by AWS Glue interactive sessions for Jupyter](interactive-sessions-magics.md "interactive-sessions-magics.md").

###### Note

Overriding properties for a running session is no longer available. In order to change the
session’s configurations, you can stop the session, set the new configurations and then start a new session.

AWS Glue supports various worker types. You can set the worker type with `%worker_type`. For example:
`%worker_type G.2X` . Available worker types include G.1X, G.2X, G.4X, G.8X, G.12X, G.16X, R.1X, R.2X, R.4X, and R.8X. The default is G.1X.

You can also specify the Number of workers with `%number_of_workers`. For example, to specify 40 workers:
`%number_of_workers 40`.

For more information see [Defining Job Properties](add-job.md "add-job.md")

## Stop a notebook session

To stop a notebook session, use the magic `%stop_session`.

If you navigate away from the notebook in the AWS console, you will receive a warning message
where you can choose to stop the session.
