

# Business verification for toll-free registrations
<a name="registration-help-tfn-verification"></a>

When you submit a toll-free number registration, your business identity is verified using the company identification number (such as an EIN) that you provide. This verification confirms that your business is legitimate and that the company name on your registration matches official records.

## Why business verification is required
<a name="registration-help-tfn-verification-why"></a>

Business verification is an industry-wide requirement for toll-free messaging. Carriers use your business registration number to confirm your identity against official business registries. This helps prevent fraud, protects legitimate businesses from impersonation, and ensures that toll-free messaging traffic is trusted.

## Accepted identification types
<a name="registration-help-tfn-verification-types"></a>

The identification type you provide must match the country where your business is registered. The following table lists common identification types by country.


| Country | ID type | Full name | Format | 
| --- | --- | --- | --- | 
| United States | EIN | Employer Identification Number | XX-XXXXXXX | 
| Canada | CBN | Canada Business Number | XXXXXXXXX (9 digits) | 
| United Kingdom | CRN | Company Registration Number | XXXXXXXX (8 chars) | 
| Australia | ABN | Australian Business Number | XX XXX XXX XXX (11 digits) | 
| EU countries | VAT | VAT Identification Number | Country prefix \+ digits (varies) | 
| New Zealand | NZBN | New Zealand Business Number | XXXXXXXXXXXXX (13 digits) | 
| Brazil | CNPJ | Cadastro Nacional da Pessoa Jurídica | XX.XXX.XXX/XXXX-XX | 

If your country or identification type is not listed above, choose **OTHER** and provide your official business registration number in the format issued by your local authority.

## How verification works
<a name="registration-help-tfn-verification-how"></a>

When you submit your toll-free registration, the following verification steps occur:

1. Your company identification number is checked against third-party business registries.

1. The **company name** on your registration is compared to the name associated with your identification number in official records.

1. If both match, verification passes automatically and your registration proceeds to content review.

1. If either check fails, your registration is denied with a business verification failure reason.

## Company name requirements
<a name="registration-help-tfn-verification-name"></a>

The company name on your registration must exactly match the legal name associated with your business registration number. This is the most common cause of verification failures.

**Important**  
Use your **legal entity name** (the name on your incorporation documents or IRS records), not your trade name, DBA (doing business as), or brand name.

For example:
+ **Correct:** "Acme Holdings LLC" (legal name on EIN records)
+ **Incorrect:** "Acme" (trade name) or "Acme Delivery" (DBA)

## When verification fails
<a name="registration-help-tfn-verification-failure"></a>

If automated business verification fails, your registration is denied. You can resolve this by uploading an official business registration document that confirms your identity.

### Accepted documents
<a name="registration-help-tfn-verification-docs"></a>

Upload one of the following documents using the optional business registration document field on the registration form:
+ **IRS CP 575** — EIN Confirmation Letter (issued when EIN was originally assigned)
+ **IRS 147C** — EIN Verification Letter (can be requested from the IRS at any time)
+ **State incorporation certificate** — Certificate of incorporation or formation from your state
+ **Official business registry extract** — For non-US businesses, an official extract from your country's business registry

The document must clearly show both the legal entity name and the registration number that match your form entries.

## Common verification failures and solutions
<a name="registration-help-tfn-verification-common-failures"></a>


| Failure reason | Cause | Solution | 
| --- | --- | --- | 
| Name mismatch | Company name on form doesn't match the name associated with your BRN in official records | Update the company name to your exact legal entity name as it appears on your incorporation or IRS documents | 
| Wrong ID type | Selected identification type doesn't match the number format provided | Verify you selected the correct type (for example, EIN for US, CBN for Canada) and that the number format matches | 
| Entity not found | Business not found in third-party verification databases | Upload an official business registration document as proof of identity. This is common for recently formed businesses or entities not in commercial databases. | 
| DBA/trade name used | Registration uses a "doing business as" name instead of the legal entity name | Replace with the legal name from your incorporation documents. Your DBA can be used in other fields like brand name. | 
| Recently formed business | Business was recently incorporated and hasn't appeared in verification databases yet | Upload your incorporation certificate or IRS CP 575 letter as supporting documentation | 

## Government entities
<a name="registration-help-tfn-verification-government"></a>

Government agencies, departments, and contractor-operated government programs are not listed in commercial business databases (such as Dun & Bradstreet). Automated business verification fails for these entities regardless of how you complete the registration form. To prevent a verification failure, upload one of the following IRS documents using the optional business registration document field when you first submit your registration:
+ **IRS CP 575** — EIN Confirmation Letter (issued when the IRS originally assigned your EIN).
+ **IRS 147C** — EIN Verification Letter (you can request this at any time; see the instructions below).
+ **IRS SS-4** — Employer Identification Number Application.

A W-9 form is **not accepted** because it is self-certified and does not meet IRS document verification standards.

### How to obtain a 147C letter
<a name="registration-help-tfn-verification-government-147c"></a>

If you do not have your original CP 575 or SS-4, you can request a 147C EIN Verification Letter from the IRS:

1. Call the IRS Business and Specialty Tax line at 1-800-829-4933.

1. Request a 147C letter be faxed to your organization.

**Note**  
The IRS typically fulfills 147C requests the same day.

### Name matching for government entities
<a name="registration-help-tfn-verification-government-name"></a>

The company name on your registration must exactly match the name on your IRS letter. Government entity names sometimes span multiple lines on IRS documents. When you enter the name on the registration form, combine all name lines with a space and omit special characters except hyphens and ampersands.

For example, if the IRS letter shows:

```
DEPARTMENT OF DEFENSE
DEFENSE HEALTH AGENCY
```

Enter: `DEPARTMENT OF DEFENSE DEFENSE HEALTH AGENCY`

### Contractor-operated programs
<a name="registration-help-tfn-verification-government-contractors"></a>

If a government program is operated by a private contractor, use the **government agency's** EIN and legal name on the registration form, not the contractor's. The registration must identify the entity on whose behalf messages are sent.