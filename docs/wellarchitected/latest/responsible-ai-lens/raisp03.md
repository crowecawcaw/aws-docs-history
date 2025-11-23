# Filtering

| RAISP03: How will you meet release criteria not fully addressed by the core AI system design (filtering)? |
| --------------------------------------------------------------------------------------------------------- |
|                                                                                                           |

Filtering strategies add protective layers around your AI system
through input and output filtering when core system design alone
isn't sufficient. Best practices cover implementing
privacy-preserving filters to remove sensitive data, security
safeguards to block unwanted or adversarial inputs, and safety
filters to catch harmful content before it reaches users, among
others. This filtering approach is especially valuable for
foundation model services where you have limited control over
core training but need to meet specific safety and
compliance-aligned requirements.

###### Best practices

- [RAISP03-BP01 Add privacy-preserving filters](raisp03-bp01.md "raisp03-bp01.md")
- [RAISP03-BP02 Add security filters](raisp03-bp02.md "raisp03-bp02.md")
- [RAISP03-BP03 Implement output filtering to catch unsafe content
  before it reaches users](raisp03-bp03.md "raisp03-bp03.md")
- [RAISP03-BP04 Implement output filtering to detect and block
  hallucinations](raisp03-bp04.md "raisp03-bp04.md")
