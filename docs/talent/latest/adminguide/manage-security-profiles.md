

# Manage security profiles and roles
<a name="manage-security-profiles"></a>

Security profiles control what users can see and do in Amazon Connect Talent. Each user must have a security profile assigned. Follow the principle of least privilege when you assign permissions.

## Default security profiles
<a name="manage-security-profiles-defaults"></a>

Amazon Connect Talent provides the following default security profiles:


| Security profile | Description | Default permissions | 
| --- | --- | --- | 
| HiringManager | Intended for hiring managers. By default, can view the hiring setup and candidate results. |  + Hiring setup – View<br />+ Candidate review – View  | 
| Recruiter | Intended for recruiters. By default, can view the hiring setup and fully manage candidate review. |  + Hiring setup – View<br />+ Candidate review – All (View, Edit, Create)  | 
| RecruitingLead | Intended for recruiting leads. By default, can do everything a recruiter can, plus manage the hiring setup, customize the experience, and view integrations. |  + Hiring setup – All (View, Edit, Create)<br />+ Candidate review – All (View, Edit, Create)<br />+ Experience customization – All (View, Edit)<br />+ Integrations – View  | 
| ResearchScientist | Intended for research scientists. By default, can manage the hiring setup and knowledge base, and view candidate results. |  + Hiring setup – All (View, Edit, Create)<br />+ Candidate review – View<br />+ Knowledge – All (View, Edit, Create, Delete)  | 
| TechAdmin | Intended for technical admins. By default, can manage users, security profiles, integrations, and knowledge. |  + Users – All (View, Edit, Create, Delete)<br />+ Security profiles – All (View, Edit, Create)<br />+ Knowledge – All (View, Edit, Create, Delete)<br />+ Integrations – All (View, Edit, Create, Delete)<br />+ Experience customization – All (View, Edit)  | 
| ComplianceAdmin | Intended for compliance owners. By default, can manage compliance settings, and view integrations and candidate results. |  + Compliance – All (View, Edit, Create)<br />+ Candidate review – View<br />+ Integrations – View  | 

The default security profiles are a starting point. A user who can manage security profiles (for example, the `TechAdmin` profile) can adjust the permissions on the default profiles as well as create new ones.

**Tip**  
The default `TechAdmin` profile does not include permissions for hiring setup or candidate review. If you need a single profile with full access to all Amazon Connect Talent features — for example, for the person who sets up and configures the instance — you have two options:  
**Add permissions to the TechAdmin profile** – Edit the `TechAdmin` profile and enable all permission categories, including hiring setup and candidate review.
**Create a new profile with all permissions** – Create a new security profile (for example, "Admin") and select all permission categories. Assign this profile to users who need full access.

## To create a security profile
<a name="manage-security-profiles-create"></a>

1. Navigate to **Settings** > **Admin** > **Security profiles**.

1. Choose **Create security profile**.

1. Enter a name and description for the profile.

1. Select the permissions to assign to the profile.

1. Choose **Save**.

## To edit a security profile
<a name="manage-security-profiles-edit"></a>

1. Navigate to **Settings** > **Admin** > **Security profiles**.

1. Choose the security profile you want to edit. This can be a default profile or one you created.

1. Adjust the selected permissions.

1. Choose **Save**.

Your changes take effect for all users assigned that profile.

## Security profile permissions
<a name="manage-security-profiles-permissions"></a>

A security profile grants permissions across the following categories.


| Permission category | Description | 
| --- | --- | 
| Hiring setup | Manage the steps that happen before a candidate applies, such as jobs, requisitions, and evaluations. Includes viewing aggregate hiring metrics. | 
| Candidate review | Send evaluations to candidates and review their results, transcripts, and recordings. Covers the steps after a candidate applies. | 
| Knowledge | Manage the files in the knowledge base. | 
| Integrations | Manage third-party integrations that connect Amazon Connect Talent to external systems such as applicant tracking systems, HR information systems, and job boards. | 
| Users | Manage users and their permissions. | 
| Security profiles | Manage the security profiles available to be assigned to users. | 
| Experience customization | Manage branding and visual customization. | 
| Compliance | Manage compliance-related settings such as disclosures and data governance. | 

**Tip**  
Use the `TechAdmin` profile during initial setup, and then switch to a more restrictive profile for daily use. Create security profiles before you add users to your instance.