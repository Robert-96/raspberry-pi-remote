# raspberry-pi-remote

Use your phone as a remote controller for your Raspberry Pi.

## Install

Clone the repository:

```bash
$ git clone
$ cd raspberry-pi-remote
```

Install **Raspberry-Pi-Remote**:

```bash
$ python -m pip install -e .
```

Or install the dependencies from `requirements.txt`:

```bash
$ python -m pip install -r requirements.txt
```

## Run

```
$ export FLASK_APP=remote
$ export FLASK_ENV=development
$ python -m flask run
```

Open http://127.0.0.1:5000 in a browser.

## Usage

TODO.

## Test

Install the development dependencies from `requirements-dev.txt`:

```bash
$ python -m pip install -r requirements-dev.txt
```

Run the tests:

```
$ python -m pytest
```

## License

This project is licensed under the [MIT License](./LICENSE).
