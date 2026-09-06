

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Set up Automation for Rocket Enterprise Analyzer (formerly Micro Focus) and Rocket Enterprise Developer Streaming Sessions
<a name="set-up-automation-m2"></a>

You can automatically run a script at session start and end to allow automation that is specific to your customer context. For more information on this WorkSpaces Applications feature, see [Use Session Scripts to Manage Your AppStream 2.0 Users' Streaming Experience](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-session-scripts.html) in the *Amazon WorkSpaces Applications Administration Guide*.

This feature requires that you have at least the following versions of the Enterprise Analyzer and Enterprise Developer images:
+ `m2-enterprise-analyzer-v8.0.4.R1`
+ `m2-enterprise-developer-v8.0.4.R1`

**Topics**
+ [Set up automation at session start](#set-up-automation-m2.start)
+ [Set up automation at session end](#set-up-automation-m2.end)

## Set up automation at session start
<a name="set-up-automation-m2.start"></a>

If you want to run an automation script when users connect to WorkSpaces Applications, create your script and name it `m2-user-setup.cmd`. Store the script in the WorkSpaces Applications Home folder for the user. The WorkSpaces Applications images that AWS Mainframe Modernization provides look for a script with that name in that location, and run it if it exists.

**Note**  
The script duration cannot exceed the limit set by WorkSpaces Applications, which is currently 60 seconds. For more information, see [Run Scripts Before Streaming Sessions Begin](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-session-scripts.html#run-scripts-before-streaming-sessions-begin) in the *Amazon WorkSpaces Applications Administration Guide*.

## Set up automation at session end
<a name="set-up-automation-m2.end"></a>

If you want to run an automation script when users disconnect from WorkSpaces Applications, create your script and name it `m2-user-teardown.cmd`. Store the script in the WorkSpaces Applications Home folder for the user. The WorkSpaces Applications images that AWS Mainframe Modernization provides look for a script with that name in that location, and run it if it exists.

**Note**  
The script duration cannot exceed the limit set by WorkSpaces Applications, which is currently 60 seconds. For more information, see [Run Scripts After Streaming Sessions End](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-session-scripts.html#run-scripts-after-streaming-sessions-end) in the *Amazon WorkSpaces Applications Administration Guide*.