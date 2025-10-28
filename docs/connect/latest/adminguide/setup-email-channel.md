# Set up email in Amazon Connect

Following is an overview of the steps to set up the email channel for your contact center.

- [Enable email for your Amazon Connect instance](enable-email1.md "enable-email1.md"). During this process
  you get an auto-generated email address. You also have the option of adding five
  custom addresses.
- [Create email addresses](create-email-address1.md "create-email-address1.md").
- [Create or update queues](create-queue.md "create-queue.md") for outbound email. In
  the **Outbound email configuration** section:
  - **Default email address**: Specify the outbound email
    address that agents will use when sending an email. For example, if an agent
    is on the phone with a customer, and they need to email the customer
    instructions after the conversation, the agent can initiate an outbound
    email with this address.
  - **Outbound email flow**: Select the **Default
    outbound flow** from the dropdown menu, or select another flow
    that is type Outbound.

- [Create or update routing profiles](routing-profiles.md "routing-profiles.md") to specify
  that agents can handle email contacts.

###### Important

In the routing profile:

    + **Default outbound queue** defines the email address
     agents will use for any outbound emails they initiate.
    + **Maximum contacts per agent** defines how many
     emails agents can receive, and double that number is how many outbound emails
     agents can initiate. For example, if you set **Maximum contacts
     per agent** to 5, agents can receive up to 5 emails and create
     up to 10 agent-initiated outbound emails.

- [Create message templates](create-message-templates1.md "create-message-templates1.md"). Email
  templates can define the structure of the email for the agent, for example, for a
  signature or a disclaimer, or they can be a full response.
- Configure flows with the [Send message](send-message.md "send-message.md") block. Use this block to send a message to
  your customer based on a template or custom message. In addition, you can specify:
  - The To and From email addresses and display names. You can specify them
    manually or dynamically by using [System attributes](connect-attrib-list.md#attribs-system-table "connect-attrib-list.md#attribs-system-table") such as:

        - **Customer endpoint address**: This is the
         customer's email address that initiated the contact.
        - **System email address**: This is the email
         address that the customer sent the email to.
        - **Customer display name**: This is captured from
         the email the customer sent to you.
        - **System display name**: The display name of the
         email the customer sent to.
        - **CC Email Address List**: The full list of cc'ed
         email addresses on the customer's email.
        - **To Email Address List**: The full list of To
         email addresses on the customer's email.

    For example, to send an automatic reply when a customer emails you, set
    **Email address** dynamically to **Customer
    endpoint address**, and **Display name**
    dynamically to **Customer display name**.

  - **Message**: Specify a template or enter plain
    text.
    - You can specify the **Subject** dynamically by
      using the **Segment attribute** - **Email
      Subject**.
    - You can specify the **Message** dynamically by
      choosing a **User-defined** attribute.

  - **Link to contact**: Choose if you want to link the
    inbound contact email to the outbound contact email. You may not want to
    choose this option for automatic reply emails.

- Use the attributes in the [Check contact
  attributes](check-contact-attributes.md "check-contact-attributes.md") block to check the channel of
  the contact. If it's an email, you can use the following [Segment attributes](connect-attrib-list.md#attribs-segment-attributes "connect-attrib-list.md#attribs-segment-attributes") to check:
  - **Email Subject**: You can check the subject for certain
    keywords, for example.
  - **Amazon SES Spam Verdict** and **Amazon SES Virus
    Verdict**: When the customer's email comes in, Amazon SES scans it
    for spam and viruses. For example, if the condition equals FAILED (that
    means, the email failed the check) you can disconnect the contact or send
    the email to a special queue for managers to review it.

- Assign the following security profile permission to your agents who need to
  initiate outbound emails.
  - **Contact Control Panel (CCP)** - **Initiate
    email conversations**
