# Graduate thesis: Environment setup

This is the method I use; it's not necessarily optimal but do this if you want to ensure we're both on the same page.

## Prerequisites

I recommend using `conda` (specifically `miniconda3` since it's lighter). You can install one of them however you wish.

## Usual way

Using conda or miniconda, run the following code in your terminal of choice:

```
conda create --name env python=3.8
```

This will create a new **Python 3.8** environment named `env` (change it at will), but it may or may not be contained with some other dependencies.

## Better way

I compile my own Python versions from scratch and keep them as versions I will later clone. This ensures there is no module contagion. Then I clone that version and use that as an environment.

So, first prepare a Python installation as a clone candidate, in other words, install *some* version of **Python** *somewhere*.

Then, run the following code:

```
conda create \
    --name env \
    --clone /path/to/python/
```

This will also create a new environment named `env`, which will inherit from whatever **Python** installation was at `/path/to/python`.

### Important thing to note

Do **NOT** move your clone candidates as it can (and likely will) break your environment.

## What I use

I name my environment for this `diprad` and my **Python 3.8** clone candidate is located at `~/programs/python/3.8`, hence I just do:

```
conda create \
    --name diprad \
    --clone ~/programs/python/3.8
```
