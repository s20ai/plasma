# Writing Plasma Components

User written Plasma Components can add custom functionality to pipelines.


## Directory structure 
- component-name
	- requirements.txt
	- README
	- component.py


Requirements.txt contains versioned dependencies of your component.
README is a text file which has instructions on how to use your components
component.py contains the actual source code of your components

## Component.py

It's neccesary that the component has a main function which accepts a
dictionary containing parameters. the main function serves as an entry point
through which the WXE ( Workflow Execution Engine ) interacts with your component.

The argument dictionary will have the base key 'operation' which is configured
through the YAML workflow file. This key can be used to trigger functions
inside the components. The argument dictionary will also have the base key 
'parameters' which can be used to pass parameters to the functions.


Example Component : 

The following component can take 2 numbers and add/subtract them.


```
def add(parameters):
	result = int(parameters['number_a']+parameters['number_b'])
	output = {"result":result}
	return output

def subtract(parameters):
	result = int(parameters['number_a']-parameters['number_b'])
	output = {"result":result}
	return output

def main(args):
	if args['operation'] == 'add':
		output = add(args['parameters'])
	elif args['operation'] == 'subtract':
		output = subtract(args['parameters'])
	return output
```

Corresponding YAML config : 

```
component-name
  add:
    number_a:5
    number_b:5
```

## Returning values from components

Plasma allows you to pass values from one component to the next by using dictionaries.
If your component returns output in the form of a dictionary. For example consider the
following component

```
def main(args):
	if args['operation'] == 'show_secret_message':
		output = {"secret-message":"Darth Vader is Luke's father"}
		return output
```

And the workflow yaml file : 

```
message-reader:
	show_secret_message:
		# assume param1 and param2 parameters you passed to the component
		param1: "a"
		param2: "b"
message-sender:
	send_secret_message:
		# the component message-sender can access the variable secre-message
		# returned by the previous component
		message: secret-message
```


## Good Practices

### Requirements.txt

Use a virtual environment to develop components. Use `pip freeze` to
generate the requirements file.

### Linting

Plasma components have to follow the pep8 guide.
You can use tools like autopep8 to automatically lint your code


### Logging

Always use logging, the logger setup is handled by plasma, to use
the logger in your code, use the following snippet

```
import logging

# initialize component logger
logger = logging.getLogger('component-name')

# log data
logger.info('Info Statements')
logger.debug('Debug Statements')
logger.error('Error Statements')
```

### Error Handling

Use try catch blocks in the code to avoid unexpected behaviour, check
for known error types and log them.

## Packaging

Compress the component directory in a zip file so that it can be served
from the registry.
