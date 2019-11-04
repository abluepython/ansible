# How to

First you have to build the image inside your computer:

```bash
    docker build -t ansible .
```

Next add your public and private ssh-key to the .ssh folder, then ran the command to get
inside the docker container:

```bash
    docker run --rm -it -v $(pwd):/ansible ansible
```
