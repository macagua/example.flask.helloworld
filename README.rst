================
flask-helloworld
================

Building a Hello World application with Flask.


Requirements
============

Please execute the following commands:

::

    $ sudo apt install git python3-virtualenv python3-pip
    $ git clone https://github.com/macagua/flask-helloworld.git
    $ cd ./flask-helloworld
    $ virtualenv --python=/usr/bin/python3 venv
    $ source ./venv/bin/activate
    $ pip3 install --upgrade pip
    $ pip3 install -r requirements.txt


Running
=======

Please execute the following command:

::

    $ flask --app hello run

Open at your Web browser the following link http://127.0.0.1:5000/

.. image:: https://raw.githubusercontent.com/macagua/flask-helloworld/master/docs/_static/flask-hello-world.png
   :class: image-inline

Display a Hello World message, like the previous figure.

References
==========

- `Quickstart — Flask documentation <http://flask.pocoo.org/docs/1.0/quickstart/>`_.
