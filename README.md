# SubVault

**Collect. Organize. Recon.**

SubVault is a lightweight passive subdomain aggregation tool that collects subdomains from multiple public intelligence providers.

It does not perform active discovery or DNS brute-force enumeration. Instead, it gathers already indexed subdomains, removes duplicates, and saves the results into timestamp-based files.

### Features

- Multiple passive subdomain providers.
- Asynchronous requests using HTTPX.
- HTTP/2 support.
- Automatic duplicate removal.
- Timestamp-based result files.
- Lightweight CLI powered by Rich.
- No expensive infrastructure required.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/KaranSRMA/subvault.git
```

**2. Navigate into the project**

```bash
cd subvault
```

**3. Create a virtual environment**

```bash
python3 -m venv venv
```

**4. Activate the virtual environment**

```bash
source venv/bin/activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

### Usage

Run SubVault:

```bash
python main.py
```

Enter the target domain when prompted.

SubVault will collect subdomains from its configured providers, remove duplicates, and automatically save the results in a timestamp-based `.txt` file in the current working directory.



### Disclaimer

SubVault is intended for authorized security research, asset discovery, and reconnaissance. Only collect and use information for domains you own or have explicit permission to assess.

### License

See the [LICENSE](LICENSE) file for licensing information.