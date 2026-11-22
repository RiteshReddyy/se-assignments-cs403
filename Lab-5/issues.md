# Movie review issue log

| Issue | Type | Line(s) | Description | Fix approach |
|---|---|---|---|---|
| B324 | Security / high | 46 | MD5 produced only a 10-hex-character ID and concatenated the title and review without a boundary. | Hash a JSON pair with SHA-256 and keep the full digest. |
| B104 | Configuration / medium | 4 | The display advertised the wildcard network address. | Make the demonstration address 127.0.0.1; the program only prints the address. |
| B105 | Security / low | 6 | A hard-coded moderator password was declared and unused. | Remove the unused credential. |
| B311 | Security / low | 41 | The default PRNG selected the featured title. | Use secrets.choice and handle an empty catalogue. |
| W0603 | Maintainability | 40 | Feature selection wrote to module-level state. | Return the selection directly. Store movie data on each MovieBoard instance. |
| R1705 / C0200 | Clarity | 28, 50 | An unnecessary else and indexed traversal obscured two simple operations. | Return the mean or zero directly. Print rows with enumerate. |
| C0103 / C0114 / C0116 | Readability | 1, 8, 11-58 | Names mixed conventions and public operations lacked descriptions. | Use snake_case and describe the module, catalogue and public operations. |
| E225 / E302 / E261 / E231 | Style | 35, 48, 70, 72 | Spacing around assignment, functions, comment and comma failed style checks. | Normalize spacing and remove the redundant inline comment. |
