from pygments import highlight

=====================================
Token requisiton script documentation
=====================================

* Git clone the repository or download and unzip it into a directory of your choice.
* We recommend that you create a virtual environment for this script, run ::

  $ python3 -m venv [name_of_your_virtual_environment]
  $ source [name_of_your_virtual_environment]/bin/activate
* Navigate into the script main directory called ``Token_requisition_script``, inside that
  directory find ``secure`` module and open the ``secrets.py`` file.
* Copy and paste your access credentials provided by Degreed as show below and save them in a
  file called ``secrets.py``. Remember if you want production tokens change the host to ``degreed``.


.. code-block:: python

   # If you want production token change the HOST to "degreed"
   # Keep credentials safe at all times
   # Remember to include this file in the .gitignore file if you are using version control

   HOST = "betatest"
   CLIENT_ID = "abcde12345"
   CLIENT_SECRET = "abcdefghi123456789klmnopqrstuvwxyz"

* If you are using Production your host should be ``degreed`` if you are
  using betatest your host should be ``betatest``.
* Once you complete pasting the credentials navigate back to the main directory
  which is ``Token_requisition_script`` and install requirements by running::

   $ pip install -r requirements.txt

* Go back to the ``secure/secrets.py`` file and find the variable ``SCOPE``

* Fill-in the scope requested by the user. if there are more than one scope
  the scope using a ``'',''`` and no space as shown below.

.. code-block:: python

   SCOPE = "content:read,content:write,users:read"

* Very token must be scope otherwise the request will fail.

* Navigate to the back to the main directory and in your command line, run ::

  $ python3 token_requisition_magic_script.py


* The script should return a token and an expiry date. if it fails it will
  return a statement ``Something went wrong...``. if that happens check that
  your API keys are correct, if they are correct, check the ``SCOPE``, remember
  **no spaces** between "," and the next scope item. This is one of the most
  common gotchas on this script.

* Once you have successfully requested for the token, send a secure file to the
   user who had requested for the token.

* Update the ACL access file and remember to keep the token documented
  as it is the only way to track the use of the API.

* Each token will expire after 2 months and has to be regenerated again.

**NB:** If you are using version control remember to put your ``secrets.py`` file within the ``.gitignore`` file.


