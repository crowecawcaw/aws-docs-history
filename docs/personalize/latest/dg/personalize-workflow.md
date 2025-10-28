# Amazon Personalize workflow details

The Amazon Personalize workflow is as follows. For a checklist that provides lists of Amazon Personalize features, requirements, and
data guidance, see the [Readiness checklist](readiness-checklist.md "readiness-checklist.md").

1. **[Match your use case to Amazon Personalize resources](use-cases-and-recipes.md "use-cases-and-recipes.md")**
   – Amazon Personalize features domain based resources and custom resources configured for different cases. When you match your
   use case to an Amazon Personalize resource, note its data requirements. After you choose a use case or recipe, this information can
   help as you prepare your data.
2. **[Prepare your training data](preparing-training-data.md "preparing-training-data.md")** –
   Based on your domain use case or custom recipe's data requirements, prepare your bulk training data in a CSV file. Depending on
   your use case or recipe, Amazon Personalize can use item interaction, item, user, action, and action interaction data.
   If you don't have bulk data, you can use individual import operations to collect data and stream events until you meet
   Amazon Personalize training requirements and the data requirements of your domain use case or recipe.
3. **[Create schema JSON files for your
   data](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md")** – Create schema JSON files for each type of data that you are importing. These files
   outline the structure and content of your data, including column names and their data types.
4. **[Create a dataset group](data-prep-ds-group.md "data-prep-ds-group.md")** – A dataset
   group is a container for Amazon Personalize resources. You can create a Domain dataset group with preconfigured resources for
   VIDEO_ON_DEMAND or ECOMMERCE domains. Or you can create a Custom dataset group and create only custom resources.
5. **[Create schemas and datasets](data-prep-creating-datasets.md "data-prep-creating-datasets.md")** – A _schema_ tells Amazon Personalize about the structure of your data and
   allows Amazon Personalize to parse the data. A _dataset_ is a container for training data in Amazon Personalize.
6. **[Import training data into datasets](import-data.md "import-data.md")** – Import your prepared interaction, item, user, action, or action interaction records.
   You can import records in bulk or individually.
7. **Train and deploy a model** – To train and deploy a model for at the VIDEO_ON_DEMAND or ECOMMERCE domains, you create domain recommenders.
   For custom resources, you create a custom solution and a solution version. For real-time recommendations, you deploy the solution version in a campaign.
   - For information about creating a domain recommenders, see [Domain recommenders](creating-recommenders.md "creating-recommenders.md").
   - For information about creating and deploying custom resources, see [Custom resources](create-custom-resources.md "create-custom-resources.md").

8. **[Get recommendations](getting-recommendations.md "getting-recommendations.md")** – Use your
   recommender or custom campaign to get recommendations. You can use filters to include
   or exclude certain types of items from recommendations. For more information, see [Filtering recommendations and user segments](filter.md "filter.md"). With custom resources, you can also get batch
   recommendations or user segments without creating a campaign.
9. **[Record real-time events](recording-events.md "recording-events.md")** – Record
   real-time events as your customers interact with recommendations. This builds out your interactions data and keeps your
   data fresh. And it tells Amazon Personalize about the current interests of your user, which can improve recommendation
   relevance.
   After you complete the Amazon Personalize workflow the first time, keep your data current, and regularly re-train any
   custom solutions that use manual training. This allows your model to learn from your user’s most recent activity and sustains and improves the
   relevance of recommendations. For more information, see [Maintaining recommendation relevance](maintaining-relevance.md "maintaining-relevance.md").
