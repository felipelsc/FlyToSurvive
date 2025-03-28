import asset
from cx_Freeze import setup, Executable
import os

executables = [Executable("main.py")]

setup(
    name="FlyToSurvive",
    version="1.0",
    description="FlyToSurvive game",
    options={"build_exe": {"packages": ['pygame']}},
    executables=executables
)