# Email Validation for Amazon SES

Email list quality is a critical factor in maintaining high delivery rates and
protecting your sender reputation. Invalid or risky email addresses can lead to
high bounce rates, spam complaints, and mailbox providers may reject emails, blacklist sending
domains, or throttle delivery rates.

_Email Validation_ is an Amazon SES feature that helps you validate email addresses
before you send to them. It checks email addresses for syntax errors, domain validity,
and other checks, and identifies risky addresses that could harm your sender reputation,
helping you maintain high deliverability rates and protect your sender reputation.

###### Why are email list quality and validation are important ?

Mailbox providers monitor key metrics such as bounce
rates, complaint rates, and engagement levels to evaluate sender reputation. When these metrics exceed acceptable
thresholds, providers implement protective measures such as rate limiting, temporary
deferrals, or permanent blocks. High bounce rates (typically above 5-10%) signal poor
list hygiene and trigger immediate reputation penalties.

Mailbox providers expect senders to maintain clean email lists and demonstrate good
sending practices. They track hard bounces from invalid addresses, monitor spam trap hits,
and measure recipient engagement to determine inbox placement. Poor list quality results in
measurable impacts: reduced delivery rates, increased latency, and potential blacklisting
that affects all future campaigns from your sending domain or IP address.

###### How Email Validation can help improve deliverability and reputation ?

Email Validation helps you improve both your deliverability and reputation with an
_API_ that checks email addresses on demand, and
_Auto Validation_ that automatically reviews and filters
outbound emails based on deliverability thresholds you set.

- API validation – Validates email addresses
  through API calls, allowing you to validate addresses at the point of collection such
  as during sign-up forms or subscription processes, and for periodic list cleaning of
  existing databases. This helps prevent invalid addresses from entering your database,
  provides timely feedback to users about address validity, and enables regular
  maintenance of email list quality.
- Auto Validation – Automatically reviews all
  outbound email addresses and only delivers messages to recipients that meet your selected
  delivery likelihood threshold (high or medium). This protects your sender reputation by
  preventing sends to invalid or risky addresses without requiring manual
  intervention.

###### Topics

- [Email Validation API](email-validation-api.md "email-validation-api.md")
- [Auto Validation](email-validation-auto.md "email-validation-auto.md")
- [Email Validation Dashboard](email-validation-dashboard.md "email-validation-dashboard.md")
