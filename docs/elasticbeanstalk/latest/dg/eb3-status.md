# **eb status**

## Description

Provides information about the status of the environment.

If the root directory contains a `platform.yaml` file specifying a
custom platform, this command also provides information about the builder environment.

## Syntax

**eb status**

**eb status `environment-name`**

## Options

| Name                                                      | Description                                                                                                               |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-v` or `--verbose`                                       | Provides more information about individual instances, such as their status with the Elastic Load Balancing load balancer. |
| [Common options](eb3-cmd-options.md "eb3-cmd-options.md") |                                                                                                                           | ## Output If successful, the command returns the following information about the environment: <br>• Environment name <br>• Application name <br>• Deployed application version <br>• Environment ID <br>• Platform <br>• Environment tier <br>• CNAME <br>• Time the environment was last updated <br>• Status <br>• Health If you use verbose mode, EB CLI also provides you with the number of running Amazon EC2 instances. ## Example The following example shows the status for the environment tmp-dev. ``$ `eb status` Environment details for: tmp-dev Application name: tmp Region: us-west-2 Deployed Version: None Environment ID: e-2cpfjbra9a Platform: 64bit Amazon Linux 2014.09 v1.0.9 running PHP 5.5 Tier: WebServer-Standard-1.0 CNAME: tmp-dev.elasticbeanstalk.com Updated: 2014-10-29 21:37:19.050000+00:00 Status: Launching Health: Grey`` |
