# Controls that enhance data residency

protection

These elective controls complement your enterprise's data residency posture. By applying
these controls together, you can set up your multi-account environment to help detect and
inhibit the purposeful or accidental creation, sharing, or copying of data, outside of your
selected AWS Region or Regions.

These controls take effect at the OU level, and they apply to all member accounts within
the OU.

###### Important

Certain global AWS services, such as AWS Identity and Access Management (IAM) and
AWS Organizations, are exempt from these controls. You can identify the services that are
exempt by reviewing the **Region deny SCP**, shown in the example code.
Services with "\*" after their identifier are exempt, because all actions are permitted
when the "\*" notation is given. This SCP essentially contains a list of explicitly
permitted actions, and all other actions are denied. You cannot deny access to your home
Region.

## Video: Enable data residency controls

This video (5:58) describes how to enable data residency controls with AWS Control Tower controls. For better
viewing, select the icon at the lower right corner of the video to enlarge it to full screen.
Captioning is available.

###### Note

AWS Control Tower no longer supports searching the controls list by _Category_,
as shown in this video. To easily identify the Data Residency controls, we recommend you sort
the controls list by _Release Date_. Controls with a release date of
November 30, 2021 are the same controls in the Data Residency category shown in the video.

This video includes the term _guardrail_, an older term
AWS Control Tower used for _control_. We updated the term to better
align with industry usage and other AWS services. These terms are synonymous for our purposes.

###### Topics

- [Data residency controls with preventive behavior](data-residency-preventive-controls.md "data-residency-preventive-controls.md")
- [Data residency controls with detective behavior](data-residency-detective-controls.md "data-residency-detective-controls.md")
