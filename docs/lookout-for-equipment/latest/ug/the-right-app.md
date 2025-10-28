On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Choosing the right application

Choosing the right application of Lookout for Equipment involves finding the right combination of
business value, equipment operations, and available data. You determine this by working
directly with a subject matter experts (SME) on your equipment. Your team should
consider the following:

- **The high cost of downtime** – Equipment
  that can either be costly to fix or that is critical to a process is a prime
  candidate for monitoring.
- **Consistency in operations** – Lookout for Equipment works
  best on equipment that is stationary and primarily does a continuous, stable
  task. A heavy duty pump that is permanently installed in a location is a good
  example.
- **Relevant data** – Having data that is
  relevant to the critical aspects of the equipment is essential. Your equipment
  should have sensors that monitor these critical aspects, so that they can
  provide data that is relevant to how your equipment could fail. Having this data
  can make the difference between inference results that can effectively catch
  potential failures and abnormal behavior, and results that don't.
- **Significant historical data** – Ideally,
  the data you use to train the machine learning (ML) model should represent all
  of the equipment's operating modes. For instance, when creating a model for a
  pump with variable speeds, the dataset should contain measurements that include
  an adequate amount of historical data for all of the pump speeds. For effective
  analysis, Lookout for Equipment should have at least six months of historical data, although a
  longer history is preferred. For equipment affected by seasonality, at least one
  year of data is highly recommended.
- **List of historical failures (that is, labels)**
  – Lookout for Equipment uses data on historical failures to enhance the model's knowledge
  of normal equipment conditions. It looks for abnormal behavior that occurred
  ahead of historical failures. With more examples of historical failures, Lookout for Equipment
  can better develop its knowledge of healthy conditions and the unhealthy
  conditions that occur prior to failures. The definition of a failure can be
  subjective, but we have found that looking for issues that cause unplanned
  downtime is a good method to identify failure. For best results, give Lookout for Equipment
  label data for every known time period where the equipment had issues or
  abnormal behavior.

###### Note

Lookout for Equipment is ultimately dependent on _your_ data. We cannot
guarantee that there are patterns in your data that will enable Lookout for Equipment to detect
failures. Determining the right set of inputs might require multiple iterations
through the Lookout for Equipment model training and monitoring process. For the greatest chance of
success, we highly recommend working with a subject matter expert to identify the
right application and data.
