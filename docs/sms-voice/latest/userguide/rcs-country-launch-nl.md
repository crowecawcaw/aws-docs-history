

# Launching RCS in the Netherlands
<a name="rcs-country-launch-nl"></a>

To launch your AWS RCS Agent in the Netherlands, submit a country launch registration using the `NL_RCS_LAUNCH_REGISTRATION` registration type. The Netherlands uses the standard baseline registration form but both carriers require a proactive brand approval email. For the baseline fields, see [Standard country launch registration](rcs-country-launch-standard.md).

## Proactive brand approval email (required after registration)
<a name="rcs-country-launch-nl-approval"></a>

**Important**  
In addition to the console registration, you must send a proactive brand approval email. Your registration cannot be fully approved until the carriers receive your brand authorization.

Both Dutch carriers (Odido and VodafoneZiggo) require proactive brand approval. After you submit your registration in the AWS End User Messaging console, send the following email:

```
FROM: [Your business email address]
TO: aws-end-user-messaging-rcs-approvals@amazon.com
SUBJECT: RCS Brand Approval - [Your Brand Name]

Dear Team,

I at [Your Brand/Company Name] hereby give permission that Infobip may use
the brand name and logo for the use of sending RCS messages to users of the
Odido and VodafoneZiggo networks in the Netherlands.

Agent ID: [Your RCS for Business ID]

Regards,
[Your Name]
[Your Job Title]
[Your Company Name]
```

**Note**  
Your Agent ID (RCS for Business ID) can be found in the AWS End User Messaging console. Navigate to **SMS > RCS agents**, select your agent, then open the **Country launch status** tab. The Agent ID is listed as the **RCS for Business ID** in the Launch Status by Country section. The format is `{agent_name}_{unique_id}_agent`.
+ The email must be sent from the same business email address listed as the brand contact in your registration form.
+ No additional documents or attachments are required for the Netherlands.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).