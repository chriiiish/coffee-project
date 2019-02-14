# This sets up the virtual environment for python
# This assumes, you know, you have python installed...

$RelativeEnvironmentPath = ".\env\Scripts\activate.ps1";

# If there is already a virtual environment, create it
if (Test-Path -Path $RelativeEnvironmentPath){
  Write-Output "Found the virtual environment - starting!";
  
  # Start the python virtual environment
  Invoke-Expression $RelativeEnvironmentPath;
  
  # Install any required packages
  pip install -r load-tests/requirements.txt;
  
  Write-Output "You are now in the python virtual environment!";
}else{
  # Setup the virtual environment
  Write-Output "Installing VirtualEnv...";
  pip install virtualenv;

  Write-Output "Setting up virtualenv `"env`"";
  virtualenv env;
  
  Write-Output "Done. Run this again to activate the virtual environment";
}