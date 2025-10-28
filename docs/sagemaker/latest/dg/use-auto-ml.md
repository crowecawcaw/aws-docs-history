# Automated ML, no-code, or low-code

Amazon SageMaker AI offers the following features to automate key machine learning tasks and use
no-code or low-code solutions.

- **Amazon SageMaker Canvas**: For a UI-based, no-code AutoML
  experience, new users should use the [Amazon SageMaker Canvas](canvas.md "canvas.md") application in [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Amazon SageMaker Canvas provides analysts and citizen data scientists no-code capabilities for
tasks such as data preparation, feature engineering, algorithm selection, training
and tuning, inference, and more. Users can leverage built-in visualizations and
what-if analysis to explore their data and different scenarios, with automated
predictions enabling them to easily productionize their models. SageMaker Canvas supports a
variety of use cases, including computer vision, demand forecasting, intelligent
search, and generative AI.

- **Amazon SageMaker Autopilot**: [Amazon SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md") is an automated
  machine learning (AutoML) feature-set that automates the end-to-end process of
  building, training, tuning, and deploying machine learning models. Amazon SageMaker Autopilot analyzes
  your data, selects algorithms suitable for your problem type, preprocesses the data
  to prepare it for training, handles automatic model training, and performs
  hyperparameter optimization to find the best performing model for your
  dataset.
  - As of November 30, 2023, the user interface (UI) for Autopilot is integrated
    into the [Amazon SageMaker Canvas](canvas.md "canvas.md") application in Studio.
  - Users of [Amazon SageMaker Studio Classic](studio.md "studio.md"), the previous
    experience of Studio, can continue using the Autopilot UI in Studio Classic.
    Users with coding experience can continue using the [AutoML API
    references](autopilot-automate-model-development.md "autopilot-automate-model-development.md") in any supported SDK for technical
    implementation.

###### Note

If you have been using Autopilot in Studio Classic until now and want to migrate to
SageMaker Canvas, you might have to grant additional permissions to your user profile or
IAM role so that you can create and use the SageMaker Canvas application. For more
information, see [(Optional) Migrate from
Autopilot in Studio Classic to SageMaker Canvas](studio-updated-migrate-ui.md#studio-updated-migrate-autopilot "studio-updated-migrate-ui.md#studio-updated-migrate-autopilot").

- **Amazon SageMaker JumpStart**: SageMaker JumpStart provides pretrained,
  open-source models for a wide range of problem types to help you get started with
  machine learning. You can incrementally train and tune these models before
  deployment. JumpStart also provides solution templates that set up infrastructure for
  common use cases, and executable example notebooks for machine learning with
  SageMaker AI.

###### Topics

- [SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md")
- [SageMaker JumpStart pretrained models](studio-jumpstart.md "studio-jumpstart.md")
