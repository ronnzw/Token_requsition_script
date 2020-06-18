from pygments import highlight


Token requisiton script documentation
=====================================

* Navigate into the script main directory called token_script, inside that
  directory find ``secure`` module and open the ``secrets.py`` file.
* Copy and paste your access credentials provided by Degreed as show below and save them in a
  file called ``secrets.py``. Remember if you want production tokens change the host to ``degreed``.


.. code-block:: python

   # If you want production token change the HOST to "degreed"
   # Keep credentials safe at all times
   # Remember to include this file in the .gitignore file if you are using version control

   HOST = "betatest"
   CLIENT_ID = ""
   CLIENT_SECRET = ""

* If you are using Production your host should be ``degreed`` if you are
  using betatest your host should be ``betatest``.

* Use the access key for production if you want to request the production
  access token and betatest if you want access token for sandbox.

* Once you have successfully requested for the token send a secure file to the
   user who had requested.

* Update the ACL access file on sharepoint remember to keep the token documented
  as it is the only way to track the use of the API.

* Each token will expire after 2 months and has to be generated again.

**NB:** The ``secure`` is a python module because of the ``__init__.py`` file.


