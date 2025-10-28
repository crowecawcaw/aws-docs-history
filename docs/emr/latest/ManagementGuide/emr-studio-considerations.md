# EMR Studio features, requirements, and limits

This topic includes Items to consider when working with Amazon EMR Studio, including considerations about regions and tools, cluster
requirements, and technical limitations.

## Considerations

Consider the following when you work with EMR Studio:

- EMR Studio is available in the following AWS Regions:

      + US East (Ohio) (us-east-2)
      + US East (N. Virginia) (us-east-1)
      + US West (N. California) (us-west-1)
      + US West (Oregon) (us-west-2)
      + Africa (Cape Town) (af-south-1)
      + Asia Pacific (Hong Kong) (ap-east-1)
      + Asia Pacific (Jakarta) (ap-southeast-3)\*
      + Asia Pacific (Melbourne) (ap-southeast-4)\*
      + Asia Pacific (Mumbai) (ap-south-1)
      + Asia Pacific (Osaka) (ap-northeast-3)\*
      + Asia Pacific (Seoul) (ap-northeast-2)
      + Asia Pacific (Singapore) (ap-southeast-1)
      + Asia Pacific (Sydney) (ap-southeast-2)
      + Asia Pacific (Tokyo) (ap-northeast-1)
      + Canada (Central) (ca-central-1)
      + Europe (Frankfurt) (eu-central-1)
      + Europe (Ireland) (eu-west-1)
      + Europe (London) (eu-west-2)
      + Europe (Milan) (eu-south-1)
      + Europe (Paris) (eu-west-3)
      + Europe (Spain) (eu-south-2)
      + Europe (Stockholm) (eu-north-1)
      + Europe (Zurich) (eu-central-2)\*
      + Israel (Tel Aviv) (il-central-1)\*
      + Middle East (UAE) (me-central-1)\*
      + South America (São Paulo) (sa-east-1)
      + AWS GovCloud (US-East) (gov-us-east-1)
      + AWS GovCloud (US-West) (gov-us-west-1)

  \* The live Spark UI isn't supported in these Regions.

- To let users provision new EMR clusters running on Amazon EC2 for a Workspace,
  you can associate an EMR Studio with a set of cluster templates. Administrators can
  define cluster templates with Service Catalog and can choose whether a user or group can access the
  cluster templates, or no cluster templates, within a Studio.
- When you define access permissions to notebook files stored in Amazon S3 or
  read secrets from AWS Secrets Manager, use the Amazon EMR service role. Session
  policies aren't supported with these permissions.
- You can create multiple EMR Studios to control access to EMR clusters in
  different VPCs.
- Use the AWS CLI to set up Amazon EMR on EKS clusters. You can then use the Studio
  interface to attach clusters to Workspaces with a managed endpoint to run
  notebook jobs.
- There are additional considerations when you use trusted identity propagation with Amazon EMR that also apply to
  EMR Studio. For more information, see [Considerations and limitations for Amazon EMR with
  the Identity Center integration](emr-idc-considerations.md "emr-idc-considerations.md").
- EMR Studio doesn't support the following Python magic commands:
  - `%alias`
  - `%alias_magic`
  - `%automagic`
  - `%macro`
  - `%%js`
  - `%%javascript`
  - Modifying `proxy_user` using `%configure`
  - Modifying `KERNEL_USERNAME` using `%env` or
    `%set_env`

- Amazon EMR on EKS clusters don't support SparkMagic commands for EMR Studio.
- To write multi-line Scala statements in notebook cells, make sure that all but the
  last line end with a period. The following example uses the correct syntax for multi-line
  Scala statements.

```
val df = spark.sql("SELECT * from table_name).
        filter("col1=='value'").
        limit(50)
```

- To augment the security for the off-console applications that you might use with
  Amazon EMR, the application hosting domains are registered in the Public Suffix List (PSL).
  Examples of these hosting domains include the following:
  `emrstudio-prod.us-east-1.amazonaws.com`,
  `emrnotebooks-prod.us-east-1.amazonaws.com`,
  `emrappui-prod.us-east-1.amazonaws.com`. For further security, if you
  ever need to set sensitive cookies in the default domain name, we recommend that you use
  cookies with a `__Host-` prefix. This helps to defend your domain against
  cross-site request forgery attempts (CSRF). For more information, see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the _Mozilla Developer
  Network_.
- Amazon EMR Studio Workspaces and Persistent UI endpoints use FIPS 140 validated cryptographic modules for encryption-in-transit, which enables easier adoption of
  the service for regulated workloads. For additional context on Persistent UI endpoints, see [View persistent application user interfaces in Amazon EMR](app-history-spark-UI.md "app-history-spark-UI.md"). For additional context regarding notebooks,
  see [Amazon EMR Notebooks overview](emr-managed-notebooks.md "emr-managed-notebooks.md").

## Known issues

- An EMR Studio that uses IAM Identity Center with trusted identity propagation enabled can only associate with
  EMR clusters that also use trusted identity propagation.
- Make sure you deactivate proxy management tools such as FoxyProxy or
  SwitchyOmega in the browser before you create a Studio. Active proxies
  can cause errors when you choose **Create Studio**, and result in a
  **Network Failure** error message.
