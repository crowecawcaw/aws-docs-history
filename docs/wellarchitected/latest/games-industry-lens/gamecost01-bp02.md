# GAMECOST01-BP02 Discover opportunities for optimization

Game developers and publishers can use AWS FinOps practices to help
optimize their cloud costs and gain better visibility into their
cloud spending. By doing so, game producers can align the average
cost required to maintain infrastructure for the players with the
financial results delivered by the game.

**Level of risk exposed if this best practice
is not established**: Low

## Implementation guidance

AWS offers a ready to use
[solution
guidance for Cloud Financial Management](https://aws.amazon.com/solutions/guidance/cloud-financial-management-on-aws/ "https://aws.amazon.com/solutions/guidance/cloud-financial-management-on-aws/") to manage and
optimize your expenses for cloud services. This capability
includes granular visibility and cost and usage analysis to
support decision-making for topics such as spend dashboards,
optimization, spend limits, charge back, and anomaly detection and
response. The solution guidance for Cloud Financial Management
includes budget and forecasting features, giving you a defined,
cost-optimized architecture for your workloads so you can select
the right pricing model and attribute resource costs relevant to
your teams. This activates tracking, notification, and cost
optimization techniques across your environment and resources. You
can centrally manage expense information and give critical
stakeholders access as needed for targeted visibility and to
support decision-making.

Another key FinOps tool is the
[Cost
Optimization Hub](../../../cost-management/latest/userguide/cost-optimization-hub.md "../../../cost-management/latest/userguide/cost-optimization-hub.md"), which provides a centralized view of cost
optimization recommendations and opportunities across your AWS accounts and AWS Regions, so that you can get the most out of your
AWS spend. You can use Cost Optimization Hub to identify, filter,
and aggregate AWS cost optimization recommendations across your
AWS accounts and AWS Regions. It makes recommendations on resource
rightsizing, idle resource deletion, Savings Plans, and Reserved
Instances. With a single dashboard, you avoid having to go to
multiple AWS products to identify cost optimization opportunities.

If your games teams are using shared AWS accounts the
[myApplications
in AWS Management Console Home](../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md "../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md"), can be used to view application
resource costs for individual workloads. This granular view allows
you to identify the specific cost trends within your game
infrastructure, enabling you to make informed decisions about
resource allocation and optimization.

Additionally, regularly reviewing your billing and cost management
data with
[AWS Data Exports](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md") uncovers hidden cost savings opportunities.
This detailed report provides a comprehensive breakdown of your
cloud spending, allowing you to identify areas of overspending,
unutilized resources, and opportunities to take advantage of more
cost-effective services or pricing models.

By embracing FinOps principles and leveraging the tools provided
by AWS, game developers and publishers can make the most efficient
use of their cloud resources, ultimately enhancing their bottom
line and freeing up funds for further game development and
innovation.

### Implementation steps

- Use AWS Cloud Financial Management tools for granular and
  detailed visibility, spend dashboards, anomaly detection,
  and cost attribution to optimize and track cloud expenses
  effectively.
- Use the Cost Optimization Hub to centralize rightsizing,
  Savings Plans, and Reserved Instance recommendations across
  AWS accounts and Regions.
- Regularly review AWS billing data using Data Exports and
  MyApplication on AWS to help analyze workload-specific
  costs, uncover savings opportunities, and optimize resource
  allocation.
