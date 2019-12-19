# Plasma 

Plasma is an open source tool which can be used to create and maintain
end to end ML Workflows. 


## Concepts

#### ML Pipelines

A machine learning pipeline is used to help automate machine learning workflows.They operate by enabling a sequence of data to be transformed and correlated together in a model that can be tested and evaluated to achieve an outcome, whether positive or negative.

![ML Pipelines](https://miro.medium.com/max/1688/1*rJGhyaChhnN_f4pg_T4__A.png)

#### Resources
An asset owned by an organization such as a DataSet or a ML Model.

#### Component
Code which can use a resource to perform one or more step in a workflow graph.

#### Workflow
A YAML defined graph comprised of resources and components which represent a ML pipeline. 

#### Execution Context
Workflow/Component configuration which would specify how the component should be executed or provisioned.


## Usage

Run the following commands

    chmod +x plasma
    ./plasma --help

## Known Bugs

- Unable to switch virtual environments before executing 
