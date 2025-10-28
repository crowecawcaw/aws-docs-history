# Amazon SNS integration with Firebase Cloud

Messaging authentication setup

This topic describes how to obtain the required FCM API (HTTP v1) credentials from Google
to use with the AWS API, AWS CLI and the AWS Management Console.

###### Important

March 26, 2024 – Amazon SNS supports FCM HTTP v1 API for Apple devices and Webpush
destinations. We recommend that you migrate your existing mobile push applications to
the latest FCM HTTP v1 API on or before June 1, 2024 to avoid application
disruption.

January 18, 2024 – Amazon SNS introduced support for FCM HTTP v1 API for mobile push
notification delivery to Android devices.

June 20, 2023 – Google deprecated their Firebase Cloud Messaging (FCM) legacy HTTP API. Amazon SNS
now supports delivery to all device types using FCM HTTP v1 API. We recommend that you
migrate your existing mobile push applications to the latest FCM HTTP v1 API on or
before June 1, 2024 to avoid disruption.

You can authorize Amazon SNS to send push notifications to your applications by providing
information that identifies you as the developer of the app. To authenticate, provide either
an **API key** or a **token**
[when creating a platform application](../api/API_SetPlatformApplicationAttributes.md "../api/API_SetPlatformApplicationAttributes.md"). You can get the following information
from your [Firebase application console](https://firebase.google.com/?gad=1&gclid=CjwKCAiA0syqBhBxEiwAeNx9N27M7zxHjlS74_gp4mAS4QTMQH5J35sTO29od-yauuq259zzX_I2DRoCrbsQAvD_BwE&gclsrc=aw.ds "https://firebase.google.com/?gad=1&gclid=CjwKCAiA0syqBhBxEiwAeNx9N27M7zxHjlS74_gp4mAS4QTMQH5J35sTO29od-yauuq259zzX_I2DRoCrbsQAvD_BwE&gclsrc=aw.ds"):

**API Key**

The API key is a credential used when calling Firebase’s Legacy API. The FCM
Legacy APIs will be removed by Google June 20, 2024. If you are currently using
an API key as your platform credential, you can update the platform credential
by selecting **Token** as the option, and uploading the
associated JSON file for your Firebase application.

**Token**

A short lived access token is used when calling the HTTP v1 API. This is
Firebase’s suggested API for sending push notifications. In order to generate
access tokens, Firebase provides developers a set of credentials in the form of
a private key file (also referred to as a service.json file).

## Prerequisite

You must obtain your FCM service.json credentials before you can begin managing FCM
settings in Amazon SNS. To obtain your service.json credentials, see [Migrate from
legacy FCM APIs to HTTP v1](https://firebase.google.com/docs/cloud-messaging/migrate-v1 "https://firebase.google.com/docs/cloud-messaging/migrate-v1") in the Google Firebase documentation.

## Managing FCM settings using the CLI

You can create FCM push notifications using the AWS API. The number and size of
Amazon SNS resources in an AWS account are limited. For more information, see [Amazon Simple Notification Service endpoints and
quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") in the _AWS General Reference Guide_.

###### To create an FCM push notification together with an Amazon SNS topic (AWS API)

When using **key** credentials, the
`PlatformCredential` is `API key`. When using
**token** credentials, the `PlatformCredential` is a
JSON formatted private key file:

- [`CreatePlatformApplication`](../api/API_CreatePlatformApplication.md "../api/API_CreatePlatformApplication.md")

###### To retrieve an FCM credential type for an existing Amazon SNS topic (AWS API)

Retrieves the credential type `"AuthenticationMethod": "Token"`, or
`"AuthenticationMethod": "Key"`:

- [GetPlatformApplicationAttributes](../api/API_GetPlatformApplicationAttributes.md "../api/API_GetPlatformApplicationAttributes.md")

###### To set an FCM attribute for an existing Amazon SNS topic (AWS

API)

Sets the FCM attribute:

- [SetPlatformApplicationAttributes](../api/API_SetPlatformApplicationAttributes.md "../api/API_SetPlatformApplicationAttributes.md")

## Managing FCM settings using the

console

You can create FCM push notifications using the AWS Command Line Interface (CLI). The number and size
of Amazon SNS resources in an AWS account are limited. For more information, see [Amazon Simple Notification Service endpoints and
quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md").

###### To create an FCM push notification together with an Amazon SNS topic (AWS CLI)

When using **key** credentials, the
`PlatformCredential` is `API key`. When using
**token** credentials, the `PlatformCredential` is a
JSON formatted private key file. When using the AWS CLI, the file
must be in string format and special characters must be ignored. To format the file
correctly,Amazon SNS recommends using the following command: `SERVICE_JSON=`jq @json
<<< cat service.json``:

- [create-platform-application](../../../cli/latest/reference/sns/create-platform-application.md "../../../cli/latest/reference/sns/create-platform-application.md")

###### To retrieve an FCM credential type for an existing Amazon SNS topic (AWS CLI)

Retrieves the credential type `"AuthenticationMethod": "Token"`, or
`"AuthenticationMethod": "Key"`:

- [get-platform-application-attributes](../../../cli/latest/reference/sns/get-platform-application-attributes.md "../../../cli/latest/reference/sns/get-platform-application-attributes.md")

###### To set an FCM attribute for an existing Amazon SNS topic (AWS CLI)

Sets the FCM attribute:

- [set-platform-application-attributes](../../../cli/latest/reference/sns/set-platform-application-attributes.md "../../../cli/latest/reference/sns/set-platform-application-attributes.md")

## Managing FCM settings (console)

Use the following steps to enter and manage your Firebase Cloud Messaging (FCM) credentials in
Amazon SNS.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the navigation pane, select **Push Notifications**.
3. In the **Platform applications** section, select the
   **FCM platform application** whose credentials
   you want to edit, and then choose **Edit**.
4. In the **Firebase Cloud Messaging Credentials** section, choose one of the
   following options:
   - **Token-based authentication**
     (recommended method) – Upload the **private
     key file** (JSON) that you downloaded from the Firebase
     Console. This file contains the credentials needed to generate
     short-lived access tokens for FCM notifications. To get this
     file:
     1. Go to your [Firebase application console](https://firebase.google.com/?gad=1&gclid=CjwKCAiA0syqBhBxEiwAeNx9N27M7zxHjlS74_gp4mAS4QTMQH5J35sTO29od-yauuq259zzX_I2DRoCrbsQAvD_BwE&gclsrc=aw.ds "https://firebase.google.com/?gad=1&gclid=CjwKCAiA0syqBhBxEiwAeNx9N27M7zxHjlS74_gp4mAS4QTMQH5J35sTO29od-yauuq259zzX_I2DRoCrbsQAvD_BwE&gclsrc=aw.ds").
     2. In the **Project Settings**,
        select **Cloud Messaging**.
     3. Download the **Private key** JSON
        file (for use in the token-based authentication method).

   - **API key authentication** – If
     you prefer to use the older API key authentication method, enter the
     **Google API key** in the provided
     field. To get this file:
     1. Go to your [Firebase application console](https://firebase.google.com/?gad=1&gclid=CjwKCAiA0syqBhBxEiwAeNx9N27M7zxHjlS74_gp4mAS4QTMQH5J35sTO29od-yauuq259zzX_I2DRoCrbsQAvD_BwE&gclsrc=aw.ds "https://firebase.google.com/?gad=1&gclid=CjwKCAiA0syqBhBxEiwAeNx9N27M7zxHjlS74_gp4mAS4QTMQH5J35sTO29od-yauuq259zzX_I2DRoCrbsQAvD_BwE&gclsrc=aw.ds").
     2. In **Project Settings**, select
        **Cloud Messaging**.
     3. Copy the **Server key** (API key)
        to use for sending notifications.

5. When you finish, choose **Save changes**.

**Related topics**

- [Using Google Firebase Cloud Messaging v1 payloads in
  Amazon SNS](sns-fcm-v1-payloads.md "sns-fcm-v1-payloads.md")
