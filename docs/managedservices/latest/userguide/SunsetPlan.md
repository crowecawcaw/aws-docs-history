

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS Advanced end of support
<a name="SunsetPlan"></a>

After careful consideration, we decided to end support for AMS Advanced, effective June 30, 2027. AMS Advanced will no longer accept new customers beginning June 30, 2026. As an existing customer with an account signed up for the service before June 30, 2026, you can continue to use AMS Advanced features. After June 30, 2027, you will no longer be able to use AMS Advanced.

AWS Managed Services (AMS) Advanced will reach end of support on June 30, 2027. After this date, AMS Advanced will no longer be available and all customers will be offboarded from the service. No new single-account landing zones (SALZ) or multi-account landing zones (MALZ) will be created after June 30, 2026.

All AMS Advanced operational capabilities will cease on June 30, 2027, including the RFC/change management system, AMS-managed patching, monitoring, incident management, access management, and AMS landing zone controls. Your underlying AWS infrastructure and workloads are not affected — only the AMS Advanced management layer will be removed.

Existing AMS Advanced customers can continue using the service as normal until June 30, 2027. During this period, AWS will continue to operate and support AMS Advanced workloads.

## Alternative solutions
<a name="SunsetPlan-alternatives"></a>

**AMS Accelerate**  
AMS Accelerate is another AMS operational model that customers can onboard into. Accelerate operates directly in your existing AWS accounts without requiring workload migration into a new landing zone. It provides incident management, patch management, backup management, and security monitoring. Note that change management and access management are not included in Accelerate — customers will manage these themselves. Additionally, your endpoint security (EPS) solution and landing zone infrastructure will be your responsibility to manage. We will be providing detailed guidance on how to transition from Advanced to Accelerate at: [AMS Advanced to Accelerate transition guide](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

**AWS Support Plan - Unified Operations**  
AWS Support Plan - Unified Operations offers some of the operational capabilities that AMS Advanced provides today, delivered as AWS-native services. This includes Incident Detection & Response (IDR) and Security Incident Response (SIR). Unified Operations is well-suited for customers who want specific operational capabilities rather than a comprehensive managed service.

**AWS Partner-Led Solutions**  
AWS Partner-Led Solutions provide full-stack managed services including multi-cloud support through qualified AWS Partners. Partners offer flexible engagement models and cost-effective delivery. AWS can facilitate introductions to qualified partners in your region.

**Self-Managed (Native AWS Services)**  
Self-Managed (Native AWS Services) is appropriate for customers with mature internal cloud operations teams. You can leverage AWS Organizations, AWS Control Tower, AWS Systems Manager, AWS Backup, Amazon CloudWatch, and AWS Security Hub to build your own operational model with full control and flexibility.

## Transition effort
<a name="SunsetPlan-transition"></a>

The transition from AMS Advanced does not require workload migration — your applications remain in your existing AWS accounts. The primary effort involves two areas. First, transitioning your access model away from AMS-managed access (such as Managed Active Directory) to an alternative such as AWS Systems Manager Session Manager or your own access solution. Second, for customers who have built automations calling AMS APIs or who execute a high volume of RFCs, you will need to redesign those operational workflows to use native AWS tools such as Console, API, Terraform, CloudFormation, or AWS Systems Manager. For customers onboarding into AMS Accelerate, Operations on Demand is available to help execute the changes currently handled by the Advanced change management system while you complete this redesign. Your Cloud Service Delivery Manager (CSDM) and Cloud Architect (CA) will help you scope the specific effort based on your environment. Detailed transition guidance will be available at: [Transitioning from AMS Advanced to AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/userguide/transition-to-accelerate.html).

## Offboarding steps
<a name="SunsetPlan-offboarding"></a>

First, assess your current AMS Advanced usage by reviewing your operational dependencies including RFC workflows, patching schedules, monitoring configurations, and access management. Then, select your target operating model from the alternatives above based on your team's capabilities and requirements.

Engage your CSDM and CA — they are your primary points of contact and can provide personalized guidance on the transition. We recommend completing your transition by March 31, 2027 to allow buffer before the service is shut down. On June 30, 2027, all remaining customers will be offboarded from AMS Advanced.

For customers on multi-account landing zones, all Application accounts must be offboarded before Core accounts. For customers on single-account landing zones, offboarding can take the form of a control hand-over (AMS transfers account control back to you) or resource termination for account closure. Detailed offboarding procedures are available at:
+ [Offboard AMS accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding.html)
+ [Offboard from single-account landing zone](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding-salz.html)
+ [Offboard from multi-account landing zone](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding-malz.html)

## Support during transition
<a name="SunsetPlan-support"></a>

AWS will continue to fully operate and support AMS Advanced through June 30, 2027. Your CSDM and CA remain your primary points of contact throughout the transition. Your TAM and Account Manager are also available for support. For additional questions, contact aws-ams-pm@amazon.com.

## Frequently asked questions
<a name="SunsetPlan-faq"></a>

**When will AMS Advanced stop working?**  
AMS Advanced will be fully shut down on June 30, 2027. All operational capabilities will cease and all customers will be offboarded on this date.

**Can I continue using AMS Advanced until the shutdown date?**  
Yes. All existing customers can continue using AMS Advanced with full support through June 30, 2027.

**What happens to my workloads after June 30, 2027?**  
Your AWS accounts and workloads remain yours. The AMS Advanced management layer (RFC system, AMS-managed operations, AMS landing zone controls) will be removed. Some configuration changes to your resources may be required as part of the offboarding process — for example, reconfiguring patching, monitoring, and access methods for your EC2 instances. Your CSDM and CA will guide you through the specific impacts for your environment. Detailed offboarding steps are available at: [Offboard AMS accounts](https://docs.aws.amazon.com/managedservices/latest/userguide/offboarding.html).

**Will new landing zones be created?**  
No. After June 30, 2026, no new single-account landing zones (SALZ) or multi-account landing zones (MALZ) will be provisioned.

**What if I cannot complete my transition by June 30, 2027?**  
Please engage your CSDM and CA as early as possible. AWS will conduct quarterly checkpoints to monitor progress and can discuss your transition.