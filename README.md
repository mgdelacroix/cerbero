# Cerbero

Cerbero is a simple program written in python to manage the SSH keys
of your remote servers. It reads a config file written in YAML where
the keys, remote machines and valid dates are specified and uses that
information to log into the machines and regenerate the
`authorized_keys` file.

It is intended to be run on its own and through a cron job every day,
so it can delete the expired keys and add the new ones.

## Roadmap

- [ ] Push the ssh keys to the remote machines.
- [ ] Merge the `authorized_keys` with a static file on the remote
  machine if exists.
- [ ] Apply start and end dates to allow keys to expire.
- [ ] Web interface to modify the config file or maybe a small db.

## Development

To run the program directly from the sources, you can use
the [virtualenv](https://virtualenv.pypa.io/en/stable/) package or you
can manage the dependencies manually.

For this second approach, the script `run_dev` will install the
dependencies locally in the `deps` directory of the repository and
will run the `main` module including those dependencies.

## Build the binary

From the repository root directory, first create a `dist` temporal
directory:

```sh
mkdir dist
```

Then install the dependencies locally in that directory:

```sh
pip3 install -r requirements.txt --system --upgrade --target dist
```

And finally, package the whole program into an executable file:

```sh
python3 -m zipapp -o cerbero.pyz -p '/usr/bin/env python3' -m cerbero
```

If you want to install it locally in your system, just move the
executable file to a directory in your path:

```sh
# You can modify the extension to make it easier to call
sudo mv cerbero.pyz /usr/local/bin/cerbero
```
