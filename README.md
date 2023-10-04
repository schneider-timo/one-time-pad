# One-Time Pad Encoder/Decoder

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

This Python script allows you to encode and decode strings using the one-time pad encryption method.

## Table of Contents

1. [Overview](#overview)
2. [History](#history)
3. [Usage](#usage)


## Overview

The one-time pad is a cryptographic method that provides perfect secrecy if used correctly. It involves the use of a random key that is as long as the message to be encoded. Each character in the message is combined with the corresponding character in the key to produce the ciphertext.

This repository contains a Python script that implements the one-time pad method for both encoding and decoding strings.

## History

The one-time pad, also known as the Vernam cipher, is an encryption technique with a fascinating history. It was developed independently by Gilbert S. Vernam and Joseph O. Mauborgne in 1917. 

- **World War I:** The one-time pad was originally used for secure communication during World War I. It offered unbreakable encryption when used with truly random keys of the same length as the message.

- **Perfect Secrecy:** One of the key features of the one-time pad is its perfect secrecy. If the key is truly random, used only once, and kept secret, it is theoretically unbreakable. This property makes it highly valuable in certain applications.

- **Limitations:** Despite its theoretical security, the practical use of one-time pads has limitations, mainly due to the challenges of generating and securely exchanging long, truly random keys.

## Usage

Clone the repository to your local machine:

   ```bash
   git clone https://github.com/schneider-timo/one-time-pad.git
   ```
Navigate to the project directory:

```bash
cd one-time-pad
```
Run the script with Python:

```bash
python3 one_time_pad.py
```
Follow the on-screen instructions to encode or decode a string.
