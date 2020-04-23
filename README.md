# pyota
python code for iota tangle

You should have Python installed in your system
check that pip is latest: 
py -m pip install --upgrade pip

install pyota:
pip install pyota[ccurl,pow]

intall virtual environment:
py -m pip install --user virtualenv

create virtual environment:
py -m venv env

activate virtual environment:
.\env\Scripts\activate

install packages:
pip install requests

In your virtual environment, run the file:
python privatenode.py
Note: replace url with your node's ip address/dns

For API reference, visit:
https://docs.iota.org/docs/node-software/0.1/iri/references/api-reference#broadcasttransactions
