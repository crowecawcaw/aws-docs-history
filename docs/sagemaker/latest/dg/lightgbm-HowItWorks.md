# How LightGBM works

LightGBM implements a conventional Gradient Boosting Decision Tree (GBDT) algorithm with the
addition of two novel techniques: Gradient-based One-Side Sampling (GOSS) and Exclusive Feature
Bundling (EFB). These techniques are designed to significantly improve the efficiency and scalability of GBDT.

The LightGBM algorithm performs well in machine learning competitions because of its robust handling
of a variety of data types, relationships, distributions, and the diversity of hyperparameters that you can fine-tune.
You can use LightGBM for regression, classification (binary and multiclass), and ranking problems.

For more information on gradient boosting, see [How the SageMaker AI XGBoost algorithm works](xgboost-HowItWorks.md "xgboost-HowItWorks.md"). For in-depth details about the additional GOSS
and EFB techniques used in the LightGBM method, see _[LightGBM: A Highly Efficient Gradient Boosting Decision
Tree](https://proceedings.neurips.cc/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf "https://proceedings.neurips.cc/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf")_.
