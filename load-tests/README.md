# Load Tests
Load tests are done using Locust (https://locust.io/)

These are python tests. As such you will need to setup a virtual python environment by following the instructions here:
https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/

Then activate your virtual environment by running:
```powershell
.\env\Scripts\activate
```

Then install the required dependencies:
```powershell
pip install -r requirements.txt
```

**NOTE**
The faster way is to just run ```.\dev_start.ps1``` from the root of the repository

-----

Running the locust tests:

(This runs 100 users, hatching 5 every second, for 2 minutes)

```powershell
locust -f basic_load_test.py --host=<your host> --no-web --clients=100 --hatch-rate=5 --run-time=2m
``` 
Where:
* --host=https://google.com/ (must include http at the start)
* --run-time=<30s|2m|6h>
