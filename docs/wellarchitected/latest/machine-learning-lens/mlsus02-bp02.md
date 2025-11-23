# MLSUS02-BP02 Select sustainable Regions

Choose the Regions where you implement your workloads based on both
your business requirements and sustainability goals.

**Desired outcome:** You select AWS Regions that align with your organizational sustainability
objectives while meeting your business requirements. By choosing
Regions with renewable energy sources and lower carbon intensity,
you reduce the environmental impact of your machine learning
workloads while maintaining optimal performance for your business
needs.

**Common anti-patterns:**

- Selecting Regions based solely on proximity without considering
  environmental impact.
- Ignoring renewable energy availability when deploying machine
  learning workloads.
- Deploying workloads across multiple Regions without considering
  their carbon footprints.

**Benefits of establishing this best
practice:**

- Alignment with organizational sustainability goals and ESG
  initiatives.
- Enhanced reputation as an environmentally responsible
  organization.
- Potential cost savings through efficient Region selection.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When deploying your machine learning workloads, Region selection
plays a crucial role in meeting both your operational requirements
and sustainability goals. While factors such as latency, data
residency, and service availability remain important,
incorporating sustainability considerations into your Region
selection process can minimize your environmental impact. AWS is
continuously expanding its renewable energy projects globally,
making it increasingly possible to host your workloads in Regions
powered by sustainable energy sources.

The cloud offers significant sustainability advantages compared to
on-premises deployments due to higher utilization rates, more
energy-efficient infrastructure, and AWS' commitment to renewable
energy. By selecting Regions thoughtfully, you can further enhance
these sustainability benefits while still meeting your business
needs.

### Implementation steps

1. **Understand your business
   requirements first**. Identify the non-negotiable
   requirements for your workload, including data sovereignty
   regulations, compliance-aligned needs, latency requirements,
   and service availability in specific Regions. Create a
   shortlist of Regions that meet these baseline requirements.
2. **Research AWS renewable energy
   projects**. Use the
   [Amazon
   Around the Globe](https://sustainability.aboutamazon.com/about/around-the-globe?energyType=true "https://sustainability.aboutamazon.com/about/around-the-globe?energyType=true") resource to identify Regions that
   are near Amazon renewable energy projects. AWS achieved
   powering its operations with
   [100%
   renewable energy](https://www.aboutamazon.com/news/sustainability/amazon-renewable-energy-goal "https://www.aboutamazon.com/news/sustainability/amazon-renewable-energy-goal") in 2023, seven years ahead of their
   original 2030 commitment.
3. **Consider the grid's carbon
   intensity**. Look for Regions where the electrical
   grid has lower published carbon intensity. This information
   may be available through regional utility reports or
   sustainability documentation. Lower carbon intensity means
   reduced emissions even for non-renewable energy sources.
4. **Evaluate the trade-offs**.
   When selecting Regions, consider potential trade-offs
   between sustainability goals and business requirements such
   as latency or availability. In some cases, minor performance
   trade-offs may be acceptable to achieve significant
   sustainability improvements.
5. **Monitor sustainability
   metrics**. After deployment, track relevant
   sustainability metrics to verify that your Region selection
   is delivering the expected environmental benefits. Consider
   implementing dashboards with key performance indicators
   (KPIs) for sustainability tracking.
6. **Review and adjust
   periodically**. As AWS adds more renewable energy
   projects and as your business requirements evolve,
   periodically reassess your Region selections to continually
   align with your sustainability goals.

## Resources

**Related documents:**

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/")
- [Delivering
  on net-zero carbon by 2040](https://sustainability.aboutamazon.com/about/around-the-globe "https://sustainability.aboutamazon.com/about/around-the-globe")
- [Climate
  solutions](https://sustainability.aboutamazon.com/about/the-climate-pledge "https://sustainability.aboutamazon.com/about/the-climate-pledge")
- [AWS Well-Architected Framework - Sustainability Pillar](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md")
- [How
  to select a Region for your workload based on sustainability
  goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/ "https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/")
