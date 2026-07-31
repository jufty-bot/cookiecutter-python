<h1 align="center">{{ project_name }}</h1>

<p align="center">
{{ project_description }}
</p>

<p align="center">
  <a href="https://github.com/{{ github_user }}/{{ project_name }}"><img src="https://img.shields.io/github/v/release/{{ github_user }}/{{ project_name }}?color=blue&label={{ project_name }}&logo=github" alt="GitHub"></a>
  {%- if publish_to_pypi == True %}
  <a href="https://pypi.python.org/pypi/{{ package_name }}/"><img src="https://img.shields.io/pypi/pyversions/{{ package_name }}?label=PyPI&logo=python" alt="PyPI"></a>
  {%- endif %}
  {%- if publish_to_docker_hub == True %}
  <a href="https://hub.docker.com/r/{{ github_user }}/{{ package_name }}"><img src="https://img.shields.io/docker/v/{{ github_user }}/{{ package_name }}?color=blue&label=docker&logo=docker" alt="Docker Image Version"></a>
  {%- endif %}
  <a href="https://github.com/{{ github_user }}/{{ project_name }}/blob/main/LICENSE"><img src="https://img.shields.io/github/license/{{ github_user }}/{{ project_name }}?color=blue&label=License" alt="GitHub License"></a>
  <a href="https://github.com/{{ github_user }}/{{ project_name }}/actions/workflows/test.yaml?query=branch%3Amain"><img src="https://github.com/{{ github_user }}/{{ project_name }}/actions/workflows/test.yaml/badge.svg?branch=main" alt="Testing Status"></a>
  <a href="https://github.com/go-task/task"><img src="https://img.shields.io/badge/task---?message=task&logo=task&color=teal&labelColor=grey" alt="task"></a>
  <a href="https://github.com/astral-sh/uv"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv"></a>
  <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-lightgreen?logo=pre-commit" alt="pre-commit"></a>
  <a href="https://{{ github_user }}.github.io/{{ project_name }}/"><img src="https://img.shields.io/static/v1?message=docs&color=526CFE&logo=Material+for+MkDocs&logoColor=FFFFFF&label=" alt="docs"></a>
  <a href="https://github.com/semantic-release/semantic-release"><img src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg" alt="semantic-release"></a>
  <a href="https://gitmoji.dev"><img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg" alt="Gitmoji"></a>
</p>
