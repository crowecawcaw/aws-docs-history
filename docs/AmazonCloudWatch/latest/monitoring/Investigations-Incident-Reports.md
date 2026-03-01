# Generate incident reports

Incident reports help you more quickly and easily write a report about your incident
investigation. You can use this report to provide details to management or to help your team
learn from the incident and take actions to prevent future such occurrences. The structure
of the report is based on industry standards for these types of reports and can be copied
into other repositories for long-term retention.

When you use the AWS Management Console to create an `investigation group`
resource in CloudWatch investigations, an IAM role is created for the group to give it access to resources
during the investigation. Generating CloudWatch investigations incident reports requires additional permissions
be granted to your investigation group. The new managed policy
`AIOpsAssistantIncidentReportPolicy` provides the required permissions and is
automatically added to investigation groups created using the AWS Management Console after October 10, 2025. For more information, see [AIOpsAssistantIncidentReportPolicy](managed-policies-cloudwatch.md#managed-policies-QInvestigations-AIOpsAssistantIncidentReportPolicy "managed-policies-cloudwatch.md#managed-policies-QInvestigations-AIOpsAssistantIncidentReportPolicy").

###### Note

If you are using the CDK or SDK, you must explicitly add the investigation group role
and specify the role policy or equivalent inline permissions on the role. For more
details about permissions, see [Security in CloudWatch investigations](Investigations-Security.md "Investigations-Security.md")

These reports capture investigation findings, root causes, timeline events, and
recommended corrective actions in a structured format that can be easily shared with
stakeholders and used for organizational learning.

Incident report generation is included at no additional charge for all CloudWatch investigations users and
integrates seamlessly with your investigation workflow.

**How incident reports work**

1. Run an investigation on your incident.
2. Accept at least one hypothesis. Each hypothesis you accept is considered for the
   report. The hypothesis doesn't need to be 100% accurate.
3. Choose **Incident report**. During the investigation
   the AI parsed the data collected for your investigation and derived facts. Facts are
   atomic pieces of information about your incident that form the basis of generating
   the report. Fact extraction can take a few minutes.
4. When fact extraction is finished, you can review the facts available in the
   following areas:
   1. **Incident Overview** – High-level overview
      of the incident including its severity, duration, and operational
      hypothesis.
   2. **Impact Assessment** – Metrics and analysis
      related to the impact of the incident on customers, service function, and
      business operations.
   3. **Detection and Response** – Metrics and
      analysis related to how and when the incident was detected and how you
      responded to the incident.
   4. **Root Cause Analysis** – Detailed analysis
      of underlying causes based on investigation hypotheses.
   5. **Mitigation and Resolution** – Metrics and
      analysis related to mitigation steps and resolution measures, along with the
      time measurement for incident mitigation and resolution.
   6. **Learning and Next Steps** – A list of
      recommended actions for your team to consider, automatically generated from
      the investigation findings. These recommendations may include preventive
      measures against similar incidents, as well as suggested improvements to
      your monitoring and response processes.

5. After reviewing the facts, choose **Generate report**
   to create a comprehensive analysis of the incident. While the selected facts serve
   as key reference points, the report draws from all available information gathered
   during the investigation. This process can take a few minutes.
6. After generating the report, you can then either:
   - Use the report as is:
     - Copy it to edit in your external editor if needed
     - Save it for later reference

   - Enhance the report by adding more data:
     - Choose **Add facts** (recommended
       method) to input additional text-based content such as incident
       tickets or custom narratives. The AI will analyze this content to
       augment existing facts or infer new ones.
     - Edit facts directly (use sparingly) - Manually edited facts may
       create inconsistencies with the investigation timeline. This should
       be used only as a last resort when **Add
       facts** doesn't achieve the desired result.

   - Choose **Regenerate report** to produce a new
     report using the updated information.

###### Topics

- [Understanding AI-derived facts in incident reports](Investigations-IncidentReports-ai-facts.md "Investigations-IncidentReports-ai-facts.md")
- [Incident report terminology](Investigations-IncidentReports-terms.md "Investigations-IncidentReports-terms.md")
- [Generate a report from an investigation](Investigations-IncidentReports-Generate.md "Investigations-IncidentReports-Generate.md")
- [Using 5 Whys analysis in incident reports](incident-report-5whys.md "incident-report-5whys.md")
