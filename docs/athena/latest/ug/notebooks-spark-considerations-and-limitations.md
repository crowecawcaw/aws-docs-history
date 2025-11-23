# Considerations and

limitations

## Apache Spark version 3.5

The following are the considerations and limitations for the release version Apache Spark version 3.5:

- This release version is available in the following AWS Regions:
  - Asia Pacific (Mumbai)
  - Asia Pacific (Singapore)
  - Asia Pacific (Sydney)
  - Asia Pacific (Tokyo)
  - Europe (Frankfurt)
  - Europe (Ireland)
  - US East (N. Virginia)
  - US East (Ohio)
  - US West (Oregon)

- This engine version does not support Athena in-console notebooks or notebook APIs. Instead, this version comes integrated with Amazon SageMaker AI Unified Studio notebooks. You can also use compatible Spark Connect clients.
- The Calculation APIs - `StartCalculationExecution`, `ListCalculationExecutions` and `GetCalculationExecution`, are not supported in this release.
- You cannot upgrade a workgroup from PySpark engine version 3 to Apache Spark version 3.5.

## Pyspark engine version 3

The following are the considerations and limitations for the release version Pyspark engine version 3:

- This release version is available in the following AWS Regions:
  - Asia Pacific (Mumbai)
  - Asia Pacific (Singapore)
  - Asia Pacific (Sydney)
  - Asia Pacific (Tokyo)
  - Europe (Frankfurt)
  - Europe (Ireland)
  - US East (N. Virginia)
  - US East (Ohio)
  - US West (Oregon)

- AWS Lake Formation is not supported.
- Tables that use partition projection are not
  supported.
- Apache Spark enabled workgroups can use the Athena notebook editor, but not the
  Athena query editor. Only Athena SQL workgroups can use the Athena query
  editor.
- Cross-engine view queries are not supported. Views created by Athena SQL are
  not queryable by Athena for Spark. Because views for the two engines are
  implemented differently, they are not compatible for cross-engine use.
- MLlib (Apache Spark machine learning library) and the
  `pyspark.ml` package are not supported. For a list of
  supported Python libraries, see the [List of preinstalled Python
  libraries](notebooks-spark-preinstalled-python-libraries.md "notebooks-spark-preinstalled-python-libraries.md").
- Currently, `pip install` is not supported in Athena for Spark
  sessions.
- Only one active session per notebook is allowed.
- When multiple users use the console to open an existing session in a
  workgroup, they access the same notebook. To avoid confusion, only open sessions
  that you create yourself.
- The hosting domains for Apache Spark applications that you might use with
  Amazon Athena (for example, `analytics-gateway.us-east-1.amazonaws.com`)
  are registered in the internet [Public Suffix List
  (PSL)](https://publicsuffix.org/list/public_suffix_list.dat "https://publicsuffix.org/list/public_suffix_list.dat"). If you ever need to set sensitive cookies in your domains, we
  recommend that you use cookies with a `__Host-` prefix to help defend
  your domain against cross-site request forgery (CSRF) attempts. For more
  information, see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla.org developer documentation.
- For information on troubleshooting Spark notebooks, sessions, and workgroups
  in Athena, see [Troubleshoot Athena for Spark](notebooks-spark-troubleshooting.md "notebooks-spark-troubleshooting.md").
