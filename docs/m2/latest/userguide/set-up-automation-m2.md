AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Set up Automation for Rocket Enterprise Analyzer (formerly Micro Focus) and Rocket Enterprise Developer

Streaming Sessions

You can automatically run a script at session start and end to allow automation that is
specific to your customer context. For more information on this AppStream 2.0 feature, see [Use Session
Scripts to Manage Your AppStream 2.0 Users' Streaming Experience](../../../appstream2/latest/developerguide/use-session-scripts.md "../../../appstream2/latest/developerguide/use-session-scripts.md") in the
_Amazon AppStream 2.0 Administration Guide_.

This feature requires that you have at least the following versions of the Enterprise Analyzer and Enterprise Developer
images:

- `m2-enterprise-analyzer-v8.0.4.R1`
- `m2-enterprise-developer-v8.0.4.R1`

###### Topics

- [Set up automation at session start](#set-up-automation-m2.start "#set-up-automation-m2.start")
- [Set up automation at session end](#set-up-automation-m2.end "#set-up-automation-m2.end")

## Set up automation at session start

If you want to run an automation script when users connect to AppStream 2.0, create your script and
name it `m2-user-setup.cmd`. Store the script in the AppStream 2.0 Home folder for the user.
The AppStream 2.0 images that AWS Mainframe Modernization provides look for a script with that name in that location, and
run it if it exists.

###### Note

The script duration cannot exceed the limit set by AppStream 2.0, which is currently 60 seconds.
For more information, see [Run Scripts Before Streaming Sessions Begin](../../../appstream2/latest/developerguide/use-session-scripts.md#run-scripts-before-streaming-sessions-begin "../../../appstream2/latest/developerguide/use-session-scripts.md#run-scripts-before-streaming-sessions-begin") in the
_Amazon AppStream 2.0 Administration Guide_.

## Set up automation at session end

If you want to run an automation script when users disconnect from AppStream 2.0, create your
script and name it `m2-user-teardown.cmd`. Store the script in the AppStream 2.0 Home folder
for the user. The AppStream 2.0 images that AWS Mainframe Modernization provides look for a script with that name in that
location, and run it if it exists.

###### Note

The script duration cannot exceed the limit set by AppStream 2.0, which is currently 60 seconds.
For more information, see [Run Scripts After Streaming Sessions End](../../../appstream2/latest/developerguide/use-session-scripts.md#run-scripts-after-streaming-sessions-end "../../../appstream2/latest/developerguide/use-session-scripts.md#run-scripts-after-streaming-sessions-end") in the
_Amazon AppStream 2.0 Administration Guide_.
