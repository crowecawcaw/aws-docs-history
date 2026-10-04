

# Country support
<a name="nx-rcs-scale-country"></a>

AWS End User Messaging supports RCS country launches in 22 countries across North America, Europe, Asia Pacific, Latin America, and the Middle East and Africa, including the United States, Canada, United Kingdom, Germany, France, and Brazil. Each country has its own registration form, requirements, and carrier approval process, and each carrier in a country reviews your AWS RCS Agent independently. Review the requirements for the countries you want to launch in before you register. For the current list of supported countries, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html).

## How to launch in a country
<a name="nx-rcs-scale-country-process"></a>

Before you can send RCS messages to any recipient in a country, rather than only to your test devices, you launch your agent in that country. A country launch takes your agent through registration and carrier review. You launch each country separately, so you can go live in one country while another is still in review.

**To launch your RCS agent in a country**

1. Confirm the country is supported and review its requirements. Requirements vary by country and can include details about your brand, your use case, and sample messages.

1. Create a country launch registration for the country. Use the console, or use the `CreateRegistration` operation with the registration type for an RCS country launch, and fill in the required fields for that country.

1. Submit the registration for review with the `SubmitRegistrationVersion` operation. AWS End User Messaging reviews the submission and forwards it to the carriers in that country.

1. Wait for carrier approval. Each carrier in the country reviews your agent independently, so a country can be partially launched while some carriers have approved and others are still reviewing. Approval timelines vary by country and by carrier.

1. When the launch is active, send to recipients on the approved carriers in that country. Messages to recipients whose carrier has not approved your agent fall back to SMS when you send through a pool or set a fallback configuration.

## Track your country launch status
<a name="nx-rcs-scale-country-status"></a>

You can check where each country launch stands, including the status for each carrier, with the `DescribeRcsAgentCountryLaunchStatus` operation or on the agent's page in the console. A country launch moves through the following statuses.


| Status | Description | 
| --- | --- | 
| Created | The country launch has been created but not yet submitted for review. | 
| Pending | The country launch has been submitted and is awaiting carrier review. | 
| Partial | Some carriers in the country have approved your agent and others are still reviewing. You can send to recipients on the approved carriers. | 
| Active | The country launch is approved and you can send to recipients in that country. | 
| Rejected | The country launch was rejected. Review the feedback, update your registration, and resubmit. | 

For how to test your agent before you launch, and the full path from the testing state to production, see [Move out of the sandbox](nx-rcs-scale-sandbox.md).