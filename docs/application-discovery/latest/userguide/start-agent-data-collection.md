AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Starting and stopping Discovery Agent data

collection

After the Discovery Agent is deployed and configured, if data collections stops you can
restart it. You can start or stop data collection through the console by following the
steps in [Starting and stopping data collectors in
the AWS Migration Hub console](start-stop-data_collection.md "start-stop-data_collection.md"), or by making API calls through the
AWS CLI. Before starting be sure to generate [access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md")
needed to manage the Discovery Agent.

###### To install the AWS CLI and start or stop data collection

1. If you have not already done so, install the AWS CLI appropriate to your OS type
   (Windows or Mac/Linux). See the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") for instructions.
2. Open the Command prompt (Windows) or Terminal (MAC/Linux).
   1. Type `aws configure` and press Enter.
   2. Enter your AWS Access Key ID and AWS Secret Access Key.
   3. Enter your home Region for the Default Region Name, for example
      `us-west-2`. (We are
      assuming that `us-west-2` is your home Region in this
      example.)
   4. Enter `text` for Default Output Format.

3. To find the ID of the agent you want to stop or start data collection for,
   type the following command:

```
aws discovery describe-agents
```

4. To start data collection by the agent, type the following command:

```
aws discovery start-data-collection-by-agent-ids --agent-ids `<agent ID>`
```

To stop data collection by the agent, type the following command:

```
aws discovery stop-data-collection-by-agent-ids --agent-ids `<agent ID>`
```
