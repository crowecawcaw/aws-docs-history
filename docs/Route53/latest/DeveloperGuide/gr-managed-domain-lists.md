# Managed Domain Lists for Route 53 Global Resolver

Managed Domain Lists contain domain names that are associated with malicious activity or other potential threats. AWS maintains these lists to enable Route 53 Global Resolver customers to check internet-bound DNS queries against them when using DNS Firewall.

Keeping up to date on the constantly changing threat landscape can be time consuming and expensive. Managed Domain Lists can save you time when you implement and use DNS Firewall on Global Resolver. AWS automatically updates the lists when new vulnerabilities and threats emerge.

Managed domain lists are categorized into Threat and Content categories, designed to help protect you from common web threats and also block query resolution to domain not safe-for-work.

As a best practice, before using a Managed Domain List in production, test it in a non-production environment, with the rule action set to `Alert`. Evaluate the rule using Amazon CloudWatch metrics combined with DNS Firewall sampled requests or Global Resolver logs. When you're satisfied that the rule does what you want, change the action setting as needed.

## Available AWS Managed Domain Lists

This section describes the Managed Domain Lists that are currently available for Global Resolver. AWS provides the following Managed Domain Lists, for all users of Global Resolver, classified by **Threat** or **Content** Type.

Threat Categories| Malware |
| Botnet/Command and Control |
| Aggregate Threat List |
| Amazon GuardDuty Threat List |
| Phishing |
| Spam |

Content Categories| Violence and Hate Speech |
| For Kids |
| Online Ads |
| Science |
| Family and Parenting |
| Pets |
| Career and Job Search |
| Religion |
| Lifestyle |
| Home and Garden |
| Criminal and Illegal Activities |
| Sports and Recreation |
| Vehicles |
| Financial Services |
| Real Estate |
| Hobbies and Interests |
| Travel |
| Food and Dining |
| Government and Legal |
| Education |
| Fashion |
| Health |
| Shopping |
| Adult and Mature Content |
| Technology and Internet |
| Business and Economy |
| News |
| Search Engines and Portals |
| Arts and Culture |
| Entertainment |
| Military |
| Social Networking |
| Proxy Avoidance |
| Redirect |
| Email |
| Translation |
| Child Abuse |
| Abortion |
| Gambling |
| Hacking |
| Marijuana |
| Cryptocurrency |
| Dating |
| Artificial Intelligence and Machine Learning |
| Parked Domains |
| Private IP Address |

Managed Domain Lists cannot be downloaded or browsed. To protect intellectual property, you can't view or edit the individual domain specifications within the Managed Domain Lists. This restriction also helps to prevent malicious users from designing threats that specifically circumvent published lists.
