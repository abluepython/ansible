#!/usr/bin/env python
import subprocess, optparse

def get_args():
    """
    Get arguments from cli.
    """
    parser = optparse.OptionParser()
    parser.add_option("-id", "--id_rsa", dest="id_rsa", help="The location of your private key.")
    parser.add_option("-idp", "--id_rsa_pub", dest="id_rsa_pub", help="The location of your public key.")
    parser.add_option("-idp", "--id_rsa_pub", dest="id_rsa_pub", help="The location of your public key.")

    (options, arguments) = parser.parse_args()

    return options

def main(id_rsa, id_rsa_pub):
    local = subprocess.call(["pwd"]) + ":/ansible/playbooks"
    
    subprocess.call(["docker", "run", "--rm", "-it", "-v", id_rsa, "-v", id_rsa_pub, "-v", ])




docker run --rm -it \
    -v ~/.ssh/id_rsa:/root/.ssh/id_rsa \
    -v ~/.ssh/id_rsa.pub:/root/.ssh/id_rsa.pub \
    -v $(pwd):/ansible/playbooks \
    walokra/ansible-playbook site.yml
