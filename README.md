# INstallation and Launching
### requirements
<ul>
    <li>python</li>
    <li>Django</li>
    <li>postgres database</li>
    <li>Rest framework</li>
</ul>

### Installation
<ul>
    <li>create a virtual environment <code>virtualenv venv</code> (for ubuntu)</li>
    <li>install required packages <code>pip install -r requirements.txt</code> (for ubuntu)</li>
    <li>create a database and substitude credentials in the <code>.env</code> file</li>
    <li>make migrations <code>python3 manage.py makemigrations</code></li>
    <li>migrate <code>python3 manage.py migrate</code></li>
    <li>run the package <code>pip install -r requirements.txt</code> (for ubuntu)</li>
</ul>

### runing the app

<ul>
    <li>Browser <code>http://127.0.0.1:8000</code></li>
</ul>

### runing the api

<ul>
    <li>In the browser or Postman</li>
    <li>get patients <code>http://127.0.0.1:8000/api/patients</code></li>
    <li>get patients details <code>http://127.0.0.1:8000/api/records</code></li>
</ul>