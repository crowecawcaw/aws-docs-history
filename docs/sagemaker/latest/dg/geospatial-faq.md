# SageMaker geospatial capabilities FAQ

Use the following FAQ items to find answers to commonly asked questions about SageMaker geospatial capabilities.

1. **What regions are Amazon SageMaker geospatial capabilities available
   in?**

Currently, SageMaker geospatial capabilities are only supported in the US West (Oregon) Region.
To view SageMaker geospatial, choose the name of the currently displayed Region in the navigation
bar of the console. Then choose the US West (Oregon) Region. 2. **What AWS Identity and Access Management permissions and policies are required to
use
SageMaker geospatial?**

To use SageMaker geospatial you need a user, group, or role that can access SageMaker AI. You also need
to create a SageMaker AI execution role so that SageMaker geospatial can perform operations on your behalf.
To learn more, see [SageMaker geospatial capabilities
roles](sagemaker-geospatial-roles.md "sagemaker-geospatial-roles.md"). 3. **I have an existing SageMaker AI execution role. Do I need to update
it?**

Yes. To use SageMaker geospatial you must specify an additional service principal in your IAM
trust policy: `sagemaker-geospatial.amazonaws.com`. To learn about
specifying a service principal in a trust relationship, see [Adding

the SageMaker geospatial service principal to an existing SageMaker AI execution
role](sagemaker-geospatial-roles-pass-role.md "sagemaker-geospatial-roles-pass-role.md") in the
_Amazon SageMaker AI Developer Guide_. 4. **Can I use SageMaker geospatial capabilities through my VPC
environment?**

Yes, you can use SageMaker geospatial through a VPN. To learn more, see [Use Amazon SageMaker geospatial capabilities in Your Amazon Virtual Private Cloud](geospatial-notebooks-and-internet-access-vpc-requirements.md "geospatial-notebooks-and-internet-access-vpc-requirements.md"). 5. **Why can't I see the SageMaker geospatial map visualizer, image or instance
type when I navigate to Amazon SageMaker Studio Classic?**

Verify that you are launching Amazon SageMaker Studio Classic in the US West (Oregon) Region and
that you are not using a shared space. 6. **Why can't I see the SageMaker geospatial image or instance type when I try
to create a notebook instance in Studio Classic?**

Verify that you are launching Amazon SageMaker Studio Classic in the US West (Oregon) Region and
that you are not using a shared space. To learn more, see [Create an Amazon SageMaker Studio Classic notebook using the
geospatial image](geospatial-launch-notebook.md "geospatial-launch-notebook.md"). 7. **What bands supported for various raster data
collections?**

Use the `GetRasterDataCollection` API response and refer to the
`ImageSourceBands` field to find the bands supported for that
particular data collection.
