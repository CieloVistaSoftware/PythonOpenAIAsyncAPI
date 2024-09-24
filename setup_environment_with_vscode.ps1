# Bypass execution policy for this session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Get the directory where the script is located
$script_dir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Navigate to the script directory
Set-Location $script_dir

# Create a virtual environment in the script directory
python -m venv "$script_dir\venv"

# Activate the virtual environment
& "$script_dir\venv\Scripts\Activate"

# Install necessary packages from pip
pip install openai

# Open Visual Studio Code in the current directory
code $script_dir
