We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Regions and Endpoints

Amazon Machine Learning (Amazon ML) supports real-time prediction endpoints in the following two regions:

| Region name           | Region    | Endpoint                                | Protocol |
| --------------------- | --------- | --------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| US East (N. Virginia) | us-east-1 | machinelearning.us-east-1.amazonaws.com | HTTPS    |
| Europe (Ireland)      | eu-west-1 | machinelearning.eu-west-1.amazonaws.com | HTTPS    | You can host data sets, train and evaluate models, and trigger predictions in any region. We recommend that you keep all of your resources in the same region. If your input data is in a different region than your Amazon ML resources, you accrue cross regional data transfer fees. You can call a real-time prediction endpoint from any region, but calling an endpoint from a region that does not have the endpoint that you're calling can impact real-time prediction latencies. |
