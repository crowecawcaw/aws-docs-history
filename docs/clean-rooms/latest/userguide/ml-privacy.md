

# Privacy protections of AWS Clean Rooms ML

Clean Rooms ML is designed to reduce the risk of *membership inference attacks* where the training data provider can learn who is in the seed data and the seed data provider can learn who is in the training data. Several steps are taken to prevent this attack.

First, seed data providers don't directly observe the Clean Rooms ML output and training data providers can never observe the seed data. Seed data providers can choose to include the seed data in the output segment.

Next, the lookalike model is created from a random sample of the training data. This sample includes a significant number of users that don't match the seed audience. This process makes it harder to determine whether a user was not in the data, which is another avenue for membership inference.

Further, multiple seed customers can be used for every parameter of seed-specific lookalike model training. This limits how much the model can overfit, and thus how much can be inferred about a user. As a result, we recommend that the minimum size of the seed data is 500 users. 

Finally, user-level metrics are never provided to training data providers, which eliminates another avenue for a membership inference attack.

## Considerations
<a name="ml-privacy-considerations"></a>

The training data provider sets a minimum matching seed size when they configure the lookalike model. A lookalike segment generation job runs only if at least that many seed users match the training data. Otherwise, the job fails. For example, if the minimum matching seed size is 100 and only 90 seed users match, the job fails.

There is a risk that the seed data provider could infer membership of specific users in the training data. This membership inference only works when the overlap between the seed data and the training data equals the minimum matching seed size. Because the seed data provider can see whether a job succeeds or fails, removing a single matched user from the seed dataset could reveal if that user was present in the training data. For example, the seed data provider runs a job that exactly matches the minimum of 100 matching users, then they create seed data with one fewer matching user and run the job again. If the job fails, the target user is present in the training data. If it succeeds, the target user is not.

To reduce this risk, we recommend the training data provider set the minimum matching seed size to 500 or higher. A higher minimum reduces the risk that the seed data provider already knows enough matching users to run this membership inference attack successfully.

Additionally, the training data provider should monitor the number of lookalike segment generation jobs. Testing many users takes many jobs. An unusually high number of jobs can be a sign of this kind of membership inference attack.