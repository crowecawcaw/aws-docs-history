# Ongoing security

| GAMESEC02: How do you achieve, maintain, and monitor ongoing security best<br>practices? |
| ---------------------------------------------------------------------------------------- |
|                                                                                          |

Adhering to best security practices is paramount for businesses across industries, but
especially in the gaming industry. The games industry relies on cultivating and sustaining
player trust and creating a strong reputation, and even minor security issues can quickly
undermine that confidence.

Moreover, the global nature of the gaming industry necessitates compliance with various
industry regulations and standards governing data protection, consumer privacy, and security
across the Regions where games are offered. Fair and secure gameplay is another critical
aspect that underscores the importance of robust security measures. Cheating, hacking, and
other forms of game exploitation can disrupt the gaming experience for legitimate players,
which makes strong security controls essential to maintain the integrity of gameplay and
foster a level playing field for participants.

###### Best practices

- [GAMESEC02-BP01 Use ready to deploy templates for standard
  security practices](gamesec02-bp01.md "gamesec02-bp01.md")
- [GAMESEC02-BP02 Use automated remediation techniques when a security event does arise](#gamesec02-bp02 "#gamesec02-bp02")

## GAMESEC02-BP02 Use automated remediation techniques when a security event does arise

Using automated remediation techniques, game developers can
proactively protect and maintain their gaming infrastructure and
minimize the potential impact a security incident might have. If a
security issue is detected, use a runbook to guide your response
to the situation. Automate these responses where possible to
remediate issues more quickly and reduce their impact. This
improves the player experience by reducing the chance of downtime
and disruptions to the game.

**Level of risk exposed if this best
practice is not established:** Medium

### Implementation guidance

Preparing to respond to security issues not only safeguards the
players' experience but also to meet the various compliance and
regulatory standards. Additionally, using automated security
responses scales your security operations as your workloads
expand. AWS provides services to help identify and automate a
response to these incidents.

**Customer example**

AnyCompany Games faced a critical security incident when an S3
bucket containing unreleased character models and textures for
their upcoming game was accidentally made public during a routine
asset pipeline update. The automated security system detected the
bucket permission change within minutes of the modification. The
system immediately executed its remediation runbook: reverting the
bucket to private status, logging access attempts during the
exposure window, notifying the security team, and creating a
detailed CloudTrail log of the permission changes.

#### Implementation steps

- Use the
  [Automated
  Security Response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/ "https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/") solution to implement
  automation runbooks that define the actions that will
  automatically be taken in response to security events in AWS Security Hub CSPM.

#### Resources

- [AWS for Games Blog — Managing Your Game Studio on AWS: Part
  1](https://aws.amazon.com/blogs/gametech/managing-your-game-studio-on-aws-part-1/ "https://aws.amazon.com/blogs/gametech/managing-your-game-studio-on-aws-part-1/")
- [AWS for Games Blog — Managing Your Game Studio on AWS part
  2](https://aws.amazon.com/blogs/gametech/managing-your-game-studio-on-aws-part-2/ "https://aws.amazon.com/blogs/gametech/managing-your-game-studio-on-aws-part-2/")
- [Register
  an existing organizational unit with AWS Control Tower](../../../controltower/latest/userguide/importing-existing.md "../../../controltower/latest/userguide/importing-existing.md")
- [AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md")
- [Tasks
  that require root user credentials](../../../IAM/latest/UserGuide/root-user-tasks.md "../../../IAM/latest/UserGuide/root-user-tasks.md")
- [Automated
  Security Response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/ "https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/")