- Kernels that run on Amazon EMR on EKS clusters can fail to start due to timeout issues. If you
  encounter an error or issue starting the kernel, close the notebook file, shut down the
  kernel, and then reopen the notebook file.
- The **Restart kernel** operation doesn't work as expected when you
  use an Amazon EMR on EKS cluster. After you select **Restart kernel**, refresh
  the Workspace for the restart to take effect.
- If a Workspace isn't attached to a cluster, an error message appears when a
  Studio user opens a notebook file and tries to select a kernel. You can ignore
  this error message by choosing **Ok**, but you must attach the
  Workspace to a cluster and select a kernel before you can run notebook
  code.
- When you use Amazon EMR 6.2.0 with a [security
  configuration](emr-security-configurations.md "emr-security-configurations.md") to set up cluster security, the Workspace interface
  appears blank and doesn't work as expected. We recommend that you use a different
  supported version of Amazon EMR if you want to configure data encryption or Amazon S3
  authorization for EMRFS for a cluster. EMR Studio works with Amazon EMR versions 5.32.0
  (Amazon EMR 5.x series) and 6.2.0 (Amazon EMR 6.x series) and higher.
- When you [Debug Amazon EMR running on Amazon EC2 jobs](emr-studio-debug.md#emr-studio-debug-ec2 "emr-studio-debug.md#emr-studio-debug-ec2"),
  the links to the on-cluster Spark UI may not work or fail to appear. To regenerate the
  links, create a new notebook cell and run the `%%info` command.
- Jupyter Enterprise Gateway doesn't clean up idle kernels on the primary node of a
  cluster in the following Amazon EMR release versions: 5.32.0, 5.33.0, 6.2.0, and 6.3.0. Idle
  kernels consume computing resources and can cause long running clusters to fail. You can
  configure idle kernel cleanup for Jupyter Enterprise Gateway using the following example
  script. You can [Connect to the Amazon EMR cluster primary node using
  SSH](emr-connect-master-node-ssh.md "emr-connect-master-node-ssh.md"), or submit the script as a step. For more
  information, see [Run commands and scripts on an
  Amazon EMR cluster](../ReleaseGuide/emr-commandrunner.md "../ReleaseGuide/emr-commandrunner.md").

```
#!/bin/bash
sudo tee -a /emr/notebook-env/conf/jupyter_enterprise_gateway_config.py << EOF
c.MappingKernelManager.cull_connected = True
c.MappingKernelManager.cull_idle_timeout = 10800
c.MappingKernelManager.cull_interval = 300
EOF
sudo systemctl daemon-reload
sudo systemctl restart jupyter_enterprise_gateway
```

- When you use an auto-termination policy with Amazon EMR versions 5.32.0, 5.33.0, 6.2.0, or
  6.3.0, Amazon EMR marks a cluster as idle and may automatically terminate the cluster even if
  you have an active Python3 kernel. This is because executing a Python3 kernel does not
  submit a Spark job on the cluster. To use auto-termination with a Python3 kernel, we
  recommend that you use Amazon EMR version 6.4.0 or later. For more information about
  auto-termination, see [Using an auto-termination policy for Amazon EMR cluster cleanup](emr-auto-termination-policy.md "emr-auto-termination-policy.md").
- When you use `%%display` to display a Spark DataFrame in a table, very wide
  tables may get truncated. You can right-click the output and select **Create New
  View for Output** to get a scrollable view of the output.
- Starting a Spark-based kernel, such as PySpark, Spark, or SparkR, starts a Spark
  session, and running a cell in a notebook queues up Spark jobs in that session. When you
  interrupt a running cell, the Spark job continues to run. To stop the Spark job, you
  should use the on-cluster Spark UI. For instructions on how to connect to the Spark UI,
  see [Debug applications and jobs with EMR Studio](emr-studio-debug.md "emr-studio-debug.md").
- Using Amazon EMR Studio Workspaces as the root user in an AWS account causes a `403: Forbidden`
  error. This is because the Jupyter Enterprise Gateway configuration in Amazon EMR doesn't allow access to the
  root user. We recommend that you don't use the root user for your everyday tasks. For other authentication options,
  see [AWS Identity and Access Management for Amazon EMR](emr-plan-access-iam.md "emr-plan-access-iam.md").

## Feature limitations

Amazon EMR Studio doesn't support the following Amazon EMR features:

- Attaching and running jobs on EMR clusters with a security configuration that
  specifies Kerberos authentication
- Clusters with multiple primary nodes
- Clusters that use Amazon EC2 instances based on AWS Graviton2 for Amazon EMR 6.x releases
  lower than 6.9.0, and 5.x releases lower than 5.36.1

The following features aren't supported from a Studio that uses trusted identity propagation:

- Creating EMR clusters without a template.
- Using EMR Serverless applications.
- Launching Amazon EMR on EKS clusters.
- Using a runtime role.
- Enabling SQL Explorer or Workspace collaboration.

## Service limits for EMR Studio

The following table displays service limits for EMR Studio.

| Item                       | Limit                                        |
| -------------------------- | -------------------------------------------- |
| EMR Studios                | Maximum of 100 per AWS account               |
| Subnets                    | Maximum of 5 associated with each EMR Studio |
| IAM Identity Center Groups | Maximum of 5 assigned to each EMR Studio     |
| IAM Identity Center Users  | Maximum of 100 assigned to each EMR Studio   |
