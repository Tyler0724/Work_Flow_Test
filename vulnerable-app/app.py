"""Intentionally vulnerable sample app for SARIF demo."""
import os
import sqlite3
import yaml


# Dummy secret to exercise secret scanners; obviously fake.
FAKE_API_KEY = "AKIAFAKE1234567890FAKE"


def unsafe_yaml_load(payload: str):
    # Using yaml.load without a safe loader can execute arbitrary code.
    return yaml.load(payload, Loader=yaml.Loader)


def insecure_sql(user_input: str):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (name TEXT)")
    cur.execute("INSERT INTO users (name) VALUES ('admin')")
    # f-string interpolation without parameters allows SQL injection.
    cur.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
    return cur.fetchall()


def use_hardcoded_secret():
    # Hardcoded secret key used directly.
    return f"Using secret: {FAKE_API_KEY}"


def main():
    payload = "{'run': 'calc.exe'}"
    unsafe_yaml_load(payload)
    insecure_sql("admin' OR '1'='1")
    use_hardcoded_secret()
    # Dangerous: execute arbitrary input (for demo only).
    eval("print('unsafe exec')")


if __name__ == "__main__":
    main()
