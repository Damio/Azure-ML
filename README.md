# Project Title

Creating and deploying a Machine Learning model on Microsoft Azure - For hand-written digits

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project was run using Jupyter notebook Microsoft Azure portal, running this on another platform may require a few tweeks
You will also need to create a microsoft aaccount to setup the Azure ML studio
Two options: Trial or paid, both will provide you with a subscription id that you will need to create a workspace on Azure

```
Give examples
```

### Installing

You will need to install a couple of packages from azureml.core

Along with the usual imports

```
from azureml.core import Workspace,Experiment,Run
```

And repeat

```
until finishedh
```

End with an example of getting some data out of the system or using it for a little demo

## Here's a simple breakdown:
Part 1 - Create our model & upload to Azure:
1) Create a remote compute target (note you can also use local computer as compute target)
2) Upload your training data to datastore (Optional)
3) Create your training script
4) Create an Estimator object
5) Submit the estimator to an experiment object under the workspace

Part 2 - Deploying model as web service
1) Create a container image
2) Deploy model as web service


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/DamiO)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This project was part of a tutorial on Microsoft website for learning ML studio


Train with an estimator
Once you've created your workspace and set up your development environment, training a model in Azure Machine Learning involves the following steps:
