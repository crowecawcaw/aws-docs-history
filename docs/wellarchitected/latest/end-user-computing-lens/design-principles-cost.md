# Design principles

The following design principles are additional considerations over
and above the Well-Architected Framework cost optimization design
principles. 

- **Establish ownership of cost
  optimization for your EUC services:** EUC services
  are typically consumed by end-users, which is why consumption
  and cost is highly dependent on user behavior, usage patterns,
  self-service capabilities, application requirements, and other
  factors. Over and above knowledge of the cloud financial
  management, cost optimization for EUC services requires
  knowledge of the specific EUC services in use and how EUC
  services generally work to understand the levers they have to
  optimize cost. This includes Operating System choices,
  application workloads and their hardware requirements,
  licensing, storage requirements, desktop & application
  management, and other areas.
- **Govern self-service capabilities of
  EUC services:** With EUC services you have the option
  to provide your users with certain self-service capabilities,
  which gives them flexibility to adjust their environment (e.g.
  CPU, RAM, Disk) according to their requirements. However, some
  of these self-service capabilities have an impact on your
  cost. With choice comes responsibility. If you leave the
  choice to your end-users, you should include the changes made
  via self-service capabilities in your cost & usage
  reporting so you can react accordingly.
- **Evaluate cost when selecting AWS EUC
  services:** AWS offers different EUC services that
  lend themselves to different use cases. It is important to
  evaluate the application landscape, understand usage patterns,
  and understand hardware requirements to map the specific
  workload to a suitable EUC service. For example, in some cases
  a monthly billing model may be more cost-effective, while in
  other cases billing by the hour or even by the second may be
  the better choice. With different use cases and personas, it
  is common practice to make use of a mix of services &
  billing models as appropriate for the given use case. It is
  therefore important to - ideally upfront - gather data on
  usage, usage patterns and resource utilization to select the
  most appropriate service for a given workload.
- **Use existing licenses for cost optimization when
  appropriate:** Whilst we give customers choice on the Operating System they
  consume, most customers deploy Microsoft Windows Operating Systems. Depending on your
  existing licensing with Microsoft, you may be able to use existing M365 or RDS CAL
  licenses with certain AWS EUC services. It is highly recommended you assess your
  eligibility to bring your own licenses upfront, since this may allow you to reduce the
  cost of your AWS EUC service. Consult the [Amazon WorkSpaces FAQs on Windows BYOL](https://aws.amazon.com/workspaces/faqs/#Windows_BYOL "https://aws.amazon.com/workspaces/faqs/#Windows_BYOL"), the [Amazon AppStream 2.0 FAQs
  on Pricing and Billing](https://aws.amazon.com/appstream2/faqs/?nc1=h_ls#Pricing_and_billing "https://aws.amazon.com/appstream2/faqs/?nc1=h_ls#Pricing_and_billing"), and the [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/?nc1=h_ls "https://aws.amazon.com/windows/resources/licensing/?nc1=h_ls") guide
  for further detail, and contact microsoft@amazon.com.
