

# Set up your instance
<a name="getting-started-setup"></a>

After you create your Amazon Connect Talent instance, configure it for your recruiting team. Complete the following steps to get your instance ready for use.

**Important**  
Before you can send evaluations to candidates or test internally, your Amazon Simple Email Service (Amazon SES) account must be moved out of sandbox mode. If you haven't done this yet, see [Move Amazon SES out of sandbox mode](getting-started-create.md#getting-started-ses).

1. **Set up your security profile** – The default `TechAdmin` profile does not include permissions for hiring setup or candidate review. If you need full access to all Amazon Connect Talent features during setup, edit the `TechAdmin` profile to enable all permission categories, or create a new security profile with all permissions. For more information, see [Manage security profiles and roles](manage-security-profiles.md).

1. **Add users** – Add your recruiting team members and assign each user a security profile that matches their role. You can add users individually or import them in bulk from a CSV file. For more information, see [Manage users](manage-users.md).

1. **Upload your knowledge base** – Upload your company values, principles, and mission to a knowledge base before you create evaluations. Amazon Connect Talent draws on your knowledge base when selecting competencies for evaluations. For more information, see [Manage knowledge bases](manage-knowledge-bases.md).

1. **Configure branding** – Personalize the candidate experience with your organization's name, logo, and colors. For more information, see [Configure branding](configure-branding.md).

1. **Configure disclosures** – Add any legal disclosures that candidates see before they start an evaluation. Consult your legal counsel to determine what disclosures are required for your organization. For more information, see [Configure disclosures](configure-disclosures.md).

1. **Create your first evaluation** – You're ready to create an evaluation. For step-by-step instructions, see [Managing evaluations](https://docs.aws.amazon.com/talent/latest/userguide/managing-evaluations.html) in the *Amazon Connect Talent User Guide*.

1. **Test your evaluation** – Before sending evaluations to candidates, test the evaluation by sending it to yourself or your team. For more information, see [Testing Amazon Connect Talent](https://docs.aws.amazon.com/talent/latest/userguide/getting-started-test.html) in the *Amazon Connect Talent User Guide*.

1. **Connect your ATS (coming soon)** – When available, connect your applicant tracking system to sync jobs and candidates automatically.
**Note**  
ATS integrations are not available at launch. Support for ATS integrations is coming soon. For more information, see [Add your ATS integration](integrations.md).