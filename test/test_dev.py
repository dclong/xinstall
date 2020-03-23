"""Test the dev module.
"""
import subprocess as sp
sp.run("sudo apt-get update", shell=True, check=True)


def test_git():
    """Test installing and configuring Git.
    """
    cmd = "sudo xinstall -y git -ic"
    sp.run(cmd, shell=True, check=True)


def test_pyjnius():
    """Test installing and configuring pyjnius.
    """
    cmd = "xinstall pyjnius -ic"
    sp.run(cmd, shell=True, check=True)


def test_nodejs():
    """Test installing nodejs.
    """
    cmd = "sudo xinstall -y nodejs -ic"
    sp.run(cmd, shell=True, check=True)


def test_bash_lsp():
    """Test installing Bash Language Server.
    """
    cmd = "xinstall bash_lsp -c"
    sp.run(cmd, shell=True, check=True)


def test_spark():
    """Test installing Spark.
    """
    cmd = "sudo xinstall spark -ic"
    sp.run(cmd, shell=True, check=True)


def test_pyspark():
    """Test installing PySpark.
    """
    cmd = "xinstall pyspark -ic"
    sp.run(cmd, shell=True, check=True)


def test_rust():
    """Test installing the Rust programming language.
    """
    cmd = "sudo xinstall -y rust -ic"
    sp.run(cmd, shell=True, check=True)


def test_ipython():
    """Test installing and configuring LightGBM.
    """
    cmd = "xinstall ipython -ic"
    sp.run(cmd, shell=True, check=True)