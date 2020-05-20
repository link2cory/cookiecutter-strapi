import os, subprocess

from github import Github
from git import Repo

# if this is a subpackage, let the root package handle everything
{% if cookiecutter.is_subpackage == 'no' -%}
    {% if cookiecutter.install_dependencies == 'yes' -%}
        subprocess.run(['yarn', 'install'])
    {% endif %}

    {% if cookiecutter.use_git == 'yes' -%}
        # activate .gitignore. It must be stored this way to facilitate versioning of
        # the cookiecutter.
        os.rename('gitignore', '.gitignore')
        
        # initialize local repo 
        local_repo = Repo.init(os.getcwd())
        local_repo.git.add(A=True)
        local_repo.index.commit('Initial Commit, project generated with cookiecutter-jam-app')

        {% if cookiecutter.use_github == 'yes' -%}
            # create the github repo
            Github('{{ cookiecutter.github_token }}').get_user().create_repo('{{ cookiecutter.project_slug }}')
            # point local repo to the remote
            remote_repo = local_repo.create_remote(
                'origin',
                'git@github.com:{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git'
            )
            #  push to the remote
            remote_repo.push(refspec='{}:{}'.format('master', 'master'))
        {% endif %}
    {% endif %}
{% endif %}
