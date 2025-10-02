## Configure a Python virtual environment for AI development

__Installing Python 3 on macOS__:

- Check if Python is already installed. Open the Terminal and type:

```bash
python3 --version
```
If Python 3 is installed, you'll see the version number. If not, proceed with the installation.

- Install Python 3 using Homebrew. Homebrew is a popular package manager for macOS. Execute the following command to install Python 3 by Homebrew:

```bash
brew install python
```
- After installation, verify that Python 3 is installed by checking the version again:

```bash
python3 --version
```
__Installing Python 3 on Linux__:

- Update the package list. Open a Terminal window and update your package list:

```bash
sudo apt update
```
- Install Python 3. For Debian-based systems like Ubuntu, use:

```bash
sudo apt install python3
```
- Verify the installation. Check if Python 3 is installed by running:

```bash
python3 --version
```

### Install Python package manager pip3

- Check if pip3 is already installed. Open the Terminal and type:

```bash
pip3 --version
```
If it's already installed, you'll see the version number.

- Install pip3 using Homebrew. If pip3 isn't installed, and you have Homebrew installed, you can install pip3 by installing Python 3 (since pip3 comes bundled with Python 3):

```bash
brew install python
```

__Installing pip3 on Linux__:

- Update the package list. Open a Terminal window and update your package list:

```bash
sudo apt update
```

- Install pip3. For Debian-based systems like Ubuntu, use:

```bash
sudo apt install python3-pip
```

- Verify the installation. Check if pip3 is installed by running:

```bash
pip3 --version
```
__Alternative Installation Method__: Using ```get-pip.py```

If pip3 is not available in your package manager, you can use the ```get-pip.py``` script to install it manually:

- Download ``get-pip.py```:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

- Run the script with Python 3:

```bash
python3 get-pip.py
```

- Verify the installation:

```bash
pip3 --version
```

### Installing and configuring Miniconda

__Step 1__: Download the Miniconda Installer.

1. **Choose the appropriate Miniconda installer:**
   - Visit the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html) and choose the macOS installer for Python 3.
   - Download the `.pkg` installer for macOS.

__Step 2__: Install Miniconda.

1. **Run the installer**:
   - Locate the downloaded `.pkg` file (usually in your Downloads folder) and double-click it to run the installer and follow the installation prompts to install Miniconda.

2. **Complete the installation**:
   - After the installation completes, you should see a confirmation screen. Click ```Close``` to exit the installer.

__Step 3__: Verify the Installation

1. **Verify the Conda installation**:
   - Type the following command in the Terminal and press Enter:
     ```bash
     conda --version
     ```
   - You should see the version of Conda that you installed, indicating that the installation was successful.

2. **Optional Step**: You can customize your Conda experience by setting the CONDA_HOME environment variable to point to the Miniconda installation directory.

```bash
export CONDA_HOME=/opt/miniconda3
export PATH="$CONDA_HOME/bin:$PATH"
```  
By default, when you install Miniconda, it will be located in: ```/opt/miniconda3```.

__Step 4__: Initialize Conda

1. **Initialize Conda for your shell**:
   - Run the following command in the Terminal to initialize Conda:
     ```bash
     conda init
     ```
   - This command configures your shell to use Conda.

2. **Restart your Terminal**:
   - Close and reopen your Terminal to apply the changes.

__Step 5__: Create and Manage Conda Environments

1. **Create a new environment**:
   - To create a new Conda environment, use the following command:
     ```bash
     conda create --name ai_book_env
     ```
   - `ai_book_env` will be our enviroment for developing applications.
2. **Activate the environment**:
   - To activate the environment, use the following command:
     ```bash
     conda activate ai_book_env
     ```
3. **Deactivate the environment**:
   - To deactivate the environment, use the following command:
     ```bash
     conda deactivate
     ```

__Step 6__: Additional Configuration (Optional)

1. **Configure Conda channels**:
   - Conda uses channels to find packages. You can add additional channels if needed. For example, to add the `conda-forge` channel:
     ```bash
     conda config --add channels conda-forge
     ```
2. **Update Conda**:
   - It's a good idea to keep Conda up to date. You can update Conda with the following command:
     ```bash
     conda update conda
     ```
