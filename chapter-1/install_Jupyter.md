## Install IDE: Jupyter lab and notebook

1. __Create a new conda environment (optional but recommended)__: It's a best practice to create a separate environment for each project. You can create a new environment for JupyterLab with a specific Python version as shown below:

```bash
conda create -n jupyterlab-env python=3.11
```
Replace ```3.11``` with the version of Python you wish to use. When prompted, type ```y``` to proceed with the installation.

2. __Activate the new environment__: Once the environment is created, activate it by the following bash command.

```bash
conda activate jupyterlab-env
```
Replace ```jupyterlab-env``` with your environment name if you used a different name.

3. __Install JupyterLab__: Now, install JupyterLab in the activated environment:

```bash
conda install -c conda-forge jupyterlab
```
This command installs JupyterLab and its dependencies from the ```conda-forge``` channel, which is a widely used community-maintained channel for conda packages.

4. __Launch JupyterLab__: After the installation is complete, you can start JupyterLab by typing:

```bash
jupyter lab
```
