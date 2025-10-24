# 🧩 ARIN Prefix Extractor

A lightweight Python script that fetches and extracts all IPv4/IPv6 prefixes (CIDRs) associated with a given ARIN organization handle using the [ARIN RDAP API](https://rdap.arin.net/registry/).

---

## 📘 Overview

This script retrieves RDAP (Registration Data Access Protocol) data for an organization and outputs a simple list of its network prefixes (both IPv4 and IPv6).  

It’s useful for network engineers, security analysts, or automation pipelines that need to quickly identify all prefixes owned by an organization in ARIN’s registry.

---

## ⚙️ How It Works

1. **Fetch RDAP JSON** — Queries ARIN’s RDAP endpoint for the given org handle.  
2. **Parse JSON Data** — Extracts all `v4prefix` and `v6prefix` entries along with their subnet lengths.  
3. **Save Prefix List** — Writes all discovered prefixes to a text file for easy use in other scripts or tools.

---

## 🚀 Usage

### **1. Prerequisites**

- Python 3.6+
- `curl` installed and available in your system’s PATH

### **2. Run the Script**

```bash
python3 get_prefixes.py <ORG_HANDLE>
```

**Example:**

```bash
python3 get_prefixes.py DNIC
```

### **3. Output Files**

- **`<ORG_HANDLE>.json`** — Raw RDAP response from ARIN  
- **`<ORG_HANDLE>_prefixes.txt`** — Clean list of network prefixes (one per line)

---

## 📄 Example Output

**Command:**
```bash
python3 get_prefixes.py DNIC
```

**Output File (`DNIC_prefixes.txt`):**
```
26.0.0.0/8
6.0.0.0/8
214.0.0.0/8
```

**Console Output:**
```
Saved 3 prefixes to DNIC_prefixes.txt
```

---

## 🧠 Notes

- The script depends on ARIN’s public RDAP API (`https://rdap.arin.net/registry/entity/<ORG_HANDLE>`).
- If the organization handle doesn’t have any `networks` in its RDAP data, the prefix list will be empty.
- This script only retrieves data for ARIN-managed resources — it won’t work for RIPE, APNIC, or other RIRs.

---

## 🧰 Example Use Cases

- Automating firewall or routing list generation  
- Inventorying IP space owned by a specific organization  
- Enriching threat intelligence datasets with ownership information  

---

## 🧑‍💻 Author

**Nick Stockhauser**  
Curious builder of network and security automation tools.
