On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# How Amazon Lookout for Equipment works

Amazon Lookout for Equipment uses machine learning to detect abnormal behavior in your equipment and identify
potential failures. Each piece of industrial equipment is referred to as an industrial
asset, or _asset_. To use Lookout for Equipment to monitor your asset, you do the
following:

1. Provide Lookout for Equipment with your asset's data. The data come from sensors that measure
   different features of your asset. For example, you could have one sensor that
   measures temperature and another that measures pressure.
2. Train an anomaly detection model on the data.
3. Monitor your asset with the model that you've trained.
   You need to train a model for each of your assets because they each have their own data
   signatures. A data signature indicates the distinct behavior and characteristics of an
   individual asset. This signature depends on the age of the equipment, its operating
   environment, what sensors are installed (including process data), who operates it, and many
   other factors. You use Amazon Lookout for Equipment to build a custom ML model for each asset. For example, you
   would build a custom model for each of two assets of the same asset type, _Pump
   1_ and _Pump 2_.

The model is trained to use data to establish a baseline for the asset. It's trained to
know what constitutes normal behavior. As it monitors your equipment, it can identify
abnormal behavior that might indicate a precursor to an asset failure. Amazon Lookout for Equipment uses
machine learning to interpret the relationships between sensors, and to detect deviations
from normal behavior because asset failures are rare and even the same failure type might
have its own unique data pattern. Detected failures are preceded by behavior or
conditions that fall out of the normal behavior of the equipment, and Lookout for Equipment is designed to
look for those behaviors or conditions.

Additionally, if available, you can highlight abnormal equipment behavior using [labels](understanding-labeling.md "understanding-labeling.md"). The trained model can use the anomalous
behavior in the dataset to improve its performance.

When you train a model, Amazon Lookout for Equipment evaluates how different types of ML models perform with
your asset's data. It chooses the model that performs the best on the dataset to monitor
your equipment.

You can now use the model to monitor your asset. You can also schedule the frequency with which
Amazon Lookout for Equipment monitors the asset.
