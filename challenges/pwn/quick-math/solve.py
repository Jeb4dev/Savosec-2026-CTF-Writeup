from pwn import *
# Wibe coded

# Connect to the server
r = remote('ctf4.savosec.fi', 2222)

# 1. Complete the handshake
r.recvuntil(b'name:')
r.sendline(b'hacker')

# 2. Start the automated loop
while True:
    try:
        # Read the server's output one line at a time
        line = r.recvline().decode('utf-8').strip()

        # Print everything so we can see the flag when it prints!
        if line:
            print(f"Server: {line}")

        # 3. Detect the math problem
        if "Solve:" in line:
            # Example line: "[1/15] Time limit: 2.00s. Solve: 2 - 50 + 1 = ?"

            # Split the string at "Solve: " and take the right half
            right_half = line.split("Solve: ")[1]

            # Remove the " = ?" to leave only the raw equation (e.g., "2 - 50 + 1")
            equation_str = right_half.replace("= ?", "").strip()

            # Calculate the answer safely
            answer = eval(equation_str)
            print(f"[*] Bot calculating: {equation_str} = {answer}")

            # Send the answer back to the server
            r.sendline(str(answer).encode())

    except EOFError:
        print("\n[*] Connection closed. Did we get the flag?")
        break