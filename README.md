DOCS TODO

```
pypy3 -m venv pypy_env
source pypy_env/bin/activate
cd rovpp_extensions
pip3 install -e .[test]

# To run the simulations
pypy3 -O -m rovpp_extensions

# Or to just run in bash you can use this, but that will keep asserts on which is slower
rovpp_extensions

# To get the diagrams of hidden hijacks
cd rovpp_extensions  # (the top level directory, not the inner directory)
pypy3 -O -m pytest rovpp_extensions --view
```
