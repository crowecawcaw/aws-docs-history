# Ingress endpoints

An ingress endpoint is the key infrastructure component in Mail Manager that receives, routes, and
manages your email by utilizing policies and rules you configure to determine which emails
should be rejected, which ones should be allowed, and which ones should be acted
upon.

Each ingress endpoint has its own traffic policy to determine which emails to block or allow, and
its own rule set to perform actions on the email you do allow in; therefore, by creating
multiple ingress endpoints, you can delegate each one to manage and route specific types of email.
This level of granularity will help you to build an email management system that's tailored
to your business needs.

###### Prerequisite workflow to create an ingress endpoint

At the time of creating your ingress endpoint, you must assign it a traffic policy and a rule
set that have _already been created_. Therefore, the workflow for
creating an ingress endpoint should be in the following order:

1. Start by creating a traffic policy to determine the email you want to block or allow.
   For details, see [Creating traffic policies and policy statements in
   the SES console](eb-filters.md#eb-filters-create-console "eb-filters.md#eb-filters-create-console").
2. Next, create a rule set to perform actions on the email you allow in. For details,
   see [Creating rule sets and rules in the SES
   console](eb-rules.md#eb-rules-create-console "eb-rules.md#eb-rules-create-console").
3. Finally, create your ingress endpoint and assign to it the traffic policy and rule set you
   just created or any others you previously created.
   Once you create your ingress endpoint, you must configure it with the environment you're using to
   receive email, whether that be the configuration of an on-premise SMTP client or a web-based
   DNS domain host. This is discussed below in [Receiving email through the public
   endpoints](#eb-ingress-a-record "#eb-ingress-a-record").

## Configuring your environment to use an

ingress endpoint

SES supports both public endpoints and Amazon Virtual Private Cloud (VPC) endpoints for ingress
endpoints to accept incoming email. The following sections explain how to configure your
ingress endpoint to use either of these options.

###### Topics

- [Public endpoint
  configuration](#eb-ingress-a-record "#eb-ingress-a-record")
- [VPC endpoint
  configuration](#eb-ingress-vpc-endpoint "#eb-ingress-vpc-endpoint")

### Receiving email through the public

endpoints

###### Using the "A" record

At the time you create an ingress endpoint, an "A" record for the endpoint will be
generated and its value displayed on the ingress endpoint's summary screen in the
SES console. The way you use the value of this record depends on the type
of endpoint you created and your use case:

- Open endpoint –
  Mail sent to your domain will resolve directly
  to your ingress endpoint—no authentication required.
  - Copy and paste the value of the "A" record either directly into
    the SMTP configuration of an on-premise SMTP client or into an MX
    record for your domain in your DNS configuration.
  - Supported port: 25
  - Supports STARTTLS: Yes

- Authenticated endpoint – Mail sent to
  your domain has to come from authorized senders whom you’ve shared your SMTP
  credentials with, such as your on-premise email servers.
  - Copy and paste the value of the "A" record directly into the SMTP
    configuration of an on-premise SMTP client as well as your user name
    and password.
  - Supported ports: 25, 587 ([RFC
    2476](https://www.ietf.org/rfc/rfc2476.txt "https://www.ietf.org/rfc/rfc2476.txt"))
  - Supports STARTTLS: Yes

If you're using an MX record in your configuration, keep in mind that while every
DNS provider has different procedures and interfaces for configuring records, the
key pieces of information you need to put into you DNS settings are listed in the
following example:

All email sent to *recipient@marketing.example.com* will go to
your ingress endpoint because you entered the ingress endpoint's "A" record as the value
for an MX record in your domain’s DNS settings:

- Domain –
  `marketing.example.com`
- MX record value –
  `890123abcdef.ghijk.mail-manager-smtp.amazonaws.com`
  _(This is the "A" record value copied from your
  ingress endpoint.)_
- Priority – `10`

###### Connecting to the authenticated endpoint

For the authorized senders whom you’ve shared your SMTP credentials with in
order to connect to your authenticated endpoint, the following protocols must be
followed for the _username_ and _password_
in order to establish a successful connection to the server:

- Username – This is the ingress endpoint ID
  and must be encoded in Base64. _(See [Step 11.](#find-ingress-id "#find-ingress-id") in the console procedures
  to learn how to find the ingress endpoint ID.)_
- Password – This is the one used
  during ingress endpoint creation and must be encoded in Base64.

The following example shows a typical SMTP AUTH server and client exchange
establishing connection:

```
S: 250 AUTH LOGIN PLAIN
C: AUTH LOGIN
S: 334 VXNlcm5hbWU6
C: SW5ncmVzc1BvaW50
S: 334 UGFzc3dvcmQ6
C: SW5ncmVzc1Bhc3N3b3Jk
S: 235 Authentication successful
```

This example contains the following properties:

- `S` means "Server"—the SMTP server accepting
  messages.
- `C` means "Client"—the SMTP client establishing
  connection with the server and sending messages to server.
- `250 AUTH LOGIN PLAIN` is a response from the server with AUTH
  methods supported, `AUTH LOGIN` or `AUTH PLAIN`, the
  sender could choose either of them, and send SMTP commands compliant with
  the SMTP Service Extension for Authentication specification [RFC 2554](https://www.ietf.org/rfc/rfc2554.txt "https://www.ietf.org/rfc/rfc2554.txt"). `AUTH
LOGIN` is used here.
- `334 VXNlcm5hbWU6` – Server prompting for the username in
  Base64.
- `SW5ncmVzc1BvaW50` – Client responding with ingress endpoint ID
  in Base64.
- `334 UGFzc3dvcmQ6` – Server prompting for the password in
  Base64.
- `SW5ncmVzc1Bhc3N3b3Jk` – Client responding with ingress endpoint
  password in Base64.

### Receiving email through Amazon VPC

endpoints

In addition to public ingress endpoints, you can use VPC endpoints with SES
ingress endpoints for secure, private email ingestion within your private network
infrastructure.

###### Configuration differences compared to using public ingress endpoints

- The "A" Record typically available for public endpoints is not
  provided.
- You must connect to the ingress endpoint using DNS names provided by your VPC
  endpoint.
- All connections use private networking within your VPC.

###### Types of ingress endpoints supported through VPC endpoints

SES supports two types of ingress points through VPC endpoints:

- Open ingress endpoint – Email sent to your
  domain route directly through the VPC endpoint without requiring sender
  authentication.

Configuration requirements:

    + Create a private open ingress endpoint by associating it with a VPC
     endpoint ID you own.
    + Supported ports: 25, 587
    + Supports STARTTLS: Yes

- Authenticated ingress endpoint – Mail sent
  to your domain has to come from authorized senders whom you’ve shared your
  SMTP credentials with, such as your on-premise email servers.

Configuration requirements:

    + Create a private authenticated ingress endpoint by associating it with a
     VPC endpoint ID you own.
    + Supported ports: 25, 587
    + Supports STARTTLS: Yes
    + Authentication uses the same base64-encoded username and password
     mechanism as public authenticated endpoints.

###### VPC endpoint requirements

To use a VPC endpoint with an SES ingress endpoint, the following requirements
must be met:

- The VPC endpoint must be active and available.
- The VPC endpoint must be owned by the same AWS account as the ingress endpoint
  (cross-account access is not supported).
- The VPC endpoint must be created for the appropriate service name based on
  the type of ingress endpoint:
  - Open ingress endpoint –
    `com.amazonaws.`region`.mail-manager-smtp.open`
  - Authenticated ingress endpoint –
    `com.amazonaws.`region`.mail-manager-smtp.auth`
  - FIPS open ingress endpoint –
    `com.amazonaws.`region`.mail-manager-smtp.open.fips`
  - FIPS authenticated ingress endpoint
    –
    `com.amazonaws.`region`.mail-manager-smtp.auth.fips`

###### Important configuration notes

- US & Canada regions – FIPS
  endpoints are the only VPC endpoints available in US and Canada
  regions and are the correct ones to use in these regions.
- One-to-one relationship – Each VPC
  endpoint can only be associated with a single ingress endpoint. You cannot use the
  same VPC endpoint for multiple ingress endpoints.
- No VPC endpoint policies – Unlike
  other AWS services, VPC endpoints used with ingress endpoints do not support VPC
  endpoint policies. SES automatically verifies that the VPC endpoint
  owner and the ingress endpoint owner are the same AWS account.
- Private DNS only – All DNS names
  provided by the VPC endpoint will be private DNS names accessible only
  within your VPC.
- Validation at creation time –
  SES performs validation during resource creation to ensure the VPC
  endpoint meets all requirements.

###### Connecting to your ingress endpoint through a VPC endpoint

After configuring your VPC endpoint and ingress endpoint:

1. Retrieve the DNS names generated for your VPC endpoint.
2. Configure your SMTP clients or email servers to use these DNS names for
   connection.
3. If using an authenticated endpoint, configure your SMTP clients with the
   appropriate base64-encoded credentials used with your authenticated
   ingress endpoint.

## Creating an ingress endpoint in the SES

console

The following procedure shows you how to use the **Ingress endpoint** page
in the SES console to create ingress endpoints and manage the ones you've already
created.

###### To create an manage ingress endpoints using the console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation panel, choose **Ingress endpoints** under
   **Mail Manager**.
3. On the **Ingress endpoints** page, select **Create ingress
   endpoint**.
4. On the **Create new ingress endpoint** page, enter a unique name for
   your ingress endpoint.
5. Choose whether it will be a **Open** or
   **Authenticated** endpoint.
   - If you choose **Authenticated**, select either
     **SMTP password** and enter a password (to be
     shared with authorized senders), or **Secret** and
     select one of your secrets from **Secret ARN**.
     _If you select a previously created secret, it must contain
     the policies indicated in the following steps for creating a new
     secret._
   - You have the option to create a new secret by choosing
     **Create new**—the AWS Secrets Manager console will
     open where you can continue to create a new key:
   1. Choose **Other type of secret** in **Secret
      type**.
   2. In **Key/value pair**, enter `password`
      for the key, and your actual password for the value.

   ###### Note

   For **Key**, you must only enter
   `password` (anything else will cause authentication
   to fail). 3. Select **Add new key** to create a KMS customer managed key
   (CMK) in **Encryption key**—the AWS KMS console
   will open. 4. Choose **Create key** on the **Customer
   manged keys** page. 5. Keep the default values on the **Configure key** page
   and select **Next**. 6. Enter a name for your key in **Alias** (optionally,
   you can add a description and tag), followed by
   **Next**. 7. Select any users (other than yourself) or roles you want to permit to
   administer the key in **Key administrators** followed
   by **Next**. 8. Select any users (other than yourself) or roles you want to permit to
   use the key in **Key users** followed by
   **Next**. 9. Copy and paste the [KMS CMK policy](eb-policies.md#eb-policies-ingress-cmk "eb-policies.md#eb-policies-ingress-cmk") into the
   **Key policy** JSON text editor at the
   `"statement"` level by adding it as an additional
   statement separated by a comma. Replace the region and account number
   with your own. 10. Choose **Finish**. 11. Select your browser's tab where you have the AWS Secrets Manager **Store
   a new secret** page open and select the _refresh
   icon_ (circular arrow) next to the **Encryption
   key** field, then click inside the field and select your
   newly created key. 12. Enter a name in the **Secret name** field on the
   **Configure secret** page. 13. Select **Edit permissions** in **Resource
   permissions**. 14. Copy and paste the [Secrets resource
   policy](eb-policies.md#eb-policies-ingress-secrets "eb-policies.md#eb-policies-ingress-secrets") into the
   **Resource permissions** JSON text editor and
   replace the region and account number with your own. (Be sure to delete
   any example code in the editor.) 15. Choose **Save** followed by
   **Next**. 16. Optionally configure rotation followed by **Next**. 17. Review and store your new secret by choosing
   **Store**. 18. Select your browser's tab where you have the SES
   **Create new ingress endpoint** page open and
   choose **Refresh list**, then select your newly created
   secret in **Secret ARN**.

6. Select a rule set containing the rule actions you want to perform on the email
   you allow in.
7. Select a traffic policy to determine the email you want to block or allow.
8. Choose whether it will be a **Public** or
   **Private** network.
   - For a public network, choose either **IPv4** only or
     **Dualstack** (IPv4 and IPv6) addressing.
   - For a private network, select or enter a VPC endpoint that you've
     shared with authorized senders in the same account, such as IAM users or
     roles. Optionally, you can create a new VPC endpoint by choosing
     **Create VPC endpoint** to open the Amazon VPC
     console.

9. Select **Create ingress endpoint**.
10. In **General details**, "Provisioning" will be displayed
    while your ingress endpoint is being created—refresh the page until "Active" is
    displayed and the **ARecord** field contains a value. Copy the
    "A" record value and paste it into your DNS configuration or your SMTP client as
    discussed in [Public endpoint
    configuration](#eb-ingress-a-record "#eb-ingress-a-record").
11. Just above the **General
    details** container on the console, there is a large, unlabeled
    number prefixed by "inp" (also replicated in the breadcrumb trail at the top of
    the page), for example, **inp-1abc2de3fghi4jkl5mnop6qr**. This
    is referred to as the _ingress endpoint ID_, its value is used as
    the _username_ to login to your ingress server. (You'll need
    to share this with your authorized senders to connect to your endpoint.)
12. You can view and manage the ingress endpoints you've already created from the
    **Ingress endpoints** page. If there's an ingress endpoint you want to
    remove, select it's radio button followed by **Delete**.
13. To edit an ingress endpoint, select its name to open its summary page:
    - You can change the endpoint's active status by choosing
      **Edit** in **General details**
      followed by **Save changes**.
    - You can select a different rule set or traffic policy by choosing
      **Edit** in either **Rule set** or
      **Traffic policy** followed by **Save
      changes**.
