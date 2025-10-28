# Cloning a solution (console)

When you create a new solution, you can use the Amazon Personalize console to clone a solution. When you clone a solution, you can
use the configuration of the existing solution as a starting point, such as the recipe and hyperparameters, and make any
changes as necessary. This is useful if you want to make one change to a solution, but leave all other properties unchanged.
For example, adding a new column of training data to your dataset. In this case, you would clone a solution, give the solution
a name, change the columns used when training, and leave all other properties unchanged.

## Cloning a solution

To clone a solution, you choose the existing solution, and choose the **Clone solution** option.
Then give the new solution a name, and modify the relevant fields.

###### To clone a solution

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your dataset group.
3. Choose **Custom resources** and choose **Solutions**.
4. Choose the solution that you want to clone.
5. Choose **Actions**, and choose **Clone solution**.
6. Give the new solution a name.
7. Make any changes to the solution details and advanced configuration. Amazon Personalize pre-populates these fields with values
   from the existing solution. For information about each field, see [Configuring a custom solution in Amazon Personalize](customizing-solution-config.md "customizing-solution-config.md").
