AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Strategy Recommendations binary analysis

Migration Hub Strategy Recommendations automatically identifies the applications in your portfolio and the
application components that belong to them. For example, if there is a Java application
in your portfolio, Strategy Recommendations identifies it as an application component with a component
type **java**. Without you configuring access to the source
code, Strategy Recommendations can perform binary
analysis.
by inspecting the IIS application DLLs on Windows or application JAR files on Linux and
provide anti-pattern reports or incompatibility reports. An anti-pattern report is a
list of known issues that Strategy Recommendations finds in your portfolio, categorized by severity. An
incompatibility report contains a subset of the anti-patterns, which are API
compatibility, Nuget Package, and Porting Action.

Strategy Recommendations performs analysis for Windows IIS and Java Tomcat and Jboss applications. If
you have an IIS application, Strategy Recommendations generates an incompatibility report by default;
you must configure source code access to receive the full anti-pattern report. If you
have a Java application, Strategy Recommendations generates the full anti-pattern report by
default.

The incompatible or anti-pattern report is displayed after the analysis is complete.
If the analysis is not successful, you can try running a source code analysis by
providing source code access as described in [Set up version control
configurations](getting-started-collector-setup.md#cli-collector-setup-git-source-config "getting-started-collector-setup.md#cli-collector-setup-git-source-config").
