# Troubleshoot end user errors in AppFabric for productivity

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

This section describes common errors and troubleshooting for AppFabric for productivity.

## Unverified application

Applications that use AppFabric for productivity to enrich their app experiences will go through a
verification process prior to launching their features to end users. If you encounter an
“unverified” banner when trying to sign in to AppFabric, this means that the application has not
undergone AppFabric’s verification process which confirms the app developer’s identity and accuracy
of the application’s registration information. All applications start as unverified and change to
verified only when the verification process is complete.

Be cautious while using an unverified application. If you're unsure about the app
developers, you may wait until the application attains verified status before proceeding.

![Warning message for an unverified application in AWS AppFabric, advising caution before authorization.](images/fabric-20.png)

## Something went wrong. Please try it again or check with your Admin (`InternalServerException`)

You might get this message when the AppFabric user portal fails to list the applications or
disconnects an application due to an unknown error, exception, or failure. Try again
later.

![Connect applications interface showing connected and not connected apps with action buttons.](images/fabric-23.png)

## The request was denied due to request throttling. Please try it again in some time (`ThrottlingException`)

You might get this message when the AppFabric user portal fails to list the applications or
disconnects an application due to a throttling issue. Try again later.

![Connect applications interface showing connected and not connected apps with action buttons.](images/fabric-22.png)

## You are not authorized to use AppFabric. Please log in to AppFabric again (`AccessDeniedException`)

You might get this message when the AppFabric user portal fails to list the applications or
disconnects an application due to an access denied exception. Sign in to AppFabric again.

![Connect applications interface showing connected and unconnected apps with action buttons.](images/fabric-21.png)
