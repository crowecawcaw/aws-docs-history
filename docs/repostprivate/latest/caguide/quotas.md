# re:Post Private quotas

AWS re:Post Private provides private re:Posts that you can use in your account in a given AWS Region.
When you sign up for re:Post Private, AWS sets default quotas (formerly referred to as limits)
on the number of private re:Posts that you can create and size of the private re:Posts.

## Service quotas

The following are the default quotas for re:Post Private for your AWS account. You can use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/ "https://console.aws.amazon.com/servicequotas/home/")
to view the default quota. None of these quotas are adjustable. You can't request a quota increase.

| Resource                      | Default           | Description                                                                   | Adjustable |
| ----------------------------- | ----------------- | ----------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| Number of private re:Posts    | 3                 | The maximum number of private re:Posts in this account in the current Region. | No         |
| Free private re:Post size     | 10                | The maximum size (in GB) of a free private re:Post.                           | No         |
| Standard private re:Post size | 100               | The maximum size (in GB) of a standard private re:Post.                       | No         | ## API throttling limits The following throttling limits apply per account, per Region in re:Post Private. These quotas can't be increased. |
| Actions                       | Token refill rate | Rate of requests                                                              |            | ---                                                                                                                                         | --- | --- |
| CreateSpace                   | 1                 | 1                                                                             |            | ListSpaces                                                                                                                                  | 10  | 10  |
| GetSpace                      | 10                | 10                                                                            |            | UpdateSpace                                                                                                                                 | 10  | 10  |
| DeleteSpace                   | 1                 | 1                                                                             |            | RegisterAdmin                                                                                                                               | 10  | 100 |
| DeRegisterAdmin               | 10                | 100                                                                           |            | SendInvites                                                                                                                                 | 1   | 1   |
| TagResource                   | 10                | 10                                                                            |            | UnTagResource                                                                                                                               | 10  | 10  |
| ListTagsForResource           | 10                | 10                                                                            |
