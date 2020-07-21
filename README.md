# Sniffr

Micro module uses watchdog library to monitor specified folder for file changes and moves the files to another folder specified.

#### By **Grishon Gikima**


## Setup/Installation Requirements

### Requirements

### Setup
* Clone the repo `git clone https://github.com/GrishonNganga/Sniffr.git`
* Install Requirements in the sniffer/requirements.txt with `pip install sniffr/requirements.txt`


### Flask Example

* We will create a new Flask project.

* Create new directory `mkdir Test-Flask`
* Move into the folder, create virtual environment and activate it.

```python 
cd /Test-Flask
python -m venv virtual
source virtual/Script/activate

```
* Install Flask extension.
```python
pip install flask
```
* Create the file that will contain our app.
`touch app.py`

Okay we are good to go. So we will create a basic functioning Flask app.

```python
from flask import Flask, session

app = Flask(__name__)

@app.route('/')
def home():

    return('Home is where the root is at')

if __name__ == '__main__':
    app.run()

```
* We we now have a basic Flask app.
* Let's now add our **Sniff** Module
* Since we had already cloned it. We will now import it at the top of `app.py` 

```python
from flask import Flask, session
from sniffr import Sniffr

```
* Let us now use it.

```python
@app.route('/')
def go_home():
    sniff = Sniffr('photos', './model/photos')
    sniff.run()

    return('Home is where the root is at')

```
We initialize the Sniffr class and pass in two parameters.\
* 1. The folder where we expect photos to be saved in.
* 2. The folder where our model expects the photos for processing.\
**NB** Note that we are passing them as relative imports.\
Our example we assumes the model expects photos in the folder ~~photos~~ inside of the directory ~~model~~.\
We also assume photos uploaded to our site are stored in the folder `/photos`
* Run the application and go back to your code editor. Drag a photo inside the `/photos` folder.\
Observe that they are moved into the `./model/photos`

**Further customization to be a working application to come.**


## Known Bugs

There are no known bugs atm. Get in touch if you discover any.
## Technologies Used

* Python

## Support and contact details

Reach out to me over email grishon.nganga01@gmail.com
### Apache License

Copyright (c) 2020 Sniffr

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Copyright (c) {2020} **Grishon Gikima**