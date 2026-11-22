

# MyChart password reset

MyChart password reset is part of the agentic capabilities for patient access. It helps a verified patient reset the password for their Epic MyChart account. The patient calls in, patient verification confirms the patient’s identity, and MyChart password reset sends a reset link to the email address or phone number on file. Callers reach it by phone. It supports English only.

To make MyChart password reset available to callers, turn it on in the web app. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

## Prerequisites
<a name="pr-prerequisites"></a>

Before you turn on MyChart password reset, make sure the following are in place:
+ Patient verification is turned on for the same agent.
+ Your organization licenses Epic MyChart.
+ Your Epic environment is set up for MyChart password reset. For more information, see [Epic EHR integration](epic-ehr-integration.md).
+ The patient record returns the patient’s MyChart account ID.

## How it works
<a name="pr-how-it-works"></a>

MyChart password reset sends the reset link to the contact information already on file. It works as follows:
+ The capability confirms whether to send the link by email or text message.
+ It never accepts a new email address or phone number. It uses only the patient’s primary email address or phone number on file in Epic.
+ If one channel does not work, it offers to send the link through the other channel. For example, if the patient hasn’t opted in to MyChart text messages, the capability offers to send the link by email.
+ It makes up to 3 send attempts in total. After that, it transfers the patient to a person.

## What MyChart password reset does not do
<a name="pr-limitations"></a>

MyChart password reset does not do the following:
+ Change or recover a username
+ Unlock an account
+ Create or activate a MyChart account, or handle activation codes
+ Change contact information, such as an email address or phone number
+ Support languages other than English

## Reasons the capability transfers to a person
<a name="pr-escalation"></a>

MyChart password reset transfers the patient to a person for any of these reasons:
+ The patient is not verified.
+ The patient has no MyChart account.
+ MyChart is not licensed.
+ A system error prevents the reset.
+ The patient reaches the limit of send attempts.
+ The capability detects a possible account security concern.

When it transfers a call, it passes the call context to the person.

## Memory and personalization
<a name="pr-memory"></a>

When memory and personalization is turned on for your domain, MyChart password reset can do the following:
+ Resume an unfinished reset from an earlier call.
+ Reuse a patient’s remembered reset channel, such as email or text message.

For more information, see [Memory and personalization](pe-memory.md).

## Customization options
<a name="pr-customization"></a>

You turn on and configure MyChart password reset in the web app. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

It has one setting:
+  **Reset method**: Choose how the capability sends the reset link. The values are **Email only**, **Text message only**, and **Let the caller choose**. The default is **Let the caller choose**.

## Answer reset-process questions from your knowledge base
<a name="pr-knowledge-base"></a>

MyChart password reset can answer questions about the reset process, such as how long a link stays valid or what the password requirements are. It answers these questions from the knowledge base (KB) documents that you provide and scope to password reset.