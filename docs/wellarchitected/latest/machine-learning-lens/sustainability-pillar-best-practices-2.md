# Sustainability pillar - Best practices

The sustainability pillar focuses on environmental impacts,
especially energy consumption and efficiency, since they are
important levers for architects to inform direct action to reduce
resource usage. This section includes best practices to consider
while processing data.

###### Best practices

- [MLSUS-04: Minimize idle resources](mlsus-04.md "mlsus-04.md")
- [MLSUS-05: Implement data lifecycle policies aligned with your sustainability goals](mlsus-05.md "mlsus-05.md")
- [MLSUS-06: Adopt sustainable storage options](mlsus-06.md "mlsus-06.md")

**Related best practices**

- **Enable data and compute
  proximity** (MLCOST-21) The two most important
  factors influencing the carbon footprint of your network
  usage when transmitting data are the size of the data and
  the distance traveled. Compress your data before moving it
  over the network. Minimize data movement across networks
  when selecting a Region. Store your data close to your
  producers and train your models close to your data.
- **Enable feature
  reusability** (MLCOST-08)- Evaluate if you can
  avoid data processing by using existing publicly available
  datasets like
  [AWS Data Exchange](https://aws.amazon.com/data-exchange/ "https://aws.amazon.com/data-exchange/") and
  [Open Data
  on AWS](https://registry.opendata.aws/ "https://registry.opendata.aws/") (which includes the
  [Amazon
  Sustainability Data Initiative](https://sustainability.aboutamazon.com/environment/the-cloud/asdi "https://sustainability.aboutamazon.com/environment/the-cloud/asdi")). They offer a variety
  of data, including weather and climate datasets, satellite
  imagery, air quality data, and energy data. By using these
  curated datasets, you avoid duplicating the compute and
  storage resources needed to download the data from the
  providers, store it in the cloud, organize, and clean
  it. For internal data, you can also reduce the duplication
  of feature engineering code across teams and projects by
  using managed feature storage services, such as
  [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/").
