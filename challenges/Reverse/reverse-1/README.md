# Reverse 1

## Description

Recover the hidden flag from the provided Linux binary reverse1.

This challenge is more about learning, your first look into reverse engineering.

Here are 2 ways to get started with analysing the binary

## strings utillity

strings utillity extracts all human-readable data from the binary

```
strings reverse1
```

Here is another example with some filtering
```
strings reverse1| grep -iE "flag|ctf|pass|key"
```

## Ghidra
Ghidra is a NSA developed tool for software reverse engineering.

How to do some basic reverse engineering with Ghidra.

### Load binary to Ghidra

Open Ghidra and:
1. Create a new project
2. Import the binary
3. Run Auto Analysis (accept defaults)

### Inspect Strings Inside Ghidra

* Navigate to Window → Defined Strings
* Sort or search for:
	* flag
	* input
	* correct
	* fail

Double-click interesting strings to locate where they’re used in code.

### Trace String References

For each suspicious string:

* Right-click → References → Show References To
* Identify functions that use the string

Focus on:

* Validation logic (e.g., strcmp, strncmp)
* Conditional branches (if statements)

### Analyze Key Functions

Look for:

* A function comparing user input to a hardcoded value
* Decoding routines (XOR, base64, loops modifying bytes)
* Obfuscated flag construction

### Reconstruct the Flag
Depending on findings:

* Direct string: copy it
* Encoded: decode manually (Python often fastest)
* Constructed at runtime: replicate logic outside Ghidra



## Files

* [reverse1](<files/reverse1>)

