**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Types of token labels in AWS WAF

This section describes the labels that AWS WAF token management adds to web requests. For general
information about labels, see [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").

When you use any of the AWS WAF bot or fraud control managed rule groups, the rule groups
use AWS WAF token management to inspect the web request
tokens and apply token labeling to the requests. For information about the managed
rule groups, see [AWS WAF Fraud Control account creation fraud prevention (ACFP) rule group](aws-managed-rule-groups-acfp.md "aws-managed-rule-groups-acfp.md"), [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md "aws-managed-rule-groups-atp.md"),
and [AWS WAF Bot Control rule group](aws-managed-rule-groups-bot.md "aws-managed-rule-groups-bot.md") .

###### Note

AWS WAF applies token labels only when you use one of these intelligent threat
mitigation managed rule groups.

Token management can add the following labels to web requests.

###### Client session label

The label `awswaf:managed:token:id:`identifier`` contains a unique identifier that AWS WAF token management uses to identify the client session. The identifier can change if the client acquires a new token, for example after discarding the token it was using.

###### Note

AWS WAF doesn't report Amazon CloudWatch metrics for this label.

###### Browser fingerprint label

The label `awswaf:managed:token:fingerprint:`fingerprint-identifier`` contains a
robust browser fingerprint identifier that AWS WAF token management computes from various client browser signals.
This identifier stays the same across multiple token acquisition attempts. The fingerprint identifier is not unique to a single client.

###### Note

AWS WAF doesn't report Amazon CloudWatch metrics for this label.

###### Token status labels: Label namespace prefixes

Token status labels report on the status of the token and of the challenge and CAPTCHA information that it contains.

Each token status label begins with one of the following namespace prefixes:

- `awswaf:managed:token:` – Used to report the general status of the token and to report on the status of the token's challenge information.
- `awswaf:managed:captcha:` – Used to report on the status of the token's CAPTCHA information.

###### Token status labels: Label names

Following the prefix, the rest of the label provides detailed token status information:

- `accepted` – The request token is present and contains the following:

      + A valid challenge or CAPTCHA solution.
      + An unexpired challenge or CAPTCHA timestamp.
      + A domain specification that's valid for the protection pack (web ACL).

  Example: The label `awswaf:managed:token:accepted` indicates that the web requests's token has a valid challenge solution, an unexpired challenge timestamp, and a valid domain.

- `rejected` – The request token is present but doesn't meet the acceptance criteria.

Along with the rejected label, token management adds a custom label namespace and name to indicate the reason.

    + `rejected:not_solved` – The token is missing the challenge or CAPTCHA solution.
    + `rejected:expired` – The token's challenge or CAPTCHA timestamp has expired, according to your protection pack (web ACL)'s configured token immunity times.
    + `rejected:domain_mismatch` – The token's domain isn't a match for your protection pack (web ACL)'s token domain configuration.
    + `rejected:invalid` – AWS WAF couldn't read the indicated token.

Example: The labels `awswaf:managed:captcha:rejected` and `awswaf:managed:captcha:rejected:expired` together indicate that the request didn't have a valid CAPTCHA solve because the CAPTCHA timestamp in the token has exceeded the CAPTCHA token immunity time that's configured in the protection pack (web ACL).

- `absent` – The request doesn't have the token or the token manager couldn't read it.

Example: The label `awswaf:managed:captcha:absent` indicates that the request doesn't have the token.
