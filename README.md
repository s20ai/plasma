# Plasma 

Plasma is an open source tool which can be used to create and maintain end to
end ML Workflows. Plasma breaks down a machine learning pipeline into smaller
reusable blocks of code called ‘components’. The sequence in which these
components are to be executed and the parameters which each component accepts
and returns are defined in a simple YAML ‘workflow’ file.

Due to this, the ML codebase becomes a collection of reusable and modular components. 
Also, Data Scientists don’t need to edit code for running the workflow and changing 
parameters. This makes the workflow more stable.

Plasma also includes an in-built component manager which allows users to search an 
online registry of open-source components. This can greatly reduce the amount of 
time needed to develop the workflow.


Plasma is a fairly new tool and might not support everything your ML workflow requires.
Hence, new component/feature requests can be raised as Github Issues.
Our project roadmap is also available [publicly](https://github.com/s20ai/plasma/projects/1).

## Usage

#### Installing dependencies :
```
pip3 -r requirements.txt
```

#### Running Plasma

```
chmod +x plasma
./plasma
```


## Docs

- [Plasma](https://github.com/s20ai/plasma-docs/blob/master/projects.md)
- [Projects](https://github.com/s20ai/plasma-docs/blob/master/projects.md)
- [Components](https://github.com/s20ai/plasma-docs/blob/master/components.md)
- [Package Manager](https://github.com/s20ai/plasma-docs/blob/master//package_manager.md)
- [Workflow](https://github.com/s20ai/plasma-docs/blob/master/workflows.md)



## Demos

- [Sentiment Analysis Workflow](https://github.com/s20ai/plasma-demos/tree/master/sentiment-analysis-demo)
