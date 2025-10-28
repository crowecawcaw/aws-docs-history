# Monitor Launch Wizard for SAP deployments

You can monitor your Launch Wizard for SAP deployments using the AWS Launch Wizard console and
AWS CLI.

###### Topics

- [Monitoring SAP deployments
  (Console)](#launch-wizard-sap-monitoring-console "#launch-wizard-sap-monitoring-console")
- [Monitor SAP deployments
  (AWS CLI)](#launch-wizard-sap-monitoring-cli "#launch-wizard-sap-monitoring-cli")

## Monitoring SAP deployments

(Console)

Once you have deployed an application, you can monitor it using the Launch Wizard
console.

###### To monitor SAP deployments using the console

1. Access the AWS Launch Wizard console located at [https://console.aws.amazon.com/launchwizard](https://console.aws.amazon.com/launchwizard "https://console.aws.amazon.com/launchwizard").
2. On the left panel, under **Deployments**, choose
   **SAP**.
3. Under **Application name**, choose the application's name
   that you are deploying.
4. You can now review the information in the **Details**
   pane and the **Deployment events** for your
   application.

## Monitor SAP deployments

(AWS CLI)

You can monitor your Launch Wizard for SAP deployments using the AWS CLI.

### Prerequisites

The following prerequisites are required in order to use the AWS CLI to monitor
your Launch Wizard deployment.

- Install or update the AWS CLI, see [Install or
  update the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Determine the deployment name used for the deployment to monitor. The
  name was specified during the deployment creation wizard, or as the
  input for the `CreateDeployment` operation. You can discover
  the name using the Launch Wizard console, or the `GetDeployment`
  operation.

### Monitoring SAP

deployments (AWS CLI)

You can use the `DescribeLogStreams` operation to find the
available log streams for the deployment. Once you have the log stream names,
you can use the **GetEventLogs** operation to list log events
for your deployment related to the log stream you specify.

###### To monitor SAP deployments using the AWS CLI

1. List the log streams available for the deployment. The streams include
   the logs and scripts that are run on instances launched for the
   deployment.

```
`$` aws logs describe-log-streams --region `us-east-1` --log-group-name LaunchWizard-`DeploymentName`

`"logStreams": [
 {
 "logStreamName": "/var/lib/amazon/ssm/packages/AWSSAP-Backint/2.0.4.768/aws-backint-agent-install-20231027153332.log",
 "creationTime": 1698420842081,
 "firstEventTimestamp": 1698420837015,
 "lastEventTimestamp": 1698420842015,
 "lastIngestionTime": 1698420842277,
 "uploadSequenceToken": "111122223333EXAMPLE",
 "arn": "arn:aws:logs:us-east-1:111122223333:log-group:LaunchWizard-b2gtehPp:log-stream:/var/lib/amazon/ssm/packages/AWSSAP-Backint/2.0.4.768/aws-backint-agent-install-20231027153332.log",
 "storedBytes": 0
 },
 {
 "logStreamName": "i-1234567890abcdef0",
 "creationTime": 1698418980895,
 "firstEventTimestamp": 1698418975818,
 "lastEventTimestamp": 1698420271819,
 "lastIngestionTime": 1698420276842,
 "uploadSequenceToken": "111122223333EXAMPLE",
 "arn": "arn:aws:logs:us-east-1:111122223333:log-group:LaunchWizard-b2gtehPp:log-stream:i-1234567890abcdef0",
 "storedBytes": 0
 },
 ...
]`
```

2. Get the log events for the relevant log stream. By default, this
   operation returns as many log events as can fit in a response size of 1
   MB (up to 10,000 log events). You can get additional log events by
   specifying one of the tokens in a subsequent call.

```
`$` userprompt;aws logs get-log-events --region `us-east-1` --log-group-name LaunchWizard-`DeploymentName` --log-stream-name `LogStreamName`

`{
 "events": [
 {
 "timestamp": 1698418975818,
 "message": "[ 10/27/2023 03:02:45 PM] [ main: 29] [ INFO] process stated.",
 "ingestionTime": 1698418981051
 },
 {
 "timestamp": 1698418975818,
 "message": "[ 10/27/2023 03:02:45 PM] [ main: 30] [ INFO] python version 3.8",
 "ingestionTime": 1698418981051
 },
 ...
 ],
 "nextBackwardToken": "b/31961209122358285602261756944988674324553373268216709120",
 "nextForwardToken": "f/31961209122447488583055879464742346735121166569214640130",
}`
```

3. Repeat these steps as necessary to review all of the relevant log
   streams.

If you find that your deployment has experienced issues, or you want to know more
about other logs generated during an SAP deployment, see [Troubleshoot AWS Launch Wizard for SAP](launch-wizard-sap-troubleshooting.md "launch-wizard-sap-troubleshooting.md").
