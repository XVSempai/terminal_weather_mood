from setuptools import setup, find_packages

setup(
    name="terminal-weather-mood",
    version="0.1.0",
    description="Weather-based terminal mood messages",
    author="Your Name",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'weathermood=terminal_weather_mood.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=["requests"],
    python_requires='>=3.6',
)
