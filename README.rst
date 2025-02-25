========================
example.flask.helloworld
========================

.. image:: https://raw.githubusercontent.com/macagua/example.flask.helloworld/master/docs/_static/flask-vertical.png
   :class: image-inline

Building a Hello World application with Flask.


Requirements
============

Please execute the following commands:

::

    $ sudo apt install -y python3-dev python3-pip python3-virtualenv
    $ sudo apt install -y git
    $ git clone https://github.com/macagua/example.flask.helloworld.git flask-helloworld
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

.. image:: https://raw.githubusercontent.com/macagua/example.flask.helloworld/master/docs/_static/flask-hello-world.png
   :class: image-inline

Display a **Hello World** message, like the previous figure.


----

Testing
=======

To run the tests, please execute the following command:

::

    $ pytest -v


This way you can check that the application is working correctly.


----


License
========

This project is licensed under the MIT License - see the `LICENSE`_ file for details.


----


References
==========

- `Quickstart — Flask documentation <https://flask.palletsprojects.com/en/stable/quickstart/>`_.
- `Testing Flask Applications — Flask documentation <https://flask.palletsprojects.com/en/stable/testing/>`_.
