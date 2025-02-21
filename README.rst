================
flask-helloworld
================

.. image:: https://raw.githubusercontent.com/macagua/flask-helloworld/master/docs/_static/flask-vertical.png
   :class: image-inline

Building a Hello World application with Flask.


Requirements
============

Please execute the following commands:

::

    $ sudo apt install -y python3-dev python3-pip python3-virtualenv
    $ sudo apt install -y git
    $ git clone https://github.com/macagua/flask-helloworld.git
    $ cd ./flask-helloworld
    $ virtualenv --python /usr/bin/python3 venv
    $ source ./venv/bin/activate
    $ pip3 install -U pip
    $ pip3 install -r requirements.txt


----

Running
=======

Please execute the following command:

::

    $ flask --app hello run

Open at your Web browser the following link http://127.0.0.1:5000/

.. image:: https://raw.githubusercontent.com/macagua/flask-helloworld/master/docs/_static/flask-hello-world.png
   :class: image-inline

Display a Hello World message, like the previous figure.


----

Testing
=======

To run the tests, please execute the following command:

::

    $ pytest -v


This way you can check that the application is working correctly.

----

Building with Docker
====================

You can also build the image with `Docker <https://www.docker.com/>`_ to test the application, run the following command:

::

    $ docker build --tag=flask-helloworld .


Create the container and run the application, execute the following command:

::

    $ docker run -d -p 5000:5000 --name flask-helloworld flask-helloworld


Use an HTTP client such as ``curl`` to test the application via command line by executing the following command:

::

    $ curl localhost:5000

Also you can open at your Web browser the following link http://127.0.0.1:5000/

----

References
==========

- `Quickstart — Flask documentation <https://flask.palletsprojects.com/en/stable/quickstart/>`_.
- `Testing Flask Applications — Flask documentation <https://flask.palletsprojects.com/en/stable/testing/>`_.
