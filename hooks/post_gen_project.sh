#! /bin/bash

# install the node_modules
{% if cookiecutter.install_dependencies == 'yes' -%}
  yarn install
{% endif %}

# activate the gitignore file
mv gitignore .gitignore


