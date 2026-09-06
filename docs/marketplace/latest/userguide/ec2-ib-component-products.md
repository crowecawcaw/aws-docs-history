

# EC2 Image Builder component-based products in AWS Marketplace
<a name="ec2-ib-component-products"></a>

As an AWS Marketplace seller, you can deliver your products to buyers with [Image Builder components](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#image-builder). An Image Builder component is a fundamental building block used in the Image Builder service to create and maintain customized EC2 Image Builder components. Components are reusable, modular pieces of configuration that define a specific set of tasks to be performed during the image creation process.

A component defines the sequence of steps required to either customize an instance before image creation (a build component), or to test an instance that was launched from the created image (a test component). An Image builder component may consist of three items:
+ The component document, a declarative, YAML or JSON file that specifies the steps and actions to be run when the component is used to build an image.
+ Component attributes that provide the configuration options for a component. They help define the component's characteristics, behavior, and compatibility.
+ Software packages, the dependencies that must be installed for the component to function correctly.

Publishing Image Builder components on AWS Marketplace is supported using the AWS Marketplace Catalog API. For instructions to publish your component using the Catalog API, see [Work with EC2 Image Builder component products](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-ec2-image-builder-products.html#publishing-ib-component-listing) in the *AWS Marketplace API Reference*.