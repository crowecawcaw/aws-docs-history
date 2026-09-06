

# View log data for CodeDeploy EC2/On-Premises deployments
<a name="deployments-view-logs"></a>

You can view the log data created by a CodeDeploy deployment by setting up the Amazon CloudWatch agent to view aggregated data in the CloudWatch console or by logging into an individual instance to review the log file.

**Note**  
 Logs are not supported for AWS Lambda or Amazon ECS deployments. They can be created for EC2/On-Premises deployments only. 

**Topics**
+ [View log file data in the Amazon CloudWatch console](#deployments-view-logs-cloudwatch)
+ [View log files on an instance](#deployments-view-logs-instance)

## View log file data in the Amazon CloudWatch console
<a name="deployments-view-logs-cloudwatch"></a>

When the Amazon CloudWatch agent is installed on an instance, deployment data for all deployments to that instance becomes available for viewing in the CloudWatch console. For simplicity, we recommend using CloudWatch to centrally monitor log files instead of viewing them instance by instance. For more information, see [Send CodeDeploy agent logs to CloudWatch](codedeploy-agent-operations-cloudwatch-agent.md).

## View log files on an instance
<a name="deployments-view-logs-instance"></a>

To view deployment log data for an individual instance, you can sign in to the instance and browse for information about errors or other deployment events.

**Topics**
+ [To view deployment log files on Amazon Linux, RHEL, and Ubuntu Server instances](#deployments-view-logs-instance-unix)
+ [To view deployment log files on Windows Server instances](#deployments-view-logs-instance-windows)

### To view deployment log files on Amazon Linux, RHEL, and Ubuntu Server instances
<a name="deployments-view-logs-instance-unix"></a>

On Amazon Linux, RHEL, and Ubuntu Server instances, deployment logs are stored in the following location:

 `/opt/codedeploy-agent/deployment-root/deployment-logs/codedeploy-agent-deployments.log`

To view or analyze deployment logs on Amazon Linux, RHEL, and Ubuntu Server instances, sign in to the instance, and then type the following command to open the CodeDeploy agent log file:

```
less /var/log/aws/codedeploy-agent/codedeploy-agent.log
```

For version 2.0.x and later, the agent log rotates daily or when the file reaches 64 MB (configurable). Rotated archives are named `codedeploy-agent.YYYYMMDD.log` (with a numeric suffix for same-day rotations) and are pruned after seven days. The scripts log (`scripts.log`) is size-rotated at 64 MB with up to 8 archived files (configurable).

Type the following commands to browse the log file for error messages:


<table>
<thead>
  <tr><th>Command</th><th>Result</th></tr>
</thead>
<tbody>
  <tr><td><b>&amp; ERROR </b></td><td>Show just the error messages in the log file. Use a single space before and after the word <b>ERROR</b>.</td></tr>
  <tr><td><b>/ ERROR </b></td><td>Search for the next error message.¹ </td></tr>
  <tr><td><b>? ERROR </b></td><td>Search for the previous error message.² Use a single space before and after the word <b>ERROR</b>.</td></tr>
  <tr><td><b>G</b></td><td>Go to the end of the log file.</td></tr>
  <tr><td><b>g</b></td><td>Go to the start of the log file.</td></tr>
  <tr><td><b>q</b></td><td>Exit the log file.</td></tr>
  <tr><td><b>h</b></td><td>Learn about additional commands.</td></tr>
  <tr><td colspan="2">¹ After you type <b>/ ERROR </b>, type <b>n</b> for the next error message. Type <b>N</b> for the previous error message. <br />² After you type <b>? ERROR </b>, type <b>n</b> for the next error message, or type <b>N</b> for the previous error message.</td></tr>
</tbody>
</table>


You can also type the following command to open a CodeDeploy scripts log file:

```
less /opt/codedeploy-agent/deployment-root/{{deployment-group-ID}}/{{deployment-ID}}/logs/scripts.log
```

Type the following commands to browse the log file for error messages:


<table>
<thead>
  <tr><th>Command</th><th>Result</th></tr>
</thead>
<tbody>
  <tr><td><b>&amp;stderr</b></td><td>Show just the error messages in the log file. </td></tr>
  <tr><td><b>/stderr</b></td><td>Search for the next error message.¹</td></tr>
  <tr><td><b>?stderr</b></td><td>Search for the previous error message.²</td></tr>
  <tr><td><b>G</b></td><td>Go to the end of the log file.</td></tr>
  <tr><td><b>g</b></td><td>Go to the start of the log file.</td></tr>
  <tr><td><b>q</b></td><td>Exit the log file.</td></tr>
  <tr><td><b>h</b></td><td>Learn about additional commands.</td></tr>
  <tr><td colspan="2">¹After you type <b>/stderr</b>, type <b>n</b> for the next error message forward. Type <b>N</b> for the previous error message backward.<br />² After you type <b>?stderr</b>, type <b>n</b> for the next error message backward. Type <b>N</b> for the previous error message forward.</td></tr>
</tbody>
</table>


### To view deployment log files on Windows Server instances
<a name="deployments-view-logs-instance-windows"></a>

**CodeDeploy agent log file**: On Windows Server instances, the CodeDeploy agent log file is stored at the following location:

For version 2.0.x and later:

`C:\ProgramData\Amazon\CodeDeploy\log\codedeploy-agent.log`

For version 1.8.x and earlier:

`C:\ProgramData\Amazon\CodeDeploy\log\codedeploy-agent-log.txt`

To view or analyze the CodeDeploy agent log file on a Windows Server instance, sign in to the instance, and then type the following command to open the file:

For version 2.0.x and later:

```
notepad C:\ProgramData\Amazon\CodeDeploy\log\codedeploy-agent.log
```

For version 1.8.x and earlier:

```
notepad C:\ProgramData\Amazon\CodeDeploy\log\codedeploy-agent-log.txt
```

To browse the log file for error messages, press CTRL\+F, type **ERROR**, and then press Enter to find the first error. 

**CodeDeploy scripts log files**: On Windows Server instances, deployment logs are stored at the following location:

`C:\ProgramData\Amazon\CodeDeploy\{{deployment-group-id}}\{{deployment-id}}\logs\scripts.log`

Where:
+ {{deployment-group-id}} is a string such as `examplebf3a9c7a-7c19-4657-8684-b0c68d0cd3c4`
+ {{deployment-id}} is an identifier such as `d-12EXAMPLE`

Type the following command to open a CodeDeploy scripts log file:

```
notepad C:\ProgramData\Amazon\CodeDeploy\{{deployment-group-ID}}\{{deployment-ID}}\logs\scripts.log
```

For version 2.0.x and later, the agent log rotates daily or when the file reaches 64 MB (configurable). The scripts log is size-rotated at 64 MB with up to 8 archived files (configurable).

To browse the log file for error messages, press CTRL\+F, type **stderr**, and then press Enter to find the first error. 