# DRHCSEC06-BP01 Restrict the number of people authorized to gain physical access to your AWS Outposts

Physical access should only be provided to those who have a
legitimate business need for it.

**Desired outcome:** Physical
access to Outposts is limited, and access is only granted with an
accompanying business requirement.

**Common anti-patterns:**

- Granting access to anyone without justified reason for the
  physical access
- Lack of awareness of the shared responsibility model for
  Outposts, as well as its differences to other AWS services
- Lack of periodic access reviews to make sure access
  requirements still exist

**Benefits of establishing this best
practice**: Reduce security risk by minimizing ability to
physically interact with hardware.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- Review the
  [AWS Outposts section of the Terms of Service](https://aws.amazon.com/service-terms/#4._AWS_Outposts "https://aws.amazon.com/service-terms/#4._AWS_Outposts") with
  specific attention to the responsibilities for physical
  security and access controls.
- Review the AWS Outposts Shared Responsibility Model in the
  [AWS Outposts High Availability Design and Architecture
  Considerations whitepaper](../../../whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.md "../../../whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.md").
- Update your access control mechanisms to only allow physical
  access to those who have a business need and when needed,
  rather than 24x7 access for people who's business need is
  only for short durations, such as electricians, fiber cable
  pullers, HVAC personnel, and staff designated to escort AWS
  maintenance technicians.
- Create a process for periodic access reviews, and
  automatically revoke access when not used for a certain
  duration.
