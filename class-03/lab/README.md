# Lab: File IO and Exceptions

## Overview

In this lab assignment you will be creating a command line application which takes advantage of Python's built in capabilities for reading and writing files.

## Resources

## Configuration

Use `Poetry` to create project named `madlib-cli`.

Refer to Creating Project with Poetry section of [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed steps.

## Repository set-up

Create repository on Github with name `madlib-cli`

Refer to Github section of [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed steps.

## Feature Tasks and Requirements

- Create a file called `madlib.py` at root of `madlib_cli` folder, which will contain all of the Python code that you will write relating to your Madlib game.
- Create a file called `test_madlib.py` in root of `tests` folder which will be used to test your executable command line script.
- Keeping in mind the concept of [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle){:target="_blank"}, build a command line tool which will perform the following:
  - Print a welcome message to the user, explaining the Madlib process and command line interactions
  - Read a template Madlib file ([Example](./assets/sample_template.txt){:target="_blank"}), and parse that file into usable parts.
    - _You need to decide what components of this file are useful, and how to break those useful pieces apart_
  - Once you know what parts of the template need user input, such as `Adjective`, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
  - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
  - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
  - Write the completed template ([Example](./assets/sample_output.txt){:target="_blank"})to a new file on your file system (in the repo).

## Testing Requirements

You are NOT required to test terminal input/output, AKA print and input functions.

However you are expected to meaningful tests for your application.

So how can we skip testing print and output functionality while still proceeding with confidence?

The resolution to that dilemma is to break down your code so that it is more easily testable.

- Create and test a **read_template** function that takes in a path to text file and returns a stripped string of the file's contents.
- Create and test a **parse** function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
- Create and test a **merge** function that takes in a "bare" template and a list of user entered language parts, and returns a string with the language parts inserted into the template.

## Stretch Goals

- Figure out / research a way to verify terminal input/output.
- Test that completed madlib is properly written to disk with correct content.

## Submission Instructions

Refer to the the [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for the complete lab submission process and expectations
