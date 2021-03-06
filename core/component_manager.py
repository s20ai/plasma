#!/usr/bin/python3

import requests
from core.project import get_config
import os
import zipfile
import io
import importlib.util

api_url = "https://dfdb32ca.s20.ai/api/v1/components"


def download_component(name):
    plasma_config = get_config()
    print('\n> downloading '+name+' from the component registry')
    response = requests.get(api_url+'/download/'+name).json()
    component = response.get('data')
    if component:
        response = requests.get(component['url'])
        print('> extracting zip file')
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall(plasma_config['paths']['components_path'])
        print('> component stored at '+plasma_config['components_path'])
        print('> download complete\n')
    else:
        print('\n> component not found')
    print()


def describe_component(name):
    plasma_config = get_config()
    if os.path.exists(plasma_config['paths']['components_path']+name):
        readme_file = plasma_config['paths']['components_path']+name+'/README'
        with open(readme_file, 'r') as readme:
            print(readme.read())
    else:
        print('\n> component not found locally\n')


def list_components():
    plasma_config = get_config()
    components_path = plasma_config['paths']['components_path']
    components = os.listdir(components_path)
    if components:
        print('\n> listing local components ')
        for item in components:
            if os.path.isdir(components_path+item):
                print('\t- '+item)
        print()
    else:
        print('\n> no components have been downloaded\n')


def search_components(query):
    print('\n> searching '+query+' in the component registry')
    response = requests.get(api_url+'/search/'+query).json()
    components = response.get('data')
    if components:
        print()
        for component in components:
            print('\t'+component['name'])
            print('\t'+component['description'])
            print('\ttags : '+', '.join(component['tags']))
        print()
    else:
        print('\n> no results found')


def component_loader(component_name, component_path):
    spec = importlib.util.spec_from_file_location(
        component_name, component_path)
    component = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(component)
    return component
