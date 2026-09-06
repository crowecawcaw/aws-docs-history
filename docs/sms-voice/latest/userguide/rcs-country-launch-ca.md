

# Launching RCS in Canada
<a name="rcs-country-launch-ca"></a>

To launch your RCS agent in Canada, submit a country launch registration using the `CA_RCS_LAUNCH_REGISTRATION` registration type in the AWS End User Messaging console or API.

The Canada launch registration uses an extended form that includes all of the standard baseline fields plus additional company information, a company address, an extended contact field, RCS partner details, and French-language compliance keywords required for Canadian bilingual regulations. For the baseline fields included in all country launch registrations, see [Standard country launch registration](rcs-country-launch-standard.md).

## Registration form (console)
<a name="rcs-country-launch-ca-console"></a>

The Canada launch registration uses an extended form. It includes all fields from the standard country launch registration (see [Standard country launch registration](rcs-country-launch-standard.md)), plus the following additional sections:Company information

**Company ID** (required)  
Your business number or tax identification number.

**Company name** (required)  
The legal name of your company as registered with the relevant authority.

**DBA name** (optional)  
Your “doing business as” name, if different from the legal company name.

**Company website** (required)  
The URL of your company's public website.

**Legal entity type** (required)  
The type of legal entity (for example, Corporation, LLC, Partnership, Sole Proprietorship, or Non-Profit).

**Stock symbol** (conditional)  
Your company's stock ticker symbol. Required only if your company is publicly traded.

**Stock exchange** (conditional)  
The stock exchange where your company is listed. Required only if your company is publicly traded.

**Company overview** (required)  
A brief description of what your company does and the products or services it offers.

**Industry sector** (required)  
The industry sector that best describes your company's primary business.Company address

**Address line 1** (required)  
The primary street address of your company.

**Address line 2** (optional)  
Additional address information such as suite or floor number.

**City** (required)  
The city where your company is located.

**State/Province** (required)  
The province where your company is located.

**Postal code** (required)  
The postal code for your company address.

**Country code** (required)  
The country code for your company address (for example, CA).Extended contact information

**Primary contact phone number** (required)  
A phone number for the primary contact person. This is in addition to the contact name, email, and job title collected in the standard baseline form.RCS partner information

**RCS partner name** (required)  
The name of your RCS technology partner or aggregator.

**RCS partner contact name** (required)  
The name of your contact person at the RCS partner organization.

**RCS partner contact email** (required)  
The email address of your contact person at the RCS partner organization.

## French compliance keywords
<a name="rcs-country-launch-ca-french"></a>

Canada's bilingual regulations require that you provide French-language equivalents for standard compliance keywords. These keywords allow French-speaking recipients to interact with your RCS agent in their preferred language. The following French compliance keywords are required in addition to the English HELP and STOP keywords collected in the standard baseline form:

**AIDE response** (required)  
The French equivalent of the HELP keyword response. When a recipient sends “AIDE”, your agent must reply with a French-language help message that explains how to get assistance and how to opt out.

**ARRÊT response** (required)  
The French equivalent of the STOP keyword response. When a recipient sends “ARRÊT”, your agent must reply with a French-language confirmation that the recipient has been opted out and will no longer receive messages.

**INFO response** (required)  
A French-language informational keyword response. When a recipient sends “INFO”, your agent must reply with a French-language message providing information about the service and the sending organization.

## Screen recording requirement
<a name="rcs-country-launch-ca-video"></a>

The Canada launch registration requires a screen recording that demonstrates your RCS messaging experience. The recording should show the end-user experience of receiving and interacting with your RCS messages. Registrations submitted without a valid screen recording are rejected.

For detailed video format and content requirements, see [Launch video requirements](rcs-compliance-video.md).