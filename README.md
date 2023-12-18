# EVM Inscription

## Overview
`EVM_inscription` is a Python script tailored for the efficient batch creation of inscriptions on Ethereum Virtual Machine (EVM)-compatible blockchains. It streamlines the process of connecting to various blockchain networks and automates the submission of multiple transactions.

## Features
- **Multiple Blockchain Support**: Compatible with several EVM blockchains like Ethereum, Binance Smart Chain, and Polygon.
- **Dynamic Configuration**: Customize the number of inscriptions, transaction data, and gas pricing.
- **Secure Private Key Handling**: Ensures the safe usage of your private key without hardcoding it in the script.
- **User-Friendly**: Simple setup and execution process.

## Prerequisites
Before using this script, make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

## Installation
1. **Install web3.py**: This script depends on the `web3.py` package. Install it by running the following command in your terminal:
   ```
   pip install web3
   ```
2. **Clone the Repository** (Optional): If the script is hosted in a repository, you can clone it using:
   ```
   git clone https://github.com/hosir-web3/EVM_inscription.git
   ```

## Setup
1. **Private Key**: For security reasons, do not hardcode your private key in the script. Instead, use an environment variable or a secure key management system.
2. **RPC URL**: Choose the appropriate RPC URL for the blockchain you intend to interact with.
3. **Configuration**:
   - `no_to_mint`: Set the number of inscriptions you wish to create.
   - `hex_data`: Provide the hexadecimal data for the inscription.
   - `price_factor`: Adjust the gas price factor according to network conditions.

## Usage
1. Open the script and enter the required configuration parameters.
2. Run the script from your terminal:
   ```
   python evm_inscription.py
   ```

## Important Notes
- Always ensure that your private key is stored securely and never exposed in the script or its logs.
- Be aware of the gas fees and network conditions of the blockchain you are interacting with to avoid unexpected costs.
